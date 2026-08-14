param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[0-9A-F]{64}$')]
    [string]$AuditedRunnerSha256
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$base = $PSScriptRoot
$journalPath = Join-Path $base '283C_B6B2_10_Q1R7_SOURCE_OPERATION_JOURNAL.txt'
$blobPath = Join-Path $base '283A_B6B2_10_Q1R7_PRIMARY_SOURCE_BLOB.bin'
$receiptPath = Join-Path $base '283B_B6B2_10_Q1R7_COMPLETE_SOURCE_RECEIPT.txt'
$resultPath = Join-Path $base '284_B6B2_10_H_RDIV_C01_RW1_V1_Q1R7_S0_S13_RESULT_SK.md'
$tempDir = Join-Path $base '.q1r7_tmp'
$blobTemp = Join-Path $base '.283A_Q1R7.tmp'
$receiptTemp = Join-Path $base '.283B_Q1R7.tmp'
$preregPath = Join-Path $base '283_B6B2_10_H_RDIV_C01_RW1_V1_Q1R6_TO_Q1R7_ORDERED_TRANSITION_COMPLETE_SOURCE_PREREGISTRATION_SK.md'
$expectedPrereg = 'E9F7AD9237BE24EB7CB4CF8EE80F58E1B1D38D6834D83FB442A5A909BD47B3B6'
$pdfinfo = 'C:\Users\jambor.CHASTIA\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdfinfo.exe'
$pdftotext = 'C:\Program Files\Git\mingw64\bin\pdftotext.exe'
$pdftoppm = 'C:\Users\jambor.CHASTIA\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe'
$title = 'Hydrodynamics of ultra-relativistic bubble walls'
$pii = 'S0550321316000535'
$utf8 = [Text.UTF8Encoding]::new($false)
$globalCts = [Threading.CancellationTokenSource]::new([TimeSpan]::FromSeconds(600))
$globalDeadline = [DateTime]::UtcNow.AddSeconds(600)
$script:ops = [Collections.Generic.List[object]]::new()
$script:slots = [ordered]@{}
$script:requestCount = 0
$script:journalFs = $null

Add-Type -TypeDefinition @'
using System;
using System.IO;
using System.IO.Compression;

public sealed class Q1R7OneByteDeadlineStream : Stream
{
    private readonly Stream inner;
    private readonly DateTime deadlineUtc;

    public Q1R7OneByteDeadlineStream(Stream inner, DateTime deadlineUtc)
    {
        this.inner = inner;
        this.deadlineUtc = deadlineUtc;
    }

    private void CheckDeadline()
    {
        if (DateTime.UtcNow >= deadlineUtc)
            throw new TimeoutException("PARSE_DEADLINE");
    }

    public override int Read(byte[] buffer, int offset, int count)
    {
        CheckDeadline();
        return inner.Read(buffer, offset, Math.Min(count, 1));
    }

    public override int Read(Span<byte> buffer)
    {
        CheckDeadline();
        return inner.Read(buffer.Slice(0, Math.Min(buffer.Length, 1)));
    }

    public override bool CanRead => true;
    public override bool CanSeek => false;
    public override bool CanWrite => false;
    public override long Length => throw new NotSupportedException();
    public override long Position
    {
        get => throw new NotSupportedException();
        set => throw new NotSupportedException();
    }
    public override void Flush() { }
    public override long Seek(long offset, SeekOrigin origin) => throw new NotSupportedException();
    public override void SetLength(long value) => throw new NotSupportedException();
    public override void Write(byte[] buffer, int offset, int count) => throw new NotSupportedException();
}

public sealed class Q1R7ExactGzipResult
{
    public bool Pass { get; set; }
    public string Error { get; set; } = "";
    public byte[] Payload { get; set; } = Array.Empty<byte>();
    public long ConsumedBytes { get; set; }
}

public static class Q1R7ExactGzip
{
    private static readonly uint[] Table = BuildTable();

    private static uint[] BuildTable()
    {
        var table = new uint[256];
        for (uint i = 0; i < 256; i++)
        {
            uint value = i;
            for (int bit = 0; bit < 8; bit++)
                value = (value & 1) != 0 ? 0xEDB88320U ^ (value >> 1) : value >> 1;
            table[i] = value;
        }
        return table;
    }

    private static uint Crc32(
        byte[] bytes,
        int offset,
        int count,
        DateTime deadlineUtc)
    {
        uint crc = 0xFFFFFFFFU;
        for (int i = offset; i < offset + count; i++)
        {
            if ((i & 0xFFF) == 0) Check(deadlineUtc);
            crc = Table[(crc ^ bytes[i]) & 0xFF] ^ (crc >> 8);
        }
        return ~crc;
    }

    private static void Check(DateTime deadlineUtc)
    {
        if (DateTime.UtcNow >= deadlineUtc)
            throw new TimeoutException("PARSE_DEADLINE");
    }

    public static Q1R7ExactGzipResult Validate(
        byte[] body,
        int maxOutputBytes,
        int maxRatio,
        DateTime deadlineUtc)
    {
        try
        {
            if (body == null || body.Length < 18)
                throw new InvalidDataException("GZIP_HEADER_OR_TRAILER_TRUNCATED");
            if (body[0] != 0x1F || body[1] != 0x8B || body[2] != 8)
                throw new InvalidDataException("GZIP_MAGIC_OR_METHOD");
            byte flags = body[3];
            if ((flags & 0xE0) != 0)
                throw new InvalidDataException("GZIP_RESERVED_FLAGS");
            int position = 10;
            int trailerLimit = body.Length - 8;
            if ((flags & 0x04) != 0)
            {
                Check(deadlineUtc);
                if (position + 2 > trailerLimit)
                    throw new InvalidDataException("GZIP_EXTRA_TRUNCATED");
                int length = body[position] | (body[position + 1] << 8);
                position += 2;
                if (position + length > trailerLimit)
                    throw new InvalidDataException("GZIP_EXTRA_TRUNCATED");
                position += length;
            }
            foreach (byte flag in new byte[] { 0x08, 0x10 })
            {
                if ((flags & flag) == 0) continue;
                while (position < trailerLimit && body[position] != 0)
                {
                    if ((position & 0xFFF) == 0) Check(deadlineUtc);
                    position++;
                }
                if (position >= trailerLimit)
                    throw new InvalidDataException("GZIP_STRING_TRUNCATED");
                position++;
            }
            if ((flags & 0x02) != 0)
            {
                if (position + 2 > trailerLimit)
                    throw new InvalidDataException("GZIP_HEADER_CRC_TRUNCATED");
                ushort expectedHeaderCrc = (ushort)(body[position] | (body[position + 1] << 8));
                ushort actualHeaderCrc = (ushort)(
                    Crc32(body, 0, position, deadlineUtc) & 0xFFFF);
                if (actualHeaderCrc != expectedHeaderCrc)
                    throw new InvalidDataException("GZIP_HEADER_CRC_MISMATCH");
                position += 2;
            }
            if (position >= trailerLimit)
                throw new InvalidDataException("GZIP_EMPTY_DEFLATE_STREAM");

            using var input = new MemoryStream(body, false);
            input.Position = position;
            using var exactInput = new Q1R7OneByteDeadlineStream(input, deadlineUtc);
            using var deflate = new DeflateStream(exactInput, CompressionMode.Decompress, true);
            using var output = new MemoryStream();
            var buffer = new byte[65536];
            int read;
            while ((read = deflate.Read(buffer, 0, buffer.Length)) > 0)
            {
                Check(deadlineUtc);
                if (output.Length + read > maxOutputBytes)
                    throw new InvalidDataException("DECOMPRESSED_LIMIT");
                output.Write(buffer, 0, read);
            }
            long deflateEnd = input.Position;
            if (deflateEnd + 8 != body.LongLength)
                throw new InvalidDataException(
                    "GZIP_TRAILING_OR_CONCATENATED_BYTES:DEFLATE_END=" +
                    deflateEnd + ":BODY=" + body.LongLength);

            byte[] payload = output.ToArray();
            uint expectedCrc = BitConverter.ToUInt32(body, checked((int)deflateEnd));
            uint expectedSize = BitConverter.ToUInt32(body, checked((int)deflateEnd + 4));
            uint actualCrc = Crc32(payload, 0, payload.Length, deadlineUtc);
            if (actualCrc != expectedCrc)
                throw new InvalidDataException("GZIP_DATA_CRC_MISMATCH");
            if ((uint)payload.Length != expectedSize)
                throw new InvalidDataException("GZIP_ISIZE_MISMATCH");
            if (body.Length > 0 && payload.Length / (double)body.Length > maxRatio)
                throw new InvalidDataException("RATIO_LIMIT");
            Check(deadlineUtc);
            return new Q1R7ExactGzipResult
            {
                Pass = true,
                Payload = payload,
                ConsumedBytes = deflateEnd + 8
            };
        }
        catch (Exception error)
        {
            return new Q1R7ExactGzipResult
            {
                Pass = false,
                Error = error.Message
            };
        }
    }
}
'@

