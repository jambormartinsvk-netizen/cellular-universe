[CmdletBinding(DefaultParameterSetName = 'SelfTest')]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[0-9A-F]{64}$')]
    [string]$ExpectedRunnerSha256,

    [Parameter(Mandatory = $true, ParameterSetName = 'SelfTest')]
    [switch]$SelfTest,

    [Parameter(Mandatory = $true, ParameterSetName = 'Acquire')]
    [switch]$Acquire,

    [Parameter(Mandatory = $true, ParameterSetName = 'Acquire')]
    [ValidatePattern('^[0-9A-F]{64}$')]
    [string]$AuthorizationLedgerSha256
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$base = $PSScriptRoot
$runnerPath = $PSCommandPath
$preregPath = Join-Path $base '285_B6B2_10_H_RDIV_C01_RW1_Q1R7_V2_TECHNICAL_RECOVERY_PREREGISTRATION_SK.md'
$v1PreregPath = Join-Path $base '283_B6B2_10_H_RDIV_C01_RW1_V1_Q1R6_TO_Q1R7_ORDERED_TRANSITION_COMPLETE_SOURCE_PREREGISTRATION_SK.md'
$v1RunnerPath = Join-Path $base '.q1r7_acquire.ps1'
$v1JournalPath = Join-Path $base '283C_B6B2_10_Q1R7_SOURCE_OPERATION_JOURNAL.txt'
$v1ResultPath = Join-Path $base '284_B6B2_10_H_RDIV_C01_RW1_V1_Q1R7_S0_S13_RESULT_SK.md'
$eventLedgerPath = Join-Path $base '..\..\..\HISTORY\00_EVENT_LEDGER.md'

$journalPath = Join-Path $base '285C_B6B2_10_Q1R7_V2_SOURCE_OPERATION_JOURNAL.txt'
$blobPath = Join-Path $base '285A_B6B2_10_Q1R7_V2_PRIMARY_SOURCE_BLOB.bin'
$receiptPath = Join-Path $base '285B_B6B2_10_Q1R7_V2_COMPLETE_SOURCE_RECEIPT.txt'
$resultPath = Join-Path $base '286_B6B2_10_H_RDIV_C01_RW1_Q1R7_V2_S0_S13_RESULT_SK.md'
$tempDir = Join-Path $base '.q1r7_v2_tmp'
$blobTemp = Join-Path $base '.285A_Q1R7_V2.tmp'
$receiptTemp = Join-Path $base '.285B_Q1R7_V2.tmp'
$selfTestDir = Join-Path $base '.q1r7_v2_selftest_tmp'

$expectedPrereg = 'EA055CE0555A35914A933870FF84D8DCF176FD25904834787A8C21269CD3F0A2'
$expectedV1Prereg = 'E9F7AD9237BE24EB7CB4CF8EE80F58E1B1D38D6834D83FB442A5A909BD47B3B6'
$expectedV1Runner = '1CBA6274580D5DF7CD88F24A5C42C50904DC8593192F644F353B49E27391BC2A'
$expectedV1Journal = 'C104472F6079E5E5CE16680E4B2B3F8E704FF5E07ECB566B53BDC0250DD7BD2F'
$expectedV1Result = '879AA3B9F9B5806E101DD1E1BAE4D5EC61ADD1B2711342FD3EC047099827F7FA'

$pdfinfo = 'C:\Users\jambor.CHASTIA\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdfinfo.exe'
$pdftotext = 'C:\Program Files\Git\mingw64\bin\pdftotext.exe'
$pdftoppm = 'C:\Users\jambor.CHASTIA\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe'
$title = 'Hydrodynamics of ultra-relativistic bubble walls'
$pii = 'S0550321316000535'
$utf8 = [Text.UTF8Encoding]::new($false)
$globalCts = [Threading.CancellationTokenSource]::new([TimeSpan]::FromSeconds(600))
$globalDeadline = [DateTime]::UtcNow.AddSeconds(600)
$script:ops = [Collections.Generic.List[object]]::new()
$script:slots = [ordered]@{ '1' = 'INHERITED_CONSUMED:O1_PUBLISHER' }
$script:requestCount = 1
$script:journalFs = $null
$script:networkDisabled = [bool]$SelfTest
$script:networkRequests = 0

