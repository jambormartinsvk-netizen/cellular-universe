[CmdletBinding(DefaultParameterSetName = 'NoAction')]
param(
    [Parameter(Mandatory = $true, ParameterSetName = 'SelfTest')]
    [switch]$SelfTest,

    [Parameter(Mandatory = $true, ParameterSetName = 'Acquire')]
    [switch]$Acquire,

    [Parameter(Mandatory = $true, ParameterSetName = 'Acquire')]
    [ValidatePattern('^[0-9A-F]{64}$')]
    [string]$PreregSha256,

    [Parameter(Mandatory = $true, ParameterSetName = 'Acquire')]
    [ValidatePattern('^[0-9A-F]{64}$')]
    [string]$AuthorizationEventLedgerSha256
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$ExpectedPreregSha256 = 'F141E8781AE61E863D795224C00A8D0F0D6411DCEBF2239ED7750A46D9142225'
$SourceUrl = 'https://export.arxiv.org/e-print/2307.12080v2'
$UserAgent = 'Teoria-Q1R1-V2-SourceAudit/1.0'
$MinHttpBytes = 10000L
$MaxHttpBytes = 8L * 1024L * 1024L
$MaxTarBytes = 32L * 1024L * 1024L
$MaxEntryBytes = 4L * 1024L * 1024L
$MaxEntries = 512
$MaxCompressionRatio = 40.0
$ValidationDeadlineSeconds = 30.0
$HttpTimeoutSeconds = 60

Add-Type -TypeDefinition @'
using System;
using System.IO;

namespace Teoria.Q1R1V2
{
    public sealed class OneByteReadStream : Stream
    {
        private readonly Stream inner;
        public OneByteReadStream(Stream inner) { this.inner = inner ?? throw new ArgumentNullException(nameof(inner)); }
        public override bool CanRead => inner.CanRead;
        public override bool CanSeek => inner.CanSeek;
        public override bool CanWrite => false;
        public override long Length => inner.Length;
        public override long Position { get => inner.Position; set => inner.Position = value; }
        public override void Flush() { }
        public override int Read(byte[] buffer, int offset, int count) => inner.Read(buffer, offset, Math.Min(1, count));
        public override int Read(Span<byte> buffer) => inner.Read(buffer.Slice(0, Math.Min(1, buffer.Length)));
        public override int ReadByte() => inner.ReadByte();
        public override long Seek(long offset, SeekOrigin origin) => inner.Seek(offset, origin);
        public override void SetLength(long value) => throw new NotSupportedException();
        public override void Write(byte[] buffer, int offset, int count) => throw new NotSupportedException();
        protected override void Dispose(bool disposing) { base.Dispose(disposing); }
    }

    public static class Crc32
    {
        public static uint Compute(byte[] data)
        {
            uint crc = 0xFFFFFFFFu;
            foreach (byte value in data)
            {
                crc ^= value;
                for (int bit = 0; bit < 8; bit++)
                    crc = (crc & 1u) != 0u ? (crc >> 1) ^ 0xEDB88320u : crc >> 1;
            }
            return ~crc;
        }
    }

    public static class LittleEndian
    {
        public static ushort ReadUInt16(byte[] bytes, int offset)
        {
            if (bytes == null) throw new ArgumentNullException(nameof(bytes));
            if (offset < 0 || offset > bytes.Length - 2) throw new ArgumentOutOfRangeException(nameof(offset));
            return (ushort)((uint)bytes[offset] | ((uint)bytes[offset + 1] << 8));
        }

        public static uint ReadUInt32(byte[] bytes, int offset)
        {
            if (bytes == null) throw new ArgumentNullException(nameof(bytes));
            if (offset < 0 || offset > bytes.Length - 4) throw new ArgumentOutOfRangeException(nameof(offset));
            return (uint)bytes[offset]
                | ((uint)bytes[offset + 1] << 8)
                | ((uint)bytes[offset + 2] << 16)
                | ((uint)bytes[offset + 3] << 24);
        }
    }
}
'@

function Throw-Guard {
    param([Parameter(Mandatory = $true)][string]$Code)
    throw [System.IO.InvalidDataException]::new($Code)
}

function Get-Sha256Hex {
    param([Parameter(Mandatory = $true)][byte[]]$Bytes)
    $sha = [System.Security.Cryptography.SHA256]::Create()
    try {
        return (($sha.ComputeHash($Bytes) | ForEach-Object { $_.ToString('X2') }) -join '')
    }
    finally {
        $sha.Dispose()
    }
}

function Get-U16LE {
    param([byte[]]$Bytes, [int]$Offset)
    return [Teoria.Q1R1V2.LittleEndian]::ReadUInt16($Bytes, $Offset)
}

function Get-U32LE {
    param([byte[]]$Bytes, [int]$Offset)
    return [Teoria.Q1R1V2.LittleEndian]::ReadUInt32($Bytes, $Offset)
}

function Test-AllZero {
    param([byte[]]$Bytes, [int]$Offset, [int]$Count)
    for ($i = 0; $i -lt $Count; $i++) {
        if ($Bytes[$Offset + $i] -ne 0) { return $false }
    }
    return $true
}

function Assert-ArchiveLimits {
    param(
        [long]$CompressedBytes,
        [long]$TarBytes,
        [int]$EntryCount,
        [long]$LargestEntry,
        [double]$ElapsedSeconds,
        [switch]$SkipMinimumHttpSize
    )
    if (-not $SkipMinimumHttpSize -and $CompressedBytes -lt $MinHttpBytes) { Throw-Guard 'HTTP_SIZE_BELOW_MINIMUM' }
    if ($CompressedBytes -gt $MaxHttpBytes) { Throw-Guard 'HTTP_SIZE_ABOVE_MAXIMUM' }
    if ($TarBytes -gt $MaxTarBytes) { Throw-Guard 'TAR_SIZE_ABOVE_MAXIMUM' }
    if ($EntryCount -lt 1 -or $EntryCount -gt $MaxEntries) { Throw-Guard 'TAR_ENTRY_COUNT_LIMIT' }
    if ($LargestEntry -gt $MaxEntryBytes) { Throw-Guard 'TAR_PER_ENTRY_LIMIT' }
    if ($CompressedBytes -le 0) { Throw-Guard 'COMPRESSED_SIZE_NONPOSITIVE' }
    if (($TarBytes / [double]$CompressedBytes) -gt $MaxCompressionRatio) { Throw-Guard 'COMPRESSION_RATIO_LIMIT' }
    if ($ElapsedSeconds -gt $ValidationDeadlineSeconds) { Throw-Guard 'ARCHIVE_VALIDATION_DEADLINE' }
}

function Read-GzipZeroTerminatedField {
    param([byte[]]$Bytes, [ref]$Index, [ref]$OptionalBytes)
    while ($true) {
        if ($Index.Value -ge $Bytes.Length) { Throw-Guard 'GZIP_TRUNCATED_OPTIONAL_FIELD' }
        $value = $Bytes[$Index.Value]
        $Index.Value++
        $OptionalBytes.Value++
        if ($OptionalBytes.Value -gt 4096) { Throw-Guard 'GZIP_OPTIONAL_HEADER_LIMIT' }
        if ($value -eq 0) { break }
    }
}

function Expand-SingleGzipMember {
    param([Parameter(Mandatory = $true)][byte[]]$Bytes)
    if ($Bytes.Length -lt 18) { Throw-Guard 'GZIP_TOO_SHORT' }
    if ($Bytes[0] -ne 0x1F -or $Bytes[1] -ne 0x8B -or $Bytes[2] -ne 8) { Throw-Guard 'GZIP_HEADER_ID_OR_METHOD' }

    $flags = [int]$Bytes[3]
    if (($flags -band 0xE0) -ne 0) { Throw-Guard 'GZIP_RESERVED_FLAGS' }
    $index = 10
    $optionalBytes = 0

    if (($flags -band 0x04) -ne 0) {
        if ($index + 2 -gt $Bytes.Length) { Throw-Guard 'GZIP_TRUNCATED_FEXTRA_LENGTH' }
        $extraLength = [int](Get-U16LE $Bytes $index)
        $index += 2
        $optionalBytes += 2 + $extraLength
        if ($optionalBytes -gt 4096 -or $index + $extraLength -gt $Bytes.Length) { Throw-Guard 'GZIP_FEXTRA_LIMIT_OR_TRUNCATION' }
        $index += $extraLength
    }
    if (($flags -band 0x08) -ne 0) { Read-GzipZeroTerminatedField $Bytes ([ref]$index) ([ref]$optionalBytes) }
    if (($flags -band 0x10) -ne 0) { Read-GzipZeroTerminatedField $Bytes ([ref]$index) ([ref]$optionalBytes) }
    if (($flags -band 0x02) -ne 0) {
        if ($index + 2 -gt $Bytes.Length) { Throw-Guard 'GZIP_TRUNCATED_FHCRC' }
        [byte[]]$headerBytes = $Bytes[0..($index - 1)]
        $expectedHeaderCrc = [uint16]([Teoria.Q1R1V2.Crc32]::Compute($headerBytes) -band 0xFFFF)
        $actualHeaderCrc = Get-U16LE $Bytes $index
        if ($actualHeaderCrc -ne $expectedHeaderCrc) { Throw-Guard 'GZIP_FHCRC_MISMATCH' }
        $index += 2
    }

    if ($index + 8 -ge $Bytes.Length) { Throw-Guard 'GZIP_MISSING_DEFLATE_OR_TRAILER' }
    $input = [System.IO.MemoryStream]::new($Bytes, $false)
    $input.Position = $index
    $bounded = [Teoria.Q1R1V2.OneByteReadStream]::new($input)
    $output = [System.IO.MemoryStream]::new()
    try {
        $deflate = [System.IO.Compression.DeflateStream]::new(
            $bounded,
            [System.IO.Compression.CompressionMode]::Decompress,
            $true
        )
        try {
            [byte[]]$buffer = [byte[]]::new(65536)
            while (($read = $deflate.Read($buffer, 0, $buffer.Length)) -gt 0) {
                $output.Write($buffer, 0, $read)
                if ($output.Length -gt $MaxTarBytes) { Throw-Guard 'GZIP_DECOMPRESSED_SIZE_LIMIT' }
            }
        }
        finally {
            $deflate.Dispose()
        }

        $trailerOffset = [int]$input.Position
        if ($trailerOffset + 8 -ne $Bytes.Length) { Throw-Guard 'GZIP_SECOND_MEMBER_OR_TRAILING_BYTES' }
        [byte[]]$expanded = $output.ToArray()
        $actualCrc = [Teoria.Q1R1V2.Crc32]::Compute($expanded)
        $expectedCrc = Get-U32LE $Bytes $trailerOffset
        if ($actualCrc -ne $expectedCrc) { Throw-Guard 'GZIP_CRC32_MISMATCH' }
        $expectedSize = Get-U32LE $Bytes ($trailerOffset + 4)
        if ([uint32]($expanded.Length % 0x100000000L) -ne $expectedSize) { Throw-Guard 'GZIP_ISIZE_MISMATCH' }
        if (($expanded.Length / [double]$Bytes.Length) -gt $MaxCompressionRatio) { Throw-Guard 'COMPRESSION_RATIO_LIMIT' }
        return $expanded
    }
    finally {
        $output.Dispose()
        $bounded.Dispose()
        $input.Dispose()
    }
}

function Read-TarOctal {
    param([byte[]]$Bytes, [int]$Offset, [int]$Length, [string]$Field)
    if (($Bytes[$Offset] -band 0x80) -ne 0) { Throw-Guard "TAR_BASE256_NOT_ALLOWED_$Field" }
    $text = [System.Text.Encoding]::ASCII.GetString($Bytes, $Offset, $Length).Trim([char]0, [char]32)
    if ($text.Length -eq 0) { return 0L }
    if ($text -notmatch '^[0-7]+$') { Throw-Guard "TAR_NON_OCTAL_$Field" }
    try { return [Convert]::ToInt64($text, 8) }
    catch { Throw-Guard "TAR_OCTAL_OVERFLOW_$Field" }
}

function Test-TarFraming {
    param([Parameter(Mandatory = $true)][byte[]]$TarBytes)
    if ($TarBytes.Length -lt 1536 -or ($TarBytes.Length % 512) -ne 0) { Throw-Guard 'TAR_NON_512_FRAMING' }
    $position = 0L
    $entryCount = 0
    $largest = 0L
    $total = 0L

    while ($position + 512 -le $TarBytes.Length) {
        $offset = [int]$position
        if (Test-AllZero $TarBytes $offset 512) {
            if ($position + 1024 -ne $TarBytes.Length) { Throw-Guard 'TAR_TERMINATOR_NOT_EXACTLY_TWO_BLOCKS_AT_EOF' }
            if (-not (Test-AllZero $TarBytes ($offset + 512) 512)) { Throw-Guard 'TAR_SECOND_TERMINATOR_BLOCK_NONZERO' }
            if ($entryCount -lt 1) { Throw-Guard 'TAR_EMPTY_INVENTORY' }
            return [pscustomobject]@{ EntryCount = $entryCount; LargestEntry = $largest; TotalPayload = $total }
        }

        $storedChecksum = Read-TarOctal $TarBytes ($offset + 148) 8 'CHECKSUM'
        $computedChecksum = 0L
        for ($i = 0; $i -lt 512; $i++) {
            if ($i -ge 148 -and $i -lt 156) { $computedChecksum += 32 }
            else { $computedChecksum += $TarBytes[$offset + $i] }
        }
        if ($storedChecksum -ne $computedChecksum) { Throw-Guard 'TAR_HEADER_CHECKSUM_MISMATCH' }

        $size = Read-TarOctal $TarBytes ($offset + 124) 12 'SIZE'
        if ($size -lt 0 -or $size -gt $MaxEntryBytes) { Throw-Guard 'TAR_PER_ENTRY_LIMIT' }
        $typeFlag = $TarBytes[$offset + 156]
        if ($typeFlag -notin @(0, [byte][char]'0', [byte][char]'5')) { Throw-Guard 'TAR_UNSAFE_ENTRY_TYPE' }
        if ($typeFlag -eq [byte][char]'5' -and $size -ne 0) { Throw-Guard 'TAR_DIRECTORY_NONZERO_SIZE' }

        $entryCount++
        if ($entryCount -gt $MaxEntries) { Throw-Guard 'TAR_ENTRY_COUNT_LIMIT' }
        if ($size -gt $largest) { $largest = $size }
        $total += $size
        if ($total -gt $MaxTarBytes) { Throw-Guard 'TAR_TOTAL_PAYLOAD_LIMIT' }
        $dataBlocks = [long][Math]::Ceiling($size / 512.0)
        $paddingStart = $offset + 512 + [int]$size
        $paddingCount = [int](512 * $dataBlocks - $size)
        if ($paddingCount -gt 0 -and -not (Test-AllZero $TarBytes $paddingStart $paddingCount)) {
            Throw-Guard 'TAR_NONZERO_PADDING'
        }
        $position += 512 + 512 * $dataBlocks
        if ($position + 1024 -gt $TarBytes.Length) { Throw-Guard 'TAR_TRUNCATED_ENTRY_OR_TERMINATOR' }
    }
    Throw-Guard 'TAR_MISSING_TERMINATOR'
}

function Get-SafeArchiveName {
    param([string]$Name, [bool]$IsDirectory)
    if ([string]::IsNullOrWhiteSpace($Name)) { Throw-Guard 'TAR_EMPTY_PATH' }
    if ($IsDirectory -and $Name.EndsWith('/')) { $Name = $Name.Substring(0, $Name.Length - 1) }
    if ([string]::IsNullOrEmpty($Name)) { Throw-Guard 'TAR_EMPTY_PATH' }
    $nfc = $Name.Normalize([System.Text.NormalizationForm]::FormC)
    if ($nfc -cne $Name) { Throw-Guard 'TAR_PATH_NOT_NFC' }
    if ($Name.StartsWith('/') -or $Name.StartsWith('\\') -or $Name.StartsWith('-')) { Throw-Guard 'TAR_ABSOLUTE_UNC_OR_OPTION_PATH' }
    if ($Name.Contains('\') -or $Name.Contains(':') -or $Name.Contains([char]0)) { Throw-Guard 'TAR_BACKSLASH_DRIVE_ADS_OR_NUL_PATH' }
    foreach ($ch in $Name.ToCharArray()) {
        if ([char]::IsControl($ch)) { Throw-Guard 'TAR_CONTROL_CHARACTER_PATH' }
    }
    $segments = $Name.Split('/', [System.StringSplitOptions]::None)
    foreach ($segment in $segments) {
        if ($segment.Length -eq 0 -or $segment -eq '.' -or $segment -eq '..' -or $segment.StartsWith('-')) { Throw-Guard 'TAR_EMPTY_DOT_OR_OPTION_SEGMENT' }
        if ($segment.TrimEnd(' ', '.') -cne $segment) { Throw-Guard 'TAR_TRAILING_DOT_OR_SPACE_SEGMENT' }
        $base = $segment.Split('.')[0]
        if ($base -match '^(?i:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])$') { Throw-Guard 'TAR_WINDOWS_RESERVED_SEGMENT' }
    }
    return $Name
}

function Read-TarInventory {
    param([byte[]]$TarBytes, [int]$ExpectedEntryCount)
    $exact = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::Ordinal)
    $folded = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    $contents = [System.Collections.Hashtable]::new([System.StringComparer]::Ordinal)
    $types = [System.Collections.Hashtable]::new([System.StringComparer]::Ordinal)
    $inventory = [System.Collections.Generic.List[object]]::new()
    $stream = [System.IO.MemoryStream]::new($TarBytes, $false)
    $reader = [System.Formats.Tar.TarReader]::new($stream, $true)
    try {
        while (($entry = $reader.GetNextEntry($false)) -ne $null) {
            $entryType = $entry.EntryType.ToString()
            if ($entryType -notin @('RegularFile', 'V7RegularFile', 'Directory')) { Throw-Guard 'TAR_READER_UNSAFE_ENTRY_TYPE' }
            $isDirectory = $entryType -eq 'Directory'
            $name = Get-SafeArchiveName $entry.Name $isDirectory
            if (-not $exact.Add($name)) { Throw-Guard 'TAR_EXACT_PATH_COLLISION' }
            if (-not $folded.Add($name)) { Throw-Guard 'TAR_CASEFOLDED_PATH_COLLISION' }
            if ($entry.Length -lt 0 -or $entry.Length -gt $MaxEntryBytes) { Throw-Guard 'TAR_READER_ENTRY_LENGTH_LIMIT' }

            [byte[]]$data = [byte[]]::new(0)
            if (-not $isDirectory) {
                if ($null -eq $entry.DataStream) { Throw-Guard 'TAR_REGULAR_ENTRY_WITHOUT_DATASTREAM' }
                $memory = [System.IO.MemoryStream]::new()
                try {
                    $entry.DataStream.CopyTo($memory)
                    if ($memory.Length -ne $entry.Length) { Throw-Guard 'TAR_ENTRY_DECLARED_ACTUAL_LENGTH_MISMATCH' }
                    $data = $memory.ToArray()
                }
                finally { $memory.Dispose() }
                $contents[$name] = $data
            }
            $types[$name] = $entryType
            $inventory.Add([pscustomobject]@{ Name = $name; Type = $entryType; Length = [long]$entry.Length })
        }
    }
    finally {
        $reader.Dispose()
        $stream.Dispose()
    }
    if ($inventory.Count -ne $ExpectedEntryCount) { Throw-Guard 'TAR_BYTE_READER_ENTRY_COUNT_MISMATCH' }
    return [pscustomobject]@{ Inventory = $inventory; Contents = $contents; Types = $types }
}

function Remove-TexComments {
    param([string]$Text)
    $builder = [System.Text.StringBuilder]::new()
    foreach ($line in ($Text -split "`n", 0, 'SimpleMatch')) {
        $cut = $line.Length
        for ($i = 0; $i -lt $line.Length; $i++) {
            if ($line[$i] -ne '%') { continue }
            $slashes = 0
            for ($j = $i - 1; $j -ge 0 -and $line[$j] -eq '\'; $j--) { $slashes++ }
            if (($slashes % 2) -eq 0) { $cut = $i; break }
        }
        [void]$builder.AppendLine($line.Substring(0, $cut))
    }
    return $builder.ToString()
}

function Normalize-TexText {
    param([string]$Text)
    $clean = Remove-TexComments $Text
    $clean = [regex]::Replace($clean, '\\[A-Za-z@]+\*?', ' ')
    $clean = $clean.Replace('{', ' ').Replace('}', ' ').Replace('~', ' ')
    return ([regex]::Replace($clean, '\s+', ' ').Trim())
}

function Test-LiteralTexTarget {
    param([string]$Target)
    if ([string]::IsNullOrWhiteSpace($Target)) { return $false }
    if ($Target -match '[\\#$%{}~^`]') { return $false }
    if ($Target.Contains(':') -or $Target.Contains('\') -or $Target.StartsWith('/') -or $Target.StartsWith('-')) { return $false }
    return $true
}

function Resolve-TexTarget {
    param([string]$From, [string]$Directory, [string]$Target, [string]$DefaultExtension)
    if (-not (Test-LiteralTexTarget $Directory) -and -not [string]::IsNullOrEmpty($Directory)) { Throw-Guard 'TEX_DYNAMIC_OR_UNSAFE_DIRECTORY' }
    if (-not (Test-LiteralTexTarget $Target)) { Throw-Guard 'TEX_DYNAMIC_OR_UNSAFE_TARGET' }
    $fromDirectory = ''
    $slash = $From.LastIndexOf('/')
    if ($slash -ge 0) { $fromDirectory = $From.Substring(0, $slash) }
    $parts = [System.Collections.Generic.List[string]]::new()
    foreach ($piece in @($fromDirectory, $Directory, $Target)) {
        if ([string]::IsNullOrEmpty($piece)) { continue }
        foreach ($segment in $piece.Split('/', [System.StringSplitOptions]::None)) {
            if ($segment.Length -eq 0 -or $segment -eq '.' -or $segment -eq '..') { Throw-Guard 'TEX_EMPTY_DOT_OR_DOTDOT_TARGET' }
            $parts.Add($segment)
        }
    }
    $resolved = $parts -join '/'
    if ([string]::IsNullOrEmpty([System.IO.Path]::GetExtension($resolved)) -and -not [string]::IsNullOrEmpty($DefaultExtension)) {
        $resolved += $DefaultExtension
    }
    return $resolved
}

function Get-StrictUtf8TextMap {
    param([hashtable]$Contents)
    $utf8 = [System.Text.UTF8Encoding]::new($false, $true)
    $map = [System.Collections.Hashtable]::new([System.StringComparer]::Ordinal)
    foreach ($name in $Contents.Keys) {
        $extension = [System.IO.Path]::GetExtension($name).ToLowerInvariant()
        if ($extension -notin @('.tex', '.sty', '.cls', '.bib')) { continue }
        try { $map[$name] = $utf8.GetString([byte[]]$Contents[$name]) }
        catch { Throw-Guard "TEXT_SOURCE_NOT_STRICT_UTF8::$name" }
    }
    return $map
}

function Expand-LiteralTexSourceTargets {
    param([hashtable]$Contents, [hashtable]$TextMap)
    $oneArgSourcePattern = '\\(?<cmd>input|include|subfile)\s*\{(?<file>[^{}]+)\}'
    $twoArgSourcePattern = '\\(?<cmd>import|subimport|inputfrom|subinputfrom|includefrom|subincludefrom)\s*\{(?<dir>[^{}]*)\}\s*\{(?<file>[^{}]+)\}'
    $utf8 = [System.Text.UTF8Encoding]::new($false, $true)
    $queue = [System.Collections.Generic.Queue[string]]::new()
    $expanded = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::Ordinal)
    foreach ($initialName in @($TextMap.Keys | Sort-Object)) { $queue.Enqueue([string]$initialName) }

    while ($queue.Count -gt 0) {
        $name = $queue.Dequeue()
        if (-not $expanded.Add($name)) { continue }
        $clean = Remove-TexComments ([string]$TextMap[$name])
        $targets = [System.Collections.Generic.List[string]]::new()
        foreach ($match in [regex]::Matches($clean, $twoArgSourcePattern)) {
            try { $targets.Add((Resolve-TexTarget $name $match.Groups['dir'].Value $match.Groups['file'].Value '.tex')) }
            catch { }
        }
        foreach ($match in [regex]::Matches($clean, $oneArgSourcePattern)) {
            try { $targets.Add((Resolve-TexTarget $name '' $match.Groups['file'].Value '.tex')) }
            catch { }
        }
        foreach ($target in $targets) {
            if (-not $Contents.ContainsKey($target) -or $TextMap.ContainsKey($target)) { continue }
            try { $TextMap[$target] = $utf8.GetString([byte[]]$Contents[$target]) }
            catch { Throw-Guard "TEXT_SOURCE_NOT_STRICT_UTF8::$target" }
            $queue.Enqueue($target)
        }
    }
    return $TextMap
}

function Add-TexProblem {
    param([System.Collections.Generic.List[string]]$Problems, [string]$Code, [string]$Member)
    $Problems.Add("$Code::$Member")
}

function Test-SupportedTexLoaderInvocation {
    param([string]$Command, [string]$Tail)
    $escaped = [regex]::Escape($Command)
    switch ($Command) {
        { $_ -in @('input', 'include', 'subfile', 'verbatiminput') } {
            return $Tail -match "^\\$escaped\s*\{[^{}]+\}"
        }
        { $_ -in @('import', 'subimport', 'inputfrom', 'subinputfrom', 'includefrom', 'subincludefrom') } {
            return $Tail -match "^\\$escaped\s*\{[^{}]*\}\s*\{[^{}]+\}"
        }
        'bibliography' {
            return $Tail -match '^\\bibliography\s*\{[^{}]+\}'
        }
        'addbibresource' {
            return $Tail -match '^\\addbibresource\s*(?:\[[^\[\]{}]*\]\s*)?\{[^{}]+\}'
        }
        { $_ -in @('documentclass', 'usepackage', 'RequirePackage', 'lstinputlisting') } {
            return $Tail -match "^\\$escaped\s*(?:\[[^\[\]{}]*\]\s*)?\{[^{}]+\}"
        }
        default { return $false }
    }
}

function Get-TexAnalysis {
    param([hashtable]$Contents)
    $exactContents = [System.Collections.Hashtable]::new([System.StringComparer]::Ordinal)
    foreach ($contentName in $Contents.Keys) {
        $exactName = [string]$contentName
        if ($exactContents.ContainsKey($exactName)) { Throw-Guard "CONTENT_EXACT_PATH_COLLISION::$exactName" }
        $exactContents[$exactName] = [byte[]]$Contents[$contentName]
    }
    $Contents = $exactContents
    $textMap = Get-StrictUtf8TextMap $Contents
    $textMap = Expand-LiteralTexSourceTargets $Contents $textMap
    $roots = [System.Collections.Generic.List[string]]::new()
    foreach ($name in $textMap.Keys) {
        if ([System.IO.Path]::GetExtension($name).ToLowerInvariant() -ne '.tex') { continue }
        $clean = Remove-TexComments $textMap[$name]
        $normalized = (Normalize-TexText $clean).ToLowerInvariant()
        if ($clean -match '\\begin\s*\{document\}' -and $clean -match '\\end\s*\{document\}' -and
            $normalized.Contains('general relativistic bubble growth in cosmological phase transitions') -and
            $normalized.Contains('giombi') -and $normalized.Contains('hindmarsh')) {
            $roots.Add($name)
        }
    }
    if ($roots.Count -ne 1) { Throw-Guard 'Q1R1_MAIN_ROOT_IDENTITY_NOT_EXACTLY_ONE' }

    $problems = [System.Collections.Generic.List[string]]::new()
    $external = [System.Collections.Generic.List[string]]::new()
    $assets = [System.Collections.Generic.List[string]]::new()
    $graph = [System.Collections.Hashtable]::new([System.StringComparer]::Ordinal)
    foreach ($name in $textMap.Keys) { $graph[$name] = [System.Collections.Generic.List[string]]::new() }

    $oneArgPattern = '\\(?<cmd>input|include|subfile|verbatiminput)\s*\{(?<file>[^{}]+)\}'
    $twoArgPattern = '\\(?<cmd>import|subimport|inputfrom|subinputfrom|includefrom|subincludefrom)\s*\{(?<dir>[^{}]*)\}\s*\{(?<file>[^{}]+)\}'
    $bibPattern = '\\(?<cmd>bibliography)\s*\{(?<files>[^{}]+)\}|\\(?<cmd2>addbibresource)\s*(?:\[[^\[\]{}]*\])?\s*\{(?<file2>[^{}]+)\}'
    $packagePattern = '\\(?<cmd>documentclass|usepackage|RequirePackage)\s*(?:\[[^\[\]{}]*\])?\s*\{(?<files>[^{}]+)\}'
    $listingPattern = '\\lstinputlisting\s*(?:\[[^\[\]{}]*\])?\s*\{(?<file>[^{}]+)\}'
    $graphicsPattern = '\\includegraphics\s*(?:\[[^\[\]{}]*\])?\s*\{(?<file>[^{}]+)\}'
    $supportedNameList = @('input','include','subfile','verbatiminput','import','subimport','inputfrom','subinputfrom','includefrom','subincludefrom','bibliography','addbibresource','documentclass','usepackage','RequirePackage','lstinputlisting')
    $supportedNameSet = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::Ordinal)
    foreach ($supportedName in $supportedNameList) { [void]$supportedNameSet.Add($supportedName) }
    $supportedNames = $supportedNameList -join '|'
    $loaderStemPattern = 'input|include|import|load|file|bibliograph|bibresource|package|documentclass|listing'
    $sourceIoNameList = @('openin','closein','newread','read','readline','scantokens','everyeof')
    $sourceIoNames = $sourceIoNameList -join '|'
    $macroDefinitionStemPattern = 'def|command|environment'
    $resolvedSourceSpellings = [System.Collections.Hashtable]::new([System.StringComparer]::Ordinal)

    foreach ($name in $textMap.Keys) {
        $clean = Remove-TexComments $textMap[$name]
        if ($clean -match '\\catcode' -or $clean -match '\\csname' -or $clean -match '\\futurelet\b' -or
            $clean -match '\\cs_[A-Za-z_:]+' -or
            $clean -match "\\let\s*\\[A-Za-z@]+\s*(?:=\s*)?\\(?:$supportedNames)\b") {
            Add-TexProblem $problems 'UNSUPPORTED_DYNAMIC_MACRO_OR_CATCODE_LOADER' $name
        }
        foreach ($commandToken in [regex]::Matches($clean, '\\(?<name>[A-Za-z@]+)\*?')) {
            $commandName = $commandToken.Groups['name'].Value
            if ($commandName -match "(?i:$macroDefinitionStemPattern)") {
                $macroTail = $clean.Substring($commandToken.Index)
                if ($macroTail -match "\\[A-Za-z@]*(?i:$loaderStemPattern)[A-Za-z@]*\b" -or
                    $macroTail -match "\\(?i:$sourceIoNames)\b") {
                    Add-TexProblem $problems 'UNSUPPORTED_MACRO_CONTAINER_WITH_POTENTIAL_LOADER' $name
                }
            }
            if ($commandName -ceq 'includegraphics' -or $supportedNameSet.Contains($commandName)) { continue }
            if ($commandName -match "(?i:$loaderStemPattern)" -or $commandName -match "^(?i:$sourceIoNames)$") {
                Add-TexProblem $problems "UNSUPPORTED_POTENTIAL_LOADER_$commandName" $name
            }
        }

        foreach ($match in [regex]::Matches($clean, $twoArgPattern)) {
            try {
                $target = Resolve-TexTarget $name $match.Groups['dir'].Value $match.Groups['file'].Value '.tex'
                if (-not $textMap.ContainsKey($target)) { Add-TexProblem $problems "MISSING_TEX_TARGET_$target" $name }
                else { $graph[$name].Add($target) }
            } catch { Add-TexProblem $problems $_.Exception.Message $name }
        }
        foreach ($match in [regex]::Matches($clean, $oneArgPattern)) {
            try {
                $defaultExtension = if ($match.Groups['cmd'].Value -eq 'verbatiminput') { '' } else { '.tex' }
                $rawTarget = $match.Groups['file'].Value
                $target = Resolve-TexTarget $name '' $rawTarget $defaultExtension
                $aliasKey = $name + [char]31 + $target
                if ($resolvedSourceSpellings.ContainsKey($aliasKey) -and $resolvedSourceSpellings[$aliasKey] -cne $rawTarget) {
                    Add-TexProblem $problems "AMBIGUOUS_SOURCE_TARGET_ALIAS_$target" $name
                } else { $resolvedSourceSpellings[$aliasKey] = $rawTarget }
                if (-not $Contents.ContainsKey($target)) { Add-TexProblem $problems "MISSING_SOURCE_TARGET_$target" $name }
                elseif ($match.Groups['cmd'].Value -ne 'verbatiminput' -and $textMap.ContainsKey($target)) { $graph[$name].Add($target) }
            } catch { Add-TexProblem $problems $_.Exception.Message $name }
        }
        foreach ($match in [regex]::Matches($clean, $listingPattern)) {
            try {
                $target = Resolve-TexTarget $name '' $match.Groups['file'].Value ''
                if (-not $Contents.ContainsKey($target)) { Add-TexProblem $problems "MISSING_LISTING_TARGET_$target" $name }
            } catch { Add-TexProblem $problems $_.Exception.Message $name }
        }
        foreach ($match in [regex]::Matches($clean, $bibPattern)) {
            $rawFiles = if ($match.Groups['files'].Success) { $match.Groups['files'].Value } else { $match.Groups['file2'].Value }
            foreach ($raw in $rawFiles.Split(',')) {
                try {
                    $target = Resolve-TexTarget $name '' $raw.Trim() '.bib'
                    if (-not $textMap.ContainsKey($target)) { Add-TexProblem $problems "MISSING_BIB_TARGET_$target" $name }
                    else { $graph[$name].Add($target) }
                } catch { Add-TexProblem $problems $_.Exception.Message $name }
            }
        }
        foreach ($match in [regex]::Matches($clean, $packagePattern)) {
            $command = $match.Groups['cmd'].Value
            $extension = if ($command -eq 'documentclass') { '.cls' } else { '.sty' }
            foreach ($raw in $match.Groups['files'].Value.Split(',')) {
                try {
                    $target = Resolve-TexTarget $name '' $raw.Trim() $extension
                    if ($textMap.ContainsKey($target)) { $graph[$name].Add($target) }
                    else { $external.Add("$command::$raw::$name") }
                } catch { Add-TexProblem $problems $_.Exception.Message $name }
            }
        }
        foreach ($match in [regex]::Matches($clean, $graphicsPattern)) {
            $assets.Add("$name::$($match.Groups['file'].Value)")
        }
        foreach ($token in [regex]::Matches($clean, '\\includegraphics\b')) {
            $tail = $clean.Substring($token.Index, [Math]::Min(2048, $clean.Length - $token.Index))
            if ($tail -notmatch '^\\includegraphics\s*(?:\[[^\[\]{}]*\]\s*)?\{[^{}]+\}') {
                Add-TexProblem $problems 'UNPARSEABLE_OR_NONLITERAL_ASSET_REFERENCE' $name
            }
        }

        foreach ($token in [regex]::Matches($clean, "\\(?<cmd>$supportedNames)\b")) {
            $tail = $clean.Substring($token.Index, [Math]::Min(2048, $clean.Length - $token.Index))
            if (-not (Test-SupportedTexLoaderInvocation $token.Groups['cmd'].Value $tail)) {
                Add-TexProblem $problems 'UNPARSEABLE_OR_NONLITERAL_SUPPORTED_LOADER' $name
            }
        }
    }

    $colors = [System.Collections.Hashtable]::new([System.StringComparer]::Ordinal)
    foreach ($name in $graph.Keys) { $colors[$name] = 0 }
    function Visit-Node([string]$node) {
        if ($colors[$node] -eq 1) { Add-TexProblem $problems 'TEX_DEPENDENCY_CYCLE' $node; return }
        if ($colors[$node] -eq 2) { return }
        $colors[$node] = 1
        foreach ($child in $graph[$node]) { Visit-Node $child }
        $colors[$node] = 2
    }
    Visit-Node $roots[0]

    $reachable = @($colors.Keys | Where-Object { $colors[$_] -eq 2 } | Sort-Object)
    $allText = @($textMap.Keys | Sort-Object)
    $status = if ($problems.Count -gt 0) { 'UNRESOLVED_SOURCE_CLOSURE' } else { 'REQUIRES_MANUAL_ALL_TEXT_REVIEW' }
    return [pscustomobject]@{
        Root = $roots[0]
        ClosureStatus = $status
        Problems = @($problems)
        ExternalTexDependencies = @($external)
        AssetReferences = @($assets)
        ReachableTextMembers = $reachable
        AllTextMembers = $allText
        ManualAllTextInventoryRequired = $true
    }
}

function Test-ArchiveBytes {
    param(
        [Parameter(Mandatory = $true)][byte[]]$Bytes,
        [switch]$SkipMinimumHttpSize,
        [switch]$ForceDeadlineExpired
    )
    $stopwatch = [System.Diagnostics.Stopwatch]::StartNew()
    $representation = 'RAW_TAR'
    [byte[]]$tarBytes = $Bytes
    if ($Bytes.Length -ge 2 -and $Bytes[0] -eq 0x1F -and $Bytes[1] -eq 0x8B) {
        $representation = 'SINGLE_GZIP_MEMBER_TAR'
        $tarBytes = Expand-SingleGzipMember $Bytes
    }
    $framing = Test-TarFraming $tarBytes
    $parsed = Read-TarInventory $tarBytes $framing.EntryCount
    $tex = Get-TexAnalysis $parsed.Contents
    $elapsed = if ($ForceDeadlineExpired) { $ValidationDeadlineSeconds + 1.0 } else { $stopwatch.Elapsed.TotalSeconds }
    Assert-ArchiveLimits $Bytes.Length $tarBytes.Length $framing.EntryCount $framing.LargestEntry $elapsed -SkipMinimumHttpSize:$SkipMinimumHttpSize
    $inventoryLines = @($parsed.Inventory | ForEach-Object { "$($_.Type)`t$($_.Length)`t$($_.Name)" })
    $inventoryDigest = Get-Sha256Hex ([System.Text.Encoding]::UTF8.GetBytes(($inventoryLines -join "`n")))
    return [pscustomobject]@{
        Representation = $representation
        ResponseSha256 = Get-Sha256Hex $Bytes
        TarSha256 = Get-Sha256Hex $tarBytes
        ResponseBytes = $Bytes.Length
        TarBytes = $tarBytes.Length
        EntryCount = $framing.EntryCount
        InventoryDigestSha256 = $inventoryDigest
        MainRoot = $tex.Root
        ClosureStatus = $tex.ClosureStatus
        ClosureProblems = $tex.Problems
        ExternalTexDependencies = $tex.ExternalTexDependencies
        AssetReferences = $tex.AssetReferences
        ReachableTextMembers = $tex.ReachableTextMembers
        AllTextMembers = $tex.AllTextMembers
        ManualAllTextInventoryRequired = $tex.ManualAllTextInventoryRequired
        ValidationSeconds = $stopwatch.Elapsed.TotalSeconds
    }
}

function Set-AsciiField {
    param([byte[]]$Buffer, [int]$Offset, [int]$Length, [string]$Text)
    [byte[]]$encoded = [System.Text.Encoding]::ASCII.GetBytes($Text)
    if ($encoded.Length -gt $Length) { Throw-Guard 'SELFTEST_TAR_FIELD_TOO_LONG' }
    [Array]::Copy($encoded, 0, $Buffer, $Offset, $encoded.Length)
}

function Set-TarChecksum {
    param([byte[]]$Header)
    for ($i = 148; $i -lt 156; $i++) { $Header[$i] = 32 }
    $sum = 0L
    foreach ($value in $Header) { $sum += $value }
    $text = [Convert]::ToString($sum, 8).PadLeft(6, '0') + "`0 "
    Set-AsciiField $Header 148 8 $text
}

function New-TestTar {
    param([Parameter(Mandatory = $true)][object[]]$Entries, [int]$TerminalZeroBlocks = 2)
    $bytes = [System.Collections.Generic.List[byte]]::new()
    foreach ($item in $Entries) {
        $header = [byte[]]::new(512)
        Set-AsciiField $header 0 100 ([string]$item.Name)
        Set-AsciiField $header 100 8 "0000644`0"
        Set-AsciiField $header 108 8 "0000000`0"
        Set-AsciiField $header 116 8 "0000000`0"
        [byte[]]$data = if ($null -eq $item.Data) { [byte[]]::new(0) } else { [byte[]]$item.Data }
        Set-AsciiField $header 124 12 ([Convert]::ToString($data.Length, 8).PadLeft(11, '0') + "`0")
        Set-AsciiField $header 136 12 "00000000000`0"
        $header[156] = if ($null -eq $item.TypeFlag) { [byte][char]'0' } else { [byte]$item.TypeFlag }
        Set-AsciiField $header 257 6 "ustar`0"
        Set-AsciiField $header 263 2 '00'
        Set-TarChecksum $header
        $bytes.AddRange($header)
        if ($data.Length -gt 0) { $bytes.AddRange($data) }
        $padding = (512 - ($data.Length % 512)) % 512
        if ($padding -gt 0) { $bytes.AddRange([byte[]]::new($padding)) }
    }
    if ($TerminalZeroBlocks -gt 0) { $bytes.AddRange([byte[]]::new(512 * $TerminalZeroBlocks)) }
    return $bytes.ToArray()
}

function New-TestGzip {
    param([byte[]]$Data)
    $memory = [System.IO.MemoryStream]::new()
    $gzip = [System.IO.Compression.GZipStream]::new($memory, [System.IO.Compression.CompressionLevel]::Optimal, $true)
    try { $gzip.Write($Data, 0, $Data.Length) }
    finally { $gzip.Dispose() }
    [byte[]]$result = $memory.ToArray()
    $memory.Dispose()
    return $result
}

function New-FhcrcGzip {
    param([byte[]]$Gzip)
    if ($Gzip[3] -ne 0) { Throw-Guard 'SELFTEST_EXPECTED_PLAIN_GZIP_HEADER' }
    $result = [byte[]]::new($Gzip.Length + 2)
    [Array]::Copy($Gzip, 0, $result, 0, 10)
    $result[3] = 0x02
    [byte[]]$header = $result[0..9]
    $crc16 = [uint16]([Teoria.Q1R1V2.Crc32]::Compute($header) -band 0xFFFF)
    $result[10] = [byte]($crc16 -band 0xFF)
    $result[11] = [byte](($crc16 -shr 8) -band 0xFF)
    [Array]::Copy($Gzip, 10, $result, 12, $Gzip.Length - 10)
    return $result
}

function Invoke-SelfTest {
    $stats = [ordered]@{
        Passed = 0
        Failed = [System.Collections.Generic.List[string]]::new()
        Names = [System.Collections.Generic.List[string]]::new()
    }
    function Assert-Pass([string]$Name, [scriptblock]$Body) {
        $stats.Names.Add($Name)
        try { & $Body; $stats.Passed = [int]$stats.Passed + 1 }
        catch { $stats.Failed.Add("$Name::$($_.Exception.Message)") }
    }
    function Assert-Reject([string]$Name, [string]$Expected, [scriptblock]$Body) {
        $stats.Names.Add($Name)
        try { & $Body; $stats.Failed.Add("$Name::DID_NOT_REJECT") }
        catch {
            if ($_.Exception.Message -like "*$Expected*") { $stats.Passed = [int]$stats.Passed + 1 }
            else { $stats.Failed.Add("$Name::WRONG_GUARD::$($_.Exception.Message)") }
        }
    }
    function Assert-ExactStringSet([object[]]$Actual, [string[]]$Expected, [string]$Guard) {
        $actualLines = @($Actual | ForEach-Object { [string]$_ } | Sort-Object)
        $expectedLines = @($Expected | Sort-Object)
        if (($actualLines -join "`n") -cne ($expectedLines -join "`n")) {
            Throw-Guard "$Guard::ACTUAL=$($actualLines -join ',')::EXPECTED=$($expectedLines -join ',')"
        }
    }
    function Assert-HasExactString([object[]]$Actual, [string]$Expected, [string]$Guard) {
        $actualSet = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::Ordinal)
        foreach ($value in $Actual) { [void]$actualSet.Add([string]$value) }
        if (-not $actualSet.Contains($Expected)) { Throw-Guard "$Guard::MISSING=$Expected" }
    }

    $root = @'
\documentclass{article}
\title{General relativistic bubble growth in cosmological phase transitions}
\author{Giombi and Hindmarsh}
\begin{document}
Model, equation, boundary, energy-momentum and conservation treatment.
\end{document}
'@
    $rootBytes = [System.Text.Encoding]::UTF8.GetBytes($root)
    $validTar = New-TestTar @([pscustomobject]@{ Name = 'main.tex'; Data = $rootBytes; TypeFlag = [byte][char]'0' })
    $validGzip = New-TestGzip $validTar
    $fhcrcGzip = New-FhcrcGzip $validGzip

    Assert-Pass 'VALID_RAW_TAR' { [void](Test-ArchiveBytes $validTar -SkipMinimumHttpSize) }
    Assert-Pass 'VALID_SINGLE_GZIP_TAR' { [void](Test-ArchiveBytes $validGzip -SkipMinimumHttpSize) }
    Assert-Pass 'VALID_FHCRC_GZIP_TAR' { [void](Test-ArchiveBytes $fhcrcGzip -SkipMinimumHttpSize) }

    [byte[]]$badCrc = $validGzip.Clone(); $badCrc[$badCrc.Length - 8] = $badCrc[$badCrc.Length - 8] -bxor 1
    Assert-Reject 'BAD_GZIP_CRC32' 'GZIP_CRC32_MISMATCH' { [void](Expand-SingleGzipMember $badCrc) }
    [byte[]]$badIsize = $validGzip.Clone(); $badIsize[$badIsize.Length - 4] = $badIsize[$badIsize.Length - 4] -bxor 1
    Assert-Reject 'BAD_GZIP_ISIZE' 'GZIP_ISIZE_MISMATCH' { [void](Expand-SingleGzipMember $badIsize) }
    [byte[]]$badFhcrc = $fhcrcGzip.Clone(); $badFhcrc[10] = $badFhcrc[10] -bxor 1
    Assert-Reject 'BAD_GZIP_FHCRC' 'GZIP_FHCRC_MISMATCH' { [void](Expand-SingleGzipMember $badFhcrc) }
    [byte[]]$concatenated = $validGzip + $validGzip
    Assert-Reject 'CONCATENATED_GZIP' 'GZIP_SECOND_MEMBER_OR_TRAILING_BYTES' { [void](Expand-SingleGzipMember $concatenated) }
    [byte[]]$gzipTrailing = $validGzip + [byte]1
    Assert-Reject 'GZIP_TRAILING_BYTE' 'GZIP_SECOND_MEMBER_OR_TRAILING_BYTES' { [void](Expand-SingleGzipMember $gzipTrailing) }

    [byte[]]$badChecksum = $validTar.Clone(); $badChecksum[0] = $badChecksum[0] -bxor 1
    Assert-Reject 'TAR_BAD_CHECKSUM' 'TAR_HEADER_CHECKSUM_MISMATCH' { [void](Test-TarFraming $badChecksum) }
    [byte[]]$non512 = $validTar + [byte]0
    Assert-Reject 'TAR_NON512' 'TAR_NON_512_FRAMING' { [void](Test-TarFraming $non512) }
    $missingTerminator = New-TestTar @([pscustomobject]@{ Name = 'main.tex'; Data = $rootBytes; TypeFlag = [byte][char]'0' }) 1
    Assert-Reject 'TAR_MISSING_SECOND_ZERO_BLOCK' 'TAR_TRUNCATED_ENTRY_OR_TERMINATOR' { [void](Test-TarFraming $missingTerminator) }
    $extraTerminator = New-TestTar @([pscustomobject]@{ Name = 'main.tex'; Data = $rootBytes; TypeFlag = [byte][char]'0' }) 3
    Assert-Reject 'TAR_EXTRA_TERMINATOR' 'TAR_TERMINATOR_NOT_EXACTLY_TWO_BLOCKS_AT_EOF' { [void](Test-TarFraming $extraTerminator) }
    [byte[]]$nonzeroPadding = $validTar.Clone(); $nonzeroPadding[512 + $rootBytes.Length] = 1
    Assert-Reject 'TAR_NONZERO_DATA_PADDING' 'TAR_NONZERO_PADDING' { [void](Test-TarFraming $nonzeroPadding) }
    [byte[]]$trailingBlock = [byte[]]::new(512); $trailingBlock[0] = 1
    [byte[]]$trailingNonzero = $validTar + $trailingBlock
    Assert-Reject 'TAR_TRAILING_NONZERO_BLOCK' 'TAR_TERMINATOR_NOT_EXACTLY_TWO_BLOCKS_AT_EOF' { [void](Test-TarFraming $trailingNonzero) }

    foreach ($type in @('1','2','3','4','6','7','s','S','x','g','K','L','D','M','N','V')) {
        $unsafeTypeTar = New-TestTar @([pscustomobject]@{ Name = 'main.tex'; Data = $rootBytes; TypeFlag = [byte][char]$type })
        Assert-Reject "TAR_UNSAFE_TYPE_$type" 'TAR_UNSAFE_ENTRY_TYPE' { [void](Test-TarFraming $unsafeTypeTar) }
    }
    foreach ($path in @('../x.tex','/abs.tex','C:/x.tex','a\b.tex','CON.txt','-x.tex','a./x.tex','a//x.tex','a:b.tex')) {
        Assert-Reject "UNSAFE_PATH_$path" 'TAR_' { [void](Get-SafeArchiveName $path $false) }
    }
    $collisionTar = New-TestTar @(
        [pscustomobject]@{ Name = 'A.tex'; Data = $rootBytes; TypeFlag = [byte][char]'0' },
        [pscustomobject]@{ Name = 'a.tex'; Data = $rootBytes; TypeFlag = [byte][char]'0' }
    )
    Assert-Reject 'CASEFOLDED_COLLISION' 'TAR_CASEFOLDED_PATH_COLLISION' {
        $frame = Test-TarFraming $collisionTar; [void](Read-TarInventory $collisionTar $frame.EntryCount)
    }
    $exactCollisionTar = New-TestTar @(
        [pscustomobject]@{ Name = 'same.tex'; Data = $rootBytes; TypeFlag = [byte][char]'0' },
        [pscustomobject]@{ Name = 'same.tex'; Data = $rootBytes; TypeFlag = [byte][char]'0' }
    )
    Assert-Reject 'EXACT_COLLISION' 'TAR_EXACT_PATH_COLLISION' {
        $frame = Test-TarFraming $exactCollisionTar; [void](Read-TarInventory $exactCollisionTar $frame.EntryCount)
    }

    Assert-Reject 'COMPRESSED_BELOW_MINIMUM' 'HTTP_SIZE_BELOW_MINIMUM' { Assert-ArchiveLimits ($MinHttpBytes - 1) 20000 1 1 0 }
    Assert-Reject 'COMPRESSED_ABOVE_MAXIMUM' 'HTTP_SIZE_ABOVE_MAXIMUM' { Assert-ArchiveLimits ($MaxHttpBytes + 1) 20000 1 1 0 }
    Assert-Reject 'COMPRESSED_NONPOSITIVE' 'COMPRESSED_SIZE_NONPOSITIVE' { Assert-ArchiveLimits 0 1 1 1 0 -SkipMinimumHttpSize }
    Assert-Reject 'ZERO_ENTRY_COUNT' 'TAR_ENTRY_COUNT_LIMIT' { Assert-ArchiveLimits 10000 20000 0 1 0 }
    Assert-Reject 'COUNT_LIMIT' 'TAR_ENTRY_COUNT_LIMIT' { Assert-ArchiveLimits 10000 20000 ($MaxEntries + 1) 1 0 }
    Assert-Reject 'PER_ENTRY_LIMIT' 'TAR_PER_ENTRY_LIMIT' { Assert-ArchiveLimits 10000 20000 1 ($MaxEntryBytes + 1) 0 }
    Assert-Reject 'TOTAL_LIMIT' 'TAR_SIZE_ABOVE_MAXIMUM' { Assert-ArchiveLimits 10000 ($MaxTarBytes + 1) 1 1 0 }
    Assert-Reject 'RATIO_LIMIT' 'COMPRESSION_RATIO_LIMIT' { Assert-ArchiveLimits 10000 500000 1 1 0 }
    Assert-Reject 'DEADLINE_LIMIT' 'ARCHIVE_VALIDATION_DEADLINE' { Assert-ArchiveLimits 10000 20000 1 1 ($ValidationDeadlineSeconds + 1) }
    Assert-Pass 'EXACT_MINIMUM_HTTP_AND_ENTRY_COUNT_ACCEPTED' { Assert-ArchiveLimits $MinHttpBytes $MinHttpBytes 1 1 0 }
    Assert-Pass 'EXACT_MAXIMUM_HTTP_TAR_COUNT_ENTRY_AND_DEADLINE_ACCEPTED' { Assert-ArchiveLimits $MaxHttpBytes $MaxTarBytes $MaxEntries $MaxEntryBytes $ValidationDeadlineSeconds }
    Assert-Pass 'EXACT_MAXIMUM_COMPRESSION_RATIO_ACCEPTED' { Assert-ArchiveLimits 10000 ([long](10000 * $MaxCompressionRatio)) 1 1 0 }

    $loaderMap = @{ 'main.tex' = $rootBytes }
    $loaderText = $root.Replace('\end{document}', @'
\input{a}\include{b}\subfile{c}
\import{d}{e}\subimport{f}{g}\inputfrom{h}{i}\subinputfrom{j}{k}
\includefrom{l}{m}\subincludefrom{n}{o}
\bibliography{refs}\addbibresource{refs2.bib}
\usepackage{local}\RequirePackage{local2}\lstinputlisting{code.txt}\verbatiminput{note.txt}
\end{document}
'@)
    $loaderMap['main.tex'] = [System.Text.Encoding]::UTF8.GetBytes($loaderText)
    foreach ($file in @('a.tex','b.tex','c.tex','d/e.tex','f/g.tex','h/i.tex','j/k.tex','l/m.tex','n/o.tex')) { $loaderMap[$file] = [System.Text.Encoding]::UTF8.GetBytes('text') }
    $loaderMap['refs.bib'] = [System.Text.Encoding]::UTF8.GetBytes('@article{x}')
    $loaderMap['refs2.bib'] = [System.Text.Encoding]::UTF8.GetBytes('@article{y}')
    $loaderMap['local.sty'] = [System.Text.Encoding]::UTF8.GetBytes('\input{styledep}')
    $loaderMap['styledep.tex'] = [System.Text.Encoding]::UTF8.GetBytes('style')
    $loaderMap['local2.sty'] = [System.Text.Encoding]::UTF8.GetBytes('style2')
    $loaderMap['code.txt'] = [System.Text.Encoding]::UTF8.GetBytes('code')
    $loaderMap['note.txt'] = [System.Text.Encoding]::UTF8.GetBytes('note')
    Assert-Pass 'ALL_SUPPORTED_LITERAL_LOADERS_AND_LOCAL_STYLE_RECURSION' {
        $analysis = Get-TexAnalysis $loaderMap
        $sortedProblems = @($analysis.Problems | ForEach-Object { [string]$_ } | Sort-Object)
        if ($sortedProblems.Count -ne 0) { Throw-Guard "SELFTEST_LOADER_PROBLEMS::$($sortedProblems -join '|')" }
        if ($analysis.ClosureStatus -ne 'REQUIRES_MANUAL_ALL_TEXT_REVIEW') { Throw-Guard "SELFTEST_LOADER_CLOSURE_NOT_CLEAN::$($analysis.ClosureStatus)" }
        Assert-ExactStringSet $analysis.ReachableTextMembers @(
            'main.tex','a.tex','b.tex','c.tex','d/e.tex','f/g.tex','h/i.tex','j/k.tex','l/m.tex','n/o.tex',
            'refs.bib','refs2.bib','local.sty','styledep.tex','local2.sty'
        ) 'SELFTEST_LOADER_REACHABLE_SET_MISMATCH'
    }

    $classRoot = $root.Replace('\documentclass{article}', '\documentclass{local}')
    $classMap = @{
        'main.tex' = [System.Text.Encoding]::UTF8.GetBytes($classRoot)
        'local.cls' = [System.Text.Encoding]::UTF8.GetBytes('\input{classdep}')
        'classdep.tex' = [System.Text.Encoding]::UTF8.GetBytes('class dependency')
    }
    Assert-Pass 'LOCAL_CLASS_RECURSION' {
        $analysis = Get-TexAnalysis $classMap
        if ($analysis.ClosureStatus -ne 'REQUIRES_MANUAL_ALL_TEXT_REVIEW') { Throw-Guard 'SELFTEST_LOCAL_CLASS_RECURSION_NOT_CLEAN' }
        Assert-ExactStringSet $analysis.ReachableTextMembers @('main.tex','local.cls','classdep.tex') 'SELFTEST_CLASS_REACHABLE_SET_MISMATCH'
    }

    $ambiguousMap = @{
        'main.tex' = [System.Text.Encoding]::UTF8.GetBytes($root.Replace('\end{document}', '\input{dep}\include{dep.tex}\end{document}'))
        'dep.tex' = [System.Text.Encoding]::UTF8.GetBytes('aliased dependency')
    }
    Assert-Pass 'AMBIGUOUS_TEX_TARGET_IS_UNRESOLVED' {
        $analysis = Get-TexAnalysis $ambiguousMap
        if ($analysis.ClosureStatus -ne 'UNRESOLVED_SOURCE_CLOSURE') { Throw-Guard 'SELFTEST_AMBIGUOUS_TARGET_NOT_UNRESOLVED' }
        Assert-ExactStringSet $analysis.ReachableTextMembers @('main.tex','dep.tex') 'SELFTEST_AMBIGUOUS_REACHABLE_SET_MISMATCH'
        Assert-HasExactString $analysis.Problems 'AMBIGUOUS_SOURCE_TARGET_ALIAS_dep.tex::main.tex' 'SELFTEST_AMBIGUOUS_PROBLEM_MISMATCH'
    }

    $missingBibMap = @{ 'main.tex' = [System.Text.Encoding]::UTF8.GetBytes($root.Replace('\end{document}', '\bibliography{missing}\end{document}')) }
    Assert-Pass 'MISSING_BIBLIOGRAPHY_IS_UNRESOLVED' {
        $analysis = Get-TexAnalysis $missingBibMap
        if ($analysis.ClosureStatus -ne 'UNRESOLVED_SOURCE_CLOSURE') { Throw-Guard 'SELFTEST_MISSING_BIB_NOT_UNRESOLVED' }
    }
    $missingTexMap = @{ 'main.tex' = [System.Text.Encoding]::UTF8.GetBytes($root.Replace('\end{document}', '\input{missing}\end{document}')) }
    Assert-Pass 'MISSING_TEX_DEPENDENCY_IS_UNRESOLVED' {
        $analysis = Get-TexAnalysis $missingTexMap
        if ($analysis.ClosureStatus -ne 'UNRESOLVED_SOURCE_CLOSURE') { Throw-Guard 'SELFTEST_MISSING_TEX_NOT_UNRESOLVED' }
        Assert-ExactStringSet $analysis.ReachableTextMembers @('main.tex') 'SELFTEST_MISSING_TEX_REACHABLE_SET_MISMATCH'
        Assert-HasExactString $analysis.Problems 'MISSING_SOURCE_TARGET_missing.tex::main.tex' 'SELFTEST_MISSING_TEX_PROBLEM_MISMATCH'
    }
    $wrongCaseMap = @{
        'main.tex' = [System.Text.Encoding]::UTF8.GetBytes($root.Replace('\end{document}', '\input{dep}\end{document}'))
        'Dep.tex' = [System.Text.Encoding]::UTF8.GetBytes('wrong-case dependency')
    }
    Assert-Pass 'WRONG_CASE_TEX_TARGET_IS_UNRESOLVED' {
        $analysis = Get-TexAnalysis $wrongCaseMap
        if ($analysis.ClosureStatus -ne 'UNRESOLVED_SOURCE_CLOSURE') { Throw-Guard 'SELFTEST_WRONG_CASE_TARGET_NOT_UNRESOLVED' }
        Assert-ExactStringSet $analysis.ReachableTextMembers @('main.tex') 'SELFTEST_WRONG_CASE_REACHABLE_SET_MISMATCH'
        Assert-HasExactString $analysis.Problems 'MISSING_SOURCE_TARGET_dep.tex::main.tex' 'SELFTEST_WRONG_CASE_PROBLEM_MISMATCH'
    }
    $alternateExtensionMap = @{
        'main.tex' = [System.Text.Encoding]::UTF8.GetBytes($root.Replace('\end{document}', '\input{nested.inc}\end{document}'))
        'nested.inc' = [System.Text.Encoding]::UTF8.GetBytes('\input{missing}')
    }
    Assert-Pass 'ALTERNATE_EXTENSION_NESTED_MISSING_IS_UNRESOLVED' {
        $analysis = Get-TexAnalysis $alternateExtensionMap
        if ($analysis.ClosureStatus -ne 'UNRESOLVED_SOURCE_CLOSURE') { Throw-Guard 'SELFTEST_ALTERNATE_EXTENSION_NOT_UNRESOLVED' }
        Assert-ExactStringSet $analysis.ReachableTextMembers @('main.tex','nested.inc') 'SELFTEST_ALTERNATE_EXTENSION_REACHABLE_SET_MISMATCH'
        Assert-HasExactString $analysis.Problems 'MISSING_SOURCE_TARGET_missing.tex::nested.inc' 'SELFTEST_ALTERNATE_EXTENSION_PROBLEM_MISMATCH'
    }
    $relativeSiblingMap = @{
        'sub/main.tex' = [System.Text.Encoding]::UTF8.GetBytes($root.Replace('\end{document}', '\input{nested.inc}\end{document}'))
        'sub/nested.inc' = [System.Text.Encoding]::UTF8.GetBytes('\input{leaf}')
        'sub/leaf.tex' = [System.Text.Encoding]::UTF8.GetBytes('relative sibling leaf')
        'nested.inc' = [System.Text.Encoding]::UTF8.GetBytes('\input{root-decoy-missing}')
    }
    Assert-Pass 'INCLUDER_RELATIVE_SIBLING_WITHOUT_ROOT_FALLBACK' {
        $analysis = Get-TexAnalysis $relativeSiblingMap
        if ($analysis.ClosureStatus -ne 'REQUIRES_MANUAL_ALL_TEXT_REVIEW') { Throw-Guard 'SELFTEST_RELATIVE_SIBLING_NOT_CLEAN' }
        Assert-ExactStringSet $analysis.ReachableTextMembers @('sub/main.tex','sub/nested.inc','sub/leaf.tex') 'SELFTEST_RELATIVE_SIBLING_REACHABLE_SET_MISMATCH'
        Assert-ExactStringSet $analysis.AllTextMembers @('sub/main.tex','sub/nested.inc','sub/leaf.tex') 'SELFTEST_RELATIVE_SIBLING_ALL_TEXT_SET_MISMATCH'
    }
    $dynamicMap = @{ 'main.tex' = [System.Text.Encoding]::UTF8.GetBytes($root.Replace('\end{document}', '\csname input\endcsname{hidden}\end{document}')) }
    Assert-Pass 'DYNAMIC_LOADER_IS_UNRESOLVED' {
        $analysis = Get-TexAnalysis $dynamicMap
        if ($analysis.ClosureStatus -ne 'UNRESOLVED_SOURCE_CLOSURE') { Throw-Guard 'SELFTEST_DYNAMIC_NOT_UNRESOLVED' }
    }
    $unsupportedMap = @{ 'main.tex' = [System.Text.Encoding]::UTF8.GetBytes($root.Replace('\end{document}', '\InputIfFileExists{hidden.tex}{}{}\end{document}')) }
    Assert-Pass 'UNSUPPORTED_LOADER_IS_UNRESOLVED' {
        $analysis = Get-TexAnalysis $unsupportedMap
        if ($analysis.ClosureStatus -ne 'UNRESOLVED_SOURCE_CLOSURE') { Throw-Guard 'SELFTEST_UNSUPPORTED_LOADER_NOT_UNRESOLVED' }
    }
    $caseVariantMap = @{ 'main.tex' = [System.Text.Encoding]::UTF8.GetBytes($root.Replace('\end{document}', '\Input{hidden}\end{document}')) }
    Assert-Pass 'CASE_VARIANT_LOADER_IS_UNRESOLVED' {
        $analysis = Get-TexAnalysis $caseVariantMap
        if ($analysis.ClosureStatus -ne 'UNRESOLVED_SOURCE_CLOSURE') { Throw-Guard 'SELFTEST_CASE_VARIANT_LOADER_NOT_UNRESOLVED' }
    }
    $sourceIoMap = @{ 'main.tex' = [System.Text.Encoding]::UTF8.GetBytes($root.Replace('\end{document}', '\openin1=hidden.tex\read1 to \payload\end{document}')) }
    Assert-Pass 'SOURCE_IO_PRIMITIVE_IS_UNRESOLVED' {
        $analysis = Get-TexAnalysis $sourceIoMap
        if ($analysis.ClosureStatus -ne 'UNRESOLVED_SOURCE_CLOSURE') { Throw-Guard 'SELFTEST_SOURCE_IO_NOT_UNRESOLVED' }
    }
    $unbalancedMap = @{ 'main.tex' = [System.Text.Encoding]::UTF8.GetBytes($root.Replace('\end{document}', '\input{hidden\end{document}')) }
    Assert-Pass 'UNBALANCED_SUPPORTED_LOADER_IS_UNRESOLVED' {
        $analysis = Get-TexAnalysis $unbalancedMap
        if ($analysis.ClosureStatus -ne 'UNRESOLVED_SOURCE_CLOSURE') { Throw-Guard 'SELFTEST_UNBALANCED_LOADER_NOT_UNRESOLVED' }
    }
    $letAliasMap = @{ 'main.tex' = [System.Text.Encoding]::UTF8.GetBytes($root.Replace('\end{document}', '\let\alias\input\end{document}')) }
    Assert-Pass 'LET_ALIAS_WITHOUT_EQUALS_IS_UNRESOLVED' {
        $analysis = Get-TexAnalysis $letAliasMap
        if ($analysis.ClosureStatus -ne 'UNRESOLVED_SOURCE_CLOSURE') { Throw-Guard 'SELFTEST_LET_ALIAS_NOT_UNRESOLVED' }
    }
    $macroLoaderMap = @{
        'main.tex' = [System.Text.Encoding]::UTF8.GetBytes($root.Replace('\end{document}', '\def\grab{\input{fixed}}\end{document}'))
        'fixed.tex' = [System.Text.Encoding]::UTF8.GetBytes('fixed literal target')
    }
    Assert-Pass 'MACRO_DEFINED_LOADER_IS_UNRESOLVED' {
        $analysis = Get-TexAnalysis $macroLoaderMap
        if ($analysis.ClosureStatus -ne 'UNRESOLVED_SOURCE_CLOSURE') { Throw-Guard 'SELFTEST_MACRO_LOADER_NOT_UNRESOLVED' }
    }
    $catcodeMap = @{ 'main.tex' = [System.Text.Encoding]::UTF8.GetBytes($root.Replace('\end{document}', '\catcode`\@=11\end{document}')) }
    Assert-Pass 'CATCODE_MUTATION_IS_UNRESOLVED' {
        $analysis = Get-TexAnalysis $catcodeMap
        if ($analysis.ClosureStatus -ne 'UNRESOLVED_SOURCE_CLOSURE') { Throw-Guard 'SELFTEST_CATCODE_NOT_UNRESOLVED' }
    }
    $cycleMap = @{
        'main.tex' = [System.Text.Encoding]::UTF8.GetBytes($root.Replace('\end{document}', '\input{a}\end{document}'))
        'a.tex' = [System.Text.Encoding]::UTF8.GetBytes('\input{main}')
    }
    Assert-Pass 'DEPENDENCY_CYCLE_IS_UNRESOLVED' {
        $analysis = Get-TexAnalysis $cycleMap
        if ($analysis.ClosureStatus -ne 'UNRESOLVED_SOURCE_CLOSURE') { Throw-Guard 'SELFTEST_CYCLE_NOT_UNRESOLVED' }
        Assert-ExactStringSet $analysis.ReachableTextMembers @('main.tex','a.tex') 'SELFTEST_CYCLE_REACHABLE_SET_MISMATCH'
        Assert-HasExactString $analysis.Problems 'TEX_DEPENDENCY_CYCLE::main.tex' 'SELFTEST_CYCLE_PROBLEM_MISMATCH'
    }

    $fixtureSetDigest = Get-Sha256Hex ([System.Text.Encoding]::UTF8.GetBytes((@($stats.Names) -join "`n")))
    $result = [ordered]@{
        task = 'Q1R1_V2_289S_R1_SELFTEST'
        network_operations = 0
        live_output_writes = 0
        fixture_count = $stats.Names.Count
        fixture_set_sha256 = $fixtureSetDigest
        fixtures_passed = $stats.Passed
        fixtures_failed = $stats.Failed.Count
        failures = @($stats.Failed)
        status = if ($stats.Failed.Count -eq 0) { 'PASS' } else { 'FAIL' }
    }
    $json = $result | ConvertTo-Json -Depth 8 -Compress
    Write-Output $json
    if ($stats.Failed.Count -ne 0) { exit 11 }
}

function Write-JournalLine {
    param([System.IO.FileStream]$Stream, [string]$Line)
    [byte[]]$bytes = [System.Text.UTF8Encoding]::new($false).GetBytes($Line + "`n")
    $Stream.Write($bytes, 0, $bytes.Length)
    $Stream.Flush($true)
}

function Invoke-Acquire {
    $scriptFullPath = [System.IO.Path]::GetFullPath($PSCommandPath)
    $expectedDirectory = 'D:\Teoria\tracks\A1\A1K1\A2\A2K4\SUBTRACKS\P5\P5_3_SEEDS'
    $expectedScript = Join-Path $expectedDirectory '289S_R1_B6B2_10_Q1R1_V2_SOURCE_ARCHIVE_ACQUISITION.ps1'
    if ($scriptFullPath -cne [System.IO.Path]::GetFullPath($expectedScript)) { Throw-Guard 'SCRIPT_PATH_MISMATCH' }
    if ($PreregSha256 -cne $ExpectedPreregSha256) { Throw-Guard 'PREREG_ARGUMENT_SHA_MISMATCH' }

    $preregPath = Join-Path $expectedDirectory '289_B6B2_10_H_RDIV_C01_RW1_Q1R1_V2_SOURCE_ARCHIVE_ELIGIBILITY_PREREGISTRATION_SK.md'
    $ledgerPath = 'D:\Teoria\tracks\A1\A1K1\A2\A2K4\HISTORY\00_EVENT_LEDGER.md'
    $journalPath = Join-Path $expectedDirectory '289J_B6B2_10_Q1R1_V2_SOURCE_ARCHIVE_OPERATION_JOURNAL.txt'
    $tempPath = Join-Path $expectedDirectory '.289A_B6B2_10_Q1R1_SOURCE_ARCHIVE.part'
    $archivePath = Join-Path $expectedDirectory '289A_B6B2_10_Q1R1_ARXIV_2307_12080V2_SOURCE_ARCHIVE.tar.gz'
    $resultPath = Join-Path $expectedDirectory '290_B6B2_10_H_RDIV_C01_RW1_Q1R1_V2_SOURCE_ARCHIVE_ELIGIBILITY_RESULT_SK.md'

    $actualPrereg = (Get-FileHash -LiteralPath $preregPath -Algorithm SHA256).Hash
    if ($actualPrereg -cne $ExpectedPreregSha256) { Throw-Guard 'FROZEN_PREREG_FILE_SHA_MISMATCH' }
    $actualLedger = (Get-FileHash -LiteralPath $ledgerPath -Algorithm SHA256).Hash
    if ($actualLedger -cne $AuthorizationEventLedgerSha256) { Throw-Guard 'AUTHORIZATION_LEDGER_SHA_MISMATCH' }
    $scriptSha = (Get-FileHash -LiteralPath $scriptFullPath -Algorithm SHA256).Hash
    $ledgerText = Get-Content -LiteralPath $ledgerPath -Raw
    foreach ($marker in @(
        'TASK_ID: A2K4-B6B2-10-H-RDIV-C01-RW1-Q1R1-V2-SOURCE-ARCHIVE-ACCESS-AUTHORIZATION-',
        "FROZEN_PREREG289_SHA256: $ExpectedPreregSha256",
        "FROZEN_289S_R1_SHA256: $scriptSha",
        'SOURCE_ACCESS_AUTHORIZED: true_Q1R1_V2_EXACT_ONE_ARCHIVE_GET'
    )) {
        if (-not $ledgerText.Contains($marker)) { Throw-Guard 'AUTHORIZATION_MARKER_MISSING' }
    }
    foreach ($target in @($journalPath, $tempPath, $archivePath, $resultPath)) {
        if ([System.IO.File]::Exists($target)) { Throw-Guard "OUTPUT_COLLISION::$target" }
    }

    $journal = $null
    $temp = $null
    $handler = $null
    $client = $null
    $request = $null
    $response = $null
    $requestReserved = $false
    $httpStatus = 'NOT_RECEIVED'
    $receivedBytes = 0L
    $tempOwned = $false
    $publishCommitted = $false
    $terminalAttempted = $false
    try {
        $journal = [System.IO.FileStream]::new(
            $journalPath,
            [System.IO.FileMode]::CreateNew,
            [System.IO.FileAccess]::Write,
            [System.IO.FileShare]::None,
            4096,
            [System.IO.FileOptions]::WriteThrough
        )
        Write-JournalLine $journal 'TASK_ID=A2K4-B6B2-10-H-RDIV-C01-RW1-Q1R1-V2-SOURCE-ARCHIVE-ACCESS'
        Write-JournalLine $journal 'OPERATION_ID=V2-O1'
        Write-JournalLine $journal "URL=$SourceUrl"
        Write-JournalLine $journal 'METHOD=GET'
        Write-JournalLine $journal 'Q1R1_V1_ACCESS=2/2_EXHAUSTED'
        Write-JournalLine $journal 'HISTORICAL_PACKAGES_TOTAL_BEFORE=1'
        Write-JournalLine $journal 'CONSECUTIVE_TECHNICAL_FAILURES_BEFORE=1/10'
        Write-JournalLine $journal "PREREG_SHA256=$ExpectedPreregSha256"
        Write-JournalLine $journal "SCRIPT_SHA256=$scriptSha"
        Write-JournalLine $journal "AUTHORIZATION_LEDGER_SHA256=$AuthorizationEventLedgerSha256"
        Write-JournalLine $journal "REQUEST_RESERVED_UTC=$([DateTime]::UtcNow.ToString('O'))"
        Write-JournalLine $journal 'REQUEST_STATE=V2-O1_REQUEST_RESERVED_CONSUMED_NO_RETRY'
        $requestReserved = $true

        $handler = [System.Net.Http.HttpClientHandler]::new()
        $handler.AllowAutoRedirect = $false
        $handler.AutomaticDecompression = [System.Net.DecompressionMethods]::None
        $handler.MaxResponseHeadersLength = 64
        $client = [System.Net.Http.HttpClient]::new($handler, $false)
        $client.Timeout = [System.Threading.Timeout]::InfiniteTimeSpan
        $request = [System.Net.Http.HttpRequestMessage]::new([System.Net.Http.HttpMethod]::Get, $SourceUrl)
        if (-not $request.Headers.AcceptEncoding.TryParseAdd('identity')) { Throw-Guard 'HTTP_ACCEPT_ENCODING_HEADER_REJECTED' }
        if (-not $request.Headers.UserAgent.TryParseAdd($UserAgent)) { Throw-Guard 'HTTP_USER_AGENT_HEADER_REJECTED' }

        $cts = [System.Threading.CancellationTokenSource]::new([TimeSpan]::FromSeconds($HttpTimeoutSeconds))
        try {
            $response = $client.SendAsync(
                $request,
                [System.Net.Http.HttpCompletionOption]::ResponseHeadersRead,
                $cts.Token
            ).GetAwaiter().GetResult()
            $status = [int]$response.StatusCode
            $httpStatus = [string]$status
            if ($status -ne 200) { Throw-Guard "HTTP_STATUS_$status" }
            $contentLength = $response.Content.Headers.ContentLength
            if ($null -ne $contentLength -and ($contentLength -lt $MinHttpBytes -or $contentLength -gt $MaxHttpBytes)) {
                Throw-Guard 'HTTP_CONTENT_LENGTH_OUT_OF_RANGE'
            }

            $temp = [System.IO.FileStream]::new(
                $tempPath,
                [System.IO.FileMode]::CreateNew,
                [System.IO.FileAccess]::Write,
                [System.IO.FileShare]::None,
                65536,
                [System.IO.FileOptions]::WriteThrough
            )
            $tempOwned = $true
            $body = $response.Content.ReadAsStreamAsync($cts.Token).GetAwaiter().GetResult()
            try {
                [byte[]]$buffer = [byte[]]::new(65536)
                $total = 0L
                while (($read = $body.ReadAsync($buffer, 0, $buffer.Length, $cts.Token).GetAwaiter().GetResult()) -gt 0) {
                    $total += $read
                    $receivedBytes = $total
                    if ($total -gt $MaxHttpBytes) { Throw-Guard 'HTTP_STREAM_BODY_ABOVE_MAXIMUM' }
                    $temp.Write($buffer, 0, $read)
                }
            }
            finally { $body.Dispose() }
            if ($total -lt $MinHttpBytes) { Throw-Guard 'HTTP_STREAM_BODY_BELOW_MINIMUM' }
            $temp.Flush($true)
            $temp.Dispose(); $temp = $null

            [byte[]]$responseBytes = [System.IO.File]::ReadAllBytes($tempPath)
            $firstNonWhitespace = $responseBytes | Where-Object { $_ -notin @(9,10,13,32) } | Select-Object -First 1
            if ($null -eq $firstNonWhitespace -or $firstNonWhitespace -eq [byte][char]'<') { Throw-Guard 'HTTP_BODY_HTML_XML_OR_EMPTY' }
            $validation = Test-ArchiveBytes $responseBytes

            Write-JournalLine $journal "HTTP_STATUS=$status"
            Write-JournalLine $journal "RESPONSE_BYTES=$($validation.ResponseBytes)"
            Write-JournalLine $journal "RESPONSE_SHA256=$($validation.ResponseSha256)"
            Write-JournalLine $journal "ARCHIVE_REPRESENTATION=$($validation.Representation)"
            Write-JournalLine $journal "TAR_SHA256=$($validation.TarSha256)"
            Write-JournalLine $journal "TAR_BYTES=$($validation.TarBytes)"
            Write-JournalLine $journal "ENTRY_COUNT=$($validation.EntryCount)"
            Write-JournalLine $journal "INVENTORY_DIGEST_SHA256=$($validation.InventoryDigestSha256)"
            Write-JournalLine $journal "MAIN_ROOT=$($validation.MainRoot)"
            Write-JournalLine $journal "SOURCE_CLOSURE_STATUS=$($validation.ClosureStatus)"
            Write-JournalLine $journal "REQUEST_RETURNED_BODY_VALIDATED_UTC=$([DateTime]::UtcNow.ToString('O'))"
            Write-JournalLine $journal 'REQUEST_STATE=REQUEST_RETURNED_BODY_VALIDATED_PUBLISH_RESERVED'
            [System.IO.File]::Move($tempPath, $archivePath, $false)
            $publishCommitted = $true
            $terminalAttempted = $true
            Write-JournalLine $journal "TERMINAL_STATE=REQUEST_COMPLETED|HTTP_STATUS=$httpStatus|RESPONSE_BYTES=$receivedBytes|ERROR_TYPE=NONE|PUBLISH_STATE=PUBLISH_COMMITTED_EXCLUSIVE_MOVE|GUARD=ALL_VALIDATION_AND_PUBLISH_GUARDS_PASSED"

            $output = [ordered]@{
                status = 'SUCCESS'
                operation = 'V2-O1'
                source_operations_cumulative = 3
                historical_packages_total = 2
                consecutive_technical_failures = 0
                archive_path = $archivePath
                journal_path = $journalPath
                archive = $validation
                python_processes = 0
            }
            Write-Output ($output | ConvertTo-Json -Depth 10 -Compress)
        }
        finally { $cts.Dispose() }
    }
    catch {
        $message = $_.Exception.Message.Replace("`r", ' ').Replace("`n", ' ')
        $message = $message.Replace('|', '/')
        $errorType = $_.Exception.GetType().FullName.Replace('|', '/')
        if ($null -ne $journal -and -not $terminalAttempted) {
            try {
                $consumptionState = if ($requestReserved) { 'CONSUMED_NO_RETRY' } else { 'NOT_RESERVED' }
                $publishState = if ($publishCommitted) { 'PUBLISH_COMMITTED' } else { 'PUBLISH_NOT_COMMITTED' }
                $terminalAttempted = $true
                Write-JournalLine $journal "TERMINAL_STATE=REQUEST_FAILED|CONSUMPTION_STATE=$consumptionState|HTTP_STATUS=$httpStatus|RESPONSE_BYTES=$receivedBytes|ERROR_TYPE=$errorType|PUBLISH_STATE=$publishState|FAILURE_GUARD=$message"
            } catch { }
        }
        if ($null -ne $temp) { try { $temp.Dispose() } catch { }; $temp = $null }
        if ($tempOwned -and -not $publishCommitted -and [System.IO.File]::Exists($tempPath)) {
            try { [System.IO.File]::Delete($tempPath) } catch { }
        }
        $failure = [ordered]@{
            status = 'TECHNICAL_FAILURE_NO_PHYSICAL_INFERENCE'
            operation = 'V2-O1'
            request_reserved = $requestReserved
            retry_allowed = $false
            http_status = $httpStatus
            response_bytes = $receivedBytes
            error_type = $errorType
            publish_committed = $publishCommitted
            failure_guard = $message
            python_processes = 0
        }
        Write-Output ($failure | ConvertTo-Json -Depth 6 -Compress)
        exit 20
    }
    finally {
        if ($null -ne $response) { $response.Dispose() }
        if ($null -ne $request) { $request.Dispose() }
        if ($null -ne $client) { $client.Dispose() }
        if ($null -ne $handler) { $handler.Dispose() }
        if ($null -ne $temp) { $temp.Dispose() }
        if ($null -ne $journal) { $journal.Dispose() }
    }
}

if ($PSCmdlet.ParameterSetName -eq 'SelfTest') {
    Invoke-SelfTest
    exit 0
}
if ($PSCmdlet.ParameterSetName -eq 'Acquire') {
    Invoke-Acquire
    exit 0
}

Write-Error 'NO_ACTION: specify exactly -SelfTest or -Acquire with all mandatory frozen arguments.'
exit 2