function Sha256([byte[]]$bytes) {
    [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($bytes))
}
function FileSha([string]$path) {
    (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash
}
function AssertGlobalDeadline {
    if ([DateTime]::UtcNow -ge $globalDeadline) { throw 'WHOLE_PROCESS_TIMEOUT' }
}
function RemainingMilliseconds([int]$localCapMs) {
    AssertGlobalDeadline
    $remaining = [int][Math]::Floor(($globalDeadline - [DateTime]::UtcNow).TotalMilliseconds)
    if ($remaining -le 0) { throw 'WHOLE_PROCESS_TIMEOUT' }
    [Math]::Min($localCapMs, $remaining)
}
function Magic16([byte[]]$bytes) {
    $n = [Math]::Min(16, $bytes.Length)
    if ($n -eq 0) { return '' }
    [Convert]::ToHexString($bytes[0..($n - 1)])
}
function Norm([string]$s) {
    if ($null -eq $s) { return '' }
    $x = $s.Normalize([Text.NormalizationForm]::FormKC).Trim()
    $x = [regex]::Replace($x, '[\x09\x0A\x0D\x20]+', ' ')
    $x.ToLowerInvariant()
}
function SameSet($a, $b) {
    $aa = @($a | ForEach-Object { Norm ([string]$_) } | Where-Object { $_ } | Sort-Object -Unique)
    $bb = @($b | ForEach-Object { Norm ([string]$_) } | Where-Object { $_ } | Sort-Object -Unique)
    if ($aa.Count -ne $bb.Count) { return $false }
    for ($i = 0; $i -lt $aa.Count; $i++) {
        if ($aa[$i] -cne $bb[$i]) { return $false }
    }
    return $true
}
function NormalizeDoi([string]$s) {
    if ([string]::IsNullOrWhiteSpace($s)) { return $null }
    $x = $s.Normalize([Text.NormalizationForm]::FormKC).Trim().ToLowerInvariant()
    if ($x.StartsWith('https://doi.org/')) { $x = $x.Substring(16) }
    elseif ($x.StartsWith('http://dx.doi.org/')) { $x = $x.Substring(18) }
    if ($x.Contains('?') -or $x.Contains('#')) { return $null }
    $p = $x.IndexOf('/')
    if ($p -le 0 -or $p -ge $x.Length - 1) { return $null }
    if ($x.Substring(0, $p) -notmatch '^10\.[0-9]+$') { return $null }
    return $x
}
function DoiUrl([string]$doi) {
    $encoded = foreach ($segment in $doi.Split('/')) {
        $value = [Uri]::EscapeDataString($segment)
        [regex]::Replace($value, '%[0-9a-fA-F]{2}', { param($m) $m.Value.ToUpperInvariant() })
    }
    'https://doi.org/' + ($encoded -join '/')
}
function WriteJournal([string]$line) {
    $bytes = $utf8.GetBytes($line + [char]10)
    $script:journalFs.Write($bytes, 0, $bytes.Length)
    $script:journalFs.Flush($true)
}
function RunProcess([string]$exe, [string[]]$arguments, [int]$timeoutMs) {
    AssertGlobalDeadline
    $effectiveTimeout = RemainingMilliseconds $timeoutMs
    $psi = [Diagnostics.ProcessStartInfo]::new()
    $psi.FileName = $exe
    $psi.UseShellExecute = $false
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    foreach ($argument in $arguments) { [void]$psi.ArgumentList.Add($argument) }
    $process = [Diagnostics.Process]::new()
    $process.StartInfo = $psi
    if (-not $process.Start()) { throw "PROCESS_START_FAILED:$exe" }
    $outTask = $process.StandardOutput.ReadToEndAsync()
    $errTask = $process.StandardError.ReadToEndAsync()
    if (-not $process.WaitForExit($effectiveTimeout)) {
        try { $process.Kill($true) } catch {}
        throw "PROCESS_TIMEOUT:$exe"
    }
    [pscustomobject]@{
        ExitCode = $process.ExitCode
        Stdout = $outTask.GetAwaiter().GetResult()
        Stderr = $errTask.GetAwaiter().GetResult()
    }
}
function GetVersion([string]$exe) {
    $run = RunProcess $exe @('-v') 10000
    (($run.Stdout + [char]10 + $run.Stderr).Trim() -replace '\r?\n', ' | ') +
        " | EXIT=$($run.ExitCode)"
}
function GetHtmlMeta([byte[]]$bytes) {
    $html = [Text.Encoding]::UTF8.GetString($bytes)
    $map = [ordered]@{
        Title = @()
        Authors = @()
        DOI = @()
        PII = @()
        ArxivID = @()
        PdfUrl = @()
    }
    foreach ($match in [regex]::Matches($html, '(?is)<meta\b[^>]*>')) {
        $name = $null
        $content = $null
        foreach ($attribute in [regex]::Matches(
                $match.Value,
                '(?is)\b(name|property|content)\s*=\s*(["''])(.*?)\2')) {
            $key = $attribute.Groups[1].Value.ToLowerInvariant()
            $value = [Net.WebUtility]::HtmlDecode($attribute.Groups[3].Value)
            if ($key -eq 'content') { $content = $value } else { $name = $value.ToLowerInvariant() }
        }
        if ($null -eq $name -or $null -eq $content) { continue }
        switch ($name) {
            'citation_title' { $map.Title += $content }
            'dc.title' { $map.Title += $content }
            'citation_author' { $map.Authors += $content }
            'dc.creator' { $map.Authors += $content }
            'citation_doi' { $map.DOI += $content }
            'dc.identifier' { if ($content -match '10\.[0-9]+/') { $map.DOI += $content } }
            'citation_pii' { $map.PII += $content }
            'citation_arxiv_id' { $map.ArxivID += $content }
            'citation_pdf_url' { $map.PdfUrl += $content }
        }
    }
    [pscustomobject]$map
}
function IsPublisherHost([string]$hostName) {
    $hostLower = $hostName.ToLowerInvariant()
    $hostLower -eq 'sciencedirect.com' -or
        $hostLower.EndsWith('.sciencedirect.com') -or
        $hostLower -eq 'elsevier.com' -or
        $hostLower.EndsWith('.elsevier.com')
}
function TestFinalHost([string]$step, [Uri]$uri) {
    $hostLower = $uri.DnsSafeHost.ToLowerInvariant()
    switch -Wildcard ($step) {
        'O1_*' { return (IsPublisherHost $hostLower) }
        'O2_FULLTEXT*' { return (IsPublisherHost $hostLower) }
        'O2_CROSSREF*' { return $hostLower -eq 'api.crossref.org' }
        'O3_*' { return $hostLower -eq 'export.arxiv.org' }
        'O4_*' { return $hostLower -eq 'arxiv.org' -or $hostLower.EndsWith('.arxiv.org') }
        'O5_*' { return $hostLower -eq 'export.arxiv.org' }
        'O6_*' { return $hostLower -eq 'doi.org' -or (IsPublisherHost $hostLower) }
        default { return $false }
    }
}
function AssertSecureUri([Uri]$uri) {
    if ($uri.Scheme -cne 'https') { throw 'URI_NOT_HTTPS' }
    if (-not [string]::IsNullOrEmpty($uri.UserInfo)) { throw 'URI_USERINFO_FORBIDDEN' }
    if (-not $uri.IsDefaultPort -and $uri.Port -ne 443) { throw 'URI_NON443_PORT_FORBIDDEN' }
}
function InvokeQ1Request([int]$ordinal, [string]$step, [string]$url) {
    AssertGlobalDeadline
    $script:requestCount++
    if ($script:requestCount -gt 6) { throw 'REQUEST_CAP_EXCEEDED' }
    $start = [DateTime]::UtcNow
    WriteJournal (
        "REQUEST_RESERVED|ordinal=$ordinal|step=$step|utc=" +
        $start.ToString('o') + "|url=$url")
    $redirects = [Collections.Generic.List[string]]::new()
    $status = $null
    $mime = 'MISSING'
    $declared = 'MISSING'
    $encoding = 'MISSING'
    $final = $url
    $body = [byte[]]@()
    $errorText = 'NONE'
    $headers = [ordered]@{}
    try {
        $handler = [Net.Http.SocketsHttpHandler]::new()
        $handler.AllowAutoRedirect = $false
        $handler.AutomaticDecompression = [Net.DecompressionMethods]::None
        $handler.UseCookies = $false
        $handler.ConnectTimeout = [TimeSpan]::FromSeconds(10)
        $handler.MaxResponseHeadersLength = 64
        $client = [Net.Http.HttpClient]::new($handler)
        try {
            $current = [Uri]$url
            AssertSecureUri $current
            $visited = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
            [void]$visited.Add($current.AbsoluteUri)
            for ($redirectIndex = 0; $redirectIndex -le 5; $redirectIndex++) {
                $request = [Net.Http.HttpRequestMessage]::new([Net.Http.HttpMethod]::Get, $current)
                [void]$request.Headers.TryAddWithoutValidation(
                    'User-Agent',
                    'Teoria-Q1R7-CompleteSource/1.0')
                [void]$request.Headers.TryAddWithoutValidation('Accept-Encoding', 'identity')
                $headersCts = [Threading.CancellationTokenSource]::CreateLinkedTokenSource(
                    $globalCts.Token)
                $headersCts.CancelAfter([TimeSpan]::FromSeconds(30))
                try {
                    $response = $client.SendAsync(
                        $request,
                        [Net.Http.HttpCompletionOption]::ResponseHeadersRead,
                        $headersCts.Token).GetAwaiter().GetResult()
                } finally {
                    $headersCts.Dispose()
                    $request.Dispose()
                }
                $code = [int]$response.StatusCode
                if ($code -in 301, 302, 303, 307, 308) {
                    if ($redirectIndex -ge 5) {
                        $response.Dispose()
                        throw 'MAX_REDIRECTS_EXCEEDED'
                    }
                    $location = $response.Headers.Location
                    if ($null -eq $location) {
                        $response.Dispose()
                        throw 'REDIRECT_WITHOUT_LOCATION'
                    }
                    $next = if ($location.IsAbsoluteUri) {
                        $location
                    } else {
                        [Uri]::new($current, $location)
                    }
                    AssertSecureUri $next
                    if (-not $visited.Add($next.AbsoluteUri)) {
                        $response.Dispose()
                        throw 'REDIRECT_LOOP'
                    }
                    $redirects.Add($next.AbsoluteUri)
                    $current = $next
                    $response.Dispose()
                    continue
                }
                $final = $current.AbsoluteUri
                if (-not (TestFinalHost $step $current)) {
                    $response.Dispose()
                    throw "FINAL_HOST_NOT_ALLOWED:$($current.DnsSafeHost)"
                }
                $status = $code
                if ($response.Content.Headers.ContentType) {
                    $mime = $response.Content.Headers.ContentType.ToString()
                }
                if ($null -ne $response.Content.Headers.ContentLength) {
                    $declared = [string]$response.Content.Headers.ContentLength
                }
                if ($response.Content.Headers.ContentEncoding.Count -gt 0) {
                    $encoding = $response.Content.Headers.ContentEncoding -join ','
                }
                foreach ($header in $response.Headers) {
                    $headers[$header.Key] = $header.Value -join ', '
                }
                foreach ($header in $response.Content.Headers) {
                    $headers[$header.Key] = $header.Value -join ', '
                }
                $bodyCts = [Threading.CancellationTokenSource]::CreateLinkedTokenSource(
                    $globalCts.Token)
                $bodyCts.CancelAfter([TimeSpan]::FromSeconds(90))
                $stream = $response.Content.ReadAsStreamAsync(
                    $bodyCts.Token).GetAwaiter().GetResult()
                $memory = [IO.MemoryStream]::new()
                try {
                    $buffer = [byte[]]::new(65536)
                    while (($read = $stream.ReadAsync(
                                    $buffer.AsMemory(0, $buffer.Length),
                                    $bodyCts.Token).AsTask().GetAwaiter().GetResult()) -gt 0) {
                        AssertGlobalDeadline
                        if ($memory.Length + $read -gt 67108864) {
                            throw 'MAX_BODY_BYTES_EXCEEDED'
                        }
                        $memory.Write($buffer, 0, $read)
                    }
                    $body = $memory.ToArray()
                } finally {
                    $stream.Dispose()
                    $memory.Dispose()
                    $bodyCts.Dispose()
                    $response.Dispose()
                }
                break
            }
        } finally {
            $client.Dispose()
            $handler.Dispose()
        }
    } catch {
        $errorText = $_.Exception.Message.Replace([char]13, ' ').Replace([char]10, ' ')
    }
    $end = [DateTime]::UtcNow
    $sha = if ($body.Length -gt 0) { Sha256 $body } else { 'MISSING' }
    $metadata = if ($body.Length -gt 0) {
        GetHtmlMeta $body
    } else {
        [pscustomobject]@{
            Title = @()
            Authors = @()
            DOI = @()
            PII = @()
            ArxivID = @()
            PdfUrl = @()
        }
    }
    $operation = [pscustomobject]@{
        Ordinal = $ordinal
        Step = $step
        StartUTC = $start.ToString('o')
        EndUTC = $end.ToString('o')
        RequestedURL = $url
        RedirectChain = @($redirects)
        FinalURL = $final
        Status = $status
        MIME = $mime
        DeclaredContentLength = $declared
        ActualLength = $body.Length
        SHA256 = $sha
        Magic16 = Magic16 $body
        ContentEncoding = $encoding
        TransportError = $errorText
        Headers = $headers
        Metadata = $metadata
        Body = $body
    }
    $script:ops.Add($operation)
    $script:slots[[string]$ordinal] = "EXECUTED:$step"
    WriteJournal (
        "REQUEST_COMPLETED|ordinal=$ordinal|step=$step|utc=" +
        $end.ToString('o') +
        "|status=$status|bytes=$($body.Length)|sha256=$sha|error=$errorText")
    return $operation
}
function AddSkipped([int]$ordinal, [string]$step, [string]$reason) {
    $script:slots[[string]$ordinal] = $reason + ':' + $step
    WriteJournal "REQUEST_SLOT_RETIRED|ordinal=$ordinal|step=$step|reason=$reason"
}
function GetPublisherPdfLinks($operation) {
    $html = [Text.Encoding]::UTF8.GetString($operation.Body)
    $links = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
    $baseUri = [Uri]$operation.FinalURL
    foreach ($match in [regex]::Matches(
            $html,
            '(?is)\b(?:href|content)\s*=\s*(["''])(.*?)\1')) {
        $raw = [Net.WebUtility]::HtmlDecode($match.Groups[2].Value)
        try {
            $uri = if ([Uri]::IsWellFormedUriString($raw, [UriKind]::Absolute)) {
                [Uri]$raw
            } else {
                [Uri]::new($baseUri, $raw)
            }
        } catch {
            continue
        }
        if ($uri.Scheme -cne 'https' -or -not (IsPublisherHost $uri.DnsSafeHost)) {
            continue
        }
        if (-not $uri.AbsoluteUri.Contains($pii, [StringComparison]::Ordinal)) {
            continue
        }
        $query = [Net.WebUtility]::UrlDecode($uri.Query)
        if ($uri.AbsolutePath.EndsWith('.pdf', [StringComparison]::OrdinalIgnoreCase) -or
            $query -match '(?i)(^|[^a-z])pdf([^a-z]|$)') {
            [void]$links.Add($uri.AbsoluteUri)
        }
    }
    @($links)
}
function TextDecodeStrict([byte[]]$bytes) {
    try {
        $encoding = [Text.UTF8Encoding]::new($false, $true)
        $text = $encoding.GetString($bytes)
        if (-not [Linq.Enumerable]::SequenceEqual($bytes, $encoding.GetBytes($text))) {
            throw 'UTF8_ROUNDTRIP'
        }
    } catch {
        [Text.Encoding]::RegisterProvider([Text.CodePagesEncodingProvider]::Instance)
        $encoding = [Text.Encoding]::GetEncoding(
            1252,
            [Text.EncoderFallback]::ExceptionFallback,
            [Text.DecoderFallback]::ExceptionFallback)
        $text = $encoding.GetString($bytes)
        if (-not [Linq.Enumerable]::SequenceEqual($bytes, $encoding.GetBytes($text))) {
            throw 'CP1252_ROUNDTRIP'
        }
    }
    for ($i = 0; $i -lt $text.Length; $i++) {
        $codepoint = [int][char]$text[$i]
        if ($codepoint -eq 0 -or
            $codepoint -eq 127 -or
            ($codepoint -lt 32 -and $codepoint -notin 9, 10, 12, 13)) {
            throw "TEXT_CONTROL_$codepoint"
        }
        $category = [Globalization.CharUnicodeInfo]::GetUnicodeCategory($text[$i])
        if ($category -eq [Globalization.UnicodeCategory]::Control -and
            $codepoint -notin 9, 10, 12, 13) {
            throw 'UNICODE_CC'
        }
        if ($category -eq [Globalization.UnicodeCategory]::Format -and
            -not ($codepoint -eq 0xFEFF -and $i -eq 0)) {
            throw 'UNICODE_CF'
        }
    }
    return $text
}
function TestPathSafe([string]$path) {
    if ([string]::IsNullOrWhiteSpace($path)) { return $false }
    if ($path.Contains('\') -or
        $path.StartsWith('/') -or
        $path.StartsWith('//') -or
        $path -match '^[A-Za-z]:' -or
        $path.Contains(':')) {
        return $false
    }
    foreach ($segment in $path.Split('/')) {
        if ($segment -eq '' -or
            $segment -eq '.' -or
            $segment -eq '..' -or
            $segment.EndsWith('.') -or
            $segment.EndsWith(' ')) {
            return $false
        }
        $stem = [IO.Path]::GetFileNameWithoutExtension($segment)
        if ($stem -match '^(?i:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])$') {
            return $false
        }
    }
    return $true
}
function HasPrefix([byte[]]$bytes, [byte[]]$prefix) {
    if ($bytes.Length -lt $prefix.Length) { return $false }
    for ($i = 0; $i -lt $prefix.Length; $i++) {
        if ($bytes[$i] -ne $prefix[$i]) { return $false }
    }
    return $true
}
function ClassifyBytes([byte[]]$bytes) {
    $allowed = @(
        [Text.Encoding]::ASCII.GetBytes('%PDF-'),
        [byte[]](0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A),
        [byte[]](0xFF, 0xD8, 0xFF),
        [Text.Encoding]::ASCII.GetBytes('GIF87a'),
        [Text.Encoding]::ASCII.GetBytes('GIF89a'),
        [Text.Encoding]::ASCII.GetBytes('%!PS'),
        [byte[]](0x49, 0x49, 0x2A, 0x00),
        [byte[]](0x4D, 0x4D, 0x00, 0x2A),
        [Text.Encoding]::ASCII.GetBytes('BM'),
        [byte[]](0xD0, 0xCF, 0x11, 0xE0, 0xA1, 0xB1, 0x1A, 0xE1),
        [byte[]](0x7F, 0x45, 0x4C, 0x46),
        [Text.Encoding]::ASCII.GetBytes('MZ')
    )
    $forbidden = @(
        [byte[]](0x50, 0x4B, 0x03, 0x04),
        [byte[]](0x1F, 0x8B, 0x08),
        [byte[]](0x52, 0x61, 0x72, 0x21, 0x1A, 0x07),
        [byte[]](0x37, 0x7A, 0xBC, 0xAF, 0x27, 0x1C)
    )
    foreach ($prefix in $forbidden) {
        if (HasPrefix $bytes $prefix) {
            return [pscustomobject]@{ Kind = 'FORBIDDEN_CONTAINER'; Text = $null }
        }
    }
    foreach ($prefix in $allowed) {
        if (HasPrefix $bytes $prefix) {
            return [pscustomobject]@{ Kind = 'ALLOWED_BINARY'; Text = $null }
        }
    }
    try {
        [pscustomobject]@{ Kind = 'TEXT'; Text = TextDecodeStrict $bytes }
    } catch {
        [pscustomobject]@{ Kind = 'UNKNOWN_NONTEXT'; Text = $null }
    }
}
function TestTexRoot([string]$text, [string[]]$authors) {
    $normalized = Norm $text
    if (-not $normalized.Contains((Norm $title), [StringComparison]::Ordinal)) {
        return $false
    }
    foreach ($author in $authors) {
        if (-not $normalized.Contains((Norm $author), [StringComparison]::Ordinal)) {
            return $false
        }
    }
    if ($text -notmatch '(?is)\\begin\s*\{\s*abstract\s*\}|\\abstract\b') {
        return $false
    }
    if ($text -notmatch '(?is)\\section\s*\{(?!\s*abstract\b)[^{}]+\}') {
        return $false
    }
    if ($text -notmatch '(?is)\\begin\s*\{\s*(equation\*?|align\*?|gather\*?|multline\*?|math|displaymath)\s*\}|\\\[|\$[^$]+\$') {
        return $false
    }
    if ($text -notmatch '(?is)\\begin\s*\{\s*thebibliography\s*\}|\\bibliography\s*\{') {
        return $false
    }
    if ($text -match '(?is)\b(abstract\s+only|first\s+page\s+only|preview\s+only)\b') {
        return $false
    }
    return $true
}
function TestArchive([byte[]]$body, [string[]]$authors) {
    $stopwatch = [Diagnostics.Stopwatch]::StartNew()
    $localArchiveDeadline = [DateTime]::UtcNow.AddSeconds(60)
    $archiveDeadline = if ($localArchiveDeadline -lt $globalDeadline) {
        $localArchiveDeadline
    } else {
        $globalDeadline
    }
    if ($body.Length -gt 67108864) {
        return [pscustomobject]@{
            Pass = $false
            Detail = 'COMPRESSED_LIMIT'
            Entries = @()
            Root = 'MISSING'
        }
    }
    $payload = $body
    $container = 'RAW'
    if (HasPrefix $body ([byte[]](0x1F, 0x8B, 0x08))) {
        $container = 'GZIP_SINGLE_MEMBER'
        $gzipResult = [Q1R7ExactGzip]::Validate(
            $body,
            268435456,
            200,
            $archiveDeadline)
        if (-not $gzipResult.Pass) {
            return [pscustomobject]@{
                Pass = $false
                Detail = 'GZIP_FAIL:' + $gzipResult.Error
                Entries = @()
                Root = 'MISSING'
            }
        }
        if ($gzipResult.ConsumedBytes -ne $body.LongLength) {
            return [pscustomobject]@{
                Pass = $false
                Detail = 'GZIP_CONSUMED_LENGTH_MISMATCH'
                Entries = @()
                Root = 'MISSING'
            }
        }
        $payload = $gzipResult.Payload
    }
    if ($stopwatch.Elapsed.TotalSeconds -gt 60 -or
        [DateTime]::UtcNow -ge $archiveDeadline) {
        return [pscustomobject]@{
            Pass = $false
            Detail = 'PARSE_DEADLINE'
            Entries = @()
            Root = 'MISSING'
        }
    }
    $isTar = $payload.Length -ge 262 -and
        ([Text.Encoding]::ASCII.GetString($payload, 257, 5) -ceq 'ustar')
    $files = [ordered]@{}
    $texts = [ordered]@{}
    $entries = [Collections.Generic.List[object]]::new()
    if (-not $isTar) {
        if ($container -ne 'GZIP_SINGLE_MEMBER') {
            return [pscustomobject]@{
                Pass = $false
                Detail = 'RAW_NON_TAR_FORBIDDEN'
                Entries = @()
                Root = 'MISSING'
            }
        }
        try {
            $singleText = TextDecodeStrict $payload
        } catch {
            return [pscustomobject]@{
                Pass = $false
                Detail = 'NOT_TAR_OR_STRICT_TEXT_TEX'
                Entries = @()
                Root = 'MISSING'
            }
        }
        if (-not (TestTexRoot $singleText $authors)) {
            return [pscustomobject]@{
                Pass = $false
                Detail = 'SINGLE_TEX_ROOT_INCOMPLETE'
                Entries = @()
                Root = 'MISSING'
            }
        }
        if ($singleText -match
            '(?is)\\(input|include|includegraphics|bibliography|bibliographystyle|addbibresource)\b') {
            return [pscustomobject]@{
                Pass = $false
                Detail = 'SINGLE_TEX_EXTERNAL_OR_DYNAMIC_TARGET_FORBIDDEN'
                Entries = @()
                Root = 'MISSING'
            }
        }
        return [pscustomobject]@{
            Pass = $true
            Detail = "$container/SINGLE_TEX_COMPLETE"
            Entries = @([pscustomobject]@{
                    Path = 'single.tex'
                    Type = 'TEXT'
                    Length = $payload.Length
                    SHA256 = Sha256 $payload
                })
            Root = 'single.tex'
        }
    }
    try {
        $memory = [IO.MemoryStream]::new($payload, $false)
        $tar = [System.Formats.Tar.TarReader]::new($memory, $false)
        $count = 0
        $total = 0
        $seen = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
        $seenCI = [Collections.Generic.HashSet[string]]::new(
            [StringComparer]::OrdinalIgnoreCase)
        while ($null -ne ($entry = $tar.GetNextEntry($false))) {
            AssertGlobalDeadline
            if ($stopwatch.Elapsed.TotalSeconds -gt 60 -or
                [DateTime]::UtcNow -ge $archiveDeadline) {
                throw 'PARSE_DEADLINE'
            }
            $count++
            if ($count -gt 512) { throw 'ENTRY_LIMIT' }
            $path = $entry.Name
            if (-not (TestPathSafe $path)) { throw "UNSAFE_PATH:$path" }
            if (-not $seen.Add($path) -or -not $seenCI.Add($path)) {
                throw "PATH_COLLISION:$path"
            }
            $entryType = [string]$entry.EntryType
            if ($entryType -notin 'RegularFile', 'V7RegularFile', 'Directory') {
                throw "ENTRY_TYPE:$entryType"
            }
            if ($entryType -eq 'Directory') {
                $entries.Add([pscustomobject]@{
                        Path = $path
                        Type = $entryType
                        Length = 0
                        SHA256 = 'N/A'
                    })
                continue
            }
            if ($entry.Length -gt 33554432) { throw "ENTRY_SIZE:$path" }
            $entryMemory = [IO.MemoryStream]::new()
            $entryBuffer = [byte[]]::new(65536)
            while (($entryRead = $entry.DataStream.Read(
                            $entryBuffer,
                            0,
                            $entryBuffer.Length)) -gt 0) {
                AssertGlobalDeadline
                if ([DateTime]::UtcNow -ge $archiveDeadline) { throw 'PARSE_DEADLINE' }
                if ($entryMemory.Length + $entryRead -gt 33554432) {
                    throw "ENTRY_SIZE:$path"
                }
                $entryMemory.Write($entryBuffer, 0, $entryRead)
            }
            $bytes = $entryMemory.ToArray()
            $entryMemory.Dispose()
            $total += $bytes.Length
            if ($total -gt 268435456) { throw 'TOTAL_LIMIT' }
            if ($bytes.Length -ge 262 -and
                ([Text.Encoding]::ASCII.GetString($bytes, 257, 5) -ceq 'ustar')) {
                throw "NESTED_TAR:$path"
            }
            $classification = ClassifyBytes $bytes
            if ($classification.Kind -in 'FORBIDDEN_CONTAINER', 'UNKNOWN_NONTEXT') {
                throw "$($classification.Kind):$path"
            }
            $files[$path] = $bytes
            if ($classification.Kind -eq 'TEXT') { $texts[$path] = $classification.Text }
            $entries.Add([pscustomobject]@{
                    Path = $path
                    Type = $classification.Kind
                    Length = $bytes.Length
                    SHA256 = Sha256 $bytes
                })
        }
        $tar.Dispose()
        $memory.Dispose()
        $roots = @()
        foreach ($pair in $texts.GetEnumerator()) {
            if ($pair.Key.EndsWith('.tex', [StringComparison]::OrdinalIgnoreCase) -and
                (TestTexRoot ([string]$pair.Value) $authors)) {
                $roots += $pair.Key
            }
        }
        if ($roots.Count -ne 1) { throw "ROOT_COUNT:$($roots.Count)" }
        $root = $roots[0]
        $reachable = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
        $visiting = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
        function VisitTex([string]$path) {
            if ($visiting.Contains($path)) { throw "TEX_CYCLE:$path" }
            if ($reachable.Contains($path)) { return }
            [void]$visiting.Add($path)
            [void]$reachable.Add($path)
            $text = [string]$texts[$path]
            $commands = [regex]::Matches(
                $text,
                '(?is)\\(input|include|includegraphics|bibliography|bibliographystyle|addbibresource)\b')
            foreach ($command in $commands) {
                $tail = $text.Substring($command.Index)
                $argument = [regex]::Match(
                    $tail,
                    '(?is)^\\(input|include|includegraphics|bibliography|bibliographystyle|addbibresource)\s*(?:\[[^\]]*\]\s*)?\{([^{}]+)\}')
                if (-not $argument.Success) { throw "DYNAMIC_TARGET:$path" }
                $commandName = $argument.Groups[1].Value.ToLowerInvariant()
                $rawTargets = if ($commandName -eq 'bibliography') {
                    $argument.Groups[2].Value.Split(',')
                } else {
                    @($argument.Groups[2].Value)
                }
                foreach ($rawTarget in $rawTargets) {
                    $target = $rawTarget.Trim()
                    if ($target -match '[\\$#{}]') { throw "DYNAMIC_PATH:$path" }
                    $parent = [IO.Path]::GetDirectoryName($path).Replace('\', '/')
                    $candidate = if ($parent) { $parent + '/' + $target } else { $target }
                    if ($commandName -in 'input', 'include') {
                        if (-not [IO.Path]::HasExtension($candidate)) { $candidate += '.tex' }
                    } elseif ($commandName -eq 'bibliography' -or
                        $commandName -eq 'addbibresource') {
                        if (-not [IO.Path]::HasExtension($candidate)) { $candidate += '.bib' }
                    } elseif ($commandName -eq 'bibliographystyle') {
                        if (-not [IO.Path]::HasExtension($candidate)) { $candidate += '.bst' }
                    } elseif ($commandName -eq 'includegraphics' -and
                        -not [IO.Path]::HasExtension($candidate)) {
                        $hits = @(
                            '.pdf', '.png', '.jpg', '.jpeg', '.eps', '.ps' |
                                ForEach-Object { $candidate + $_ } |
                                Where-Object { $files.Contains($_) })
                        if ($hits.Count -ne 1) { throw "GRAPHICS_TARGET_COUNT:$candidate" }
                        $candidate = $hits[0]
                    }
                    if (-not (TestPathSafe $candidate) -or
                        -not $files.Contains($candidate)) {
                        throw "MISSING_TARGET:$candidate"
                    }
                    if ($commandName -in 'input', 'include') {
                        if (-not $texts.Contains($candidate)) {
                            throw "NONTEXT_TEX_TARGET:$candidate"
                        }
                        VisitTex $candidate
                    }
                }
            }
            [void]$visiting.Remove($path)
        }
        VisitTex $root
        $allTex = @($texts.Keys | Where-Object {
                $_.EndsWith('.tex', [StringComparison]::OrdinalIgnoreCase)
            })
        foreach ($texPath in $allTex) {
            if (-not $reachable.Contains($texPath)) { throw "UNREACHABLE_TEX:$texPath" }
        }
        return [pscustomobject]@{
            Pass = $true
            Detail = "$container/TAR_COMPLETE"
            Entries = @($entries)
            Root = $root
        }
    } catch {
        try { $tar.Dispose() } catch {}
        try { $memory.Dispose() } catch {}
        return [pscustomobject]@{
            Pass = $false
            Detail = 'TAR_FAIL:' + $_.Exception.Message
            Entries = @($entries)
            Root = 'MISSING'
        }
    }
}
function TestPdf([byte[]]$body, [string[]]$authors) {
    if (-not (HasPrefix $body ([Text.Encoding]::ASCII.GetBytes('%PDF-')))) {
        return [pscustomobject]@{ Pass = $false; Detail = 'MAGIC_NOT_PDF' }
    }
    $pdf = Join-Path $tempDir 'candidate.pdf'
    $textPath = Join-Path $tempDir 'candidate.txt'
    $prefix = Join-Path $tempDir 'page'
    [IO.File]::WriteAllBytes($pdf, $body)
    try {
        $info = RunProcess $pdfinfo @($pdf) 120000
        if ($info.ExitCode -ne 0 -or
            $info.Stderr -match '(?i)(Error|Syntax Error|Warning)') {
            throw 'PDFINFO_FAIL'
        }
        $pageMatch = [regex]::Match($info.Stdout, '(?im)^Pages:\s*(\d+)\s*$')
        if (-not $pageMatch.Success) { throw 'PAGE_COUNT_MISSING' }
        $pages = [int]$pageMatch.Groups[1].Value
        if ($pages -lt 1 -or $pages -gt 200) { throw 'PAGE_COUNT_RANGE' }
        if ($info.Stdout -match '(?im)^Encrypted:\s*yes') { throw 'ENCRYPTED' }
        $textRun = RunProcess $pdftotext @(
            '-layout',
            '-enc',
            'UTF-8',
            '-nopgbrk',
            $pdf,
            $textPath) 120000
        if ($textRun.ExitCode -ne 0 -or
            $textRun.Stderr -match '(?i)(Error|Syntax Error|Warning)') {
            throw 'PDFTOTEXT_FAIL'
        }
        $text = [IO.File]::ReadAllText($textPath, [Text.Encoding]::UTF8)
        $renderRun = RunProcess $pdftoppm @(
            '-png',
            '-r',
            '144',
            '-f',
            '1',
            '-l',
            [string]$pages,
            $pdf,
            $prefix) 120000
        if ($renderRun.ExitCode -ne 0 -or
            $renderRun.Stderr -match '(?i)(Error|Syntax Error|Warning)') {
            throw 'PDFTOPPM_FAIL'
        }
        $renders = @(Get-ChildItem -LiteralPath $tempDir -File -Filter 'page-*.png')
        if ($renders.Count -ne $pages) { throw "RENDER_COUNT:$($renders.Count)/$pages" }
        $renderBytes = [int64]0
        foreach ($render in $renders) {
            if ($render.Length -eq 0) { throw 'ZERO_RENDER' }
            $renderBytes += $render.Length
        }
        if ($renderBytes -gt 536870912) { throw 'RENDER_TOTAL_LIMIT' }
        $normalized = Norm $text
        if (-not $normalized.Contains((Norm $title), [StringComparison]::Ordinal)) {
            throw 'TITLE_MISSING'
        }
        foreach ($author in $authors) {
            if (-not $normalized.Contains((Norm $author), [StringComparison]::Ordinal)) {
                throw "AUTHOR_MISSING:$author"
            }
        }
        if ($text -notmatch '(?i)\babstract\b') { throw 'ABSTRACT_MISSING' }
        if ($text -notmatch '(?i)\b(introduction|background|hydrodynamics)\b') {
            throw 'BODY_SECTION_MISSING'
        }
        if ($text -notmatch '(?i)\breferences\b') { throw 'REFERENCES_MISSING' }
        if ($pages -le 1 -or
            $text -match '(?i)\b(abstract only|first page only|preview only)\b') {
            throw 'INCOMPLETE_ARTICLE'
        }
        if ($text -notmatch '=') { throw 'EQUATION_SIGNAL_MISSING' }
        $pageEvidence = @()
        foreach ($page in 1..$pages) {
            $render = $renders | Where-Object {
                $_.BaseName -match ('-' + $page.ToString().PadLeft(
                        [Math]::Max(1, $pages.ToString().Length),
                        '0') + '$')
            } | Select-Object -First 1
            $pageEvidence += [pscustomobject]@{
                Page = $page
                RenderPath = if ($render) { $render.Name } else { 'MISSING' }
                RenderSHA256 = if ($render) { FileSha $render.FullName } else { 'MISSING' }
            }
        }
        return [pscustomobject]@{
            Pass = $false
            Detail = 'PENDING_MANUAL_PDF_CERTIFICATION'
            Pages = $pages
            TextSHA256 = FileSha $textPath
            RenderCount = $renders.Count
            RenderBytes = $renderBytes
            PageEvidence = $pageEvidence
            MechanicalEvidence = @(
                'TITLE',
                'ALL_BOUND_AUTHORS',
                'ABSTRACT',
                'SUBSTANTIVE_BODY',
                'EQUATION_SIGNAL',
                'REFERENCES')
            MissingCertification = @(
                'EQUATION_TO_PAGE_READABILITY',
                'APPENDIX_SUPPLEMENT_COMPLETENESS')
        }
    } catch {
        return [pscustomobject]@{ Pass = $false; Detail = $_.Exception.Message }
    }
}
function PublicOpView($operation) {
    [pscustomobject]@{
        ordinal = $operation.Ordinal
        step = $operation.Step
        utc_start = $operation.StartUTC
        utc_end = $operation.EndUTC
        requested_url = $operation.RequestedURL
        redirect_chain = $operation.RedirectChain
        final_url = $operation.FinalURL
        http_status = $operation.Status
        mime = $operation.MIME
        content_length = $operation.DeclaredContentLength
        actual_byte_length = $operation.ActualLength
        sha256 = $operation.SHA256
        magic16 = $operation.Magic16
        content_encoding = $operation.ContentEncoding
        transport_error = $operation.TransportError
        title = @($operation.Metadata.Title)
        authors = @($operation.Metadata.Authors)
        doi = @($operation.Metadata.DOI)
        pii = @($operation.Metadata.PII)
        arxiv_id = @($operation.Metadata.ArxivID)
    }
}

foreach ($path in @(
        $journalPath,
        $blobPath,
        $receiptPath,
        $resultPath,
        $tempDir,
        $blobTemp,
        $receiptTemp)) {
    if (Test-Path -LiteralPath $path) { throw "PREFLIGHT_TARGET_EXISTS:$path" }
}
if ((FileSha $preregPath) -cne $expectedPrereg) { throw 'PREREG_HASH_DRIFT' }
$actualRunnerSha256 = FileSha $PSCommandPath
if ($actualRunnerSha256 -cne $AuditedRunnerSha256) {
    throw 'AUDITED_RUNNER_HASH_DRIFT'
}
foreach ($tool in @($pdfinfo, $pdftotext, $pdftoppm)) {
    if (-not (Test-Path -LiteralPath $tool -PathType Leaf)) {
        throw "PREFLIGHT_TOOL_MISSING:$tool"
    }
}
$toolVersions = [ordered]@{
    pdfinfo = GetVersion $pdfinfo
    pdftotext = GetVersion $pdftotext
    pdftoppm = GetVersion $pdftoppm
}

$script:journalFs = [IO.File]::Open(
    $journalPath,
    [IO.FileMode]::CreateNew,
    [IO.FileAccess]::Write,
    [IO.FileShare]::None)
WriteJournal 'JOURNAL_VERSION=Q1R7_V1'
WriteJournal "PREREG_SHA256=$expectedPrereg"
WriteJournal "AUDITED_RUNNER_SHA256=$AuditedRunnerSha256"
WriteJournal ('PROCESS_START_UTC=' + [DateTime]::UtcNow.ToString('o'))
[IO.Directory]::CreateDirectory($tempDir) | Out-Null

$accepted = $false
$acceptedBytes = $null
$acceptedType = 'NONE'
$classifier = $null
$boundAuthors = @()
$boundDois = @()
$doiEvidenceOps = @()
$arxivId = $null
$acceptedEvidenceOrdinal = $null
$identityConflict = $false

$o1 = InvokeQ1Request 1 'O1_PUBLISHER' (
    'https://www.sciencedirect.com/science/article/pii/S0550321316000535')
$o1Title = @($o1.Metadata.Title |
    Where-Object { (Norm $_) -ceq (Norm $title) } |
    Select-Object -Unique)
$boundAuthors = @($o1.Metadata.Authors |
    Where-Object { $_ } |
    Select-Object -Unique)
$o1Eligible = $o1Title.Count -eq 1 -and $boundAuthors.Count -gt 0
$o1BodyText = [Text.Encoding]::UTF8.GetString($o1.Body)
$o1HeaderValues = @($o1.Headers.Values) -join ' '
$o1PiiEvidence = @($o1.Metadata.PII | Where-Object {
        $_ -ceq $pii
    }).Count -gt 0 -or
    $o1BodyText.Contains($pii, [StringComparison]::Ordinal) -or
    $o1HeaderValues.Contains($pii, [StringComparison]::Ordinal)
$o1Eligible = $o1Eligible -and
    $o1.Status -ge 200 -and
    $o1.Status -lt 300 -and
    $o1PiiEvidence
if ($o1Eligible) {
    $boundDois = @($o1.Metadata.DOI |
        ForEach-Object { NormalizeDoi $_ } |
        Where-Object { $_ } |
        Sort-Object -Unique)
    if ($boundDois.Count -gt 0) { $doiEvidenceOps += 1 }
}
$pdfLinks = if ($o1.Body.Length -gt 0) {
    @(GetPublisherPdfLinks $o1)
} else {
    @()
}

if ($pdfLinks.Count -eq 1) {
    $o2 = InvokeQ1Request 2 'O2_FULLTEXT' $pdfLinks[0]
    if ($o2.Status -ge 200 -and
        $o2.Status -lt 300 -and
        ($o2.ContentEncoding -eq 'MISSING' -or $o2.ContentEncoding -eq 'identity') -and
        $o1Eligible) {
        $classifier = TestPdf $o2.Body $boundAuthors
        if ($classifier.Pass) {
            $accepted = $true
            $acceptedBytes = $o2.Body
            $acceptedType = 'CANONICAL_FULL_ARTICLE_PDF'
            $acceptedEvidenceOrdinal = 2
        }
    }
} else {
    $o2 = InvokeQ1Request 2 'O2_CROSSREF' (
        'https://api.crossref.org/works?query=S0550321316000535&rows=3&select=DOI%2Ctitle%2Cauthor%2CURL')
    $eligible = @()
    if ($o2.Status -ge 200 -and $o2.Status -lt 300 -and $o1Eligible) {
        try {
            $json = [Text.Encoding]::UTF8.GetString($o2.Body) |
                ConvertFrom-Json -Depth 20
            foreach ($item in @($json.message.items)) {
                $recordTitle = if (@($item.title).Count -gt 0) {
                    [string]@($item.title)[0]
                } else {
                    ''
                }
                $recordAuthors = @($item.author | ForEach-Object {
                        (($_.given, $_.family | Where-Object { $_ }) -join ' ').Trim()
                    })
                if ((Norm $recordTitle) -ceq (Norm $title) -and
                    (SameSet $recordAuthors $boundAuthors)) {
                    $eligible += [pscustomobject]@{
                        Title = $recordTitle
                        Authors = $recordAuthors
                        DOI = NormalizeDoi ([string]$item.DOI)
                        URL = [string]$item.URL
                    }
                }
            }
        } catch {}
    }
    if ($eligible.Count -eq 1 -and $eligible[0].DOI) {
        $boundDois = @($boundDois + $eligible[0].DOI | Sort-Object -Unique)
        $doiEvidenceOps += 2
        $o2.Metadata.Title = @($eligible[0].Title)
        $o2.Metadata.Authors = @($eligible[0].Authors)
        $o2.Metadata.DOI = @($eligible[0].DOI)
    }
}
if ($boundDois.Count -gt 1) {
    $identityConflict = $true
    $accepted = $false
    $acceptedBytes = $null
    $acceptedType = 'NONE'
    $classifier = [pscustomobject]@{
        Pass = $false
        Detail = 'CONFLICTING_DISTINCT_DOI_SET'
    }
}

if ($accepted) {
    AddSkipped 3 'O3_ARXIV_EXACT_TITLE_QUERY' 'SKIPPED_SOURCE_ALREADY_ACCEPTED'
    AddSkipped 4 'O4_ARXIV_ABSTRACT' 'SKIPPED_SOURCE_ALREADY_ACCEPTED'
    AddSkipped 5 'O5_ARXIV_EPRINT' 'SKIPPED_SOURCE_ALREADY_ACCEPTED'
    AddSkipped 6 'O6_DOI_BINDING' 'SKIPPED_SOURCE_ALREADY_ACCEPTED'
} else {
    $o3 = InvokeQ1Request 3 'O3_ARXIV_EXACT_TITLE_QUERY' (
        'https://export.arxiv.org/api/query?search_query=ti%3A%22Hydrodynamics%20of%20ultra-relativistic%20bubble%20walls%22&start=0&max_results=3&sortBy=relevance&sortOrder=descending')
    $matches = @()
    if ($o3.Status -ge 200 -and $o3.Status -lt 300) {
        try {
            [xml]$xml = [Text.Encoding]::UTF8.GetString($o3.Body)
            foreach ($entry in @($xml.SelectNodes(
                        '/*[local-name()="feed"]/*[local-name()="entry"]'))) {
                $entryTitle = $entry.SelectSingleNode(
                    './*[local-name()="title"]').InnerText
                $entryAuthors = @($entry.SelectNodes(
                        './*[local-name()="author"]/*[local-name()="name"]') |
                        ForEach-Object { $_.InnerText })
                $entryId = $entry.SelectSingleNode(
                    './*[local-name()="id"]').InnerText
                $doiNode = $entry.SelectSingleNode('./*[local-name()="doi"]')
                $entryDoi = if ($doiNode) { NormalizeDoi $doiNode.InnerText } else { $null }
                $doiMatch = $entryDoi -and $boundDois -contains $entryDoi
                $authorMatch = $boundAuthors.Count -gt 0 -and
                    (SameSet $entryAuthors $boundAuthors)
                if ((Norm $entryTitle) -ceq (Norm $title) -and
                    ($doiMatch -or $authorMatch)) {
                    $matches += [pscustomobject]@{
                        Title = $entryTitle
                        Authors = $entryAuthors
                        IdUri = $entryId
                        DOI = $entryDoi
                    }
                }
            }
        } catch {}
    }
    if ($matches.Count -eq 1) {
        $match = $matches[0]
        if ($match.DOI) {
            $boundDois = @($boundDois + $match.DOI | Sort-Object -Unique)
            $doiEvidenceOps += 3
            if ($boundDois.Count -gt 1) { $identityConflict = $true }
        }
        $arxivId = ([Uri]$match.IdUri).Segments[-1].TrimEnd('/')
        if ($arxivId -notmatch
            '^(?:[0-9]{4}\.[0-9]{4,5}(?:v[0-9]+)?|[A-Za-z.-]+/[0-9]{7}(?:v[0-9]+)?)$') {
            throw 'ARXIV_CANONICAL_ID_SYNTAX_FAILURE'
        }
        $o3.Metadata.Title = @($match.Title)
        $o3.Metadata.Authors = @($match.Authors)
        $o3.Metadata.DOI = @($match.DOI | Where-Object { $_ })
        $o3.Metadata.ArxivID = @($arxivId)
        $o4 = InvokeQ1Request 4 'O4_ARXIV_ABSTRACT' (
            'https://arxiv.org/abs/' + $arxivId)
        $o4Metadata = GetHtmlMeta $o4.Body
        $o4.Metadata = $o4Metadata
        $o4Ok = $o4.Status -ge 200 -and
            $o4.Status -lt 300 -and
            @($o4Metadata.Title |
                Where-Object { (Norm $_) -ceq (Norm $title) }).Count -eq 1 -and
            (SameSet $o4Metadata.Authors $boundAuthors) -and
            [Text.Encoding]::UTF8.GetString($o4.Body).Contains(
                $arxivId,
                [StringComparison]::Ordinal)
        if ($o4Ok) {
            $o5 = InvokeQ1Request 5 'O5_ARXIV_EPRINT' (
                'https://export.arxiv.org/e-print/' + $arxivId)
            if ($o5.Status -ge 200 -and
                $o5.Status -lt 300 -and
                ($o5.ContentEncoding -eq 'MISSING' -or
                    $o5.ContentEncoding -eq 'identity')) {
                $classifier = if (HasPrefix $o5.Body (
                        [Text.Encoding]::ASCII.GetBytes('%PDF-'))) {
                    TestPdf $o5.Body $boundAuthors
                } else {
                    TestArchive $o5.Body $boundAuthors
                }
                if ($classifier.Pass) {
                    $accepted = $true
                    $acceptedBytes = $o5.Body
                    $acceptedEvidenceOrdinal = 5
                    $acceptedType = if ($classifier.Detail -eq 'PDF_COMPLETE') {
                        'CANONICAL_FULL_ARTICLE_PDF'
                    } else {
                        'SOURCE_ARCHIVE'
                    }
                }
            }
        } else {
            AddSkipped 5 'O5_ARXIV_EPRINT' 'SKIPPED_PRECONDITION'
        }
    } else {
        AddSkipped 4 'O4_ARXIV_ABSTRACT' 'SKIPPED_PRECONDITION'
        AddSkipped 5 'O5_ARXIV_EPRINT' 'SKIPPED_PRECONDITION'
    }
    if ($accepted) {
        AddSkipped 6 'O6_DOI_BINDING' 'SKIPPED_SOURCE_ALREADY_ACCEPTED'
    } elseif ($boundDois.Count -eq 1) {
        $o6 = InvokeQ1Request 6 'O6_DOI_BINDING' (DoiUrl $boundDois[0])
    } else {
        AddSkipped 6 'O6_DOI_BINDING' 'SKIPPED_PRECONDITION'
    }
}

if (-not $o1Eligible -or $identityConflict -or $boundDois.Count -gt 1) {
    $accepted = $false
    $acceptedBytes = $null
    $acceptedType = 'NONE'
    if ($null -eq $classifier -or $classifier.Pass) {
        $classifier = [pscustomobject]@{
            Pass = $false
            Detail = if (-not $o1Eligible) {
                'O1_EXACT_TITLE_AUTHOR_PII_BINDING_MISSING'
            } else {
                'CONFLICTING_DISTINCT_DOI_SET'
            }
        }
    }
}

for ($i = 1; $i -le 6; $i++) {
    if (-not $script:slots.Contains([string]$i)) { throw "UNACCOUNTED_SLOT:$i" }
}
$sourceSha = 'MISSING'
if ($accepted) {
    $file = [IO.File]::Open(
        $blobTemp,
        [IO.FileMode]::CreateNew,
        [IO.FileAccess]::Write,
        [IO.FileShare]::None)
    try {
        $file.Write($acceptedBytes, 0, $acceptedBytes.Length)
        $file.Flush($true)
    } finally {
        $file.Dispose()
    }
    $sourceSha = FileSha $blobTemp
    if ($sourceSha -cne (Sha256 $acceptedBytes)) {
        throw 'TEMP_BLOB_HASH_MISMATCH'
    }
}
Get-ChildItem -LiteralPath $tempDir -Force | Remove-Item -Force
[IO.Directory]::Delete($tempDir)
AssertGlobalDeadline
WriteJournal (
    'TERMINAL_SLOT_STATE=' +
    (($script:slots.GetEnumerator() |
            Sort-Object { [int]$_.Key } |
            ForEach-Object { "$($_.Key)=$($_.Value)" }) -join ';'))
WriteJournal "FINAL_REQUEST_COUNT=$($script:requestCount)/6_TERMINAL"
WriteJournal ('READY_TO_COMMIT|utc=' + [DateTime]::UtcNow.ToString('o'))
$script:journalFs.Dispose()
$script:journalFs = $null
$journalSha = FileSha $journalPath
if ($accepted) {
    AssertGlobalDeadline
    [IO.File]::Move($blobTemp, $blobPath, $false)
    if ((FileSha $blobPath) -cne $sourceSha) { throw 'FINAL_BLOB_HASH_MISMATCH' }
}
$operationViews = @($script:ops | ForEach-Object { PublicOpView $_ })
$crossBinding = @()
if ($accepted) {
    $crossBinding += [pscustomobject]@{
        IdentifierType = 'PII'
        Identifier = $pii
        SourceSHA256 = $sourceSha
        EvidenceOperations = @(1, $acceptedEvidenceOrdinal | Sort-Object -Unique)
    }
    if ($boundDois.Count -eq 1) {
        $crossBinding += [pscustomobject]@{
            IdentifierType = 'DOI'
            Identifier = $boundDois[0]
            SourceSHA256 = $sourceSha
            EvidenceOperations = @(
                $doiEvidenceOps + $acceptedEvidenceOrdinal |
                    Sort-Object -Unique)
        }
    }
    if ($arxivId) {
        $crossBinding += [pscustomobject]@{
            IdentifierType = 'ARXIV'
            Identifier = $arxivId
            SourceSHA256 = $sourceSha
            EvidenceOperations = @(3, 4, 5)
        }
    }
}
$receipt = [ordered]@{
    TASK_ID = 'A1_K1_A2_K4_P5_3_B6B2_10_C01_RW1_Q1R7_SOURCE_ACQUISITION_TASK290'
    THEORY_AUTHOR = 'Martin Jambor'
    PROCESS_AND_ACQUISITION_IMPLEMENTER = 'Codex'
    ROUTE = 'A1_K1_A2_K4/P5.3/B6b-2.10/H_RDIV-MF1-v1/C01-RW1/Q1R7'
    PREREG_SHA256 = $expectedPrereg
    AUDITED_RUNNER_SHA256 = $AuditedRunnerSha256
    RUN_AUTHORIZED = $false
    PYTHON_PROCESSES = 0
    USER_AGENT = 'Teoria-Q1R7-CompleteSource/1.0'
    TOOL_VERSIONS = $toolVersions
    SOURCE_OPERATION_COUNT = "$($script:requestCount)/6_TERMINAL"
    SLOT_LEDGER = $script:slots
    OPERATIONS = $operationViews
    FROZEN_TITLE = $title
    BOUND_AUTHORS = @($boundAuthors)
    BOUND_DOIS = @($boundDois)
    BOUND_PII = $pii
    BOUND_ARXIV_ID = if ($arxivId) { $arxivId } else { 'MISSING' }
    SOURCE_UNIVERSE_COMPLETE = if ($accepted) { 'PASS' } else { 'FAIL_NOT_CERTIFIED' }
    ACCEPTED_SOURCE_TYPE = $acceptedType
    ACCEPTED_SOURCE_SHA256 = $sourceSha
    CLASSIFIER = if ($classifier) {
        $classifier
    } else {
        [pscustomobject]@{ Pass = $false; Detail = 'NO_CANDIDATE_SOURCE' }
    }
    CROSS_BINDING = $crossBinding
    JOURNAL_SHA256 = $journalSha
    OUTCOME = if ($accepted) {
        'ACQUISITION_COMPLETE_PENDING_INDEPENDENT_PHYSICS_SCREEN'
    } else {
        'REVIEW_Q1R7_SOURCE_UNIVERSE_NOT_CERTIFIED_NO_PHYSICAL_INFERENCE'
    }
    NONCLAIMS = @(
        'No S0-S13 physics result',
        'No complete W10 claim',
        'No score/depth/A3 change',
        'No P5.4/G8/G9 authorization')
}
$json = $receipt | ConvertTo-Json -Depth 30
$receiptBytes = $utf8.GetBytes($json + [char]10)
$receiptFile = [IO.File]::Open(
    $receiptTemp,
    [IO.FileMode]::CreateNew,
    [IO.FileAccess]::Write,
    [IO.FileShare]::None)
try {
    $receiptFile.Write($receiptBytes, 0, $receiptBytes.Length)
    $receiptFile.Flush($true)
} finally {
    $receiptFile.Dispose()
}
[IO.File]::Move($receiptTemp, $receiptPath, $false)

Write-Output "Q1R7_SOURCE_OPERATION_COUNT=$($script:requestCount)/6_TERMINAL"
Write-Output ('SOURCE_UNIVERSE_COMPLETE=' + $receipt.SOURCE_UNIVERSE_COMPLETE)
Write-Output "ACCEPTED_SOURCE_TYPE=$acceptedType"
Write-Output "ACCEPTED_SOURCE_SHA256=$sourceSha"
Write-Output "JOURNAL_SHA256=$journalSha"
Write-Output ('RECEIPT_SHA256=' + (FileSha $receiptPath))
