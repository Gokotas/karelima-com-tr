# Bir kez, yonetici PowerShell'de calistirilir. Otomatik guncelleyiciyi kurar.
# Sadece C:\inetpub\karelima-com-tr\deploy klasorunu ve bir zamanlanmis gorev ekler.
$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$D = 'C:\inetpub\karelima-com-tr\deploy'
New-Item -ItemType Directory -Force -Path $D | Out-Null
Invoke-WebRequest -UseBasicParsing -Uri 'https://raw.githubusercontent.com/Gokotas/karelima-com-tr/main/deploy/update.ps1' -OutFile (Join-Path $D 'update.ps1')

# deploy klasorunu sadece SYSTEM ve Administrators yazabilsin / okuyabilsin
icacls $D /inheritance:r /grant:r 'SYSTEM:(OI)(CI)F' 'Administrators:(OI)(CI)F' | Out-Null

$name = 'karelima-com-tr guncelleme'
$a = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument ('-NoProfile -ExecutionPolicy Bypass -File "' + (Join-Path $D 'update.ps1') + '"')
$t = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) -RepetitionInterval (New-TimeSpan -Minutes 10)
$p = New-ScheduledTaskPrincipal -UserId 'SYSTEM' -LogonType ServiceAccount -RunLevel Highest
$s = New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Minutes 15) -MultipleInstances IgnoreNew -StartWhenAvailable
Register-ScheduledTask -TaskName $name -Action $a -Trigger $t -Principal $p -Settings $s -Force | Out-Null
Get-ScheduledTask -TaskName $name | Select-Object TaskName, State
Write-Host 'Kuruldu. Gunluk: C:\inetpub\karelima-com-tr\deploy\update.log'
