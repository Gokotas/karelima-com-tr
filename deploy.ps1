# karelima.com.tr - IIS kurulum / guncelleme betigi
# Sadece karelima.com.tr ve www.karelima.com.tr host baglamali YENI bir site ekler.
# Mevcut siteler (Digiturk / karelima.com) DEGISTIRILMEZ. IIS yeniden baslatilmaz.
$ErrorActionPreference = 'Stop'
$SiteName = 'karelima-com-tr'
$Root     = 'C:\inetpub\karelima-com-tr'
$Web      = Join-Path $Root 'wwwroot'
$ZipUrl   = 'https://github.com/Gokotas/karelima-com-tr/raw/main/karelima-com-tr-site.zip'
$Hosts    = @('karelima.com.tr','www.karelima.com.tr')
$appcmd   = "$env:windir\system32\inetsrv\appcmd.exe"
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

Write-Host '--- 1) Mevcut siteler (degistirilmeyecek) ---'
& $appcmd list site

# Bu host'lar baska bir sitede bagli mi? Bagliysa dur.
foreach ($h in $Hosts) {
  $other = & $appcmd list site /text:name | Where-Object { $_ -ne $SiteName } | ForEach-Object {
    $n = $_; $b = & $appcmd list site "$n" /text:bindings; if ($b -match [regex]::Escape(":$h")) { $n } }
  if ($other) { throw "DUR: $h zaten '$other' sitesinde bagli. Hicbir sey degistirilmedi." }
}

Write-Host '--- 2) IIS yapilandirma yedegi ---'
$bk = 'pre-karelima-com-tr-' + (Get-Date -Format 'yyyyMMdd-HHmmss')
& $appcmd add backup $bk
Write-Host "Yedek: $bk  (geri donus: appcmd restore backup $bk)"

Write-Host '--- 3) Dosyalari indir ve ac ---'
New-Item -ItemType Directory -Force -Path $Root | Out-Null
$zip = Join-Path $env:TEMP 'karelima-com-tr-site.zip'
Invoke-WebRequest -UseBasicParsing -Uri $ZipUrl -OutFile $zip
if (Test-Path $Web) {
  $old = "$Web-eski-" + (Get-Date -Format 'yyyyMMdd-HHmmss')
  Rename-Item $Web $old
  Write-Host "Onceki surum: $old"
}
Expand-Archive -Path $zip -DestinationPath $Web -Force
Write-Host ("Dosya sayisi: " + (Get-ChildItem $Web -Recurse -File).Count)

Write-Host '--- 4) Uygulama havuzu ve site ---'
$pools = & $appcmd list apppool /text:name
if ($pools -notcontains $SiteName) {
  & $appcmd add apppool /name:$SiteName /managedRuntimeVersion:"" /managedPipelineMode:Integrated
}
$sites = & $appcmd list site /text:name
if ($sites -notcontains $SiteName) {
  $bind = ($Hosts | ForEach-Object { "http/*:80:$_" }) -join ','
  & $appcmd add site /name:$SiteName /physicalPath:$Web /bindings:$bind
  & $appcmd set app "$SiteName/" /applicationPool:$SiteName
} else {
  & $appcmd set vdir "$SiteName/" /physicalPath:$Web
}
icacls $Root /grant "IIS AppPool\${SiteName}:(OI)(CI)RX" /T /Q | Out-Null

Write-Host '--- 5) Test (sunucu icinden, Host basligi ile) ---'
foreach ($p in @('/','/hizmetler/','/sitemap.xml','/robots.txt','/olmayan-sayfa')) {
  try {
    $r = Invoke-WebRequest -UseBasicParsing -Uri ("http://127.0.0.1" + $p) -Headers @{Host='karelima.com.tr'}
    Write-Host ("{0,-16} {1}" -f $p, $r.StatusCode)
  } catch {
    $c = $_.Exception.Response.StatusCode.value__
    Write-Host ("{0,-16} {1}" -f $p, $c)
  }
}
Write-Host '--- Bitti. Diger sitelerin durumu: ---'
& $appcmd list site
