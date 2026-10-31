# -*- coding: utf-8 -*-
import os, shutil, json, datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
from content import *
from pages_hizmet import PAGES_HIZMET
from pages_sektor import PAGES_SEKTOR, PAGE_FIYAT

ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(ROOT, '..', 'dist')
env = Environment(loader=FileSystemLoader(os.path.join(ROOT, 'templates')), autoescape=select_autoescape(['html']))
TODAY = datetime.date.today().isoformat()
S = SITE
ORG_ID = S['url'] + '/#organization'

ORG = {
    '@context': 'https://schema.org', '@type': ['Organization', 'ProfessionalService'], '@id': ORG_ID,
    'name': 'Karelima', 'legalName': S['legal_name'], 'url': S['url'] + '/', 'logo': S['url'] + '/favicon.svg',
    'image': S['url'] + '/assets/img/operasyon-merkezi-1400.jpg',
    'description': 'İzmir merkezli, 7/24 hizmet veren kurumsal çağrı merkezi. Gelen çağrı yönetimi, randevu ve rezervasyon, dış arama, memnuniyet aramaları ve back office hizmetleri.',
    'foundingDate': S['founding'], 'taxID': S['vkn'], 'telephone': '+90 850 480 38 73', 'email': S['email'],
    'numberOfEmployees': {'@type': 'QuantitativeValue', 'minValue': 20},
    'address': {'@type': 'PostalAddress', 'streetAddress': 'Çınarlı Mah. Şehit Polis Fethi Sekin Cad. No:3 SUNUCU Plaza Kat:14 D:1405', 'addressLocality': 'Konak', 'addressRegion': 'İzmir', 'addressCountry': 'TR'},
    'areaServed': {'@type': 'Country', 'name': 'Türkiye'},
    'openingHoursSpecification': {'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 'opens': '00:00', 'closes': '23:59'},
    'knowsLanguage': 'tr', 'sameAs': [S['partner_site']],
    'contactPoint': {'@type': 'ContactPoint', 'telephone': '+90 850 480 38 73', 'contactType': 'sales', 'areaServed': 'TR', 'availableLanguage': 'Turkish', 'hoursAvailable': 'Mo-Su 00:00-23:59'},
}
WEBSITE = {'@context': 'https://schema.org', '@type': 'WebSite', '@id': S['url'] + '/#website', 'url': S['url'] + '/', 'name': 'Karelima', 'inLanguage': 'tr-TR', 'publisher': {'@id': ORG_ID}}

def crumbs_ld(items):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': it['name'], 'item': S['url'] + it['url']} for i, it in enumerate(items)]}

def faq_ld(items):
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q['q'], 'acceptedAnswer': {'@type': 'Answer', 'text': q['a']}} for q in items]}

def service_ld(name, desc, path, audience=None):
    d = {'@context': 'https://schema.org', '@type': 'Service', 'name': name, 'description': desc, 'url': S['url'] + path,
         'serviceType': 'Çağrı merkezi hizmeti', 'provider': {'@id': ORG_ID}, 'areaServed': {'@type': 'Country', 'name': 'Türkiye'}, 'availableChannel': {'@type': 'ServiceChannel', 'servicePhone': '+90 850 480 38 73'}}
    if audience: d['audience'] = {'@type': 'BusinessAudience', 'name': audience}
    return d

SECTORS_LIVE = [dict(name='Hastane çağrı merkezi', url='/sektorler/saglik/hastane-cagri-merkezi/')] + [dict(name=p['name'], url=p['path']) for p in PAGES_SEKTOR]
SECTORS_ALL = ['Sağlık (hastane, klinik)', 'Otomotiv (bayi, servis)', 'E-ticaret ve perakende', 'Telekom ve abonelik', 'Eğitim', 'Gayrimenkul', 'Sigorta', 'Turizm ve otelcilik', 'Teknoloji ve yazılım', 'Teknik servis', 'Restoran ve franchise', 'Enerji', 'Lojistik ve kargo', 'Finans']
COMMON = dict(site=S, services=SERVICES, sectors_live=SECTORS_LIVE, sectors_all=SECTORS_ALL)
PAGES = []

