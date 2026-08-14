param(
    [Parameter(Mandatory = $true)]
    [string]$PackagePath,
    [string]$ResponseRoot,
    [string]$AuditSubmissionId
)

if ($PSVersionTable.PSVersion.Major -lt 7) {
    Write-Error 'Test-ExternalAuditPackage.ps1 R6 requires PowerShell 7+; run it with pwsh.'
    exit 2
}

$ErrorActionPreference = 'Stop'
$package = (Resolve-Path -LiteralPath $PackagePath).Path
$packageId = Split-Path -Leaf $package
$packagesRoot = Split-Path -Parent $package
$externalAuditsRoot = Split-Path -Parent $packagesRoot
$repositoryRoot = Split-Path -Parent $externalAuditsRoot
if (-not $ResponseRoot) {
    $ResponseRoot = Join-Path $externalAuditsRoot 'RESPONSES'
}

$checks = [System.Collections.Generic.List[object]]::new()
function Add-Check {
    param([string]$Name, [bool]$Passed, [string]$Detail)
    $checks.Add([pscustomobject]@{ Check = $Name; Passed = $Passed; Detail = $Detail })
}

function Get-Sha256 {
    param([string]$Path)
    return (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash.ToUpperInvariant()
}

$required = @(
    '00_SCOPE_AND_READ_ORDER.md',
    '01_MANIFEST_SHA256.md',
    '01_MANIFEST_SHA256.tsv',
    '02_AUDITOR_INSTRUCTIONS.md',
    '03_REPRODUCTION_AND_EXPECTATIONS.md',
    '04_RUNTIME_DEPENDENCY_MAP.tsv',
    '05_PACKAGE_HISTORY.md'
)
foreach ($relative in $required) {
    $path = Join-Path $package $relative
    Add-Check "required:$relative" (Test-Path -LiteralPath $path -PathType Leaf) $path
}

$manifestPath = Join-Path $package '01_MANIFEST_SHA256.tsv'
if (Test-Path -LiteralPath $manifestPath -PathType Leaf) {
    $rows = @(Import-Csv -LiteralPath $manifestPath -Delimiter "`t")
    Add-Check 'manifest:nonempty' ($rows.Count -gt 0) "rows=$($rows.Count)"
    foreach ($row in $rows) {
        $copy = Join-Path $package $row.copy_path
        $copyExists = Test-Path -LiteralPath $copy -PathType Leaf
        Add-Check "manifest-copy-exists:$($row.copy_path)" $copyExists $copy
        if ($copyExists) {
            $copyHash = Get-Sha256 $copy
            Add-Check "manifest-copy-hash:$($row.copy_path)" ($copyHash -ceq $row.copy_sha256.ToUpperInvariant()) "observed=$copyHash expected=$($row.copy_sha256)"
        }
        if ($row.source_path -and $row.source_path -ne 'PACKAGE_GENERATED') {
            $source = Join-Path $repositoryRoot $row.source_path
            $sourceExists = Test-Path -LiteralPath $source -PathType Leaf
            Add-Check "manifest-source-exists:$($row.source_path)" $sourceExists $source
            if ($sourceExists) {
                $sourceHash = Get-Sha256 $source
                Add-Check "manifest-source-hash:$($row.source_path)" ($sourceHash -ceq $row.source_sha256.ToUpperInvariant()) "observed=$sourceHash expected=$($row.source_sha256)"
                if ($copyExists) {
                    Add-Check "manifest-source-copy-parity:$($row.copy_path)" ($sourceHash -ceq (Get-Sha256 $copy)) "source=$sourceHash copy=$(Get-Sha256 $copy)"
                }
            }
        }
    }
}

$runtimeMapPath = Join-Path $package '04_RUNTIME_DEPENDENCY_MAP.tsv'
if (Test-Path -LiteralPath $runtimeMapPath -PathType Leaf) {
    $runtimeRows = @(Import-Csv -LiteralPath $runtimeMapPath -Delimiter "`t")
    $reproRoot = Join-Path $package 'REPRO'
    $reproFiles = @()
    if (Test-Path -LiteralPath $reproRoot -PathType Container) {
        $reproFiles = @(Get-ChildItem -LiteralPath $reproRoot -Recurse -Force -File)
    }
    $runtimeMapCardinalityValid =
        ($runtimeRows.Count -gt 0) -or ($reproFiles.Count -eq 0)
    Add-Check 'runtime-map:declared-or-empty-no-repro' $runtimeMapCardinalityValid "rows=$($runtimeRows.Count) repro_files=$($reproFiles.Count)"
    $runtimePathSet = [System.Collections.Generic.HashSet[string]]::new(
        [System.StringComparer]::OrdinalIgnoreCase
    )
    foreach ($row in $runtimeRows) {
        [void]$runtimePathSet.Add(($row.runtime_path -replace '\\', '/'))
        $runtimeFile = Join-Path $package $row.runtime_path
        $exists = Test-Path -LiteralPath $runtimeFile -PathType Leaf
        Add-Check "runtime-exists:$($row.runtime_path)" $exists "role=$($row.role) required_by=$($row.required_by)"
        if ($exists) {
            $hash = Get-Sha256 $runtimeFile
            Add-Check "runtime-hash:$($row.runtime_path)" ($hash -ceq $row.sha256.ToUpperInvariant()) "observed=$hash expected=$($row.sha256)"
        }
    }

    foreach ($file in $reproFiles) {
        $relative = [System.IO.Path]::GetRelativePath($package, $file.FullName) -replace '\\', '/'
        Add-Check "runtime-map-covers:$relative" ($runtimePathSet.Contains($relative)) $relative
    }
    Add-Check 'runtime-map:exact-repro-file-count' ($runtimePathSet.Count -eq $reproFiles.Count) "map=$($runtimePathSet.Count) repro_files=$($reproFiles.Count)"

    $localPathPattern = '(?<path>(?:scripts|tracks)/[^"''\r\n]+\.(?:py|md|json|csv|txt))'
    foreach ($row in $runtimeRows | Where-Object { $_.runtime_path -match '\.py$' }) {
        $runtimeFile = Join-Path $package $row.runtime_path
        if (-not (Test-Path -LiteralPath $runtimeFile -PathType Leaf)) {
            continue
        }
        $content = Get-Content -LiteralPath $runtimeFile -Raw
        $declaredLocalPaths = @(
            [regex]::Matches($content, $localPathPattern) |
                ForEach-Object { $_.Groups['path'].Value } |
                Sort-Object -Unique
        )
        foreach ($localPath in $declaredLocalPaths) {
            $expectedRuntimePath = "REPRO/$localPath"
            Add-Check "runtime-hardcoded-dependency:$expectedRuntimePath" ($runtimePathSet.Contains($expectedRuntimePath)) "declared_by=$($row.runtime_path)"
        }
    }
}

$scopePath = Join-Path $package '00_SCOPE_AND_READ_ORDER.md'
if (Test-Path -LiteralPath $scopePath -PathType Leaf) {
    $scope = Get-Content -LiteralPath $scopePath -Raw
    foreach ($marker in @('## Presná otázka', '## Nonclaims', 'Target tier', 'Autorita')) {
        Add-Check "scope-marker:$marker" $scope.Contains($marker) $marker
    }
}

$instructionsPath = Join-Path $package '02_AUDITOR_INSTRUCTIONS.md'
if (Test-Path -LiteralPath $instructionsPath -PathType Leaf) {
    $instructions = Get-Content -LiteralPath $instructionsPath -Raw
    foreach ($marker in @('exit code', 'wall time', 'generated JSON', 'odchýl')) {
        Add-Check "instructions-marker:$marker" $instructions.Contains($marker) $marker
    }
}

$responsePackageRoot = Join-Path $ResponseRoot $packageId
if ($AuditSubmissionId) {
    $response = Join-Path (Join-Path $responsePackageRoot $AuditSubmissionId) '00_AUDITOR_AUDIT.md'
} else {
    $response = Join-Path $responsePackageRoot '00_AUDITOR_AUDIT.md'
}
Add-Check 'response-template:exists' (Test-Path -LiteralPath $response -PathType Leaf) $response

$tempFiles = @(Get-ChildItem -LiteralPath $package -Recurse -Force -File | Where-Object { $_.Name -match '\.tmp-|\.partial$' })
Add-Check 'hygiene:no-temp-files' ($tempFiles.Count -eq 0) (($tempFiles.FullName) -join '; ')

$pendingHashMatches = @(Get-ChildItem -LiteralPath $package -Recurse -Force -File | Select-String -Pattern 'PENDING_HASH|TODO_HASH')
Add-Check 'manifest:no-pending-hash-markers' ($pendingHashMatches.Count -eq 0) "matches=$($pendingHashMatches.Count)"

$failed = @($checks | Where-Object { -not $_.Passed })
$checks | Format-Table -AutoSize
[pscustomobject]@{
    package_id = $packageId
    checks = $checks.Count
    failed = $failed.Count
    passed = ($failed.Count -eq 0)
} | ConvertTo-Json -Compress

if ($failed.Count -gt 0) {
    exit 1
}
exit 0
