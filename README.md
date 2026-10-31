# karelima.com.tr

Karelima Bilişim kurumsal çağrı merkezi sitesi. Statik site, Windows IIS üzerinde yayında.
**karelima.com (Digitürk satış sitesi) bu depoyla ilgili değildir; ona dokunulmaz.**

## Nasıl çalışır?

1. `src/` içindeki kaynak (Python + Jinja2) `main` dalına gönderilir.
2. GitHub Actions (`.github/workflows/build.yml`) siteyi derler, görselleri ve fontları
   `karelima-com-tr-site.zip` içinden ekler ve hazır siteyi `site` dalına yazar.
3. Sunucudaki zamanlanmış görev ("karelima-com-tr guncelleme", SYSTEM, 10 dakikada bir)
   `site` dalında yeni commit görürse indirir, doğrular, yedekler ve sadece
   `C:\inetpub\karelima-com-tr\wwwroot` klasörünü günceller.

Sunucu konsoluna girmeye gerek yoktur. Güncelleme = `main` dalına commit.

## Yerel derleme

```
pip install jinja2
python src/build.py      # çıktı: dist/
```

## Sunucu

- IIS sitesi: `karelima-com-tr` (sadece karelima.com.tr ve www.karelima.com.tr bağlamaları, 80 + 443)
- SSL: win-acme (Let's Encrypt), otomatik yenileme
- Yönlendirme: tüm adresler `https://www.karelima.com.tr` adresine 301 ile gider (web.config)
- Güncelleyici günlüğü: `C:\inetpub\karelima-com-tr\deploy\update.log`
- Yedekler (son 10): `C:\inetpub\karelima-com-tr\deploy\backups\`
- Geri dönüş: yedek zip'i `wwwroot` içine açın veya `main`'de önceki commit'i geri alın.
- Güncelleyiciyi ilk kurulum: `deploy/install-updater.ps1` (yönetici PowerShell, bir kez).

## Görseller

Fotoğraflar ve fontlar şimdilik `karelima-com-tr-site.zip` içinde (`assets/img`, `assets/fonts`).
Yeni fotoğraf eklerken bu zip güncellenmeli ya da `src/static/assets/img/` altına eklenmeli.