def render(tpl, path, page, **ctx):
    page.setdefault('jsonld', [])
    page['path'] = path
    html = env.get_template(tpl).render(page=page, **COMMON, **ctx)
    out = os.path.join(DIST, path.strip('/'), 'index.html') if path.endswith('/') else os.path.join(DIST, path.strip('/'))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(html)
    if not page.get('robots', '').startswith('noindex'):
        PAGES.append((path, page.get('priority', '0.7')))

def assert_len(page):
    assert len(page['title']) <= 65, ('title too long', page['title'], len(page['title']))
    assert len(page['description']) <= 160, ('desc too long', page['description'], len(page['description']))

def P(**kw):
    assert_len(kw); return kw

# temizle ve statik dosyaları kopyala
if os.path.exists(DIST):
    for n in os.listdir(DIST):
        p = os.path.join(DIST, n)
        if n == 'assets':
            for m in os.listdir(p):
                if m not in ('img', 'fonts'): q = os.path.join(p, m); shutil.rmtree(q) if os.path.isdir(q) else os.remove(q)
        else:
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
shutil.copytree(os.path.join(ROOT, 'static'), DIST, dirs_exist_ok=True)

# Ana sayfa
render('index.html', '/', P(title='Karelima | İzmir Çağrı Merkezi Hizmeti, 7/24 Dış Kaynak',
    description="İzmir'den 7/24 kurumsal çağrı merkezi: gelen çağrı yönetimi, randevu ve rezervasyon, dış arama, memnuniyet aramaları. 10 iş gününde kurulum.",
    priority='1.0', jsonld=[ORG, WEBSITE, faq_ld(HOME_FAQ)]), home_sectors=HOME_SECTORS, home_faq=HOME_FAQ)

# Hizmetler hub
cards = [dict(icon=s['icon'], name=s['name'], text=s['short'], url=('/hizmetler/%s/' % s['slug']) if s['live'] else None) for s in SERVICES]
cr = [dict(name='Ana sayfa', url='/'), dict(name='Hizmetler', url='/hizmetler/')]
render('hub.html', '/hizmetler/', P(title='Çağrı Merkezi Hizmetleri | Karelima',
    description='Gelen çağrı, randevu, dış arama, memnuniyet anketi, WhatsApp desteği ve back office: Karelima\'nın 7/24 çağrı merkezi hizmetleri.',
    section='hizmetler', crumbs=cr, priority='0.9', jsonld=[crumbs_ld(cr)]),
    h=dict(eyebrow='Hizmetler', h1='Çağrı merkezi hizmetlerimiz', answer='Karelima, firmaların telefon, WhatsApp ve e-posta üzerinden gelen ve giden tüm müşteri temaslarını İzmir\'deki ekibiyle 7/24 yönetir. İhtiyacınıza göre tek bir hizmetle başlayabilir ya da birkaçını birleştirebilirsiniz.', cards=cards))

# Sektörler hub
scards = []
for s in SECTORS:
    links = [dict(url='/sektorler/%s/%s/' % (s['slug'], ch['slug']), name=ch['name']) for ch in s.get('children', []) if ch.get('live')]
    scards.append(dict(icon=s['icon'], name=s['name'], text=s['text'], sub=s['sub'], url=links[0]['url'] if links else None, links=links))
cr = [dict(name='Ana sayfa', url='/'), dict(name='Sektörler', url='/sektorler/')]
render('hub.html', '/sektorler/', P(title='Sektörlere Özel Çağrı Merkezi Çözümleri | Karelima',
    description='Sağlık, otomotiv, e-ticaret, eğitim, turizm ve daha fazlası için sektörün diline ve mevzuatına uygun çağrı merkezi hizmeti.',
    section='sektorler', crumbs=cr, priority='0.9', jsonld=[crumbs_ld(cr)]),
    h=dict(eyebrow='Sektörler', h1='Sektörünüzün dilini bilen çağrı merkezi', answer='Her sektörün çağrı akışı, mevzuatı ve hassasiyetleri farklıdır. Karelima, temsilcilerini işinize özel konuşma akışı ve eğitimle hazırlar; sağlıkta KVKK, satışta İYS gibi kurallara uygun çalışır.', cards=scards))

