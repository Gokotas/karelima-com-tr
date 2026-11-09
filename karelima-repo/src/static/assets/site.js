(function () {
  'use strict';
  window.dataLayer = window.dataLayer || [];
  function track(ev, extra) { try { window.dataLayer.push(Object.assign({ event: ev }, extra || {})); } catch (e) {} }

  // Çerez onayı (Consent Mode v2)
  var cc = document.getElementById('cc');
  function readConsent() { try { return JSON.parse(localStorage.getItem('klm_consent') || 'null'); } catch (e) { return null; } }
  function saveConsent(a, m) {
    try { localStorage.setItem('klm_consent', JSON.stringify({ a: a ? 1 : 0, m: m ? 1 : 0, t: Date.now() })); } catch (e) {}
    if (typeof gtag === 'function') gtag('consent', 'update', { analytics_storage: a ? 'granted' : 'denied', ad_storage: m ? 'granted' : 'denied', ad_user_data: m ? 'granted' : 'denied', ad_personalization: m ? 'granted' : 'denied' });
    track('consent_update', { consent_analytics: a ? 'granted' : 'denied', consent_ads: m ? 'granted' : 'denied' });
    if (cc) cc.hidden = true;
  }
  if (cc) {
    var opts = document.getElementById('cc-opts'), ca = document.getElementById('cc-a'), cm = document.getElementById('cc-m');
    var prefsBtn = cc.querySelector('[data-cc="prefs"]');
    if (!readConsent()) cc.hidden = false;
    cc.addEventListener('click', function (e) {
      var b = e.target.closest && e.target.closest('[data-cc]'); if (!b) return;
      var k = b.getAttribute('data-cc');
      if (k === 'accept') saveConsent(true, true);
      else if (k === 'reject') saveConsent(false, false);
      else if (k === 'prefs') {
        if (opts.hidden) { var c = readConsent() || {}; ca.checked = !!c.a; cm.checked = !!c.m; opts.hidden = false; prefsBtn.textContent = 'Seçimi kaydet'; }
        else saveConsent(ca.checked, cm.checked);
      }
    });
    document.addEventListener('click', function (e) {
      if (e.target.closest && e.target.closest('[data-cc-open]')) { opts.hidden = true; prefsBtn.textContent = 'Tercihler'; cc.hidden = false; }
    });
  }

  // Kaynak bilgisi (ilk giriş sayfası, UTM, gclid) — yalnızca bu oturum için
  var attr = {};
  try {
    attr = JSON.parse(sessionStorage.getItem('klm_attr') || 'null');
    if (!attr) {
      var q = new URLSearchParams(location.search); attr = { giris_sayfasi: location.pathname };
      ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'gclid'].forEach(function (k) { if (q.get(k)) attr[k] = q.get(k).slice(0, 200); });
      if (!attr.utm_source && document.referrer && document.referrer.indexOf(location.host) < 0) attr.utm_source = document.referrer.split('/')[2] || '';
      sessionStorage.setItem('klm_attr', JSON.stringify(attr));
    }
  } catch (e) { attr = {}; }

  // Menü
  var btn = document.querySelector('.menu-btn'), nav = document.getElementById('nav');
  if (btn && nav) btn.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  });

  // Ölçüm: telefon ve CTA tıklamaları
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('[data-ev]');
    if (a) track(a.getAttribute('data-ev'), { link_url: a.getAttribute('href') || '' });
  });

  // Sektör sekmeleri
  var tabs = Array.prototype.slice.call(document.querySelectorAll('[role="tab"]'));
  function select(t) {
    tabs.forEach(function (x) {
      var on = x === t;
      x.setAttribute('aria-selected', on ? 'true' : 'false');
      x.tabIndex = on ? 0 : -1;
      var p = document.getElementById(x.getAttribute('aria-controls'));
      if (p) p.hidden = !on;
    });
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { select(t); });
    t.addEventListener('keydown', function (e) {
      var j = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : null;
      if (j === null) return;
      e.preventDefault();
      var n = tabs[(j + tabs.length) % tabs.length]; n.focus(); select(n);
    });
  });

  // Canlı operasyon akışı (örnek olaylar)
  var box = document.getElementById('feed-rows');
  if (box) {
    var ev = [
      ['Otomotiv bayi', 'Test sürüşü randevusu oluşturuldu', 'Planlandı', 'b'],
      ['Hastane', 'Kardiyoloji randevusu onaylandı', 'Onaylandı', 'g'],
      ['Web formu', 'Yeni talep saniyeler içinde arandı', 'Arandı', 'o'],
      ['Kalite', 'Yeni görüşmeler kaydedildi', 'Kaydedildi', 'b'],
      ['Diş kliniği', 'Yarınki hastalara hatırlatma yapıldı', 'Tamamlandı', 'g'],
      ['E-ticaret', 'İade talebi kayda alındı', 'Kayıt açıldı', 'o'],
      ['Servis', 'Periyodik bakım randevusu verildi', 'Planlandı', 'b'],
      ['Kampanya', 'Hedef müşteri listesi aramaya alındı', 'Başladı', 'b'],
      ['Telekom', 'Yeni abonelik başvurusu alındı', 'Satış', 'g'],
      ['Otel', 'Rezervasyon tarihi güncellendi', 'Güncellendi', 'b'],
      ['Özel okul', 'Kampüs ziyareti randevusu oluşturuldu', 'Planlandı', 'b'],
      ['Klinik', 'Gelmeyen hastaya yeni saat verildi', 'Yeniden planlandı', 'b'],
      ['Memnuniyet', 'Hizmet sonrası anket tamamlandı', 'Tamamlandı', 'g'],
      ['Konut projesi', 'Örnek daire ziyareti planlandı', 'Planlandı', 'b'],
      ['Sigorta', 'Poliçe yenileme hatırlatması yapıldı', 'Arandı', 'o'],
      ['E-ticaret', 'Kargo sorusu ilk temasta çözüldü', 'Çözüldü', 'g'],
      ['Gece hattı', 'Mesai dışı çağrı karşılandı', 'Karşılandı', 'g'],
      ['Otomotiv bayi', 'Satış sonrası memnuniyet araması yapıldı', 'Tamamlandı', 'g'],
      ['Teknik servis', 'Arıza kaydı oluşturuldu', 'Kayıt açıldı', 'o'],
      ['WhatsApp', 'Müşteri mesajı yanıtlandı', 'Yanıtlandı', 'g'],
      ['GES firması', 'Keşif randevusu planlandı', 'Planlandı', 'b'],
      ['Hastane', 'Check-up randevusu oluşturuldu', 'Onaylandı', 'g'],
      ['Eğitim', 'Kayıt hatırlatma araması yapıldı', 'Arandı', 'o'],
      ['Telekom', 'Kurulum randevusu teyit edildi', 'Onaylandı', 'g'],
      ['Karelima CRM', 'Günün talepleri müşteriye raporlandı', 'Raporlandı', 'g'],
      ['Otomotiv bayi', 'İkinci el ekspertiz randevusu verildi', 'Planlandı', 'b'],
      ['Restoran', 'Şube geri bildirimi kayda alındı', 'Kayıt açıldı', 'o'],
      ['Klinik', 'Online ön görüşme saati ayarlandı', 'Planlandı', 'b'],
      ['Kampanya', 'Randevu aramaları tamamlandı', 'Tamamlandı', 'g'],
      ['Yazılım firması', 'Demo görüşmesi takvime eklendi', 'Planlandı', 'b']
    ];
    var ages = ['Şimdi', '1 dk', '3 dk', '6 dk'], tick = 0;
    function esc(s) { return s.replace(/[&<>]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]; }); }
    function render() {
      var html = '';
      for (var i = 0; i < 4; i++) {
        var e = ev[((tick - i) % ev.length + ev.length) % ev.length];
        html += '<div class="feed-row' + (i === 0 && tick > 0 ? ' is-new' : '') + '"><span class="feed-age">' + ages[i] + '</span><span class="feed-txt"><span class="feed-tag">' + esc(e[0]) + '</span><span class="feed-msg">' + esc(e[1]) + '</span></span><span class="chip chip-' + e[3] + '">' + esc(e[2]) + '</span></div>';
      }
      box.innerHTML = html;
    }
    render();
    setInterval(function () { if (!document.hidden) { tick++; render(); } }, 2800);
  }

  // Teklif formu
  var form = document.getElementById('teklif-form');
  if (form) {
    var msg = document.getElementById('form-msg');
    function show(text, ok) { msg.hidden = false; msg.className = 'form-msg ' + (ok ? 'ok' : 'err'); msg.textContent = text; }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.web_sitesi.value) return;
      var req = ['firma', 'ad_soyad', 'telefon', 'eposta', 'sektor'];
      for (var i = 0; i < req.length; i++) {
        var f = form.elements[req[i]];
        if (!f.value.trim()) { show('Lütfen zorunlu alanları doldurun.', false); f.focus(); return; }
      }
      if (!form.eposta.checkValidity()) { show('Lütfen geçerli bir e-posta adresi yazın.', false); form.eposta.focus(); return; }
      var tel = form.telefon.value.replace(/\D/g, '');
      if (tel.length < 10 || tel.length > 13) { show('Lütfen telefon numaranızı alan koduyla birlikte yazın.', false); form.telefon.focus(); return; }
      var hizmet = Array.prototype.map.call(form.querySelectorAll('input[name="hizmet"]:checked'), function (x) { return x.value; });
      if (!hizmet.length) { show('Lütfen en az bir hizmet seçin.', false); return; }
      if (!form.kvkk.checked) { show('Devam etmek için KVKK Aydınlatma Metni onayını işaretleyin.', false); return; }
      var data = {
        firma: form.firma.value.trim(), ad_soyad: form.ad_soyad.value.trim(), telefon: form.telefon.value.trim(),
        eposta: form.eposta.value.trim(), hizmet: hizmet.join(', '), sektor: form.sektor.value, hacim: form.hacim.value,
        baslangic: form.baslangic.value, mesaj: form.mesaj.value.trim(), sayfa: location.href, zaman: new Date().toISOString()
      };
      Object.keys(attr || {}).forEach(function (k) { data[k] = attr[k]; });
      var endpoint = form.getAttribute('data-endpoint');
      var button = form.querySelector('button[type="submit"]');
      function done() {
        track('generate_lead', { form_name: 'teklif', sektor: data.sektor, hizmet: data.hizmet });
        form.reset();
        show('Teşekkürler, talebiniz bize ulaştı. Ekibimiz sizi en kısa sürede arayacak.', true);
      }
      if (endpoint) {
        button.disabled = true;
        fetch(endpoint, { method: 'POST', headers: { 'Content-Type': 'text/plain;charset=utf-8' }, body: JSON.stringify(data) })
          .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
          .then(function (j) { if (!j || !j.ok) throw new Error((j && j.error) || 'hata'); done(); })
          .catch(function () { show('Gönderilemedi. Lütfen 0534 374 76 92 numarasından bize ulaşın.', false); })
          .then(function () { button.disabled = false; });
      } else {
        var body = Object.keys(data).map(function (k) { return k + ': ' + data[k]; }).join('\n');
        location.href = 'mailto:info@karelima.com?subject=' + encodeURIComponent('Teklif talebi: ' + data.firma) + '&body=' + encodeURIComponent(body);
        done();
      }
    });
  }
})();
