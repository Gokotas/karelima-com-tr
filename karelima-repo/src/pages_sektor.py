# -*- coding: utf-8 -*-
"""Sektör alt sayfaları ve rehber sayfaları."""

FIYAT = dict(url='/rehber/cagri-merkezi-hizmeti-fiyatlari/', name='Çağrı merkezi hizmeti fiyatları')
TEKLIF = dict(url='/teklif-al/', name='Teklif alın')
SAGLIK_LAW = dict(title='Mevzuata uygun çalışma', text='Sağlık Hizmetlerinde Tanıtım ve Bilgilendirme Faaliyetleri Hakkında Yönetmelik, kişilerin rızası olmadan tanıtım amacıyla aranmasını ve hasta yönlendirmesini yasaklar. Klinik projelerinde gelen çağrı, randevu, hatırlatma ve memnuniyet aramaları yaparız; izinsiz tanıtım ya da kampanya araması yapmayız.')

PAGES_SEKTOR = [
# ---------------------------------------------------------------- Klinik
dict(path='/sektorler/saglik/klinik-ve-dis-hekimligi-cagri-merkezi/', name='Klinik ve diş hekimliği çağrı merkezi', sector='Sağlık',
     og_image='saglik-randevu', audience='Diş, estetik, göz ve fizik tedavi klinikleri',
     title='Klinik ve Diş Hekimi Randevu Hattı, Çağrı Merkezi | Karelima',
     description='Diş, estetik, göz ve fizik tedavi klinikleri için 7/24 randevu hattı: randevu, seans hatırlatma, teyit ve memnuniyet aramaları. KVKK uyumlu süreç.',
     d=dict(
    eyebrow='Sektörler · Sağlık', h1='Klinik ve diş hekimliği merkezleri için randevu hattı ve çağrı merkezi',
    answer='Karelima; diş, estetik, göz, fizik tedavi ve tüp bebek gibi kliniklerin randevu ve bilgi hattını 7/24 karşılar. Randevuyu klinik yazılımınıza işler, tedavi ve seans öncesi hatırlatma yapar, gelemeyecek hastaya yeni saat verir. Sağlık verisini veri işleme sözleşmesi ve sınırlı erişimle korur; izinsiz tanıtım araması yapmaz.',
    facts=['7/24 randevu hattı', 'Seans ve kontrol takibi', 'KVKK uyumlu süreç', 'Kurulum 10 iş günü'],
    illus='illus/klinik.svg',
    tasks_title='Klinik hattında üstlendiğimiz işler', tasks_sub='Hekimleriniz ve asistanlarınız hastaya odaklanırken telefon ve mesajlar bizde.',
    tasks=[
        dict(icon='cal', name='Randevu alma ve değiştirme', text='Hekim ve işlem türüne göre randevuyu klinik yazılımınıza işler, değişiklik ve iptal taleplerini karşılarız.'),
        dict(icon='clock', name='Seans ve kontrol hatırlatma', text='Çok seanslı tedavilerde ve kontrol randevularında hastayı önceden arar ya da mesajla hatırlatırız.'),
        dict(icon='users', name='Ön bilgi ve yönlendirme', text='Çalışma saatleri, hekim günleri, adres ve muayene öncesi hazırlık sorularını yanıtlarız.'),
        dict(icon='chat', name='WhatsApp ve web talepleri', text='Web formu ve WhatsApp\'tan gelen randevu taleplerini aynı ekip ve aynı kayıtla yönetiriz.'),
        dict(icon='moon', name='Mesai dışı hat', text='Akşam ve hafta sonu gelen çağrıları karşılar, randevuyu ilk uygun saate planlarız.'),
        dict(icon='star', name='Hasta memnuniyeti', text='Tedavi sonrası memnuniyeti ölçer, olumsuz geri bildirimi aynı gün kliniğe iletiriz.'),
    ],
    flow_title='Bir klinik randevusu bizde böyle ilerler',
    flow=[
        dict(name='Arama karşılanır', text='Hasta, kliniğinizin adıyla ve onaylı karşılama cümlesiyle karşılanır.'),
        dict(name='İhtiyaç belirlenir', text='İşlem türü, hekim tercihi ve uygun gün sorulur; tıbbi yorum yapılmaz.'),
        dict(name='Randevu işlenir', text='Randevu klinik yazılımınıza işlenir, hastaya teyit mesajı gider.'),
        dict(name='Hatırlatılır', text='Randevu ya da seanstan önce hatırlatma yapılır; gelemeyecekse yeni saat verilir.'),
        dict(name='Raporlanır', text='Randevu, iptal ve gelmeme oranları düzenli olarak raporlanır.'),
    ],
    qa=[
        dict(q='Diş kliniği randevu hattı dışarıya nasıl verilir?', p=[
            'Temsilcilerimiz kullandığınız klinik yazılımına yetkili kullanıcı olarak erişir. Kurulumda hekimlerinizin çalışma takvimi, işlem türleri ve süreleri, sık sorulan sorular ve yönlendirme kuralları konuşma akışına eklenir.',
            'Hasta aradığında karşısında kliniğinizin adıyla açılan, işleyişinizi bilen bir temsilci bulur. Randevu doğrudan sisteminize düşer; asistanlarınız telefona yetişmeye çalışmak yerine hastaya odaklanır.']),
        dict(q='Seans ve kontrol randevuları nasıl takip edilir?', p=[
            'İmplant, ortodonti, fizik tedavi ya da estetik uygulamalar gibi çok aşamalı tedavilerde bir sonraki seansın kaçırılması tedavi sürecini uzatır. Seans listesini sizinle paylaşır, her randevudan önce hastayı hatırlatma aramasıyla bilgilendiririz.',
            'Gelemeyecek hastaya hemen yeni saat verilir, boşalan saat bekleyen başka bir hastaya açılır.']),
        dict(q='Hasta verileri nasıl korunuyor?', p=[
            'Sağlık verisi, KVKK\'da özel nitelikli kişisel veri olarak tanımlanır. Bu projelerde klinik veri sorumlusu, Karelima veri işleyendir ve veri işleme sözleşmesiyle çalışılır.',
            'Verilere yalnızca projeye atanmış temsilciler erişir, görüşmeler kayıt altına alınır ve saklama süreleri sözleşmede belirlenir.']),
        dict(q='Sağlık turizmi ve yabancı hastalar için hizmet veriyor musunuz?', p=[
            'Ekibimiz şu anda Türkçe hizmet veriyor. Yabancı dil ihtiyacınızı keşif görüşmesinde konuşalım; projenin kapsamına göre çözüm üretebiliriz.']),
    ],
    law=SAGLIK_LAW,
    why=['7/24 randevu hattı', 'Seans takibiyle daha az boş koltuk', 'Veri işleme sözleşmesiyle çalışma', 'Kurulum 10 iş gününde'],
    faq_title='Klinik çağrı merkezi hakkında',
    faq=[
        dict(q='Temsilciler fiyat ya da tedavi bilgisi veriyor mu?', a='Temsilcilerimiz tıbbi yorum yapmaz. Hangi bilgilerin telefonda paylaşılacağını sizin belirlediğiniz kurallara ve mevzuata göre konuşma akışına ekleriz; diğer sorular kliniğe yönlendirilir.'),
        dict(q='Hangi klinik yazılımlarıyla çalışabilirsiniz?', a='Yetkili kullanıcı erişimi verilen her web tabanlı klinik yazılımıyla çalışabiliriz. Gerekirse API ile entegrasyon kurarız.'),
        dict(q='Tek hekimli muayenehaneler için de uygun mu?', a='Evet. Düşük çağrı hacminde paylaşımlı ekip ya da yalnızca mesai dışı ve yoğun saatler için hizmet alabilirsiniz.'),
        dict(q='Hastaları kampanya için arıyor musunuz?', a='Hayır. Mevzuat, rızası olmayan kişilerin tanıtım amacıyla aranmasını yasaklar. Randevu, hatırlatma ve memnuniyet aramaları yaparız.'),
        dict(q='Kurulum ne kadar sürer?', a='Standart bir klinik randevu hattı için kurulum ve temsilci eğitimi 10 iş gününde tamamlanır.'),
    ],
    related=[dict(url='/sektorler/saglik/hastane-cagri-merkezi/', name='Hastane çağrı merkezi'), dict(url='/hizmetler/randevu-ve-rezervasyon-yonetimi/', name='Randevu yönetimi'), dict(url='/hizmetler/sanal-sekreter-ve-cagri-karsilama/', name='Sanal sekreter'), dict(url='/hizmetler/memnuniyet-ve-anket-aramalari/', name='Hasta memnuniyet aramaları'), FIYAT, TEKLIF],
    cta_title='Kliniğinizin telefonu hiç meşgul çalmasın.', cta_text='Hekim sayınızı, günlük çağrı hacminizi ve kullandığınız yazılımı paylaşın; size özel teklifimizi iletelim.')),

# ---------------------------------------------------------------- Otomotiv
dict(path='/sektorler/otomotiv/bayi-ve-servis-cagri-merkezi/', name='Bayi ve servis çağrı merkezi', sector='Otomotiv',
     og_image='temsilci-ofis', audience='Otomotiv bayileri ve yetkili servisler',
     title='Otomotiv Bayi ve Servis Çağrı Merkezi | Karelima',
     description='Test sürüşü planlama, servis randevusu, bakım hatırlatma ve satış sonrası memnuniyet aramaları. Bayiler için 7/24 çağrı merkezi, kurulum 10 iş günü.',
     d=dict(
    eyebrow='Sektörler · Otomotiv', h1='Otomotiv bayileri ve yetkili servisler için çağrı merkezi',
    answer='Karelima; otomotiv bayilerinin web sitesinden ve kampanyalarından gelen test sürüşü taleplerini aynı gün arar, satış danışmanının takvimine işler. Servis randevularını, periyodik bakım hatırlatmalarını ve satış ile servis sonrası memnuniyet aramalarını yönetir. Her temas kayıt altında, sonuçlar düzenli raporlanır.',
    facts=['Test sürüşü planlama', 'Servis randevu hattı', 'Bakım hatırlatma', 'Satış sonrası memnuniyet'],
    illus='illus/otomotiv.svg',
    tasks_title='Bayi ve serviste üstlendiğimiz işler', tasks_sub='Showroom ve servis ekibiniz müşteriye odaklanırken telefon trafiğini biz yönetiriz.',
    tasks=[
        dict(icon='cal', name='Test sürüşü planlama', text='Web ve kampanya taleplerini saniyeler içinde arar; model, gün ve saati alıp satış danışmanınızın takvimine işleriz.'),
        dict(icon='phone', name='Servis randevu hattı', text='Bakım, onarım ve hasar randevularını servis kapasitenize göre planlarız.'),
        dict(icon='clock', name='Periyodik bakım hatırlatma', text='Bakım zamanı yaklaşan araç sahiplerini arayarak randevu öneririz.'),
        dict(icon='star', name='Satış ve servis sonrası memnuniyet', text='Teslimat ve servis sonrası memnuniyeti markanızın belirlediği formatta ölçeriz.'),
        dict(icon='doc', name='İkinci el ve ekspertiz randevusu', text='Takas ve ikinci el taleplerinde değerleme ve ekspertiz randevusu ayarlarız.'),
        dict(icon='in', name='Kaçan çağrılara geri dönüş', text='Showroom ve servis hattında cevapsız kalan çağrıları aynı gün geri ararız.'),
    ],
    flow_title='Bir test sürüşü talebi bizde böyle ilerler',
    flow=[
        dict(name='Talep gelir', text='Web formu, reklam ya da telefonla gelen talep Karelima CRM\'e kaydedilir.'),
        dict(name='Hızlı dönüş', text='Müşteri saniyeler içinde aranır; model ve uygun saat tercihi alınır.'),
        dict(name='Takvime işlenir', text='Randevu bayinin takvimine ve satış danışmanına aktarılır.'),
        dict(name='Teyit edilir', text='Bir gün önce teyit alınır; gelemeyecekse yeni saat planlanır.'),
        dict(name='Sonuç raporlanır', text='Sürüş sonrası memnuniyet sorulur; tüm adımlar raporunuza yansır.'),
    ],
    qa=[
        dict(q='Test sürüşü talepleri satışa nasıl dönüşür?', p=[
            'Test sürüşü talebi bırakan kişi satın almaya en yakın müşterilerdendir; aynı gün birkaç markaya talep bırakmış olabilir. Talebi saniyeler içinde arayıp uygun saati hemen belirlemek, randevunun gerçekleşme ihtimalini artırır.',
            'Randevudan bir gün önce yapılan teyit araması, satış danışmanınızın boşa beklemesini önler. Sürüş sonrası yapılan kısa memnuniyet araması ise teklif aşamasındaki müşteriyle bağı sıcak tutar.']),
        dict(q='Servis randevu hattı dışarıdan nasıl yönetilir?', p=[
            'Temsilcilerimiz servis randevu sisteminize ya da bayi yönetim yazılımınıza (DMS) yetkili kullanıcı olarak erişir. Servis kapasitesi, iş emri türleri ve süreleri konuşma akışına eklenir; randevu doğrudan sisteminize işlenir.',
            'Danışmanlarınız telefona yetişmeye çalışmak yerine araç kabulüne ve müşteriye odaklanır.']),
        dict(q='Periyodik bakım hatırlatması nasıl yapılır?', p=[
            'Araç satış ve servis kayıtlarınızdan bakım zamanı yaklaşan müşterilerin listesi çıkarılır. Temsilcimiz müşteriyi arayarak bakım zamanını hatırlatır ve uygun gün için randevu önerir.',
            'Mevcut müşteriye kullandığı ürünün bakımıyla ilgili yapılan bu bilgilendirme aramaları, kampanya aramalarından ayrı tutulur.']),
    ],
    why=['Saniyeler içinde test sürüşü dönüşü', 'Bayi sistemine doğrudan kayıt', 'Satışta kanıtlanmış ekip', 'Kurulum 10 iş gününde'],
    faq_title='Otomotiv çağrı merkezi hakkında',
    faq=[
        dict(q='Birden fazla showroom ya da şube için çalışabilir misiniz?', a='Evet. Talepleri şube, marka ya da model bazında ayırır, her şubenin takvimine ayrı ayrı randevu veririz.'),
        dict(q='Markanın memnuniyet anketi formatını kullanabilir misiniz?', a='Evet. Markanızın belirlediği soru setini ve puanlama yöntemini kullanır, sonuçları istenen formatta raporlarız.'),
        dict(q='Kampanya dönemlerinde ek kapasite sağlıyor musunuz?', a='Evet. Lansman ve kampanya dönemlerinde ekibi hacme göre kısa sürede büyütebiliriz.'),
        dict(q='Galeriler ve araç kiralama firmalarıyla da çalışıyor musunuz?', a='Evet. İkinci el galeriler ve kiralama firmaları için de talep karşılama, randevu ve rezervasyon hattı kuruyoruz.'),
        dict(q='Ne kadar sürede başlarız?', a='Standart kurulum ve temsilci eğitimi 10 iş gününde tamamlanır.'),
    ],
    related=[dict(url='/hizmetler/lead-ve-talep-yonetimi/', name='Lead ve talep yönetimi'), dict(url='/hizmetler/randevu-ve-rezervasyon-yonetimi/', name='Randevu yönetimi'), dict(url='/hizmetler/memnuniyet-ve-anket-aramalari/', name='Memnuniyet aramaları'), FIYAT, TEKLIF],
    cta_title='Test sürüşü taleplerinizi aynı gün randevuya çevirelim.', cta_text='Aylık talep sayınızı, şube sayınızı ve kullandığınız sistemi paylaşın; teklifimizi iletelim.')),

# ---------------------------------------------------------------- E-ticaret
dict(path='/sektorler/e-ticaret-ve-perakende/e-ticaret-cagri-merkezi/', name='E-ticaret çağrı merkezi', sector='E-ticaret ve perakende',
     og_image='hero-temsilci', audience='Online mağazalar ve perakendeciler',
     title='E-Ticaret Çağrı Merkezi ve Müşteri Hizmetleri | Karelima',
     description='Sipariş, kargo, iade ve değişim çağrılarınızı telefon, WhatsApp ve e-postadan karşılıyoruz. Kampanya dönemlerinde ek kapasite, 7/24 hizmet.',
     d=dict(
    eyebrow='Sektörler · E-ticaret ve perakende', h1='E-ticaret çağrı merkezi: sipariş, kargo ve iade sorularını biz karşılayalım',
    answer='Karelima, online mağazaların sipariş, kargo, iade ve değişim taleplerini telefon, WhatsApp ve e-posta üzerinden karşılar. Mağaza panelinize ve kargo takip sistemine yetkili kullanıcı olarak erişir, soruyu çoğunlukla ilk temasta çözer. Kampanya ve indirim dönemlerinde ekibi hacme göre büyütür.',
    facts=['Telefon, WhatsApp, e-posta', 'İlk temasta çözüm', 'Kampanya dönemi kapasitesi', '7/24 hizmet'],
    illus='illus/eticaret.svg',
    tasks_title='E-ticarette üstlendiğimiz işler', tasks_sub='Satış öncesinden teslimat sonrasına kadar müşterinizin her sorusu tek ekipte.',
    tasks=[
        dict(icon='doc', name='Sipariş ve kargo bilgilendirme', text='Sipariş durumunu ve kargo takibini panelinizden kontrol eder, müşteriye anında bilgi veririz.'),
        dict(icon='in', name='İade ve değişim', text='İade ve değişim taleplerini kayda alır, süreç ve süreler hakkında doğru bilgi veririz.'),
        dict(icon='chat', name='Satış öncesi ürün soruları', text='Ürün, beden, stok ve teslimat sorularını yanıtlar, siparişe yardımcı oluruz.'),
        dict(icon='out', name='Yarım kalan sipariş aramaları', text='Onay vermiş müşterilerde tamamlanmamış siparişler için hatırlatma araması yaparız.'),
        dict(icon='users', name='Kampanya dönemi kapasite', text='Özel gün ve indirim dönemlerinde ek temsilciyle çağrı ve mesaj yığılmasını önleriz.'),
        dict(icon='star', name='Memnuniyet ve yorum takibi', text='Teslimat sonrası memnuniyeti ölçer, olumsuz deneyimi kalıcı şikâyete dönüşmeden çözeriz.'),
    ],
    flow_title='Bir müşteri talebi bizde böyle ilerler',
    flow=[
        dict(name='Talep gelir', text='Arama, WhatsApp mesajı ya da e-posta Karelima CRM\'de tek kayıtta toplanır.'),
        dict(name='Sipariş bulunur', text='Sipariş numarası ya da telefonla panelinizden kayıt bulunur.'),
        dict(name='Çözüm', text='Kargo, iade ya da değişim işlemi tanımlı kurallara göre yapılır ya da başlatılır.'),
        dict(name='Takip', text='Çözümü sizde olan talepler takip numarasıyla ilgili birime iletilir.'),
        dict(name='Rapor', text='Talep konuları, çözüm süreleri ve memnuniyet düzenli raporlanır.'),
    ],
    qa=[
        dict(q='E-ticaret müşteri hizmetleri dışarıya verilir mi?', p=[
            'Evet; özellikle büyüyen mağazalarda en sık devredilen işlerden biridir. Sipariş ve kargo soruları tekrar eden, kurala bağlanabilen sorulardır; eğitimli bir ekip bunları ilk temasta çözebilir.',
            'Siz ürün, kampanya ve operasyona odaklanırken müşterinizin sorusu hafta sonu ve gece de cevapsız kalmaz.']),
        dict(q='Kampanya dönemlerinde ek kapasite nasıl planlanır?', p=[
            'Önceki dönemlerin sipariş ve talep verilerine bakarak beklenen yoğunluğu birlikte tahmin ederiz. Ek temsilciler kampanyadan önce ürünlerinize ve kampanya kurallarınıza göre eğitilir.',
            'Kampanya bitince ekip normal hacme göre küçülür; yalnızca ihtiyaç duyduğunuz kapasiteye ödeme yaparsınız.']),
        dict(q='Hangi e-ticaret altyapılarıyla çalışabilirsiniz?', p=[
            'Temsilcilerimiz kullandığınız e-ticaret altyapısının yönetim paneline, pazar yeri satıcı panellerine ve kargo firmalarının takip sistemlerine yetkili kullanıcı olarak erişebilir. Panel yetkilerini yalnızca ihtiyaç duyulan işlemlerle sınırlamanızı öneririz.']),
    ],
    law=dict(title='Tüketici mevzuatına uygun bilgilendirme', text='İade ve değişim taleplerinde Mesafeli Sözleşmeler Yönetmeliği\'ndeki cayma hakkı ve süreleri ile sizin iade politikanız esas alınır. Tanıtım ve hatırlatma aramaları yalnızca İYS onayı bulunan müşterilere yapılır.'),
    why=['Telefon, WhatsApp ve e-posta tek ekipte', 'Kampanya döneminde esnek kapasite', 'Panelinizle doğrudan çalışma', '7/24 hizmet'],
    faq_title='E-ticaret çağrı merkezi hakkında',
    faq=[
        dict(q='Sadece WhatsApp ve e-posta için hizmet alabilir miyiz?', a='Evet. Telefon hattı olmadan yalnızca yazılı kanalları da devredebilirsiniz.'),
        dict(q='Pazar yeri mesajlarını da yanıtlıyor musunuz?', a='Evet. Pazar yeri satıcı panellerindeki müşteri sorularını tanımlı kurallarla yanıtlayabiliriz.'),
        dict(q='İade onayını kim veriyor?', a='İade kurallarınızı birlikte belirleriz. Kurala uyan talepleri biz başlatırız; istisnalar onayınıza sunulur.'),
        dict(q='Küçük mağazalar için uygun mu?', a='Evet. Düşük hacimde paylaşımlı ekip modeliyle, ihtiyaç kadar ödeme yaparak başlayabilirsiniz.'),
        dict(q='Ne kadar sürede başlarız?', a='Panel erişimleri ve konuşma akışı hazırlandıktan sonra kurulum 10 iş gününde tamamlanır.'),
    ],
    related=[dict(url='/hizmetler/gelen-cagri-yonetimi/', name='Gelen çağrı yönetimi'), dict(url='/hizmetler/sanal-sekreter-ve-cagri-karsilama/', name='Çağrı karşılama'), dict(url='/hizmetler/memnuniyet-ve-anket-aramalari/', name='Memnuniyet aramaları'), FIYAT, TEKLIF],
    cta_title='Müşteri hizmetlerinizi kampanya dönemine hazırlayalım.', cta_text='Aylık sipariş ve talep sayınızı, kullandığınız kanalları paylaşın; teklifimizi iletelim.')),

# ---------------------------------------------------------------- Sigorta
dict(path='/sektorler/sigorta/sigorta-cagri-merkezi/', name='Sigorta çağrı merkezi', sector='Sigorta',
     og_image='operasyon-merkezi', audience='Sigorta acenteleri ve brokerler',
     title='Sigorta Acenteleri için Çağrı Merkezi | Karelima',
     description='Poliçe yenileme hatırlatma, teklif talebi karşılama, hasar bilgilendirme ve taksit hatırlatma aramaları. Görüşmeler kayıtlı, düzenli rapor.',
     d=dict(
    eyebrow='Sektörler · Sigorta', h1='Sigorta acenteleri ve brokerler için çağrı merkezi',
    answer='Karelima; sigorta acentelerinin poliçe yenileme hatırlatma, teklif talebi karşılama, hasar bilgilendirme ve taksit hatırlatma aramalarını yürütür. Poliçe teklifi ve satışı yetkili teknik personelinizde kalır; biz talebi karşılar, bilgileri toplar ve doğru kişiye aktarırız. Görüşmeler kayıt altında, sonuçlar düzenli raporlanır.',
    facts=['Yenileme hatırlatma', 'Teklif talebi karşılama', 'Hasar bilgilendirme', 'Görüşmeler kayıtlı'],
    illus='illus/sigorta.svg',
    tasks_title='Sigorta acentesinde üstlendiğimiz işler', tasks_sub='Teknik personeliniz teklif ve poliçeye odaklanırken müşteri teması bizde.',
    tasks=[
        dict(icon='clock', name='Poliçe yenileme hatırlatma', text='Vadesi yaklaşan poliçeler için müşteriyi arar, yenileme görüşmesini teknik personelinize planlarız.'),
        dict(icon='doc', name='Teklif talebi karşılama', text='Web ve reklam formlarından gelen trafik, kasko, konut ve sağlık sigortası taleplerini hemen arar, gerekli bilgileri toplarız.'),
        dict(icon='shield', name='Hasar bilgilendirme', text='Hasar anında müşteriyi karşılar, ilk bilgileri kaydeder ve süreci ilgili birime iletiriz.'),
        dict(icon='cal', name='Taksit ve ödeme hatırlatma', text='Taksit tarihi yaklaşan müşterilere nazik ve kayıtlı hatırlatma yaparız.'),
        dict(icon='users', name='Sıcak aktarım', text='Teklif görüşmesine hazır müşteriyi hat üzerinde yetkili personelinize aktarırız.'),
        dict(icon='star', name='Memnuniyet aramaları', text='Hasar ve poliçe süreçleri sonrası memnuniyeti ölçer, riskli müşteriyi size bildiririz.'),
    ],
    flow_title='Bir yenileme süreci bizde böyle ilerler',
    flow=[
        dict(name='Liste', text='Vadesi yaklaşan poliçeler belirlenen gün sayısı önceden listelenir.'),
        dict(name='Arama', text='Müşteri aranır, poliçe bitişi hatırlatılır, değişen bilgileri sorulur.'),
        dict(name='Bilgi toplama', text='Araç, adres ya da teminat değişiklikleri kayda alınır.'),
        dict(name='Aktarım', text='Teklif için müşteri yetkili teknik personelinize aktarılır ya da randevu verilir.'),
        dict(name='Rapor', text='Ulaşılan, yenilenen ve kaybedilen poliçeler raporlanır.'),
    ],
    qa=[
        dict(q='Poliçe yenileme aramaları neden kritik?', p=[
            'Poliçe bitiş tarihi geçtiğinde ya da müşteriye zamanında ulaşılmadığında müşteri başka bir acenteye ya da doğrudan sigorta şirketine yönelebilir. Düzenli ve zamanında yapılan yenileme araması, mevcut portföyünüzü korumanın en etkili yoludur.',
            'Yenileme görüşmesi aynı zamanda müşterinin değişen ihtiyaçlarını öğrenmek için de fırsattır: yeni araç, yeni konut ya da aile sağlık sigortası gibi.']),
        dict(q='Çağrı merkezi temsilcileri poliçe satabilir mi?', p=[
            'Sigorta teklifinin sunulması ve sözleşmenin kurulması, mevzuat gereği yetkili kişilerce yapılmalıdır. Bu nedenle temsilcilerimiz poliçe satmaz; müşteriyi karşılar, bilgileri toplar, randevu verir ve teklif için yetkili teknik personelinize aktarır.',
            'Bu yapı hem mevzuata uygun çalışmanızı sağlar hem de teknik personelinizin zamanını gerçekten satışa dönüşecek görüşmelere ayırır.']),
        dict(q='Hasar anında müşteri nasıl karşılanır?', p=[
            'Hasar anında arayan müşteri genellikle streslidir. Temsilcilerimiz sakin ve net bir dille karşılar, ilk bilgileri kaydeder, izlenecek adımları anlatır ve dosyayı ilgili birime iletir.']),
    ],
    law=dict(title='Yetkiye uygun çalışma', text='Poliçe teklifi ve satışı acentenizin yetkili teknik personelinde kalır. Tanıtım aramaları yalnızca İYS onayı bulunan müşterilere yapılır; kişisel veriler KVKK\'ya uygun işlenir.'),
    why=['Portföy kaybını azaltan yenileme takibi', 'Mevzuata uygun görev ayrımı', 'Her görüşme kayıtlı', 'Satışta kanıtlanmış ekip'],
    faq_title='Sigorta çağrı merkezi hakkında',
    faq=[
        dict(q='Yenileme araması poliçe bitişinden ne kadar önce yapılmalı?', a='Branşa göre değişmekle birlikte bitişten birkaç hafta önce başlayıp bitişe yakın bir teyit aramasıyla tamamlanan bir plan öneriyoruz. Takvimi birlikte belirleriz.'),
        dict(q='Acente yazılımımızı kullanabilir misiniz?', a='Evet. Yetkili kullanıcı erişimiyle ya da düzenli liste paylaşımıyla çalışabiliriz.'),
        dict(q='Brokerler için de çalışıyor musunuz?', a='Evet. Kurumsal müşteri portföyü olan brokerler için yenileme takibi ve bilgi toplama aramaları yapıyoruz.'),
        dict(q='Görüşmeler kaydediliyor mu?', a='Evet. Tüm görüşmeler kayıt altına alınır ve veri işleme sözleşmesi kapsamında size açıktır.'),
        dict(q='Ne kadar sürede başlarız?', a='Standart kurulum ve temsilci eğitimi 10 iş gününde tamamlanır.'),
    ],
    related=[dict(url='/hizmetler/dis-arama-ve-telesatis/', name='Dış arama ve telesatış'), dict(url='/hizmetler/lead-ve-talep-yonetimi/', name='Teklif talebi geri arama'), dict(url='/hizmetler/gelen-cagri-yonetimi/', name='Gelen çağrı yönetimi'), FIYAT, TEKLIF],
    cta_title='Portföyünüzdeki hiçbir yenileme kaçmasın.', cta_text='Aylık yenileme ve teklif talebi sayınızı paylaşın; çalışma planımızı ve teklifimizi iletelim.')),

# ---------------------------------------------------------------- Emlak
dict(path='/sektorler/gayrimenkul/emlak-ve-konut-projesi-cagri-merkezi/', name='Emlak ve konut projesi çağrı merkezi', sector='Gayrimenkul',
     og_image='temsilci-ofis', audience='Konut projeleri ve emlak ofisleri',
     title='Emlak ve Konut Projesi Çağrı Merkezi | Karelima',
     description='İlan ve proje taleplerini aynı gün arıyor, ön eleme yapıp satış ofisi ve örnek daire randevusu veriyoruz. Lansman dönemlerinde ek kapasite.',
     d=dict(
    eyebrow='Sektörler · Gayrimenkul', h1='Emlak ofisleri ve konut projeleri için çağrı merkezi',
    answer='Karelima; konut projeleri ve emlak ofislerine ilan, reklam ve web sitesinden gelen talepleri saniyeler içinde arar. Bütçe, oda sayısı ve zamanlama gibi sorularla ön eleme yapar, satış ofisi ya da örnek daire ziyareti için randevu verir. Pazarlık ve aracılık satış danışmanlarınızda kalır; biz talebi sıcak tutarız.',
    facts=['Saniyeler içinde arama', 'Ön eleme', 'Satış ofisi randevusu', 'Lansman kapasitesi'],
    illus='illus/emlak.svg',
    tasks_title='Gayrimenkulde üstlendiğimiz işler', tasks_sub='Satış danışmanlarınız ziyaretçiye ve kapanışa odaklanırken ilk temas bizde.',
    tasks=[
        dict(icon='phone', name='İlan ve proje talebi arama', text='İlan sitelerinden, reklamlardan ve web sitenizden gelen talepleri hemen ararız.'),
        dict(icon='doc', name='Ön eleme', text='Bütçe, oda sayısı, kullanım amacı, kredi ihtiyacı ve zamanlamayı sorar, talebi etiketleriz.'),
        dict(icon='cal', name='Satış ofisi ve örnek daire randevusu', text='Uygun müşteriler için ziyaret randevusu verir, bir gün önce teyit alırız.'),
        dict(icon='clock', name='Takip aramaları', text='Karar aşamasındaki müşteriyi belirlenen aralıklarla arar, yeni gelişmeleri iletiriz.'),
        dict(icon='users', name='Lansman dönemi kapasite', text='Proje lansmanında artan çağrı ve talep hacmine göre ekibi büyütürüz.'),
        dict(icon='chart', name='Kaynak bazlı rapor', text='Hangi ilan ya da reklamdan gelen talebin ziyarete ve satışa döndüğünü raporlarız.'),
    ],
    flow_title='Bir proje talebi bizde böyle ilerler',
    flow=[
        dict(name='Talep gelir', text='İlan, reklam ya da web formu talebi Karelima CRM\'e düşer.'),
        dict(name='Hızlı arama', text='Kişi saniyeler içinde aranır, proje hakkında temel bilgi verilir.'),
        dict(name='Ön eleme', text='Bütçe ve ihtiyaç soruları sorulur, uygunluk belirlenir.'),
        dict(name='Randevu', text='Uygun müşteriye satış ofisi ya da örnek daire randevusu verilir.'),
        dict(name='Takip ve rapor', text='Ziyaret sonrası takip yapılır; sonuçlar kaynak bazında raporlanır.'),
    ],
    qa=[
        dict(q='Konut projesi taleplerini kim aramalı?', p=[
            'Satış danışmanlarınız zamanlarını ziyaretçilere ve kapanış görüşmelerine ayırdığında en verimli çalışır. Reklam ve ilanlardan gelen her talebi tek tek aramak ise yoğun dönemlerde gecikmeye neden olur.',
            'İlk aramayı ve ön elemeyi bizim yapmamız, danışmanlarınızın yalnızca ziyarete gelecek ve bütçesi uygun müşterilerle görüşmesini sağlar.']),
        dict(q='Ön eleme hangi sorularla yapılır?', p=[
            'Genellikle bütçe aralığı, oda sayısı, oturum ya da yatırım amacı, kredi kullanımı ve satın alma zamanı sorulur. Soru setini projenize göre birlikte belirleriz; soruların kısa ve rahatsız etmeyen bir dille sorulmasına dikkat ederiz.']),
        dict(q='Lansman döneminde hat nasıl yönetilir?', p=[
            'Lansman haftalarında çağrı ve talep hacmi birkaç katına çıkabilir. Ek temsilciler lansmandan önce projeye göre eğitilir; böylece reklam bütçesiyle gelen hiçbir talep beklemez.']),
    ],
    law=dict(title='Görev ayrımı ve izin', text='Temsilcilerimiz pazarlık ya da aracılık yapmaz; satış ve sözleşme süreçleri danışmanlarınızda kalır. Tanıtım aramaları yalnızca talep bırakan ya da İYS onayı bulunan kişilere yapılır.'),
    why=['Talebe saniyeler içinde dönüş', 'Danışman zamanını koruyan ön eleme', 'Lansmanda esnek kapasite', 'Kaynak bazlı sonuç raporu'],
    faq_title='Emlak çağrı merkezi hakkında',
    faq=[
        dict(q='Emlak ofisleri için de uygun mu?', a='Evet. Tek ofisli emlak firmaları için ilan taleplerini karşılama ve randevu verme hizmetini paylaşımlı ekip modeliyle sunuyoruz.'),
        dict(q='Birden fazla proje için çalışabilir misiniz?', a='Evet. Talepleri proje bazında ayırır, her projenin satış ofisine ayrı randevu veririz.'),
        dict(q='Temsilciler fiyat bilgisi veriyor mu?', a='Hangi bilgilerin telefonda paylaşılacağını siz belirlersiniz; fiyat ve ödeme planı sorularını kurallarınıza göre yanıtlar ya da danışmanınıza aktarırız.'),
        dict(q='Ziyarete gelmeyen müşteri ne oluyor?', a='Gelmeyen müşteri aranır, yeni bir ziyaret saati önerilir ve sonuç raporunuza işlenir.'),
        dict(q='Ne kadar sürede başlarız?', a='Proje bilgileri ve konuşma akışı hazırlandıktan sonra kurulum 10 iş gününde tamamlanır.'),
    ],
    related=[dict(url='/hizmetler/lead-ve-talep-yonetimi/', name='Lead ve talep yönetimi'), dict(url='/hizmetler/randevu-ve-rezervasyon-yonetimi/', name='Randevu yönetimi'), dict(url='/hizmetler/dis-arama-ve-telesatis/', name='Dış arama'), FIYAT, TEKLIF],
    cta_title='Proje taleplerinizi aynı gün ziyarete çevirelim.', cta_text='Proje sayınızı ve aylık talep hacminizi paylaşın; çalışma planımızı ve teklifimizi iletelim.')),

# ---------------------------------------------------------------- Otel
dict(path='/sektorler/turizm-ve-otelcilik/otel-rezervasyon-cagri-merkezi/', name='Otel rezervasyon çağrı merkezi', sector='Turizm ve otelcilik',
     og_image='temsilci-ofis', audience='Oteller, acenteler ve tur operatörleri',
     title='Otel Rezervasyon Çağrı Merkezi ve 7/24 Hat | Karelima',
     description='Otelinizin rezervasyon hattını 7/24 karşılıyoruz: rezervasyon, değişiklik, erken rezervasyon, konaklama öncesi teyit ve memnuniyet aramaları.',
     d=dict(
    eyebrow='Sektörler · Turizm ve otelcilik', h1='Oteller için rezervasyon çağrı merkezi ve 7/24 rezervasyon hattı',
    answer='Karelima, otellerin rezervasyon hattını 7/24 karşılar. Rezervasyonu otel yönetim sisteminize işler, değişiklik ve iptal taleplerini yönetir, erken rezervasyon dönemlerinde dış arama yapar, konaklama öncesi teyit ve sonrasında memnuniyet aramalarıyla misafirle bağı güçlü tutar.',
    facts=['7/24 rezervasyon hattı', 'Doğrudan rezervasyon', 'Konaklama öncesi teyit', 'Sezon kapasitesi'],
    illus='illus/otel.svg',
    tasks_title='Otel rezervasyon hattında üstlendiğimiz işler', tasks_sub='Ön büro ekibiniz misafire odaklanırken telefon ve mesajlar bizde.',
    tasks=[
        dict(icon='cal', name='Rezervasyon alma', text='Oda tipi, tarih ve konsepte göre müsaitliği kontrol eder, rezervasyonu sisteminize işleriz.'),
        dict(icon='in', name='Değişiklik ve iptal', text='Tarih değişikliği ve iptal taleplerini iptal politikanıza göre yönetiriz.'),
        dict(icon='out', name='Erken rezervasyon aramaları', text='Önceki misafirlerinizden izinli olanları erken rezervasyon dönemlerinde ararız.'),
        dict(icon='clock', name='Konaklama öncesi teyit', text='Giriş tarihinden önce misafiri arar, varış saati ve özel taleplerini alırız.'),
        dict(icon='users', name='Grup ve etkinlik talepleri', text='Grup, toplantı ve düğün taleplerinin ilk bilgilerini toplar, satış ekibinize iletiriz.'),
        dict(icon='star', name='Konaklama sonrası memnuniyet', text='Misafir deneyimini ölçer, olumsuz geri bildirimi aynı gün size iletiriz.'),
    ],
    flow_title='Bir rezervasyon talebi bizde böyle ilerler',
    flow=[
        dict(name='Arama karşılanır', text='Misafir, otelinizin adıyla 7/24 karşılanır.'),
        dict(name='Müsaitlik', text='Tarih, oda tipi ve kişi sayısına göre müsaitlik ve fiyat kontrol edilir.'),
        dict(name='Rezervasyon', text='Rezervasyon sisteminize işlenir, misafire teyit iletilir.'),
        dict(name='Teyit', text='Konaklamadan önce misafir aranır, varış ve özel talepler alınır.'),
        dict(name='Memnuniyet', text='Konaklama sonrası memnuniyet sorulur, sonuçlar raporlanır.'),
    ],
    qa=[
        dict(q='Rezervasyon hattını dışarıya vermek doğrudan satışı nasıl etkiler?', p=[
            'Telefonla arayan misafir genellikle rezervasyon yapmaya hazırdır. Hat meşgul çaldığında ya da gece cevap verilmediğinde misafir çoğunlukla çevrim içi seyahat acentelerine yönelir ve satış komisyonlu kanala kayar.',
            '7/24 açık ve hızlı cevap veren bir rezervasyon hattı, bu misafirlerin doğrudan rezervasyon yapmasına yardımcı olur.']),
        dict(q='Hangi otel yazılımlarıyla çalışabilirsiniz?', p=[
            'Temsilcilerimiz otel yönetim sisteminize (PMS) ve kanal yöneticinize yetkili kullanıcı olarak erişebilir. Fiyat, kontenjan ve iptal kurallarınız konuşma akışına eklenir; rezervasyon doğrudan sisteminize işlenir.']),
        dict(q='Sezon yoğunluğu nasıl karşılanır?', p=[
            'Erken rezervasyon kampanyaları ve yaz sezonu gibi yoğun dönemlerde ekibi hacme göre büyütürüz. Ek temsilciler sezon öncesinde otelinize ve konseptinize göre eğitilir.']),
        dict(q='Yabancı misafirler için hizmet veriyor musunuz?', p=[
            'Ekibimiz şu anda Türkçe hizmet veriyor. Yabancı dil ihtiyacınızı keşif görüşmesinde konuşalım; projenin kapsamına göre çözüm üretebiliriz.']),
    ],
    why=['7/24 açık rezervasyon hattı', 'Doğrudan rezervasyona destek', 'Sezonda esnek kapasite', 'Sisteminize doğrudan kayıt'],
    faq_title='Otel rezervasyon çağrı merkezi hakkında',
    faq=[
        dict(q='Birden fazla otel için tek hat kurabilir misiniz?', a='Evet. Otel grupları için tek bir rezervasyon hattı kurar, çağrıyı ilgili otele göre yönetiriz.'),
        dict(q='Acente ve tur operatörleriyle de çalışıyor musunuz?', a='Evet. Tur bilgilendirme, rezervasyon ve konaklama öncesi teyit aramalarını acenteler için de yürütüyoruz.'),
        dict(q='Ödeme alıyor musunuz?', a='Kart bilgisi telefonda alınmaz. Ödeme, otelinizin güvenli ödeme bağlantısı ya da tanımlı yöntemleriyle tamamlanır.'),
        dict(q='Sadece gece hattı için hizmet alabilir miyiz?', a='Evet. Yalnızca gece, hafta sonu ya da yoğun saatler için hizmet alabilirsiniz.'),
        dict(q='Ne kadar sürede başlarız?', a='Sistem erişimleri ve konuşma akışı hazırlandıktan sonra kurulum 10 iş gününde tamamlanır.'),
    ],
    related=[dict(url='/hizmetler/randevu-ve-rezervasyon-yonetimi/', name='Randevu ve rezervasyon yönetimi'), dict(url='/hizmetler/sanal-sekreter-ve-cagri-karsilama/', name='Mesai dışı çağrı karşılama'), dict(url='/hizmetler/memnuniyet-ve-anket-aramalari/', name='Misafir memnuniyeti'), FIYAT, TEKLIF],
    cta_title='Rezervasyon hattınız sezon boyunca açık kalsın.', cta_text='Oda sayınızı, sezon takviminizi ve kullandığınız sistemi paylaşın; teklifimizi iletelim.')),
]