# Gelen çağrı yönetimi
d = DETAIL_GELEN
cr = [dict(name='Ana sayfa', url='/'), dict(name='Hizmetler', url='/hizmetler/'), dict(name='Gelen çağrı yönetimi', url='/hizmetler/gelen-cagri-yonetimi/')]
render('detail.html', '/hizmetler/gelen-cagri-yonetimi/', P(title='Gelen Çağrı Yönetimi (Inbound) Hizmeti | Karelima',
    description='Bilgi, sipariş, şikâyet ve santral hattınızı 7/24 karşılıyoruz. Her çağrı Karelima CRM\'e kayıtlı, kurulum 10 iş günü. İzmir merkezli çağrı merkezi.',
    section='hizmetler', crumbs=cr, og_image='temsilci-ofis',
    jsonld=[service_ld('Gelen çağrı yönetimi', d['answer'], '/hizmetler/gelen-cagri-yonetimi/'), crumbs_ld(cr), faq_ld(d['faq'])]), d=d)

# Hastane
d = DETAIL_HASTANE
cr = [dict(name='Ana sayfa', url='/'), dict(name='Sektörler', url='/sektorler/'), dict(name='Sağlık', url='/sektorler/'), dict(name='Hastane çağrı merkezi', url='/sektorler/saglik/hastane-cagri-merkezi/')]
render('detail.html', '/sektorler/saglik/hastane-cagri-merkezi/', P(title='Hastane Çağrı Merkezi ve Randevu Yönetimi | Karelima',
    description='Hastaneler için 7/24 randevu hattı: randevu alma, hatırlatma ve teyit aramaları, mesai dışı hat. KVKK uyumlu süreç, kurulum 10 iş günü.',
    section='sektorler', crumbs=cr, og_image='saglik-randevu',
    jsonld=[service_ld('Hastane çağrı merkezi ve randevu yönetimi', d['answer'], '/sektorler/saglik/hastane-cagri-merkezi/', 'Hastaneler ve sağlık kuruluşları'), crumbs_ld([c for i, c in enumerate(cr) if i != 2]), faq_ld(d['faq'])]), d=d)

# Yeni hizmet sayfaları
for pg in PAGES_HIZMET:
    d = pg['d']
    cr = [dict(name='Ana sayfa', url='/'), dict(name='Hizmetler', url='/hizmetler/'), dict(name=pg['name'], url=pg['path'])]
    render('detail.html', pg['path'], P(title=pg['title'], description=pg['description'], section='hizmetler', crumbs=cr, og_image=pg['og_image'],
        jsonld=[service_ld(pg['name'], d['answer'], pg['path'], pg.get('audience')), crumbs_ld(cr), faq_ld(d['faq'])]), d=d)

# Yeni sektör sayfaları
for pg in PAGES_SEKTOR:
    d = pg['d']
    cr = [dict(name='Ana sayfa', url='/'), dict(name='Sektörler', url='/sektorler/'), dict(name=pg['sector'], url='/sektorler/'), dict(name=pg['name'], url=pg['path'])]
    render('detail.html', pg['path'], P(title=pg['title'], description=pg['description'], section='sektorler', crumbs=cr, og_image=pg['og_image'],
        jsonld=[service_ld(pg['name'], d['answer'], pg['path'], pg.get('audience')), crumbs_ld([c for i, c in enumerate(cr) if i != 2]), faq_ld(d['faq'])]), d=d)

# Rehber: fiyatlar
pg = PAGE_FIYAT; d = pg['d']
cr = [dict(name='Ana sayfa', url='/'), dict(name=pg['name'], url=pg['path'])]
article = {'@context': 'https://schema.org', '@type': 'Article', 'headline': d['h1'], 'description': pg['description'], 'inLanguage': 'tr-TR',
           'url': S['url'] + pg['path'], 'mainEntityOfPage': S['url'] + pg['path'], 'image': S['url'] + '/assets/img/%s-1400.jpg' % pg['og_image'],
           'author': {'@id': ORG_ID}, 'publisher': {'@id': ORG_ID}, 'dateModified': TODAY}
