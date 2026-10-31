# karelima.com.tr otomatik guncelleyici (sunucuda SYSTEM olarak 10 dakikada bir calisir)
# - GitHub'daki "site" dalinin (GitHub Actions'in urettigi hazir site) son commit'ine bakar.
# - Degisiklik varsa indirir, dogrular, mevcut siteyi yedekler ve SADECE
#   C:\inetpub\karelima-com-tr\wwwroot klasorunu gunceller.
# - IIS ayarlarina, diger sitelere (karelima.com / Digiturk, Kablonet) dokunmaz. Indirdigi kodu calistirmaz.
$ErrorActionPreference = 'Stop'
$Root   = 'C:\inetpub\karelima-com-tr'
$Web    = Join-Path $Root 'wwwroot'
$D      = Join-Path $Root 'deploy'
$Log    = Join-Path $D 'update.log'
$Repo   = 'Gokotas/karelima-com-tr'
$Branch = 'site'
function L($m) { Add-Content -Path $Log -Value ((Get-Date -Format 'yyyy-MM-dd HH:mm:ss') + ' ' + $m) -Encoding UTF8 }

try {
  [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
  $h = @{ 'User-Agent' = 'karelima-updater'; 'Accept' = 'application/vnd.github+json' }
  $sha = (Invoke-RestMethod -UseBasicParsing -Uri "https://api.github.com/repos/$Repo/commits/$Branch" -Headers $h).sha
  if ($sha -notmatch '^[0-9a-f]{40}$') { throw 'gecersiz commit kimligi' }
  $shaFile = Join-Path $D 'last.sha'
  $last = ''
  if (Test-Path $shaFile) { $last = (Get-Content $shaFile -Raw).Trim() }
  if ($sha -eq $last) { exit 0 }

  $tmp = Join-Path $D 'tmp'
  if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force }
  New-Item -ItemType Directory -Path $tmp | Out-Null
  Invoke-WebRequest -UseBasicParsing -Uri "https://codeload.github.com/$Repo/zip/$sha" -OutFile (Join-Path $tmp 's.zip')
  Expand-Archive -Path (Join-Path $tmp 's.zip') -DestinationPath (Join-Path $tmp 'x') -Force
  $src = (Get-ChildItem (Join-Path $tmp 'x') -Directory | Select-Object -First 1).FullName

  # Dogrulama: temel dosyalar var mi, web.config gecerli XML mi, sadece statik dosya turleri mi
  foreach ($f in 'index.html', '404.html', 'web.config', 'sitemap.xml', 'assets\site.css', 'assets\fonts\pjs-latin.woff2') {
    if (-not (Test-Path (Join-Path $src $f))) { throw "eksik dosya: $f" }
  }
  $null = [xml](Get-Content (Join-Path $src 'web.config') -Raw)
  $ok = '.html', '.css', '.js', '.svg', '.webp', '.jpg', '.jpeg', '.png', '.gif', '.ico', '.woff2', '.woff', '.xml', '.txt', '.json', '.webmanifest', '.config', '.pdf'
  $bad = Get-ChildItem $src -Recurse -File | Where-Object { $ok -notcontains $_.Extension.ToLower() }
  if ($bad) { throw ('izin verilmeyen dosya: ' + (($bad | Select-Object -ExpandProperty Name) -join ', ')) }
  $n = (Get-ChildItem $src -Recurse -File).Count
  if ($n -lt 20) { throw "cok az dosya: $n" }

  # Yedek (son 10 surum saklanir)
  $bk = Join-Path $D 'backups'
  New-Item -ItemType Directory -Force -Path $bk | Out-Null
  Compress-Archive -Path (Join-Path $Web '*') -DestinationPath (Join-Path $bk ('wwwroot-' + (Get-Date -Format 'yyyyMMdd-HHmmss') + '.zip'))
  Get-ChildItem $bk -Filter *.zip | Sort-Object LastWriteTime -Descending | Select-Object -Skip 10 | Remove-Item -Force

  # Yayinla (SSL dogrulama klasoru .well-known korunur)
  robocopy $src $Web /MIR /XD .well-known /R:2 /W:2 /NFL /NDL /NJH /NJS /NP | Out-Null
  if ($LASTEXITCODE -ge 8) { throw "robocopy hata kodu $LASTEXITCODE" }

  Set-Content -Path $shaFile -Value $sha
  Remove-Item $tmp -Recurse -Force
  L "GUNCELLENDI $sha ($n dosya)"
} catch {
  L ('HATA ' + $_.Exception.Message)
  exit 1
}
