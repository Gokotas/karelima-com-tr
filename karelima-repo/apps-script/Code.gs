/**
 * karelima.com.tr teklif formu alıcısı (Google Apps Script web uygulaması)
 * - Talebi "Karelima.com.tr Teklif Talepleri" tablosuna yazar
 * - gokberk.tas@getberq.com adresine bildirim e-postası gönderir
 * Dağıtım: Web uygulaması · Yürüten: Ben · Erişim: Herkes
 */
var SHEET_ID = '1YN4WyhyW9g3_CmtigfrapfDLs66O1NC-nlr3wgOiwRM';
var SHEET_NAME = 'Talepler';
var NOTIFY_TO = 'gokberk.tas@getberq.com';
var FIELDS = ['firma', 'ad_soyad', 'telefon', 'eposta', 'hizmet', 'sektor', 'hacim', 'baslangic', 'mesaj',
              'sayfa', 'giris_sayfasi', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'gclid'];
var LABELS = { firma: 'Firma', ad_soyad: 'Ad soyad', telefon: 'Telefon', eposta: 'E-posta', hizmet: 'Hizmet',
  sektor: 'Sektör', hacim: 'Aylık hacim', baslangic: 'Başlangıç', mesaj: 'Mesaj', sayfa: 'Sayfa',
  giris_sayfasi: 'Gelen sayfa', utm_source: 'utm_source', utm_medium: 'utm_medium', utm_campaign: 'utm_campaign',
  utm_term: 'utm_term', gclid: 'gclid' };

function doGet() {
  return json_({ ok: true, service: 'karelima-teklif' });
}

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(10000);
  try {
    var d = {};
    try { d = JSON.parse((e && e.postData && e.postData.contents) || '{}'); } catch (err) { return json_({ ok: false, error: 'format' }); }
    if (d.web_sitesi) return json_({ ok: true });                       // bal küpü (bot)
    var req = ['firma', 'ad_soyad', 'telefon', 'eposta'];
    for (var i = 0; i < req.length; i++) if (!String(d[req[i]] || '').trim()) return json_({ ok: false, error: 'eksik' });
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(String(d.eposta))) return json_({ ok: false, error: 'eposta' });
    var digits = String(d.telefon).replace(/\D/g, '');
    if (digits.length < 10 || digits.length > 13) return json_({ ok: false, error: 'telefon' });

    // Aynı kişiden 10 dakika içinde tekrar gönderimi tek kayıt say
    var cache = CacheService.getScriptCache();
    var key = 'k' + Utilities.base64EncodeWebSafe(Utilities.computeDigest(Utilities.DigestAlgorithm.MD5,
      (String(d.eposta) + digits).toLowerCase()));
    if (cache.get(key)) return json_({ ok: true, dup: true });
    cache.put(key, '1', 600);

    var id = Utilities.getUuid().slice(0, 8);
    var row = [new Date()].concat(FIELDS.map(function (f) { return clean_(d[f]); })).concat(['Yeni', '', id]);
    var sh = SpreadsheetApp.openById(SHEET_ID).getSheetByName(SHEET_NAME);
    sh.appendRow(row);

    var rows = FIELDS.filter(function (f) { return String(d[f] || '').trim(); }).map(function (f) {
      return '<tr><td style="padding:6px 12px;color:#4A5568;white-space:nowrap">' + LABELS[f] + '</td><td style="padding:6px 12px">' + esc_(d[f]) + '</td></tr>';
    }).join('');
    MailApp.sendEmail({
      to: NOTIFY_TO,
      replyTo: String(d.eposta),
      name: 'karelima.com.tr',
      subject: 'Yeni teklif talebi: ' + String(d.firma).slice(0, 80) + (d.sektor ? ' (' + String(d.sektor).slice(0, 40) + ')' : ''),
      htmlBody: '<div style="font-family:Arial,sans-serif;font-size:14px;color:#0B1524"><p><b>karelima.com.tr</b> üzerinden yeni bir teklif talebi geldi. Kayıt no: ' + id + '</p>' +
        '<table style="border-collapse:collapse;border:1px solid #E3E8EF">' + rows + '</table>' +
        '<p><a href="tel:' + digits + '">Hemen ara</a> · <a href="https://docs.google.com/spreadsheets/d/' + SHEET_ID + '">Tüm talepler</a></p></div>'
    });
    return json_({ ok: true, id: id });
  } catch (err) {
    console.error(err);
    return json_({ ok: false, error: 'sunucu' });
  } finally {
    lock.releaseLock();
  }
}

function clean_(v) {
  var s = String(v == null ? '' : v).slice(0, 2000).trim();
  return /^[=+\-@]/.test(s) ? "'" + s : s;                            // tabloda formül çalıştırılmasını engelle
}
function esc_(v) {
  return String(v == null ? '' : v).slice(0, 2000).replace(/[&<>"]/g, function (c) {
    return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
  }).replace(/\n/g, '<br>');
}
function json_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