render('detail.html', pg['path'], P(title=pg['title'], description=pg['description'], crumbs=cr, og_image=pg['og_image'], priority='0.8',
    jsonld=[article, crumbs_ld(cr), faq_ld(d['faq'])]), d=d)

# Teklif al
cr = [dict(name='Ana sayfa', url='/'), dict(name='Teklif alın', url='/teklif-al/')]
render('teklif.html', '/teklif-al/', P(title='Çağrı Merkezi Teklifi Alın | Karelima',
    description='Çağrı merkezi ihtiyacınızı anlatın; ekip, süre ve fiyat önerimizi yazılı olarak iletelim. Taahhütsüz ilk görüşme, pilot dönem imkânı.',
    crumbs=cr, jsonld=[crumbs_ld(cr)]))

def simple(path, title, desc, s, crumbs_name, section=None, robots=None, priority='0.6', extra_ld=None):
    cr = [dict(name='Ana sayfa', url='/'), dict(name=crumbs_name, url=path)]
    pg = P(title=title, description=desc, crumbs=cr, section=section, priority=priority, jsonld=[crumbs_ld(cr)] + (extra_ld or []))
    if robots: pg['robots'] = robots
    render('simple.html', path, pg, s=s)

T = env.get_template('fragments.html').module
simple('/is-ortaklarimiz/', 'İş Ortaklarımız: Digitürk ve Türksat | Karelima',
       'Karelima, Digitürk ve Türksat\'ın satış iş ortağıdır. Bireysel abonelik başvuruları için karelima.com adresini ziyaret edin.',
       dict(eyebrow='İş ortaklarımız', h1='Digitürk ve Türksat iş ortaklığı', answer='Karelima, telekom ve yayın sektöründe Digitürk ve Türksat\'ın satış iş ortağı olarak yüksek hacimli abonelik satışını kendi ekibiyle yürütür. Bu deneyimi, çağrı merkezi hizmeti verdiğimiz tüm sektörlere taşırız.', body=T.partner(S), cta=True),
       'İş ortaklarımız', section='partner')
simple('/hakkimizda/', 'Hakkımızda | Karelima Bilişim, İzmir Çağrı Merkezi',
       'Karelima Bilişim 2021\'den bu yana İzmir\'den 7/24 kurumsal çağrı merkezi, satış ve müşteri deneyimi hizmeti veriyor. 20+ kişilik ekip, Karelima CRM.',
       dict(eyebrow='Hakkımızda', h1='Karelima Bilişim hakkında', answer='Karelima Bilişim Hizmetleri San. ve Tic. A.Ş., 2021\'de İzmir\'de kuruldu. 20\'den fazla kişilik ekibiyle 7 gün 24 saat kurumsal çağrı merkezi, satış ve müşteri deneyimi hizmeti veriyor.', body=T.about(S), cta=True),
       'Hakkımızda', section='kurumsal', priority='0.7', extra_ld=[ORG])
simple('/iletisim/', 'İletişim | Karelima Çağrı Merkezi, İzmir',
       'Karelima ile iletişime geçin: 0850 480 38 73, info@karelima.com. Çınarlı Mah. SUNUCU Plaza, Konak / İzmir. 7/24 hizmet.',
       dict(eyebrow='İletişim', h1='Bize ulaşın', answer='Çağrı merkezi hizmeti için teklif almak ya da operasyon merkezimizi ziyaret etmek için bize ulaşabilirsiniz. 7 gün 24 saat hizmet veriyoruz.', body=T.contact(S), cta=False),
       'İletişim', section='iletisim', extra_ld=[ORG])
simple('/kariyer/', 'Kariyer: Müşteri Temsilcisi İş İlanları İzmir | Karelima',
       'Karelima İzmir operasyon merkezinde müşteri temsilcisi ve takım lideri olarak çalışmak için başvurun.',
       dict(eyebrow='Kariyer', h1='Karelima\'da çalışın', answer='İletişimi güçlü, İzmir\'de çalışmak isteyen müşteri temsilcileri ve takım liderleri arıyoruz.', body=T.career(S), cta=False), 'Kariyer', priority='0.5')