# ---------------------------------------------------------------- Rehber: Fiyatlar
PAGE_FIYAT = dict(path='/rehber/cagri-merkezi-hizmeti-fiyatlari/', name='Çağrı merkezi hizmeti fiyatları',
     og_image='operasyon-merkezi',
     title='Çağrı Merkezi Hizmeti Fiyatları ve Maliyet Rehberi | Karelima',
     description='Çağrı merkezi hizmeti nasıl fiyatlandırılır? Temsilci başı, çağrı başı ve sonuç bazlı modeller, maliyeti belirleyen 8 unsur ve kendi ekibinizle karşılaştırma.',
     d=dict(
    eyebrow='Rehber · Fiyatlandırma', h1='Çağrı merkezi hizmeti fiyatları: maliyeti belirleyen 8 unsur',
    answer='Çağrı merkezi hizmeti tek bir liste fiyatıyla satılmaz; fiyat çalışma saatleri, çağrı hacmi, görüşme süresi, hizmet seviyesi hedefi ve ekip modeline göre hesaplanır. Bu rehberde fiyatlandırma modellerini, maliyeti etkileyen unsurları ve kendi çağrı merkezinizi kurmakla dış kaynak kullanmak arasındaki farkı anlatıyoruz.',
    facts=['Temsilci başı', 'Çağrı ya da dakika başı', 'Saatlik ve proje bazlı', 'Sonuç bazlı karma'],
    illus='illus/fiyat.svg',
    tasks_title='Fiyatı belirleyen 8 unsur', tasks_sub='Teklif hazırlarken bu soruların cevaplarına bakarız. Cevapları önceden hazırlamanız teklif sürecini kısaltır.',
    tasks=[
        dict(icon='clock', name='1. Çalışma saatleri', text='Mesai saatleri, uzatılmış saatler ya da 7/24. Gece ve hafta sonu vardiyaları gereken kişi sayısını artırır.'),
        dict(icon='chart', name='2. Aylık hacim ve dağılımı', text='Toplam çağrı sayısı kadar, çağrıların gün ve saatlere nasıl dağıldığı da önemlidir.'),
        dict(icon='phone', name='3. Ortalama görüşme süresi', text='Kısa bilgi çağrıları ile uzun satış ya da destek görüşmeleri farklı kapasite gerektirir.'),
        dict(icon='star', name='4. Hizmet seviyesi hedefi', text='Örneğin çağrıların belirli bir yüzdesinin kaç saniyede açılacağı hedefi, ekip büyüklüğünü doğrudan belirler.'),
        dict(icon='chat', name='5. Kanal sayısı', text='Yalnızca telefon mu, yoksa WhatsApp, e-posta ve canlı destek de mi?'),
        dict(icon='users', name='6. Ekip modeli', text='Yalnızca size ayrılmış bir ekip mi, yoksa paylaşımlı bir ekip mi?'),
        dict(icon='doc', name='7. Entegrasyon ve raporlama', text='Sistemlerinize erişim, API entegrasyonu ve özel rapor ihtiyaçları kurulum kapsamını etkiler.'),
        dict(icon='cal', name='8. Süre ve dönemsellik', text='Sürekli bir hizmet mi, yoksa kampanya ya da sezon dönemine özel bir proje mi?'),
    ],
    table=dict(title='Çağrı merkezi fiyatlandırma modelleri', head=['Model', 'Nasıl hesaplanır?', 'Kimler için uygun?'], rows=[
        ['Size ayrılmış ekip', 'Temsilci başına aylık sabit ücret', 'Düzenli ve yüksek hacimli gelen ya da giden çağrı'],
        ['Paylaşımlı ekip', 'Çağrı ya da dakika başına ücret', 'Düşük veya değişken hacim, mesai dışı ve taşma desteği'],
        ['Saatlik ya da proje bazlı', 'Saat başı ücret veya dönemsel paket', 'Kampanya, lansman ve sezon dönemleri'],
        ['Sonuç bazlı karma model', 'Sabit ücret + randevu ya da satış başına prim', 'Telesatış, lead ve randevu projeleri'],
    ]),
    flow_title='Teklifiniz nasıl hazırlanır?',
    flow=[
        dict(name='Keşif görüşmesi', text='İşinizi, hedeflerinizi ve mevcut çağrı akışınızı dinleriz.'),
        dict(name='Hacim analizi', text='Çağrı sayısı, saat dağılımı ve görüşme süreleri incelenir.'),
        dict(name='Model önerisi', text='Size uygun ekip ve fiyat modeli belirlenir.'),
        dict(name='Yazılı teklif', text='Kapsam, hizmet seviyesi hedefleri ve fiyat yazılı olarak iletilir.'),
        dict(name='Pilot', text='İsterseniz sınırlı hacimle başlar, sonuçlara göre ölçeklendiririz.'),
    ],
    qa=[
        dict(q='Kendi çağrı merkezini kurmak mı, dış kaynak mı daha ekonomik?', p=[
            'Kendi çağrı merkezinizi kurduğunuzda maaş ve SGK işveren payının yanında takım lideri ve kalite personeli, santral ve çağrı merkezi yazılımı lisansları, hat ve donanım, ofis alanı, işe alım ve eğitim maliyetleri de oluşur. Personel değişimi yüksek olduğu için eğitim maliyeti sürekli tekrar eder.',
            '7/24 açık tek bir temsilci koltuğu için vardiya, izin ve molalar hesaba katıldığında en az 4-5 kişilik bir kadro gerekir. Dış kaynakta bu kadro, altyapı ve yönetim çağrı merkezi firmasına aittir; siz yalnızca ihtiyaç duyduğunuz kapasite ve hizmet seviyesi için ödeme yaparsınız.',
            'Çok yüksek ve çok özel bilgi gerektiren hacimlerde kendi ekip mantıklı olabilir. Değişken hacim, mesai dışı ihtiyaç ve hızlı başlangıç istendiğinde dış kaynak genellikle daha ekonomiktir.']),
        dict(q='Fiyat teklifi almak için hangi bilgiler gerekli?', p=[
            'Aylık tahmini çağrı ya da talep sayısı, çalışma saatleri, hizmet vermek istediğiniz kanallar, görüşmelerin konusu ve ortalama süresi, kullandığınız sistemler ve başlamak istediğiniz tarih. Bilmediğiniz bilgileri keşif görüşmesinde birlikte tahmin ederiz.']),
        dict(q='Pilot dönem neden önemli?', p=[
            'Pilot dönem, gerçek çağrılarla ortalama görüşme süresini, ulaşılabilirliği ve dönüşüm oranlarını ölçmenizi sağlar. Bu veriler, uzun dönemli ekip büyüklüğünün ve fiyatın doğru belirlenmesine yardımcı olur.']),
    ],
    why=['Şeffaf fiyat modeli', 'Taahhütsüz ilk görüşme', 'Pilot dönemle başlama imkânı', 'Kurulum 10 iş gününde'],
    faq_title='Çağrı merkezi fiyatları hakkında',
    faq=[
        dict(q='Çağrı merkezi hizmeti fiyatları neden sitede yazmıyor?', a='Çünkü fiyat; çalışma saatleri, hacim, görüşme süresi ve hizmet seviyesi hedefine göre her projede farklı hesaplanır. Keşif görüşmesinin ardından yazılı teklif sunuyoruz.'),
        dict(q='En ekonomik başlangıç modeli hangisi?', a='Düşük ve değişken hacimde çağrı ya da dakika başı ücretlendirilen paylaşımlı ekip modeli genellikle en ekonomik başlangıçtır.'),
        dict(q='Kurulum için ayrıca ücret var mı?', a='Kurulum kapsamı projeye göre değişir. Varsa kurulum bedeli teklifte ayrıca ve açıkça belirtilir.'),
        dict(q='Minimum sözleşme süresi var mı?', a='Projeye göre belirlenir. Pilot dönemle başlayıp sonuçlara göre devam etmek mümkündür.'),
        dict(q='Teklif ne kadar sürede hazırlanır?', a='Gerekli bilgiler paylaşıldıktan sonra yazılı teklifi kısa sürede iletiyoruz.'),
    ],
    related=[dict(url='/hizmetler/', name='Hizmetler'), dict(url='/hizmetler/sanal-sekreter-ve-cagri-karsilama/', name='Sanal sekreter'), dict(url='/hizmetler/gelen-cagri-yonetimi/', name='Gelen çağrı yönetimi'), dict(url='/hizmetler/dis-arama-ve-telesatis/', name='Telesatış'), TEKLIF],
    cta_title='Size özel fiyatı birlikte hesaplayalım.', cta_text='Çağrı hacminizi ve çalışma saatlerinizi paylaşın; ekip, süre ve fiyat önerimizi yazılı olarak iletelim.'))
