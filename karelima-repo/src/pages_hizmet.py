# -*- coding: utf-8 -*-
"""Hizmet sayfaları. Her sayfa: yol, SEO başlığı/açıklaması ve detail.html içeriği (d)."""

H = '/hizmetler/'
FIYAT = dict(url='/rehber/cagri-merkezi-hizmeti-fiyatlari/', name='Çağrı merkezi hizmeti fiyatları')
TEKLIF = dict(url='/teklif-al/', name='Teklif alın')

PAGES_HIZMET = [
# ---------------------------------------------------------------- Randevu
dict(path=H + 'randevu-ve-rezervasyon-yonetimi/', name='Randevu ve rezervasyon yönetimi', og_image='temsilci-ofis',
     title='Randevu Çağrı Merkezi ve Randevu Yönetimi Hizmeti | Karelima',
     description='Randevu alma, hatırlatma, teyit ve iptal yönetimi tek ekipte. Klinik, bayi, servis, okul ve oteller için 7/24 randevu hattı; kurulum 10 iş günü.',
     audience='Randevu ve rezervasyonla çalışan işletmeler',
     d=dict(
    eyebrow='Hizmetler · Randevu ve rezervasyon', h1='Randevu çağrı merkezi: randevu alma, hatırlatma ve teyit tek ekipte',
    answer='Karelima; klinik, bayi, servis, okul ve otel gibi randevuyla çalışan işletmelerin telefon, WhatsApp ve web formundan gelen randevu taleplerini 7/24 karşılar. Randevuyu sizin sisteminize işler, bir gün önce hatırlatma araması ya da mesajıyla teyit alır, gelemeyecek kişiye yeni saat verir.',
    facts=['7/24 randevu hattı', 'Hatırlatma ve teyit', 'Sisteminize doğrudan kayıt', 'Kurulum 10 iş günü'],
    illus='illus/randevu.svg',
    tasks_title='Randevu hattında üstlendiğimiz işler', tasks_sub='Randevunun alınmasından gerçekleşmesine kadar her adım tek ekipte ve tek kayıtta.',
    tasks=[
        dict(icon='cal', name='Randevu alma', text='Telefon, WhatsApp ve web formundan gelen talepleri karşılar, uygun saati bulup randevuyu takviminize işleriz.'),
        dict(icon='clock', name='Hatırlatma ve teyit', text='Randevudan önce arama ya da mesajla hatırlatma yapar, katılımı teyit ederiz.'),
        dict(icon='in', name='Değişiklik ve iptal', text='Saat değişikliği ve iptal taleplerini anında işler, boşalan saati yeniden kullanıma açarız.'),
        dict(icon='users', name='Gelmeyenleri yeniden planlama', text='Randevusuna gelmeyen kişiyi arar, yeni bir saat önerir ve takvime geri kazandırırız.'),
        dict(icon='doc', name='Bekleme listesi', text='Dolu günler için bekleme listesi tutar, iptal olan saatleri sıradaki kişiye veririz.'),
        dict(icon='chart', name='Doluluk raporu', text='Alınan, iptal edilen ve gerçekleşmeyen randevuları düzenli olarak raporlarız.'),
    ],
    flow_title='Bir randevu talebi bizde böyle ilerler',
    flow=[
        dict(name='Talep gelir', text='Arama, WhatsApp mesajı ya da web formu Karelima CRM\'e düşer.'),
        dict(name='Uygun saat bulunur', text='Takviminize ya da randevu sisteminize bakılarak kişiye seçenek sunulur.'),
        dict(name='Randevu işlenir', text='Randevu sisteminize kaydedilir; kişiye SMS ya da e-posta ile teyit gider.'),
        dict(name='Hatırlatılır', text='Randevudan önce hatırlatma yapılır; gelemeyecekse yeni saat verilir.'),
        dict(name='Raporlanır', text='Doluluk, iptal ve gelmeme oranları raporunuza yansır.'),
    ],
    qa=[
        dict(q='Randevu yönetimini dış kaynağa vermek kimler için uygun?', p=[
            'Günde onlarca randevu talebi alan, telefonu sık meşgul çalan ya da resepsiyon ekibi hem yüz yüze hem telefonda hizmet vermeye yetişemeyen işletmeler için uygundur. Klinikler, otomotiv bayileri ve servisler, güzellik merkezleri, eğitim kurumları ve oteller en sık çalıştığımız gruplardır.',
            'Randevu hattını devrettiğinizde ekibiniz yüz yüze hizmete odaklanır; telefondaki talepler ise eğitimli temsilcilerimiz tarafından aynı kalitede karşılanır.']),
        dict(q='Randevuya gelmeme oranı hatırlatma aramasıyla nasıl düşer?', p=[
            'Gelmeyen her randevu, başka birine verilebilecek boş bir saat demektir. Randevudan önce yapılan hatırlatma, kişinin gelemeyeceğini önceden öğrenmenizi sağlar.',
            'Boşalan saat bekleme listesindeki kişiye verilir; böylece takviminiz dolu kalır. Hatırlatmanın kaç saat önce, arama mı mesaj mı olacağını sizin işleyişinize göre birlikte belirleriz.']),
        dict(q='Hangi randevu sistemleriyle çalışabilirsiniz?', p=[
            'Temsilcilerimiz kullandığınız randevu yazılımına, klinik ya da bayi sistemine, otel rezervasyon programına veya Google ve Outlook takvimine yetkili kullanıcı olarak erişebilir. Gerekirse API ile entegrasyon kurarız.',
            'Henüz bir sisteminiz yoksa randevular Karelima CRM\'de tutulur ve size günlük liste olarak iletilir.']),
        dict(q='Randevu hattının maliyeti nasıl belirlenir?', p=[
            'Maliyeti çalışma saatleri, aylık talep sayısı, hatırlatma araması yapılıp yapılmayacağı ve ekip modeli belirler. Ayrıntılı bilgi için çağrı merkezi hizmeti fiyatları rehberimize göz atabilirsiniz.']),
    ],
    why=['7/24 randevu karşılama', 'Hatırlatma ile daha az boş saat', 'Sisteminize doğrudan kayıt', 'Kurulum 10 iş gününde'],
    faq_title='Randevu yönetimi hakkında',
    faq=[
        dict(q='Randevu hatırlatması arama ile mi, mesajla mı yapılıyor?', a='İkisi de mümkün. Önemli ya da uzun süreli randevularda arama, rutin randevularda SMS veya WhatsApp mesajı öneririz. Yöntemi birlikte belirleriz.'),
        dict(q='Kendi randevu yazılımımızı kullanabilir misiniz?', a='Evet. Temsilcilerimiz sisteminize yetkili kullanıcı olarak girer ya da API ile entegrasyon kurarız.'),
        dict(q='Rezervasyon (otel, restoran, etkinlik) için de çalışıyor musunuz?', a='Evet. Rezervasyon alma, değişiklik, iptal ve teyit süreçlerini aynı yöntemle yönetiyoruz.'),
        dict(q='Mesai dışında gelen randevu talepleri ne oluyor?', a='7/24 çalıştığımız için gece ve hafta sonu gelen talepler de karşılanır; randevu ilk uygun saate planlanır.'),
        dict(q='Ne kadar sürede başlayabiliriz?', a='Standart bir randevu hattı için kurulum ve temsilci eğitimi 10 iş gününde tamamlanır.'),
    ],
    related=[dict(url='/sektorler/saglik/klinik-ve-dis-hekimligi-cagri-merkezi/', name='Klinik randevu hattı'), dict(url='/sektorler/otomotiv/bayi-ve-servis-cagri-merkezi/', name='Bayi ve servis randevuları'), dict(url='/sektorler/turizm-ve-otelcilik/otel-rezervasyon-cagri-merkezi/', name='Otel rezervasyon hattı'), dict(url='/hizmetler/sanal-sekreter-ve-cagri-karsilama/', name='Sanal sekreter'), FIYAT, TEKLIF],
    cta_title='Randevu hattınızı 10 iş gününde devralalım.', cta_text='Günlük randevu sayınızı ve kullandığınız sistemi paylaşın; ekip ve fiyat önerimizi yazılı olarak iletelim.')),

# ---------------------------------------------------------------- Telesatış
dict(path=H + 'dis-arama-ve-telesatis/', name='Dış arama ve telesatış', og_image='operasyon-merkezi',
     title='Telesatış ve Dış Arama (Outbound) Hizmeti | Karelima',
     description='Kampanya duyurusu, yenileme, çapraz satış ve geri kazanım aramaları. İYS ve KVKK uyumlu dış arama, her görüşme kayıtlı, günlük sonuç raporu.',
     audience='Satış ve kampanya ekipleri olan firmalar',
     d=dict(
    eyebrow='Hizmetler · Dış arama ve telesatış', h1='Telesatış ve dış arama: doğru kişiye, doğru zamanda, kurallara uygun',
    answer='Karelima; kampanya duyurusu, abonelik yenileme, çapraz satış, toplantı ayarlama ve kayıp müşteri geri kazanımı için dış arama (outbound) projeleri yürütür. Aramalar İYS ve KVKK kurallarına uygun listelerle yapılır, her görüşme kaydedilir ve sonuçlar günlük raporlanır. Telekom iş ortaklarımız için yüksek hacimli abonelik satışını her gün kendi ekibimizle yapıyoruz.',
    facts=['Günlük sonuç raporu', 'İYS ve KVKK uyumlu', 'Her görüşme kayıtlı', 'Telekomda kanıtlanmış satış'],
    illus='illus/telesatis.svg',
    tasks_title='Dış arama projelerinde üstlendiğimiz işler', tasks_sub='Satış hedefinize göre tek bir kampanya ya da sürekli bir telesatış ekibi kurabiliriz.',
    tasks=[
        dict(icon='out', name='Kampanya ve lansman duyurusu', text='Yeni ürün, kampanya ya da lansmanı izinli müşterilerinize telefonla duyurur, ilgilenenleri satışa ya da randevuya bağlarız.'),
        dict(icon='clock', name='Yenileme aramaları', text='Abonelik, üyelik ve sözleşme bitişlerinden önce müşterinizi arar, yenilemeyi kolaylaştırırız.'),
        dict(icon='chart', name='Çapraz ve üst satış', text='Mevcut müşterilerinize ihtiyaçlarına uygun tamamlayıcı ürün ya da üst paket öneririz.'),
        dict(icon='cal', name='Toplantı ve demo ayarlama', text='B2B projelerde karar vericiye ulaşır, satış ekibiniz için toplantı ya da demo ayarlarız.'),
        dict(icon='users', name='Kayıp müşteri geri kazanımı', text='Hizmetinizi bırakan müşterileri arar, ayrılma nedenini öğrenir ve geri dönüş teklifinizi iletiriz.'),
        dict(icon='doc', name='Yarım kalan başvuru ve sepet', text='Başvurusunu ya da siparişini tamamlamayan kişiye ulaşır, işlemi tamamlamasına yardımcı oluruz.'),
    ],
    flow_title='Bir dış arama projesi bizde böyle ilerler',
    flow=[
        dict(name='Hedef ve liste', text='Hedef kitle ve liste birlikte belirlenir; İYS izinleri ve mükerrer kayıtlar kontrol edilir.'),
        dict(name='Konuşma akışı', text='Teklif, sık sorulan sorular ve itiraz yanıtları içeren akış hazırlanır.'),
        dict(name='Pilot', text='Sınırlı hacimle başlanır; görüşmeler birlikte dinlenip akış iyileştirilir.'),
        dict(name='Arama ve kayıt', text='Her arama ve sonucu Karelima CRM\'e işlenir; ret bildiren kişi bir daha aranmaz.'),
        dict(name='Rapor', text='Ulaşılan kişi, satış ve randevu sayıları günlük raporlanır.'),
    ],
    qa=[
        dict(q='Telesatış hizmeti nasıl fiyatlandırılır?', p=[
            'Telesatış projelerinde en sık kullanılan modeller temsilci başına aylık ücret, saatlik ücret ve sabit ücret ile birlikte satış ya da randevu başına prim içeren karma modeldir.',
            'Hangisinin uygun olduğu liste büyüklüğüne, ürünün satış döngüsüne ve hedeflere göre değişir. Keşif görüşmesinin ardından yazılı teklif sunarız.']),
        dict(q='Telesatışta hangi kurallara uyulmalı?', p=[
            '6563 sayılı Kanun ve ilgili yönetmelik uyarınca tüketicilere yapılacak tanıtım ve satış aramaları için İleti Yönetim Sistemi\'nde (İYS) kayıtlı onay gerekir. Tacir ve esnafa önceden onay aranmadan ulaşılabilir; ancak aranmak istemediğini bildiren kişi bir daha aranmaz.',
            'Kişisel veriler KVKK\'ya uygun işlenir. Veri listesi satın almıyor ve satmıyoruz; aramalar sizin izinli müşteri listenizle ya da talep bırakan kişilerle yapılır.']),
        dict(q='Dış arama ile gelen çağrı yönetimi birlikte yürüyebilir mi?', p=[
            'Evet. Aynı ekip sabah gelen hattı karşılarken öğleden sonra kampanya aramalarını yapabilir. Böylece temsilciler ürününüzü her iki yönden de tanır, müşterinize tutarlı bir deneyim sunulur.']),
    ],
    law=dict(title='İYS ve KVKK uyumu', text='Tüketicilere tanıtım amaçlı arama yalnızca İYS\'de onayı bulunan numaralara yapılır. Ret bildirimi anında kaydedilir ve kişi aranmaz. Liste satın alınmaz, satılmaz.'),
    why=['Satışta kanıtlanmış ekip', 'İzinli liste ve ret yönetimi', 'Her görüşme kayıtlı', 'Günlük sonuç raporu'],
    faq_title='Dış arama ve telesatış hakkında',
    faq=[
        dict(q='Arama listesini siz mi sağlıyorsunuz?', a='Hayır. Veri listesi satın almıyor ve satmıyoruz. Aramalar sizin izinli müşteri listenizle ya da form ve kampanyalardan talep bırakan kişilerle yapılır.'),
        dict(q='Günde kaç arama yapılabilir?', a='Liste kalitesine, görüşme süresine ve ulaşılabilirlik oranına göre değişir. Pilot dönemde gerçekleşen sayıları ölçer, hedefleri buna göre birlikte belirleriz.'),
        dict(q='Görüşme kayıtlarını dinleyebilir miyiz?', a='Evet. Veri işleme sözleşmesi kapsamında görüşme kayıtlarına ve raporlara erişebilirsiniz.'),
        dict(q='Satış sözleşmesini kim yapıyor?', a='Satışın nasıl tamamlanacağı sizin süreçlerinize göre belirlenir: telefonda sipariş alınabilir, ödeme linki iletilebilir ya da satış ekibinize sıcak aktarım yapılabilir.'),
        dict(q='Hangi sektörlerde telesatış yapıyorsunuz?', a='Telekom ve abonelik satışında her gün çalışıyoruz. Eğitim, otomotiv, gayrimenkul, sigorta ve e-ticaret projelerinde de dış arama yapıyoruz.'),
    ],
    related=[dict(url='/hizmetler/lead-ve-talep-yonetimi/', name='Lead ve talep yönetimi'), dict(url='/hizmetler/memnuniyet-ve-anket-aramalari/', name='Memnuniyet aramaları'), dict(url='/sektorler/sigorta/sigorta-cagri-merkezi/', name='Sigorta çağrı merkezi'), dict(url='/sektorler/gayrimenkul/emlak-ve-konut-projesi-cagri-merkezi/', name='Emlak çağrı merkezi'), FIYAT, TEKLIF],
    cta_title='Satış hedefinizi konuşalım.', cta_text='Ürününüzü, hedef kitlenizi ve liste büyüklüğünüzü paylaşın; pilot planı ve fiyat önerimizi iletelim.')),

# ---------------------------------------------------------------- Sanal sekreter
dict(path=H + 'sanal-sekreter-ve-cagri-karsilama/', name='Sanal sekreter ve çağrı karşılama', og_image='hero-temsilci',
     title='Sanal Sekreter ve 7/24 Çağrı Karşılama Hizmeti | Karelima',
     description='Telefonlarınız şirketinizin adıyla karşılansın: sanal sekreter, mesaj alma, aktarma ve mesai dışı hat. Numaranız değişmez, 7/24 hizmet.',
     audience='Telefon trafiğini karşılamakta zorlanan işletmeler',
     d=dict(
    eyebrow='Hizmetler · Sanal sekreter', h1='Sanal sekreter ve çağrı karşılama: telefonlarınız şirketinizin adıyla açılsın',
    answer='Karelima\'nın sanal sekreter hizmetinde firmanıza gelen çağrılar, İzmir\'deki ekibimiz tarafından şirketinizin adıyla karşılanır. Arayanın kim olduğu ve ne istediği not alınır, ilgili kişiye aktarılır ya da mesaj olarak anında iletilir. Mesai dışında, öğle arasında ve hat yoğunken hiçbir çağrı cevapsız kalmaz.',
    facts=['7/24 karşılama', 'Şirketinizin adıyla', 'Anında mesaj iletimi', 'Numaranız değişmez'],
    illus='illus/sanal-sekreter.svg',
    tasks_title='Sanal sekreter olarak üstlendiğimiz işler', tasks_sub='Tüm çağrılarınızı ya da yalnızca kaçan, mesai dışı ve yoğun saat çağrılarını devredebilirsiniz.',
    tasks=[
        dict(icon='phone', name='Çağrı karşılama', text='Çağrıyı şirketinizin adıyla, onaylı karşılama cümlesiyle açar ve arayanın ihtiyacını dinleriz.'),
        dict(icon='users', name='Aktarma', text='Belirlediğiniz kurallara göre çağrıyı ilgili kişiye ya da birime aktarırız.'),
        dict(icon='chat', name='Mesaj alma ve iletme', text='Ulaşılamayan kişi için mesajı alır; e-posta, SMS ya da WhatsApp ile anında iletiriz.'),
        dict(icon='moon', name='Mesai dışı hat', text='Gece, hafta sonu ve bayramlarda çağrılarınızı karşılar, acil durumları tanımlı kişiye bildiririz.'),
        dict(icon='in', name='Yoğunluk desteği', text='Hattınız meşgulken ya da çağrı belirli sürede açılmazsa çağrı bize yönlenir.'),
        dict(icon='cal', name='Randevu ve ön bilgi', text='Basit bilgi sorularını yanıtlar, gerekirse görüşme ya da randevu ayarlarız.'),
    ],
    flow_title='Bir çağrı sanal sekreterde böyle ilerler',
    flow=[
        dict(name='Yönlendirme', text='Numaranız değişmez; meşgulde, cevapsızda, mesai dışında ya da tüm gün yönlendirme yapılır.'),
        dict(name='Karşılama', text='Çağrı şirketinizin adıyla açılır.'),
        dict(name='Not alma', text='Arayanın adı, telefonu, konusu ve aciliyeti kaydedilir.'),
        dict(name='Aktarım ya da mesaj', text='Kurallara göre aktarılır ya da mesaj anında iletilir.'),
        dict(name='Günlük özet', text='Gün sonunda tüm çağrıların özeti e-postanıza gelir.'),
    ],
    qa=[
        dict(q='Sanal sekreter nedir, kimler kullanır?', p=[
            'Sanal sekreter, şirketinize gelen telefonların sizin adınıza uzaktaki bir ekip tarafından karşılanmasıdır. Arayan kişi doğrudan şirketinizle konuştuğunu bilir; çağrı not alınır, aktarılır ya da mesaj olarak size iletilir.',
            'Resepsiyon personeli olmayan ya da yetmeyen ofisler, sahada çalışan ekipler, danışmanlık ve hizmet firmaları, tek kişilik telefon hattıyla büyüyen işletmeler en sık kullananlardır.']),
        dict(q='Çağrı yönlendirme nasıl kurulur?', p=[
            'Mevcut numaranızda operatörünüzün ya da santralinizin çağrı yönlendirme özelliği kullanılır. Tüm çağrıları, yalnızca cevapsız kalanları, meşgul olanları ya da mesai dışındakileri yönlendirebilirsiniz.',
            'Kurulumda karşılama cümlesi, aktarım kuralları ve mesajların kime, hangi kanaldan iletileceği belirlenir.']),
        dict(q='Sanal sekreter ile çağrı merkezi arasındaki fark ne?', p=[
            'Sanal sekreter çağrıyı karşılar, yönlendirir ve mesaj alır. Çağrı merkezi hizmetinde ise temsilciler ürününüzü ayrıntılı öğrenir; sipariş, randevu, şikâyet ve satış gibi işlemleri baştan sona yürütür.',
            'İşiniz büyüdükçe sanal sekreterden tam kapsamlı gelen çağrı yönetimine aynı ekip ve aynı kayıtla geçebilirsiniz.']),
    ],
    why=['7/24 aynı kalitede karşılama', 'Numaranız değişmez', 'Mesajlar anında iletilir', 'İhtiyaç büyüdükçe genişleyen kapsam'],
    faq_title='Sanal sekreter hakkında',
    faq=[
        dict(q='Arayan kişi dışarıdan bir ekiple konuştuğunu anlar mı?', a='Çağrılar şirketinizin adıyla ve sizin onayladığınız karşılama cümlesiyle açılır. Temsilciler kurum dilinize göre eğitilir.'),
        dict(q='Mesajları nasıl alacağız?', a='Her mesaj anında e-posta, SMS ya da WhatsApp ile iletilir; gün sonunda tüm çağrıların özeti de ayrıca gönderilir.'),
        dict(q='Sadece mesai dışında çalışabilir misiniz?', a='Evet. Yalnızca mesai dışı, öğle arası ya da yoğun saatler için hizmet alabilirsiniz.'),
        dict(q='Ücret neye göre belirleniyor?', a='Çalışma saatlerine ve aylık çağrı sayısına göre. Düşük hacimde paylaşımlı ekip modeli genellikle en ekonomik seçenektir.'),
        dict(q='Ne zaman başlayabiliriz?', a='Karşılama metni ve aktarım kuralları belirlendikten sonra kurulum 10 iş günü içinde tamamlanır.'),
    ],
    related=[dict(url='/hizmetler/gelen-cagri-yonetimi/', name='Gelen çağrı yönetimi'), dict(url='/hizmetler/randevu-ve-rezervasyon-yonetimi/', name='Randevu yönetimi'), dict(url='/sektorler/saglik/klinik-ve-dis-hekimligi-cagri-merkezi/', name='Klinik çağrı merkezi'), FIYAT, TEKLIF],
    cta_title='Hiçbir çağrınız cevapsız kalmasın.', cta_text='Hangi saatlerde ve ne kadar çağrı aldığınızı paylaşın; size uygun sanal sekreter planını önerelim.')),

# ---------------------------------------------------------------- Memnuniyet
dict(path=H + 'memnuniyet-ve-anket-aramalari/', name='Memnuniyet ve anket aramaları', og_image='ekip-egitim',
     title='Müşteri Memnuniyeti ve Telefon Anketi Hizmeti | Karelima',
     description='Satış ve hizmet sonrası memnuniyet, NPS ve geri bildirim aramaları. Şikâyetler aynı gün iletilir, sonuçlar düzenli raporlanır. 7/24 ekip.',
     audience='Müşteri deneyimini ölçmek isteyen firmalar',
     d=dict(
    eyebrow='Hizmetler · Memnuniyet ve anket', h1='Müşteri memnuniyeti ve telefon anketi aramaları',
    answer='Karelima, hizmet ya da satış sonrası müşterilerinizi arayarak memnuniyet, NPS ve geri bildirim anketleri yapar. Cevapları Karelima CRM\'e işler, şikâyeti olan müşteriyi aynı gün ilgili birime iletir ve sonuçları düzenli olarak raporlar.',
    facts=['Memnuniyet ve NPS', 'Şikâyet aynı gün iletilir', 'Görüşmeler kayıtlı', 'Düzenli trend raporu'],
    illus='illus/anket.svg',
    tasks_title='Anket projelerinde üstlendiğimiz işler', tasks_sub='Soruları birlikte hazırlar, aramaları yapar, sonuçları anlaşılır raporlara dönüştürürüz.',
    tasks=[
        dict(icon='star', name='Satış sonrası memnuniyet', text='Satın alma deneyimini, teslimatı ve beklentilerin karşılanıp karşılanmadığını sorarız.'),
        dict(icon='phone', name='Hizmet ve servis sonrası anket', text='Servis, muayene ya da kurulum sonrası müşterinin görüşünü kısa bir aramayla alırız.'),
        dict(icon='chart', name='NPS ölçümü', text='Müşterinin sizi tavsiye etme olasılığını düzenli ölçer, nedenleriyle birlikte raporlarız.'),
        dict(icon='users', name='Kayıp müşteri araştırması', text='Hizmetinizi bırakan müşterilere ayrılma nedenlerini sorar, tekrar eden sorunları ortaya çıkarırız.'),
        dict(icon='chat', name='Şikâyet yönlendirme', text='Memnun olmayan müşteriyi aynı gün ilgili birime iletir, geri dönüş yapılıp yapılmadığını takip ederiz.'),
        dict(icon='doc', name='Etkinlik ve eğitim geri bildirimi', text='Etkinlik, eğitim ya da lansman sonrası katılımcı görüşlerini toplarız.'),
    ],
    flow_title='Bir anket projesi bizde böyle ilerler',
    flow=[
        dict(name='Soru seti', text='Amaç belirlenir, kısa ve yönlendirmesiz sorular birlikte hazırlanır.'),
        dict(name='Liste', text='Aranacak müşteriler ve arama zamanı (ör. hizmetten 2 gün sonra) belirlenir.'),
        dict(name='Arama', text='Temsilci kendini tanıtır, onay alır ve soruları sorar; satış yapılmaz.'),
        dict(name='Aynı gün aksiyon', text='Şikâyet ve risk taşıyan cevaplar aynı gün size iletilir.'),
        dict(name='Rapor', text='Puanlar, açık uçlu yorumlar ve trendler düzenli raporlanır.'),
    ],
    qa=[
        dict(q='Telefon anketi mi, online anket mi?', p=[
            'Online anketler ucuzdur ancak cevaplama oranı düşüktür ve çoğunlukla çok memnun ya da çok memnuniyetsiz müşteriler yanıt verir. Telefon anketinde cevaplama oranı daha yüksektir; temsilci açık uçlu cevabı netleştirebilir ve şikâyeti anında yakalayabilir.',
            'En iyi sonuç çoğu zaman ikisinin birlikte kullanılmasıyla alınır: geniş kitleye online anket, önemli müşteri gruplarına telefon.']),
        dict(q='Anket aramasında hangi sorular sorulmalı?', p=[
            'Az ve net soru sorulmalıdır. Genellikle bir puan sorusu (memnuniyet ya da tavsiye etme), bir ya da iki konu sorusu ve bir açık uçlu "neyi daha iyi yapabiliriz?" sorusu yeterlidir.',
            'Soruların yönlendirici olmamasına ve görüşmenin birkaç dakikayı geçmemesine dikkat ederiz.']),
        dict(q='Sonuçları nasıl raporluyorsunuz?', p=[
            'Her çağrının sonucu Karelima CRM\'e işlenir. Raporda ulaşılan müşteri sayısı, puan ortalaması, NPS, konu dağılımı ve öne çıkan yorumlar yer alır; dönemler arası değişimi izleyebilirsiniz.']),
    ],
    law=dict(title='Satış yapılmaz', text='Anket aramalarında kampanya ya da satış teklifi sunulmaz. Böylece görüşme bilgi alma amacında kalır ve müşteriniz rahatsız edilmez.'),
    why=['Yüksek cevaplama oranı', 'Şikâyete aynı gün aksiyon', 'Yönlendirmesiz soru seti', 'Anlaşılır trend raporu'],
    faq_title='Memnuniyet ve anket aramaları hakkında',
    faq=[
        dict(q='Bir anket araması ne kadar sürer?', a='Soru sayısına göre değişmekle birlikte birkaç dakikayı geçmemesini öneriyoruz. Kısa anketlerde cevaplama oranı daha yüksektir.'),
        dict(q='NPS nedir?', a='Net Tavsiye Skoru (NPS), müşteriye sizi tavsiye etme olasılığının 0-10 arasında sorulmasıyla hesaplanan bir sadakat ölçüsüdür.'),
        dict(q='Markamızın kendi anket formunu kullanabilir misiniz?', a='Evet. Kendi soru setinizi ve formatınızı kullanabilir, cevapları sisteminize işleyebiliriz.'),
        dict(q='Kimleri arıyorsunuz?', a='Yalnızca sizden hizmet ya da ürün almış müşterilerinizi, sizin ilettiğiniz liste üzerinden ararız.'),
        dict(q='Sonuçları ne sıklıkla alırız?', a='Şikâyetler aynı gün, özet sonuçlar haftalık, ayrıntılı rapor aylık olarak iletilir. Sıklığı birlikte belirleriz.'),
    ],
    related=[dict(url='/sektorler/otomotiv/bayi-ve-servis-cagri-merkezi/', name='Bayi ve servis memnuniyet aramaları'), dict(url='/sektorler/saglik/hastane-cagri-merkezi/', name='Hasta memnuniyeti'), dict(url='/hizmetler/dis-arama-ve-telesatis/', name='Dış arama'), FIYAT, TEKLIF],
    cta_title='Müşterinizin sesini düzenli duyun.', cta_text='Hangi müşteri grubunu, ne sıklıkla dinlemek istediğinizi paylaşın; soru setini ve teklifimizi birlikte hazırlayalım.')),

# ---------------------------------------------------------------- Lead
dict(path=H + 'lead-ve-talep-yonetimi/', name='Lead ve talep yönetimi', og_image='operasyon-merkezi',
     title='Lead Yönetimi ve Form Geri Arama Hizmeti | Karelima',
     description='Web formu, Google ve Meta reklamlarından gelen talepleri saniyeler içinde arıyoruz. Ön eleme, randevu, tekrar deneme ve kampanya bazlı rapor.',
     audience='Reklamla talep toplayan firmalar',
     d=dict(
    eyebrow='Hizmetler · Lead ve talep yönetimi', h1='Lead yönetimi: web formu ve reklam taleplerini saniyeler içinde arıyoruz',
    answer='Web sitenizden, Google ve Meta reklamlarınızdan gelen talepler Karelima CRM\'e düştüğü anda temsilcilerimiz tarafından saniyeler içinde aranır. İhtiyaç netleştirilir, randevu ya da satış görüşmesi planlanır, ulaşılamayan kişi belirli aralıklarla yeniden aranır. Her talebin sonucu raporlanır; hangi kampanyanın satış getirdiğini görürsünüz.',
    facts=['Saniyeler içinde arama', 'Ulaşılamayana tekrar deneme', 'Ön eleme', 'Kampanya bazlı rapor'],
    illus='illus/lead.svg',
    tasks_title='Talep yönetiminde üstlendiğimiz işler', tasks_sub='Reklam bütçenizle gelen her talebin sonuca bağlanması için.',
    tasks=[
        dict(icon='phone', name='Anında geri arama', text='Form ya da reklamdan gelen talep CRM\'e düştüğü anda aranır.'),
        dict(icon='clock', name='Tekrar deneme planı', text='Ulaşılamayan kişi gün içinde farklı saatlerde ve sonraki günlerde yeniden aranır.'),
        dict(icon='doc', name='Ön eleme', text='Bütçe, zaman ve ihtiyaç gibi sorularla talebin niteliği belirlenir.'),
        dict(icon='cal', name='Randevu ve toplantı', text='Nitelikli talep için satış ekibinize randevu ya da görüşme ayarlanır.'),
        dict(icon='users', name='Sıcak aktarım', text='Hemen görüşmek isteyen kişi, hat üzerinde satış danışmanınıza aktarılır.'),
        dict(icon='chart', name='Kampanya bazlı rapor', text='Hangi kaynaktan gelen talebin randevuya ve satışa dönüştüğünü raporlarız.'),
    ],
    flow_title='Bir talep bizde böyle ilerler',
    flow=[
        dict(name='Talep düşer', text='Web formu, reklam formu ya da e-posta talebi entegrasyonla Karelima CRM\'e gelir.'),
        dict(name='Saniyeler içinde arama', text='Sıradaki uygun temsilci kişiyi hemen arar.'),
        dict(name='Ön eleme', text='İhtiyaç, bütçe ve zamanlama sorulur; talep etiketlenir.'),
        dict(name='Randevu ya da aktarım', text='Uygun talep satış ekibinize randevu ya da sıcak aktarımla iletilir.'),
        dict(name='Sonuç raporu', text='Ulaşma, randevu ve satış oranları kampanya bazında raporlanır.'),
    ],
    qa=[
        dict(q='Talebe hızlı dönüş neden bu kadar önemli?', p=[
            'Formu dolduran kişi o an ilgilidir ve büyük olasılıkla başka firmalara da talep bırakmıştır. Dakikalar ve saatler geçtikçe ulaşma şansı azalır; ulaşılsa bile kişi kararını vermiş olabilir.',
            'Bu yüzden talepleri gün sonunda ya da ertesi gün değil, düştüğü anda arıyoruz. Telekom iş ortaklarımız için yürüttüğümüz satış operasyonunda bu disiplini her gün uyguluyoruz.']),
        dict(q='Hangi kaynaklardan gelen talepleri alabilirsiniz?', p=[
            'Web sitenizdeki formlar, Google ve Meta reklam formları, açılış sayfaları ve e-posta ile gelen talepleri alabiliriz. Bağlantı çoğunlukla webhook ya da API ile kurulur; gerekirse form bildirim e-postaları da kullanılabilir.']),
        dict(q='Talep kalitesini ve reklam verimini nasıl raporluyorsunuz?', p=[
            'Her talep kaynağı, kampanyası ve sonucu ile birlikte kaydedilir: ulaşıldı mı, nitelikli mi, randevu ya da satış oldu mu. Bu rapor, hangi reklamın gerçekten iş getirdiğini görmenizi ve bütçenizi buna göre yönetmenizi sağlar.']),
    ],
    why=['Saniyeler içinde ilk arama', 'Planlı tekrar deneme', 'Kampanya bazlı sonuç raporu', 'Satışta kanıtlanmış ekip'],
    faq_title='Lead ve talep yönetimi hakkında',
    faq=[
        dict(q='Mesai dışında gelen talepler ne zaman aranıyor?', a='7/24 çalıştığımız için gece gelen talepler de aranabilir. Hangi saatlerde arama yapılacağını hedef kitlenize göre birlikte belirleriz.'),
        dict(q='Ulaşılamayan kişi kaç kez aranıyor?', a='Tekrar deneme sayısı ve aralığı projeye göre belirlenir; kişiyi rahatsız etmeyecek şekilde farklı saatlerde denenir.'),
        dict(q='Kendi CRM sistemimize kayıt yapabilir misiniz?', a='Evet. Sonuçları sisteminize yetkili kullanıcı olarak işleyebilir ya da API ile aktarabiliriz.'),
        dict(q='Reklam yönetimini de yapıyor musunuz?', a='Bu sayfadaki hizmet, gelen talebin aranması ve sonuca bağlanmasıdır. Reklam hesaplarınız size ya da ajansınıza ait kalır; sonuç raporlarımızı onlarla paylaşabilirsiniz.'),
        dict(q='Fiyatlandırma nasıl yapılıyor?', a='Aylık talep sayısına göre talep başı, temsilci başı ya da sabit ücret ve randevu başı prim içeren karma model önerebiliriz.'),
    ],
    related=[dict(url='/hizmetler/dis-arama-ve-telesatis/', name='Telesatış'), dict(url='/sektorler/gayrimenkul/emlak-ve-konut-projesi-cagri-merkezi/', name='Konut projesi talepleri'), dict(url='/sektorler/otomotiv/bayi-ve-servis-cagri-merkezi/', name='Test sürüşü talepleri'), dict(url='/sektorler/saglik/klinik-ve-dis-hekimligi-cagri-merkezi/', name='Klinik talepleri'), FIYAT, TEKLIF],
    cta_title='Reklam bütçenizle gelen talepler boşa gitmesin.', cta_text='Aylık talep sayınızı ve kaynaklarınızı paylaşın; entegrasyon ve fiyat önerimizi iletelim.')),
]