simple('/kvkk-aydinlatma-metni/', 'KVKK Aydınlatma Metni | Karelima',
       'Karelima Bilişim\'in teklif, iletişim ve web sitesi süreçlerinde kişisel verileri nasıl işlediğine dair 6698 sayılı KVKK kapsamındaki aydınlatma metni.',
       dict(h1='Kişisel Verilerin Korunması Aydınlatma Metni', body=T.kvkk(S), cta=False), 'KVKK Aydınlatma Metni', priority='0.3')
simple('/gizlilik-ve-cerez-politikasi/', 'Gizlilik ve Çerez Politikası | Karelima',
       'karelima.com.tr web sitesinde kullanılan çerezler ve gizlilik uygulamalarımız hakkında bilgi.',
       dict(h1='Gizlilik ve Çerez Politikası', body=T.privacy(S), cta=False), 'Gizlilik ve Çerez Politikası', priority='0.3')

# 404
pg = dict(title='Sayfa bulunamadı | Karelima', description='Aradığınız sayfa bulunamadı.', robots='noindex, follow', crumbs=None, jsonld=[])
pg['path'] = '/404.html'
open(os.path.join(DIST, '404.html'), 'w', encoding='utf-8').write(env.get_template('simple.html').render(page=pg, s=dict(h1='Aradığınız sayfa bulunamadı', answer='Sayfa taşınmış ya da kaldırılmış olabilir.', body=T.notfound(S), cta=False), **COMMON))

# sitemap, robots, llms.txt
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for path, pr in PAGES:
    sm.append('<url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>' % (S['url'], path, TODAY, pr))
sm.append('</urlset>')
open(os.path.join(DIST, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(sm) + '\n')
open(os.path.join(DIST, 'robots.txt'), 'w', encoding='utf-8').write(
    'User-agent: *\nAllow: /\n\n# Yapay zeka arama motorlarına açık\nUser-agent: GPTBot\nAllow: /\nUser-agent: OAI-SearchBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % S['url'])
llms = """# Karelima

> Karelima Bilişim Hizmetleri San. ve Tic. A.Ş., 2021'de İzmir'de kurulan, 20'den fazla kişilik ekiple 7/24 kurumsal çağrı merkezi hizmeti veren bir firmadır. Gelen çağrı yönetimi, randevu ve rezervasyon, dış arama ve telesatış, memnuniyet aramaları, WhatsApp desteği ve back office hizmetleri sunar.

- Adres: {address}
- Telefon: {phone} · E-posta: {email}
- Kuruluş: 9 Eylül 2021 (İzmir Ticaret Sicili) · VKN {vkn}
- Hizmet saatleri: 7 gün 24 saat · Kurulum süresi: 10 iş günü · Talepler saniyeler içinde geri aranır
- Kendi CRM altyapısı: Karelima CRM
- İş ortaklıkları: Digitürk ve Türksat (bireysel abonelik: {partner})

## Sayfalar
- [Ana sayfa]({url}/): Hizmetler, sektörler, çalışma modeli, sık sorulanlar
- [Hizmetler]({url}/hizmetler/)
- [Gelen çağrı yönetimi]({url}/hizmetler/gelen-cagri-yonetimi/)
{hizmet}
- [Sektörler]({url}/sektorler/)
- [Hastane çağrı merkezi ve randevu yönetimi]({url}/sektorler/saglik/hastane-cagri-merkezi/)
{sektor}
- [Çağrı merkezi hizmeti fiyatları rehberi]({url}/rehber/cagri-merkezi-hizmeti-fiyatlari/)
- [Hakkımızda]({url}/hakkimizda/)
- [Teklif alın]({url}/teklif-al/)
- [İletişim]({url}/iletisim/)
""".format(partner=S['partner_site'],
    hizmet='\n'.join('- [%s](%s%s): %s' % (p['name'], S['url'], p['path'], p['description']) for p in PAGES_HIZMET),
    sektor='\n'.join('- [%s](%s%s): %s' % (p['name'], S['url'], p['path'], p['description']) for p in PAGES_SEKTOR), **S)
open(os.path.join(DIST, 'llms.txt'), 'w', encoding='utf-8').write(llms)
print('OK', len(PAGES), 'sayfa')
