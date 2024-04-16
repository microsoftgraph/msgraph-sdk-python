Push-Location -Path (Join-Path -Path $PSScriptRoot -ChildPath "..")
$versionFileContent = Get-Content -Path "msgraph/_version.py" -Raw
$version = $versionFileContent.Split("`r`n")[0] -replace "VERSION: str = '", '' -replace "'", ''
$versionParts = $version -split "\."
$versionParts[1] = [int]$versionParts[1] + 1
$versionParts[2] = 0
$newVersion = $versionParts -join "."
$versionFileContent -replace $version, $newVersion | Set-Content -Path "msgraph/_version.py" -NoNewline
$pyprojectFileContent = Get-Content -Path "pyproject.toml" -Raw
$pyprojectFileContent -replace $version, $newVersion | Set-Content -Path "pyproject.toml" -NoNewline
Pop-Location