function BootstrapFileSha([string]$path) {
    (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash
}

foreach ($binding in @(
        @($runnerPath, $ExpectedRunnerSha256, 'RUNNER_HASH_DRIFT'),
        @($preregPath, $expectedPrereg, 'PREREG_HASH_DRIFT'),
        @($v1PreregPath, $expectedV1Prereg, 'V1_PREREG_HASH_DRIFT'),
        @($v1RunnerPath, $expectedV1Runner, 'V1_RUNNER_HASH_DRIFT'),
        @($v1JournalPath, $expectedV1Journal, 'V1_JOURNAL_HASH_DRIFT'),
        @($v1ResultPath, $expectedV1Result, 'V1_RESULT_HASH_DRIFT'))) {
    if (-not (Test-Path -LiteralPath $binding[0] -PathType Leaf)) {
        throw "IMMUTABLE_INPUT_MISSING:$($binding[0])"
    }
    if ((BootstrapFileSha $binding[0]) -cne $binding[1]) {
        throw $binding[2]
    }
}

function AssertAbsentTargets([string[]]$paths) {
    foreach ($path in @($paths)) {
        if (Test-Path -LiteralPath $path) {
            throw "PREFLIGHT_TARGET_EXISTS:$path"
        }
    }
}

function OpenJournalThenTempDirectory(
    [string]$newJournalPath,
    [string]$newTempDirectory
) {
    $file = [IO.File]::Open(
        $newJournalPath,
        [IO.FileMode]::CreateNew,
        [IO.FileAccess]::Write,
        [IO.FileShare]::None)
    try {
        [IO.Directory]::CreateDirectory($newTempDirectory) | Out-Null
        return $file
    } catch {
        $file.Dispose()
        throw
    }
}

function AssertPathInsideRoot(
    [string]$path,
    [string]$allowedRoot,
    [string]$failureCode
) {
    $resolvedRoot = [IO.Path]::GetFullPath($allowedRoot).TrimEnd(
        [char[]]@(
            [IO.Path]::DirectorySeparatorChar,
            [IO.Path]::AltDirectorySeparatorChar))
    $resolvedPath = [IO.Path]::GetFullPath($path)
    if (-not $resolvedPath.StartsWith(
            $resolvedRoot + [IO.Path]::DirectorySeparatorChar,
            [StringComparison]::OrdinalIgnoreCase)) {
        throw $failureCode
    }
}

function RemoveScopedDirectory([string]$path, [string]$allowedRoot) {
    AssertPathInsideRoot $path $allowedRoot 'DIRECTORY_CLEANUP_SCOPE_FAILURE'
    if (Test-Path -LiteralPath $path) {
        Remove-Item -LiteralPath $path -Recurse -Force
    }
}

function RemoveScopedFile([string]$path, [string]$allowedRoot) {
    AssertPathInsideRoot $path $allowedRoot 'FILE_CLEANUP_SCOPE_FAILURE'
    if (Test-Path -LiteralPath $path) {
        Remove-Item -LiteralPath $path -Force
    }
}

AssertAbsentTargets @(
    $journalPath,
    $blobPath,
    $receiptPath,
    $resultPath,
    $tempDir,
    $blobTemp,
    $receiptTemp,
    $selfTestDir)

# Reuse only hash-bound, previously audited pure classifier/helper definitions.
# The V1 request adapter and every V1 top-level statement are deliberately excluded.
$v1Text = [IO.File]::ReadAllText($v1RunnerPath)
$typeMatch = [regex]::Match(
    $v1Text,
    "(?s)Add-Type -TypeDefinition @'\r?\n(?<code>.*?)\r?\n'@")
if (-not $typeMatch.Success) { throw 'V1_TYPE_BLOCK_NOT_FOUND' }
Add-Type -TypeDefinition $typeMatch.Groups['code'].Value -Language CSharp

$tokens = $null
$parseErrors = $null
$v1Ast = [Management.Automation.Language.Parser]::ParseFile(
    $v1RunnerPath,
    [ref]$tokens,
    [ref]$parseErrors)
if (@($parseErrors).Count -ne 0) { throw 'V1_AST_PARSE_ERROR' }
$functionAsts = @($v1Ast.FindAll({
            param($node)
            $node -is [Management.Automation.Language.FunctionDefinitionAst]
        }, $false))
$functionMap = @{}
foreach ($node in $functionAsts) {
    if ($functionMap.ContainsKey($node.Name)) {
        throw "V1_DUPLICATE_FUNCTION:$($node.Name)"
    }
    $functionMap[$node.Name] = $node
}
$helperAllowlist = @(
    'Sha256',
    'FileSha',
    'AssertGlobalDeadline',
    'RemainingMilliseconds',
    'Magic16',
    'Norm',
    'SameSet',
    'NormalizeDoi',
    'DoiUrl',
    'WriteJournal',
    'RunProcess',
    'GetVersion',
    'GetHtmlMeta',
    'IsPublisherHost',
    'AssertSecureUri',
    'TextDecodeStrict',
    'TestPathSafe',
    'HasPrefix',
    'ClassifyBytes',
    'TestTexRoot',
    'TestArchive',
    'TestPdf',
    'PublicOpView')
foreach ($name in $helperAllowlist) {
    if (-not $functionMap.ContainsKey($name)) {
        throw "V1_ALLOWLIST_FUNCTION_MISSING:$name"
    }
    . ([scriptblock]::Create($functionMap[$name].Extent.Text))
}

function ReadBodyBytes(
    [IO.Stream]$Stream,
    [Threading.CancellationToken]$CancellationToken,
    [long]$MaxBytes = 67108864
) {
    $memory = [IO.MemoryStream]::new()
    try {
        $buffer = [byte[]]::new(65536)
        while ($true) {
            $readTask = $Stream.ReadAsync(
                $buffer,
                0,
                $buffer.Length,
                $CancellationToken)
            $read = $readTask.GetAwaiter().GetResult()
            if ($read -eq 0) { break }
            AssertGlobalDeadline
            if ($memory.Length + $read -gt $MaxBytes) {
                throw 'MAX_BODY_BYTES_EXCEEDED'
            }
            $memory.Write($buffer, 0, $read)
        }
        $bytes = [byte[]]$memory.ToArray()
        return ,$bytes
    } finally {
        $memory.Dispose()
    }
}

function TestV2FinalHost([string]$step, [Uri]$uri) {
    $hostLower = $uri.DnsSafeHost.ToLowerInvariant()
    switch -Wildcard ($step) {
        'O2_*' { return $hostLower -eq 'api.crossref.org' }
        'O3_*' { return $hostLower -eq 'export.arxiv.org' }
        'O4_*' {
            return $hostLower -eq 'arxiv.org' -or
                $hostLower.EndsWith('.arxiv.org')
        }
        'O5_*' { return $hostLower -eq 'export.arxiv.org' }
        'O6_*' {
            return $hostLower -eq 'doi.org' -or
                $hostLower -eq 'sciencedirect.com' -or
                $hostLower.EndsWith('.sciencedirect.com')
        }
        default { return $false }
    }
}

function InvokeNetworkSend(
    [Net.Http.HttpClient]$Client,
    [Net.Http.HttpRequestMessage]$Request,
    [Threading.CancellationToken]$CancellationToken
) {
    if ($script:networkDisabled) { throw 'NETWORK_DISABLED_SELFTEST' }
    $script:networkRequests++
    $Client.SendAsync(
        $Request,
        [Net.Http.HttpCompletionOption]::ResponseHeadersRead,
        $CancellationToken).GetAwaiter().GetResult()
}

function GetNextCumulativeRequestCount([int]$currentCount, [int]$ordinal) {
    if ($ordinal -ne ($currentCount + 1)) {
        throw "REQUEST_ORDINAL_NOT_CUMULATIVE:$ordinal/$currentCount"
    }
    if ($ordinal -lt 2 -or $ordinal -gt 6) {
        throw "REQUEST_ORDINAL_OUT_OF_RANGE:$ordinal"
    }
    return $currentCount + 1
}

function InvokeV2Request([int]$ordinal, [string]$step, [string]$url) {
    AssertGlobalDeadline
    if ($script:slots.Contains([string]$ordinal)) {
        throw "REQUEST_SLOT_ALREADY_ACCOUNTED:$ordinal"
    }
    $script:requestCount = GetNextCumulativeRequestCount (
        $script:requestCount) $ordinal
    $start = [DateTime]::UtcNow
    WriteJournal (
        "REQUEST_RESERVED|ordinal=$ordinal|step=$step|utc=" +
        $start.ToString('o') + "|url=$url")
    $redirects = [Collections.Generic.List[string]]::new()
    $status = -1
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
            $visited = [Collections.Generic.HashSet[string]]::new(
                [StringComparer]::Ordinal)
            [void]$visited.Add($current.AbsoluteUri)
            for ($redirectIndex = 0; $redirectIndex -le 5; $redirectIndex++) {
                $request = [Net.Http.HttpRequestMessage]::new(
                    [Net.Http.HttpMethod]::Get,
                    $current)
                [void]$request.Headers.TryAddWithoutValidation(
                    'User-Agent',
                    'Teoria-Q1R7-CompleteSource/1.0')
                [void]$request.Headers.TryAddWithoutValidation(
                    'Accept-Encoding',
                    'identity')
                $headersCts =
                    [Threading.CancellationTokenSource]::CreateLinkedTokenSource(
                        $globalCts.Token)
                $headersCts.CancelAfter([TimeSpan]::FromSeconds(30))
                try {
                    $response = InvokeNetworkSend $client $request $headersCts.Token
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
                if (-not (TestV2FinalHost $step $current)) {
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
                $bodyCts =
                    [Threading.CancellationTokenSource]::CreateLinkedTokenSource(
                        $globalCts.Token)
                $bodyCts.CancelAfter([TimeSpan]::FromSeconds(90))
                try {
                    $stream = $response.Content.ReadAsStreamAsync(
                        $bodyCts.Token).GetAwaiter().GetResult()
                    try {
                        $body = [byte[]](ReadBodyBytes $stream $bodyCts.Token)
                    } finally {
                        $stream.Dispose()
                    }
                } finally {
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
        $errorText = $_.Exception.Message.Replace(
            [char]13,
            ' ').Replace(
            [char]10,
            ' ')
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
    if ($errorText -cne 'NONE') {
        throw "REQUEST_TECHNICAL_FAILURE:${ordinal}:$errorText"
    }
    return $operation
}

function AddV2Skipped([int]$ordinal, [string]$step, [string]$reason) {
    if ($script:slots.Contains([string]$ordinal)) {
        throw "REQUEST_SLOT_ALREADY_ACCOUNTED:$ordinal"
    }
    $script:slots[[string]$ordinal] = $reason + ':' + $step
    WriteJournal "REQUEST_SLOT_RETIRED|ordinal=$ordinal|step=$step|reason=$reason"
}

function RetireV2Range([int]$startOrdinal, [string]$reason) {
    $steps = @{
        2 = 'O2_CROSSREF'
        3 = 'O3_ARXIV_EXACT_TITLE_QUERY'
        4 = 'O4_ARXIV_ABSTRACT'
        5 = 'O5_ARXIV_EPRINT'
        6 = 'O6_DOI_PII_BINDING'
    }
    for ($ordinal = $startOrdinal; $ordinal -le 6; $ordinal++) {
        if (-not $script:slots.Contains([string]$ordinal)) {
            AddV2Skipped $ordinal $steps[$ordinal] $reason
        }
    }
}

function AssertSelfTest([bool]$condition, [string]$message) {
    if (-not $condition) { throw "SELFTEST_ASSERT:$message" }
}

function InvokeLocalSelfTest {
    [IO.Directory]::CreateDirectory($selfTestDir) | Out-Null
    $v1JournalBefore = FileSha $v1JournalPath
    $v1ResultBefore = FileSha $v1ResultPath
    $results = [Collections.Generic.List[string]]::new()
    try {
        foreach ($size in @(0, 1, 65536, 65537)) {
            $input = [byte[]]::new($size)
            for ($i = 0; $i -lt $size; $i++) {
                $input[$i] = [byte]($i % 251)
            }
            $stream = [IO.MemoryStream]::new($input, $false)
            try {
                $actual = ReadBodyBytes $stream ([Threading.CancellationToken]::None)
            } finally {
                $stream.Dispose()
            }
            AssertSelfTest ($actual -is [byte[]]) "F01_TYPE_$size"
            AssertSelfTest ($actual.Length -eq $size) "F01_LENGTH_$size"
            AssertSelfTest (
                [Linq.Enumerable]::SequenceEqual($actual, $input)) "F01_BYTES_$size"
        }
        $results.Add('F01_BYTE_ARRAY_READ_API=PASS')

        $response = [Net.Http.HttpResponseMessage]::new(
            [Net.HttpStatusCode]::Forbidden)
        try {
            $response.Content = [Net.Http.ByteArrayContent]::new([byte[]]@())
            $stream = $response.Content.ReadAsStream()
            try {
                $empty403 = ReadBodyBytes $stream ([Threading.CancellationToken]::None)
            } finally {
                $stream.Dispose()
            }
            AssertSelfTest ($response.StatusCode -eq 403) 'F02_STATUS'
            AssertSelfTest ($empty403 -is [byte[]]) 'F02_TYPE'
            AssertSelfTest ($empty403.Length -eq 0) 'F02_LENGTH'
        } finally {
            $response.Dispose()
        }
        $results.Add('F02_HTTP403_EMPTY_BODY=PASS')

        $payload = [Text.Encoding]::ASCII.GetBytes('abc')
        $response = [Net.Http.HttpResponseMessage]::new(
            [Net.HttpStatusCode]::Forbidden)
        try {
            $response.Content = [Net.Http.ByteArrayContent]::new($payload)
            $stream = $response.Content.ReadAsStream()
            try {
                $nonempty403 =
                    ReadBodyBytes $stream ([Threading.CancellationToken]::None)
            } finally {
                $stream.Dispose()
            }
            AssertSelfTest ($nonempty403 -is [byte[]]) 'F03_TYPE'
            AssertSelfTest ($nonempty403.Length -eq 3) 'F03_LENGTH'
            AssertSelfTest (
                (Sha256 $nonempty403) -ceq
                'BA7816BF8F01CFEA414140DE5DAE2223B00361A396177A9CB410FF61F20015AD') 'F03_SHA'
        } finally {
            $response.Dispose()
        }
        $results.Add('F03_HTTP403_NONEMPTY_BODY=PASS')

        foreach ($label in @(
                'PDF_LINKS',
                'TITLE',
                'AUTHORS',
                'DOI',
                'CROSSREF_ITEMS',
                'ARXIV_MATCHES')) {
            $zero = @($null | Where-Object { $_ })
            $one = @('x')
            $many = @('x', 'y')
            AssertSelfTest (
                $zero.Count -eq 0 -and
                $one.Count -eq 1 -and
                $many.Count -eq 2) "F04_LABEL_$label"
        }
        $results.Add('F04_ARRAY_SHAPE_0_1_MANY=PASS')

        $journalText = [IO.File]::ReadAllText($v1JournalPath)
        AssertSelfTest ((FileSha $v1JournalPath) -ceq $expectedV1Journal) 'F05_SHA'
        AssertSelfTest (
            $journalText.Contains(
                'PREREG_SHA256=E9F7AD9237BE24EB7CB4CF8EE80F58E1B1D38D6834D83FB442A5A909BD47B3B6',
                [StringComparison]::Ordinal)) 'F05_PREREG'
        AssertSelfTest (
            $journalText.Contains(
                'AUDITED_RUNNER_SHA256=1CBA6274580D5DF7CD88F24A5C42C50904DC8593192F644F353B49E27391BC2A',
                [StringComparison]::Ordinal)) 'F05_RUNNER'
        AssertSelfTest (
            ([regex]::Matches($journalText, 'REQUEST_RESERVED\|ordinal=1\|')).Count -eq 1) 'F05_O1'
        AssertSelfTest (
            -not [regex]::IsMatch($journalText, 'REQUEST_RESERVED\|ordinal=[2-6]\|')) 'F05_NO_O2_O6'
        $results.Add('F05_PRIOR_JOURNAL_BINDING=PASS')

        $state = [pscustomobject]@{ Consumed = 1 }
        foreach ($ordinal in 2..6) {
            $state.Consumed = GetNextCumulativeRequestCount (
                $state.Consumed) $ordinal
        }
        AssertSelfTest ($state.Consumed -eq 6) 'F06_FINAL_COUNT'
        foreach ($badCase in @(
                [pscustomobject]@{
                    Current = 1
                    Ordinal = 1
                    Label = 'DUPLICATE'
                },
                [pscustomobject]@{
                    Current = 1
                    Ordinal = 3
                    Label = 'OUT_OF_ORDER'
                },
                [pscustomobject]@{
                    Current = 6
                    Ordinal = 7
                    Label = 'SEVENTH'
                })) {
            $blockedCase = $false
            try {
                [void](GetNextCumulativeRequestCount (
                        $badCase.Current) $badCase.Ordinal)
            } catch {
                $blockedCase = $true
            }
            AssertSelfTest $blockedCase "F06_$($badCase.Label)"
        }
        $skipState = [pscustomobject]@{ Consumed = 1; Slots = 1 }
        $skipState.Slots++
        AssertSelfTest ($skipState.Consumed -eq 1) 'F06_SKIP_NO_REQUEST'
        $results.Add('F06_CUMULATIVE_CAP=PASS')

        $collisionDir = Join-Path $selfTestDir 'collision'
        [IO.Directory]::CreateDirectory($collisionDir) | Out-Null
        $collisionPath = Join-Path $collisionDir 'exists'
        [IO.File]::WriteAllBytes($collisionPath, [byte[]](1))
        $collisionObserved = $false
        try {
            AssertAbsentTargets @($collisionPath)
        } catch {
            $collisionObserved =
                $_.Exception.Message.StartsWith(
                    'PREFLIGHT_TARGET_EXISTS:',
                    [StringComparison]::Ordinal)
        }
        AssertSelfTest $collisionObserved 'F07_COLLISION_NOT_BLOCKED'
        AssertSelfTest (
            -not (Test-Path -LiteralPath $journalPath)) 'F07_REAL_JOURNAL_CREATED'
        $results.Add('F07_FRESH_TARGET_COLLISION=PASS')

        $transactionDir = Join-Path $selfTestDir 'transaction'
        [IO.Directory]::CreateDirectory($transactionDir) | Out-Null
        $order = [Collections.Generic.List[string]]::new()
        $testJournal = Join-Path $transactionDir 'journal'
        $testWorkDir = Join-Path $transactionDir 'work'
        $testSourceTemp = Join-Path $transactionDir 'source.tmp'
        $testSource = Join-Path $transactionDir 'source'
        $testReceiptTemp = Join-Path $transactionDir 'receipt.tmp'
        $testReceipt = Join-Path $transactionDir 'receipt'
        $journalFs = OpenJournalThenTempDirectory $testJournal $testWorkDir
        try {
            $journalFs.WriteByte(1)
            $journalFs.Flush($true)
        } finally {
            $journalFs.Dispose()
        }
        $order.Add('JOURNAL_FIRST')
        AssertSelfTest (
            (Test-Path $testJournal) -and
            (Test-Path $testWorkDir)) 'F08_SHARED_OPEN'
        [IO.File]::WriteAllBytes(
            (Join-Path $testWorkDir 'classifier.tmp'),
            [byte[]](8))
        [IO.File]::WriteAllBytes($testSourceTemp, [byte[]](2))
        RemoveScopedDirectory $testWorkDir $transactionDir
        AssertSelfTest (-not (Test-Path $testWorkDir)) 'F08_SUCCESS_TEMP_CLEANUP'
        [IO.File]::Move($testSourceTemp, $testSource, $false)
        $order.Add('SOURCE_FIRST')
        [IO.File]::WriteAllBytes($testReceiptTemp, [byte[]](3))
        [IO.File]::Move($testReceiptTemp, $testReceipt, $false)
        $order.Add('RECEIPT_LAST')
        AssertSelfTest (
            ($order -join ',') -ceq
            'JOURNAL_FIRST,SOURCE_FIRST,RECEIPT_LAST') 'F08_ORDER'
        AssertSelfTest (
            (Test-Path $testJournal) -and
            (Test-Path $testSource) -and
            (Test-Path $testReceipt)) 'F08_COMMIT_FILES'
        $failureDir = Join-Path $selfTestDir 'failure'
        [IO.Directory]::CreateDirectory($failureDir) | Out-Null
        $failureJournal = Join-Path $failureDir 'journal'
        $failureWorkDir = Join-Path $failureDir 'work'
        $failureFs = OpenJournalThenTempDirectory (
            $failureJournal) $failureWorkDir
        try {
            $failureFs.WriteByte(4)
            $failureFs.Flush($true)
        } finally {
            $failureFs.Dispose()
        }
        [IO.File]::WriteAllBytes(
            (Join-Path $failureWorkDir 'orphan.tmp'),
            [byte[]](5))
        RemoveScopedDirectory $failureWorkDir $failureDir
        AssertSelfTest (
            (Test-Path $failureJournal) -and
            -not (Test-Path $failureWorkDir) -and
            -not (Test-Path $receiptPath)) 'F08_FAILURE_PRESERVATION'
        AssertSelfTest (
            (FileSha $v1JournalPath) -ceq $v1JournalBefore -and
            (FileSha $v1ResultPath) -ceq $v1ResultBefore) 'F08_V1_PRESERVED'
        $results.Add('F08_TRANSACTION_SUCCESS_FAILURE=PASS')

        $blocked = $false
        try {
            InvokeNetworkSend $null $null ([Threading.CancellationToken]::None)
        } catch {
            $blocked = $_.Exception.Message -ceq 'NETWORK_DISABLED_SELFTEST'
        }
        AssertSelfTest $blocked 'F09_DISPATCH_NOT_BLOCKED'
        AssertSelfTest ($script:networkRequests -eq 0) 'F09_NETWORK_COUNT'
        $results.Add('F09_NETWORK_DISABLE_GUARD=PASS')
    } finally {
        if ((BootstrapFileSha $v1JournalPath) -cne $v1JournalBefore -or
            (BootstrapFileSha $v1ResultPath) -cne $v1ResultBefore) {
            throw 'SELFTEST_V1_FORENSIC_DRIFT'
        }
        $resolvedBase = [IO.Path]::GetFullPath($base)
        $resolvedSelfTest = [IO.Path]::GetFullPath($selfTestDir)
        if (-not $resolvedSelfTest.StartsWith(
                $resolvedBase + [IO.Path]::DirectorySeparatorChar,
                [StringComparison]::OrdinalIgnoreCase)) {
            throw 'SELFTEST_CLEANUP_SCOPE_FAILURE'
        }
        if (Test-Path -LiteralPath $selfTestDir) {
            Remove-Item -LiteralPath $selfTestDir -Recurse -Force
        }
    }
    foreach ($result in $results) { Write-Output $result }
    Write-Output "SELFTEST_SUMMARY=$($results.Count)/9 PASS"
    Write-Output "NETWORK_REQUESTS=$($script:networkRequests)"
    Write-Output 'SOURCE_OPERATIONS=0'
    Write-Output 'PYTHON_PROCESSES=0'
}

function AssertAcquisitionAuthorization {
    if ((FileSha $eventLedgerPath) -cne $AuthorizationLedgerSha256) {
        throw 'AUTHORIZATION_LEDGER_HASH_DRIFT'
    }
    $marker =
        "SOURCE_ACQUISITION_AUTHORIZED: true_Q1R7_V2_EXACT_RUNNER_$ExpectedRunnerSha256"
    $ledgerText = [IO.File]::ReadAllText($eventLedgerPath)
    if (-not $ledgerText.Contains($marker, [StringComparison]::Ordinal)) {
        throw 'SOURCE_ACQUISITION_NOT_AUTHORIZED'
    }
}

function InvokeAcquisition {
    AssertAcquisitionAuthorization
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
    $script:journalFs = OpenJournalThenTempDirectory $journalPath $tempDir
    try {
        WriteJournal 'JOURNAL_VERSION=Q1R7_V2'
        WriteJournal "PREREG_SHA256=$expectedPrereg"
        WriteJournal "AUDITED_RUNNER_SHA256=$ExpectedRunnerSha256"
        WriteJournal "V1_PREREG_SHA256=$expectedV1Prereg"
        WriteJournal "V1_RUNNER_SHA256=$expectedV1Runner"
        WriteJournal "V1_JOURNAL_SHA256=$expectedV1Journal"
        WriteJournal "V1_RESULT_SHA256=$expectedV1Result"
        WriteJournal 'STARTING_CUMULATIVE_SOURCE_OPERATIONS=1'
        WriteJournal 'STARTING_CONSECUTIVE_TECHNICAL_FAILURES=1'
        WriteJournal ('PROCESS_START_UTC=' + [DateTime]::UtcNow.ToString('o'))

        $accepted = $false
        $acceptedBytes = $null
        $acceptedType = 'NONE'
        $classifier = [pscustomobject]@{
            Pass = $false
            Detail = 'NO_CANDIDATE_SOURCE'
        }
        $boundAuthors = @()
        $boundDois = @()
        $arxivId = $null
        $identityPass = $false

        $o2 = InvokeV2Request 2 'O2_CROSSREF' (
            'https://api.crossref.org/works?query=S0550321316000535&rows=3&select=DOI%2Ctitle%2Cauthor%2CURL')
        $eligible = @()
        if ($o2.Status -ge 200 -and
            $o2.Status -lt 300 -and
            ($o2.ContentEncoding -eq 'MISSING' -or
                $o2.ContentEncoding -eq 'identity')) {
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
                            (($_.given, $_.family |
                                    Where-Object { $_ }) -join ' ').Trim()
                        } | Where-Object { $_ })
                    $recordDoi = NormalizeDoi ([string]$item.DOI)
                    $urlDoi = NormalizeDoi ([string]$item.URL)
                    if ((Norm $recordTitle) -ceq (Norm $title) -and
                        $recordAuthors.Count -gt 0 -and
                        $recordDoi -and
                        $urlDoi -and
                        $recordDoi -ceq $urlDoi) {
                        $eligible += [pscustomobject]@{
                            Title = $recordTitle
                            Authors = @($recordAuthors)
                            DOI = $recordDoi
                            URL = [string]$item.URL
                        }
                    }
                }
            } catch {
                $eligible = @()
            }
        }
        $eligible = @($eligible)
        if ($eligible.Count -eq 1) {
            $boundAuthors = @($eligible[0].Authors)
            $boundDois = @($eligible[0].DOI)
            $o2.Metadata.Title = @($eligible[0].Title)
            $o2.Metadata.Authors = @($boundAuthors)
            $o2.Metadata.DOI = @($boundDois)
        } else {
            $classifier = [pscustomobject]@{
                Pass = $false
                Detail = "O2_ELIGIBLE_COUNT_$($eligible.Count)"
            }
            RetireV2Range 3 'SKIPPED_PRECONDITION'
        }

        if ($eligible.Count -eq 1) {
            $o3 = InvokeV2Request 3 'O3_ARXIV_EXACT_TITLE_QUERY' (
                'https://export.arxiv.org/api/query?search_query=ti%3A%22Hydrodynamics%20of%20ultra-relativistic%20bubble%20walls%22&start=0&max_results=3&sortBy=relevance&sortOrder=descending')
            $matches = @()
            if ($o3.Status -ge 200 -and
                $o3.Status -lt 300 -and
                ($o3.ContentEncoding -eq 'MISSING' -or
                    $o3.ContentEncoding -eq 'identity')) {
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
                        $doiNode = $entry.SelectSingleNode(
                            './*[local-name()="doi"]')
                        $doiPresent = $null -ne $doiNode
                        $entryDoi = if ($doiNode) {
                            NormalizeDoi $doiNode.InnerText
                        } else {
                            $null
                        }
                        $doiCompatible = if ($doiPresent) {
                            $entryDoi -and
                                $entryDoi -ceq $boundDois[0]
                        } else {
                            $true
                        }
                        if ((Norm $entryTitle) -ceq (Norm $title) -and
                            (SameSet $entryAuthors $boundAuthors) -and
                            $doiCompatible) {
                            $matches += [pscustomobject]@{
                                Title = $entryTitle
                                Authors = @($entryAuthors)
                                IdUri = $entryId
                                DOI = $entryDoi
                            }
                        }
                    }
                } catch {
                    $matches = @()
                }
            }
            $matches = @($matches)
            if ($matches.Count -eq 1) {
                $match = $matches[0]
                $candidateArxivId = $null
                try {
                    $candidateArxivId =
                        ([Uri]$match.IdUri).Segments[-1].TrimEnd('/')
                } catch {}
                if ($candidateArxivId -and
                    $candidateArxivId -match
                    '^(?:[0-9]{4}\.[0-9]{4,5}(?:v[0-9]+)?|[A-Za-z.-]+/[0-9]{7}(?:v[0-9]+)?)$') {
                    $arxivId = $candidateArxivId
                    $o3.Metadata.Title = @($match.Title)
                    $o3.Metadata.Authors = @($match.Authors)
                    $o3.Metadata.DOI = @($match.DOI | Where-Object { $_ })
                    $o3.Metadata.ArxivID = @($arxivId)
                } else {
                    $classifier = [pscustomobject]@{
                        Pass = $false
                        Detail = 'O3_CANONICAL_ID_SYNTAX_FAIL'
                    }
                    RetireV2Range 4 'SKIPPED_PRECONDITION'
                }
            } else {
                $classifier = [pscustomobject]@{
                    Pass = $false
                    Detail = "O3_ELIGIBLE_COUNT_$($matches.Count)"
                }
                RetireV2Range 4 'SKIPPED_PRECONDITION'
            }
        }

        if ($arxivId) {
            $o4 = InvokeV2Request 4 'O4_ARXIV_ABSTRACT' (
                'https://arxiv.org/abs/' + $arxivId)
            $o4Metadata = GetHtmlMeta $o4.Body
            $o4.Metadata = $o4Metadata
            $o4Titles = @($o4Metadata.Title | Where-Object {
                    (Norm $_) -ceq (Norm $title)
                })
            $o4RawDois = @($o4Metadata.DOI |
                Where-Object { -not [string]::IsNullOrWhiteSpace([string]$_) })
            $o4NormalizedDois = @($o4RawDois |
                ForEach-Object { NormalizeDoi $_ } |
                Where-Object { $_ })
            $o4DistinctDois = @($o4NormalizedDois | Sort-Object -Unique)
            $o4DoiPass = if ($o4RawDois.Count -eq 0) {
                $true
            } else {
                $o4NormalizedDois.Count -eq $o4RawDois.Count -and
                    $o4DistinctDois.Count -eq 1 -and
                    $o4DistinctDois[0] -ceq $boundDois[0]
            }
            $o4Ok =
                $o4.Status -ge 200 -and
                $o4.Status -lt 300 -and
                ($o4.ContentEncoding -eq 'MISSING' -or
                    $o4.ContentEncoding -eq 'identity') -and
                $o4Titles.Count -eq 1 -and
                (SameSet $o4Metadata.Authors $boundAuthors) -and
                $o4DoiPass -and
                [Text.Encoding]::UTF8.GetString($o4.Body).Contains(
                    $arxivId,
                    [StringComparison]::Ordinal)
            if (-not $o4Ok) {
                $classifier = [pscustomobject]@{
                    Pass = $false
                    Detail = 'O4_IDENTITY_BINDING_FAIL'
                }
                RetireV2Range 5 'SKIPPED_PRECONDITION'
            } else {
                $identityPass = $true
            }
        }

        $provisional = $false
        if ($identityPass) {
            $o5 = InvokeV2Request 5 'O5_ARXIV_EPRINT' (
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
                    $provisional = $true
                    $acceptedBytes = $o5.Body
                    $acceptedType = if ($classifier.Detail -eq 'PDF_COMPLETE') {
                        'CANONICAL_FULL_ARTICLE_PDF'
                    } else {
                        'SOURCE_ARCHIVE'
                    }
                }
            }
            if (-not $provisional) {
                RetireV2Range 6 'SKIPPED_PRECONDITION'
            }
        }

        if ($provisional) {
            $o6 = InvokeV2Request 6 'O6_DOI_PII_BINDING' (
                DoiUrl $boundDois[0])
            $finalUri = [Uri]$o6.FinalURL
            $finalHost = $finalUri.DnsSafeHost.ToLowerInvariant()
            $pathSegments = @($finalUri.AbsolutePath.Split(
                    [char[]]@('/'),
                    [StringSplitOptions]::RemoveEmptyEntries))
            $exactPiiPairs = @()
            for ($segmentIndex = 0;
                $segmentIndex -lt ($pathSegments.Count - 1);
                $segmentIndex++) {
                if ($pathSegments[$segmentIndex] -ceq 'pii' -and
                    $pathSegments[$segmentIndex + 1] -ceq $pii) {
                    $exactPiiPairs += $segmentIndex
                }
            }
            $o6StatusPass =
                ($o6.Status -ge 200 -and $o6.Status -lt 300) -or
                ($o6.Status -ge 400 -and $o6.Status -lt 500)
            $o6Binding =
                $o6StatusPass -and
                ($o6.ContentEncoding -eq 'MISSING' -or
                    $o6.ContentEncoding -eq 'identity') -and
                ($finalHost -eq 'sciencedirect.com' -or
                    $finalHost.EndsWith('.sciencedirect.com')) -and
                $exactPiiPairs.Count -eq 1
            if ($o6Binding) {
                $accepted = $true
            } else {
                $classifier = [pscustomobject]@{
                    Pass = $false
                    Detail = 'O6_DOI_PII_REDIRECT_BINDING_FAIL'
                }
                $acceptedBytes = $null
                $acceptedType = 'NONE'
            }
        }

        for ($ordinal = 1; $ordinal -le 6; $ordinal++) {
            if (-not $script:slots.Contains([string]$ordinal)) {
                throw "UNACCOUNTED_SLOT:$ordinal"
            }
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

        RemoveScopedDirectory $tempDir $base
        AssertGlobalDeadline
        WriteJournal (
            'TERMINAL_SLOT_STATE=' +
            (($script:slots.GetEnumerator() |
                    Sort-Object { [int]$_.Key } |
                    ForEach-Object { "$($_.Key)=$($_.Value)" }) -join ';'))
        WriteJournal "FINAL_CUMULATIVE_REQUEST_COUNT=$($script:requestCount)/6_TERMINAL"
        WriteJournal ('READY_TO_COMMIT|utc=' + [DateTime]::UtcNow.ToString('o'))
        $script:journalFs.Dispose()
        $script:journalFs = $null
        $journalSha = FileSha $journalPath

        if ($accepted) {
            [IO.File]::Move($blobTemp, $blobPath, $false)
            if ((FileSha $blobPath) -cne $sourceSha) {
                throw 'FINAL_BLOB_HASH_MISMATCH'
            }
        }
        $operationViews = @($script:ops |
            ForEach-Object { PublicOpView $_ })
        $crossBinding = @()
        if ($accepted) {
            $crossBinding = @(
                [pscustomobject]@{
                    IdentifierType = 'PII'
                    Identifier = $pii
                    SourceSHA256 = $sourceSha
                    EvidenceOperations = @(2, 3, 4, 5, 6)
                },
                [pscustomobject]@{
                    IdentifierType = 'DOI'
                    Identifier = $boundDois[0]
                    SourceSHA256 = $sourceSha
                    EvidenceOperations = @(2, 3, 4, 5, 6)
                },
                [pscustomobject]@{
                    IdentifierType = 'ARXIV'
                    Identifier = $arxivId
                    SourceSHA256 = $sourceSha
                    EvidenceOperations = @(3, 4, 5)
                })
        }
        $receipt = [ordered]@{
            TASK_ID =
                'A1_K1_A2_K4_P5_3_B6B2_10_C01_RW1_Q1R7_V2_SOURCE_ACQUISITION'
            THEORY_AUTHOR = 'Martin Jambor'
            PROCESS_AND_ACQUISITION_IMPLEMENTER = 'Codex'
            ROUTE =
                'A1_K1_A2_K4/P5.3/B6b-2.10/H_RDIV-MF1-v1/C01-RW1/Q1R7'
            PREREG_SHA256 = $expectedPrereg
            AUDITED_RUNNER_SHA256 = $ExpectedRunnerSha256
            V1_PREREG_SHA256 = $expectedV1Prereg
            V1_RUNNER_SHA256 = $expectedV1Runner
            V1_JOURNAL_SHA256 = $expectedV1Journal
            V1_RESULT_SHA256 = $expectedV1Result
            STARTING_CUMULATIVE_SOURCE_OPERATIONS = 1
            FINAL_CUMULATIVE_SOURCE_OPERATIONS = $script:requestCount
            HISTORICAL_PACKAGES_TOTAL_AFTER = 2
            CONSECUTIVE_TECHNICAL_FAILURES_AFTER =
                '0/10_IF_MAIN_ACCEPTS_INTERPRETABLE_CLEAN_COVERAGE_RESULT'
            RUN_AUTHORIZED = $false
            PYTHON_PROCESSES = 0
            USER_AGENT = 'Teoria-Q1R7-CompleteSource/1.0'
            TOOL_VERSIONS = $toolVersions
            SLOT_LEDGER = $script:slots
            OPERATIONS = $operationViews
            FROZEN_TITLE = $title
            BOUND_AUTHORS = @($boundAuthors)
            BOUND_DOIS = @($boundDois)
            BOUND_PII = $pii
            BOUND_ARXIV_ID = if ($arxivId) { $arxivId } else { 'MISSING' }
            SOURCE_UNIVERSE_COMPLETE =
                if ($accepted) { 'PASS' } else { 'FAIL_NOT_CERTIFIED' }
            ACCEPTED_SOURCE_TYPE = $acceptedType
            ACCEPTED_SOURCE_SHA256 = $sourceSha
            CLASSIFIER = $classifier
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

        Write-Output (
            "Q1R7_CUMULATIVE_SOURCE_OPERATION_COUNT=$($script:requestCount)/6_TERMINAL")
        Write-Output (
            'SOURCE_UNIVERSE_COMPLETE=' + $receipt.SOURCE_UNIVERSE_COMPLETE)
        Write-Output "ACCEPTED_SOURCE_TYPE=$acceptedType"
        Write-Output "ACCEPTED_SOURCE_SHA256=$sourceSha"
        Write-Output "JOURNAL_SHA256=$journalSha"
        Write-Output ('RECEIPT_SHA256=' + (FileSha $receiptPath))
    } catch {
        if ($null -ne $script:journalFs) {
            try {
                WriteJournal (
                    'PROCESS_ABORTED_TECHNICAL|utc=' +
                    [DateTime]::UtcNow.ToString('o') +
                    '|error=' +
                    $_.Exception.Message.Replace(
                        [char]13,
                        ' ').Replace(
                        [char]10,
                        ' '))
            } catch {}
            $script:journalFs.Dispose()
            $script:journalFs = $null
        }
        RemoveScopedDirectory $tempDir $base
        RemoveScopedFile $blobTemp $base
        RemoveScopedFile $receiptTemp $base
        throw
    } finally {
        if ($null -ne $script:journalFs) {
            $script:journalFs.Dispose()
            $script:journalFs = $null
        }
    }
}

try {
    if ($SelfTest) {
        InvokeLocalSelfTest
    } elseif ($Acquire) {
        InvokeAcquisition
    } else {
        throw 'MODE_NOT_SELECTED'
    }
} finally {
    $globalCts.Dispose()
}
