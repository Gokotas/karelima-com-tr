# -*- coding: utf-8 -*-
"""Üçüncü tur: 4 hizmet + 8 sektör sayfası."""

FIYAT = dict(url='/rehber/cagri-merkezi-hizmeti-fiyatlari/', name='Çağrı merkezi hizmeti fiyatları')
TEKLIF = dict(url='/teklif-al/', name='Teklif alın')
H = '/hizmetler/'
IYS = 'Tüketicilere tanıtım amaçlı arama yalnızca İYS\'de onayı bulunan kişilere yapılır; aranmak istemediğini bildiren kişi bir daha aranmaz. Kişisel veriler KVKK\'ya uygun işlenir.'

def faq_kurulum(x='Standart kurulum ve temsilci eğitimi 10 iş gününde tamamlanır.'):
    return dict(q='Ne kadar sürede başlarız?', a=x)

PAGES_HIZMET2 = [
# ---------------------------------------------------------------- WhatsApp
dict(path=H + 'whatsapp-ve-canli-destek/', name='WhatsApp ve canlı destek', og_image='hero-temsilci',
     title='WhatsApp Müşteri Hizmetleri ve Canlı Destek Hizmeti | Karelima',
     description='WhatsApp, canlı destek ve e-posta taleplerinizi telefonla aynı ekip ve aynı kayıtla yönetiyoruz. 7/24 yazılı müşteri hizmetleri, hızlı ilk yanıt.',
     audience='Yazılı kanallardan müşteri talebi alan firmalar',
     d=dict(
    eyebrow='Hizmetler · WhatsApp ve canlı destek', h1='WhatsApp ve canlı destek: yazılı kanallarda da hızlı ve tutarlı yanıt',
    answer='Karelima, firmanızın WhatsApp, web sitesi canlı destek ve e-posta kanallarından gelen mesajları telefon hattıyla aynı ekip ve aynı kayıt sistemiyle yönetir. Mesajlar kurum dilinizle yanıtlanır, çözülemeyen talepler takip kaydıyla ilgili birime iletilir. 7/24 çalışıyoruz; gece gelen mesaj sabahı beklemez.',
    facts=['WhatsApp, canlı destek, e-posta', 'Telefonla aynı kayıt', '7/24 yanıt', 'Hazır yanıt kütüphanesi'],
    illus='illus/whatsapp.svg',
    tasks_title='Yazılı kanallarda üstlendiğimiz işler', tasks_sub='Müşteriniz hangi kanaldan yazarsa yazsın, aynı bilgiyi ve aynı özeni bulur.',
    tasks=[
        dict(icon='chat', name='WhatsApp mesajları', text='WhatsApp Business hesabınıza gelen soruları, sipariş ve randevu taleplerini yanıtlarız.'),
        dict(icon='phone', name='Web sitesi canlı destek', text='Sitenizdeki canlı destek penceresinden gelen ziyaretçilere anında yanıt veririz.'),
        dict(icon='doc', name='E-posta ve form yanıtları', text='Müşteri hizmetleri e-postalarını ve iletişim formu mesajlarını belirlenen sürede yanıtlarız.'),
        dict(icon='cal', name='Randevu ve sipariş alma', text='Yazılı kanallardan gelen randevu ve sipariş taleplerini sisteminize işleriz.'),
        dict(icon='users', name='Telefona geçiş', text='Yazışmayla çözülmeyen konularda müşteriyi arar, görüşmeyi telefonda tamamlarız.'),
        dict(icon='chart', name='Kanal raporu', text='Mesaj sayısı, ilk yanıt süresi ve konu dağılımını kanal bazında raporlarız.'),
    ],
    flow_title='Bir mesaj bizde böyle ilerler',
    flow=[
        dict(name='Mesaj gelir', text='WhatsApp, canlı destek ya da e-posta mesajı tek bir panelde toplanır.'),
        dict(name='Müşteri tanınır', text='Önceki yazışma ve görüşmeleri Karelima CRM\'de görüntülenir.'),
        dict(name='Yanıt', text='Onaylı yanıt kütüphanesi ve kurum dilinizle yanıtlanır.'),
        dict(name='Takip', text='Çözümü sizde olan talep takip kaydıyla ilgili birime iletilir.'),
        dict(name='Rapor', text='Yanıt süreleri ve konu dağılımı düzenli raporlanır.'),
    ],
    qa=[
        dict(q='WhatsApp müşteri hizmetleri dışarıya nasıl verilir?', p=[
            'WhatsApp Business hesabınızın mesajları, birden fazla temsilcinin aynı anda çalışabildiği bir panel üzerinden yönetilir. Temsilcilerimiz bu panele yetkili kullanıcı olarak bağlanır; numaranız ve hesabınız sizde kalır.',
            'Kurulumda sık sorulan sorular için onaylı yanıt kütüphanesi hazırlanır, hangi konuların hangi birime aktarılacağı belirlenir.']),
        dict(q='Yazılı kanallar telefon hattıyla birlikte yönetilmeli mi?', p=[
            'Müşteri aynı konuyu bazen önce WhatsApp\'tan yazar, sonra arar. İki kanal farklı ekiplerdeyse müşteri her seferinde baştan anlatmak zorunda kalır.',
            'Aynı ekip ve aynı kayıt sistemiyle çalıştığımızda temsilci önceki yazışmayı görür, müşteri tekrar anlatmaz ve çözüm hızlanır.']),
        dict(q='İlk yanıt süresi neden önemli?', p=[
            'Yazılı kanalda bekleyen müşteri çoğunlukla başka bir sekmede rakibinize de yazmıştır. İlk yanıtın hızlı gelmesi, müşterinin sizinle devam etmesini sağlar. Hedef ilk yanıt sürelerini sözleşmede birlikte belirleriz.']),
    ],
    why=['Telefon ve yazılı kanal tek ekipte', '7/24 yanıt', 'Onaylı yanıt kütüphanesi', 'Kanal bazında rapor'],
    faq_title='WhatsApp ve canlı destek hakkında',
    faq=[
        dict(q='WhatsApp numaramız değişir mi?', a='Hayır. Hesap ve numara size ait kalır; temsilcilerimiz yetkili kullanıcı olarak çalışır.'),
        dict(q='Hangi canlı destek yazılımlarıyla çalışırsınız?', a='Yetkili kullanıcı erişimi verilen web tabanlı canlı destek ve müşteri hizmetleri panelleriyle çalışabiliriz.'),
        dict(q='Mesai dışında mesajlar yanıtlanıyor mu?', a='Evet. 7/24 çalıştığımız için gece ve hafta sonu gelen mesajlar da yanıtlanır.'),
        dict(q='Sadece yazılı kanallar için hizmet alabilir miyiz?', a='Evet. Telefon hattı olmadan yalnızca WhatsApp, canlı destek ve e-posta kanallarını devredebilirsiniz.'),
        faq_kurulum(),
    ],
    related=[dict(url='/hizmetler/gelen-cagri-yonetimi/', name='Gelen çağrı yönetimi'), dict(url='/sektorler/e-ticaret-ve-perakende/e-ticaret-cagri-merkezi/', name='E-ticaret müşteri hizmetleri'), dict(url='/hizmetler/teknik-destek-hatti/', name='Teknik destek hattı'), FIYAT, TEKLIF],
    cta_title='Yazılı kanallarınızda hiçbir mesaj beklemesin.', cta_text='Aylık mesaj sayınızı ve kullandığınız kanalları paylaşın; ekip ve fiyat önerimizi iletelim.')),

# ---------------------------------------------------------------- Back office
dict(path=H + 'back-office-operasyonlari/', name='Back office operasyonları', og_image='ekip-egitim',
     title='Back Office Hizmeti: Veri Girişi ve Evrak Kontrolü | Karelima',
     description='Veri girişi, başvuru ve sipariş takibi, evrak kontrolü, CRM güncelleme gibi arka plan işlerini çağrı süreciyle birlikte yürütüyoruz. Kayıtlı, raporlu.',
     audience='Operasyon yükünü azaltmak isteyen firmalar',
     d=dict(
    eyebrow='Hizmetler · Back office', h1='Back office operasyonları: çağrının arkasındaki işler de tek ekipte',
    answer='Karelima; veri girişi, başvuru ve sipariş takibi, evrak kontrolü, sistem güncellemeleri ve raporlama gibi arka plan işlerini çağrı merkezi süreciyle birlikte yürütür. Telefonda alınan bilgi aynı ekip tarafından sisteminize işlenir ve takip edilir; işler el değiştirirken kaybolmaz.',
    facts=['Veri girişi', 'Başvuru ve evrak takibi', 'CRM güncelleme', 'Günlük iş raporu'],
    illus='illus/backoffice.svg',
    tasks_title='Back office tarafında üstlendiğimiz işler', tasks_sub='Tekrarlayan, kurala bağlanabilen işleri devredin; ekibiniz karar gerektiren işlere odaklansın.',
    tasks=[
        dict(icon='doc', name='Veri girişi', text='Form, başvuru ve sipariş bilgilerini sisteminize doğru ve eksiksiz işleriz.'),
        dict(icon='shield', name='Evrak kontrolü', text='Başvurulara eklenen belgeleri kontrol listesine göre inceler, eksikleri müşteriden isteriz.'),
        dict(icon='clock', name='Başvuru ve sipariş takibi', text='Bekleyen başvuruları ve siparişleri takip eder, gecikenleri ilgili birime bildiririz.'),
        dict(icon='users', name='CRM ve veri güncelleme', text='Müşteri kayıtlarını günceller, mükerrer ve eksik kayıtları temizleriz.'),
        dict(icon='phone', name='Eksik bilgi aramaları', text='Başvurusunda eksik bilgi ya da belge olan müşteriyi arayarak tamamlatırız.'),
        dict(icon='chart', name='İş raporları', text='Tamamlanan, bekleyen ve sorunlu işleri günlük olarak raporlarız.'),
    ],
    flow_title='Bir başvuru bizde böyle ilerler',
    flow=[
        dict(name='Başvuru gelir', text='Web, telefon ya da e-posta ile gelen başvuru kayda alınır.'),
        dict(name='Kontrol', text='Bilgi ve belgeler kontrol listesine göre incelenir.'),
        dict(name='Eksik tamamlama', text='Eksik varsa müşteri aranır ve tamamlatılır.'),
        dict(name='Sisteme işleme', text='Tamamlanan başvuru sisteminize işlenir ve ilgili birime iletilir.'),
        dict(name='Rapor', text='Başvuru durumları günlük raporunuza yansır.'),
    ],
    qa=[
        dict(q='Hangi back office işleri dışarıya verilebilir?', p=[
            'Tanımlı kurallarla yapılabilen, tekrarlayan işler dış kaynak için uygundur: veri girişi, başvuru ön kontrolü, sipariş ve kargo takibi, kayıt güncelleme, eksik belge takibi ve rutin raporlama gibi.',
            'Onay, fiyatlandırma ya da hukuki değerlendirme gerektiren kararlar sizde kalır; biz bu kararlar için gereken bilgiyi eksiksiz ve düzenli hale getiririz.']),
        dict(q='Çağrı merkezi ile back office neden aynı ekipte olmalı?', p=[
            'Telefonda alınan bilgi başka bir ekibe aktarılırken eksik kalabilir ya da gecikebilir. Aynı ekip hem görüşmeyi yapıp hem sisteme işlediğinde hata ve bekleme azalır; müşteriye verilen bilgiyle sistemdeki kayıt birbirini tutar.']),
        dict(q='Verilerin güvenliği nasıl sağlanıyor?', p=[
            'Sistemlerinize yalnızca projeye atanmış temsilciler, ihtiyaç duydukları yetkilerle erişir. Çalışma, veri işleme sözleşmesi kapsamında yürütülür ve yapılan işlemler kayıt altında tutulur.']),
    ],
    why=['Görüşme ve işlem tek ekipte', 'Kontrol listesiyle hatasız işlem', 'Yetki bazlı erişim', 'Günlük iş raporu'],
    faq_title='Back office hizmeti hakkında',
    faq=[
        dict(q='Kendi sistemlerimizde mi çalışıyorsunuz?', a='Evet. Temsilcilerimiz sistemlerinize yetkili kullanıcı olarak erişir; gerekirse Karelima CRM üzerinden çalışıp size aktarırız.'),
        dict(q='Ücretlendirme nasıl yapılıyor?', a='İş hacmine göre işlem başı, saatlik ya da size ayrılmış ekip modeliyle fiyatlandırıyoruz.'),
        dict(q='Sadece back office hizmeti alabilir miyiz?', a='Evet. Çağrı hizmeti olmadan yalnızca arka plan işlerini de devredebilirsiniz.'),
        dict(q='İş kalitesini nasıl ölçüyorsunuz?', a='Hata oranı, işlem süresi ve bekleyen iş sayısı gibi hedefleri birlikte belirler, düzenli olarak raporlarız.'),
        faq_kurulum('Süreç ve kontrol listeleri hazırlandıktan sonra kurulum 10 iş günü içinde tamamlanır.'),
    ],
    related=[dict(url='/hizmetler/gelen-cagri-yonetimi/', name='Gelen çağrı yönetimi'), dict(url='/hizmetler/lead-ve-talep-yonetimi/', name='Talep yönetimi'), dict(url='/sektorler/sigorta/sigorta-cagri-merkezi/', name='Sigorta operasyonları'), FIYAT, TEKLIF],
    cta_title='Operasyon yükünüzü birlikte hafifletelim.', cta_text='Devretmek istediğiniz işleri ve aylık hacmi paylaşın; süreç önerimizi iletelim.')),

# ---------------------------------------------------------------- Teknik destek
dict(path=H + 'teknik-destek-hatti/', name='Teknik destek hattı', og_image='temsilci-ofis',
     title='Teknik Destek Hattı ve Help Desk Hizmeti (1. Seviye) | Karelima',
     description='Birinci seviye teknik destek, arıza kaydı, adım adım çözüm yönlendirmesi ve uzman ekibe aktarım. Kullanıcılarınız 7/24 destek bulur, her kayıt raporlanır.',
     audience='Yazılım, donanım ve hizmet firmaları',
     d=dict(
    eyebrow='Hizmetler · Teknik destek', h1='Teknik destek hattı: birinci seviye destek ve arıza kaydı',
    answer='Karelima, ürün ve hizmetlerinizi kullanan müşterilerin teknik destek taleplerini birinci seviyede karşılar. Sık karşılaşılan sorunları hazır çözüm adımlarıyla telefonda çözer, çözülemeyenleri eksiksiz bir arıza kaydıyla uzman ekibinize aktarır. Her talep takip numarasıyla izlenir ve raporlanır.',
    facts=['1. seviye destek', 'Arıza kaydı ve takip no', 'Uzman ekibe aktarım', '7/24 hat'],
    illus='illus/teknik-destek.svg',
    tasks_title='Teknik destek hattında üstlendiğimiz işler', tasks_sub='Uzman ekibiniz yalnızca gerçekten uzmanlık gerektiren sorunlarla ilgilensin.',
    tasks=[
        dict(icon='phone', name='Destek çağrılarını karşılama', text='Kullanıcının sorununu dinler, ürün ve sürüm bilgilerini alırız.'),
        dict(icon='doc', name='Hazır çözüm adımları', text='Sık görülen sorunları onaylı çözüm adımlarıyla telefonda çözeriz.'),
        dict(icon='shield', name='Arıza kaydı', text='Çözülemeyen sorunu ekran görüntüsü, hata mesajı ve adımlarla eksiksiz kaydederiz.'),
        dict(icon='users', name='Uzman ekibe aktarım', text='Kaydı tanımlı önceliklere göre ikinci seviye ekibinize iletiriz.'),
        dict(icon='clock', name='Takip ve geri dönüş', text='Açık kayıtları takip eder, çözüm sonrası kullanıcıyı arayarak teyit alırız.'),
        dict(icon='chart', name='Sorun raporu', text='En sık görülen sorunları ve çözüm sürelerini raporlarız; ürün ekibiniz için değerli bir veri olur.'),
    ],
    flow_title='Bir destek talebi bizde böyle ilerler',
    flow=[
        dict(name='Karşılama', text='Kullanıcı tanınır, ürün ve sorun bilgisi alınır.'),
        dict(name='Teşhis', text='Sorun, çözüm kütüphanesindeki senaryolarla eşleştirilir.'),
        dict(name='Çözüm', text='Adım adım yönlendirmeyle mümkünse ilk temasta çözülür.'),
        dict(name='Aktarım', text='Çözülemezse eksiksiz kayıtla uzman ekibe aktarılır.'),
        dict(name='Kapanış', text='Çözüm sonrası kullanıcıdan teyit alınır, kayıt kapatılır.'),
    ],
    qa=[
        dict(q='Birinci seviye teknik destek dışarıya verilir mi?', p=[
            'Evet. Teknik destek taleplerinin önemli bir kısmı şifre, kurulum, ayar ve kullanım soruları gibi tekrar eden konulardır. Bu konular için hazırlanmış çözüm adımlarıyla eğitimli temsilciler talebi ilk temasta çözebilir.',
            'Böylece yazılımcı ve mühendisleriniz yalnızca gerçekten uzmanlık gerektiren sorunlarla ilgilenir.']),
        dict(q='Çözüm kütüphanesi nasıl hazırlanıyor?', p=[
            'Kurulumda mevcut destek kayıtlarınız ve dokümanlarınız incelenir, en sık görülen sorunlar için adım adım çözüm akışları hazırlanır. Hatta yeni sorunlar geldikçe kütüphane sizin onayınızla güncellenir.']),
        dict(q='Hangi destek sistemleriyle çalışırsınız?', p=[
            'Kullandığınız destek talebi ya da help desk sistemine yetkili kullanıcı olarak erişebiliriz. Sisteminiz yoksa kayıtlar Karelima CRM\'de tutulur ve size aktarılır.']),
    ],
    why=['İlk temasta çözüm odaklı çalışma', 'Eksiksiz arıza kaydı', 'Uzman ekibinizin zamanı korunur', 'Sorun bazlı rapor'],
    faq_title='Teknik destek hattı hakkında',
    faq=[
        dict(q='Uzaktan bağlantıyla destek veriyor musunuz?', a='Projenin kapsamına ve sizin güvenlik kurallarınıza göre belirlenir. Birinci seviyede çoğunlukla telefon ve ekran paylaşımı gerektirmeyen yönlendirme yapılır.'),
        dict(q='Kurumsal (B2B) müşterilerimize destek verebilir misiniz?', a='Evet. Bayi, kurum ve son kullanıcı ayrımına göre farklı karşılama ve öncelik kuralları tanımlayabiliriz.'),
        dict(q='Arıza kayıtları bize nasıl ulaşıyor?', a='Kayıtlar destek sisteminize doğrudan açılır ya da e-posta ve API ile aktarılır.'),
        dict(q='7/24 teknik destek mümkün mü?', a='Evet. Gece ve hafta sonu da hat açık tutulabilir; acil durumlar için nöbetçi uzmanınıza yönlendirme tanımlanır.'),
        faq_kurulum('Çözüm kütüphanesi hazırlandıktan sonra kurulum ve eğitim 10 iş gününde tamamlanır.'),
    ],
    related=[dict(url='/sektorler/teknoloji-ve-yazilim/yazilim-firmalari-icin-cagri-merkezi/', name='Yazılım firmaları için çağrı merkezi'), dict(url='/sektorler/teknik-servis/teknik-servis-cagri-merkezi/', name='Teknik servis çağrı merkezi'), dict(url='/hizmetler/whatsapp-ve-canli-destek/', name='Canlı destek'), FIYAT, TEKLIF],
    cta_title='Destek hattınızı birlikte kuralım.', cta_text='Aylık destek talebi sayınızı ve en sık görülen sorunları paylaşın; ekip önerimizi iletelim.')),

# ---------------------------------------------------------------- Ödeme hatırlatma
dict(path=H + 'odeme-hatirlatma/', name='Ödeme hatırlatma', og_image='operasyon-merkezi',
     title='Ödeme Hatırlatma Aramaları Hizmeti | Karelima',
     description='Vadesi yaklaşan ve geciken ödemeler için kibar, kayıtlı ve mevzuata uygun hatırlatma aramaları. Müşteri ilişkisini koruyarak tahsilat sürecini destekliyoruz.',
     audience='Abonelik, taksit ve vadeli satış yapan firmalar',
     d=dict(
    eyebrow='Hizmetler · Ödeme hatırlatma', h1='Ödeme hatırlatma aramaları: müşteri ilişkisini koruyan nazik takip',
    answer='Karelima, vadesi yaklaşan ve geciken ödemeler için müşterilerinizi kibar ve kayıtlı aramalarla bilgilendirir. Ödeme tarihini ve yöntemini hatırlatır, gerekirse ödeme bağlantınızı iletir, ödeme sözü ve itirazları kayda alır. Baskı ve tehdit içeren dil kullanmaz; müşteri ilişkinizi korur.',
    facts=['Vade öncesi hatırlatma', 'Gecikme takibi', 'Ödeme sözü kaydı', 'Görüşmeler kayıtlı'],
    illus='illus/odeme.svg',
    tasks_title='Ödeme hatırlatmada üstlendiğimiz işler', tasks_sub='Amaç müşteriyi kaybetmeden ödemenin zamanında yapılmasını sağlamaktır.',
    tasks=[
        dict(icon='clock', name='Vade öncesi hatırlatma', text='Ödeme tarihi yaklaşan müşteriye tarihi ve tutarı nazikçe hatırlatırız.'),
        dict(icon='phone', name='Gecikme aramaları', text='Ödemesi geciken müşteriyi arar, gecikmenin nedenini öğrenir ve çözüm yolunu iletiriz.'),
        dict(icon='doc', name='Ödeme sözü kaydı', text='Müşterinin verdiği ödeme tarihini kaydeder, gününde takip ederiz.'),
        dict(icon='out', name='Ödeme bağlantısı iletimi', text='Sizin güvenli ödeme bağlantınızı SMS ya da e-postayla iletiriz; kart bilgisi telefonda alınmaz.'),
        dict(icon='chat', name='İtiraz ve talep kaydı', text='Fatura itirazı ya da yapılandırma talebini kayda alır, ilgili birime iletiriz.'),
        dict(icon='chart', name='Tahsilat raporu', text='Ulaşılan müşteri, ödeme sözü ve gerçekleşen ödemeleri raporlarız.'),
    ],
    flow_title='Bir hatırlatma süreci bizde böyle ilerler',
    flow=[
        dict(name='Liste', text='Vadesi yaklaşan ve geciken ödemeler günlük olarak paylaşılır.'),
        dict(name='Arama', text='Müşteri kibar bir dille aranır; yalnızca borçlu kişiyle görüşülür.'),
        dict(name='Çözüm', text='Ödeme tarihi ve yöntemi netleşir, gerekirse ödeme bağlantısı iletilir.'),
        dict(name='Takip', text='Ödeme sözü gününde kontrol edilir, gerekirse yeniden aranır.'),
        dict(name='Rapor', text='Sonuçlar günlük ve aylık olarak raporlanır.'),
    ],
    qa=[
        dict(q='Ödeme hatırlatma araması nasıl yapılmalı?', p=[
            'Ödeme hatırlatmasının amacı müşteriyi zor durumda bırakmak değil, ödemenin zamanında yapılmasını kolaylaştırmaktır. Arama kibar bir dille yapılır, yalnızca borçlu kişiyle konuşulur ve borç bilgisi üçüncü kişilerle paylaşılmaz.',
            'Müşterinin durumu dinlenir; ödeme tarihi, ödeme yöntemi ya da varsa yapılandırma seçenekleri sizin belirlediğiniz kurallar çerçevesinde iletilir.']),
        dict(q='Vade öncesi hatırlatma neden etkilidir?', p=[
            'Gecikmelerin önemli bir kısmı unutmaktan kaynaklanır. Vade gününden önce yapılan kısa bir hatırlatma, gecikmeyi oluşmadan önler ve müşteride olumlu bir hizmet algısı bırakır.']),
        dict(q='Hukuki takip sürecini de yürütüyor musunuz?', p=[
            'Hayır. Hizmetimiz hatırlatma, bilgilendirme ve ödeme sözü takibiyle sınırlıdır. Hukuki takip ve icra süreçleri avukatınız ya da yetkili birimleriniz tarafından yürütülür.']),
    ],
    law=dict(title='Saygılı ve kurallara uygun', text='Aramalarda tehdit, baskı ve küçük düşürücü dil kullanılmaz; borç bilgisi yalnızca borçlu kişiyle paylaşılır. Kişisel veriler KVKK\'ya uygun işlenir, kart bilgisi telefonda alınmaz.'),
    why=['Müşteri ilişkisini koruyan dil', 'Ödeme sözü takibi', 'Her görüşme kayıtlı', 'Günlük sonuç raporu'],
    faq_title='Ödeme hatırlatma hakkında',
    faq=[
        dict(q='Telefonda ödeme alıyor musunuz?', a='Hayır. Kart bilgisi telefonda alınmaz; müşteriye sizin güvenli ödeme bağlantınız ya da banka bilgileriniz iletilir.'),
        dict(q='Hangi firmalar için uygun?', a='Abonelik, üyelik, taksitli satış ve vadeli fatura ile çalışan firmalar için uygundur.'),
        dict(q='Hangi saatlerde arama yapıyorsunuz?', a='Müşteriyi rahatsız etmeyecek, makul saatlerde arama yapılır; saat aralığını birlikte belirleriz.'),
        dict(q='Yapılandırma teklifi verebilir misiniz?', a='Sizin belirlediğiniz kurallar ve yetki çerçevesinde seçenekleri iletebiliriz; onay sizde kalır.'),
        faq_kurulum(),
    ],
    related=[dict(url='/sektorler/finans/finans-cagri-merkezi/', name='Finans çağrı merkezi'), dict(url='/sektorler/telekom-ve-abonelik/telekom-ve-abonelik-cagri-merkezi/', name='Abonelik çağrı merkezi'), dict(url='/hizmetler/dis-arama-ve-telesatis/', name='Dış arama'), FIYAT, TEKLIF],
    cta_title='Gecikmeleri oluşmadan önleyelim.', cta_text='Aylık hatırlatma hacminizi ve ödeme yöntemlerinizi paylaşın; çalışma planımızı iletelim.')),
]

S = '/sektorler/'
PAGES_SEKTOR2 = [
# ---------------------------------------------------------------- Eğitim
dict(path=S + 'egitim/okul-ve-kurs-cagri-merkezi/', name='Okul ve kurs çağrı merkezi', sector='Eğitim', og_image='ekip-egitim',
     audience='Özel okullar, kolejler, kurslar ve üniversiteler',
     title='Özel Okul ve Kurslar için Çağrı Merkezi | Karelima',
     description='Kayıt döneminde aday öğrenci ve veli taleplerini karşılıyor, kampüs ziyareti ve kayıt görüşmesi randevusu veriyoruz. Dönemsel esnek ekip.',
     d=dict(
    eyebrow='Sektörler · Eğitim', h1='Özel okullar, kolejler ve kurslar için çağrı merkezi',
    answer='Karelima; özel okul, kolej, kurs ve üniversitelerin aday öğrenci ve veli taleplerini karşılar. Program, ücret ve burs sorularını sizin belirlediğiniz bilgilerle yanıtlar, kampüs ziyareti ve kayıt görüşmesi randevusu verir, web ve reklam taleplerini aynı gün arar. Kayıt dönemlerinde ekibi hacme göre büyütür.',
    facts=['Aday ve veli bilgilendirme', 'Kampüs ziyareti randevusu', 'Kayıt dönemi kapasitesi', '7/24 hat'],
    illus='illus/egitim.svg',
    tasks_title='Eğitim kurumlarında üstlendiğimiz işler', tasks_sub='Kayıt ofisiniz yüz yüze görüşmelere odaklanırken telefon ve mesajlar bizde.',
    tasks=[
        dict(icon='phone', name='Aday ve veli bilgilendirme', text='Program, kademe, servis ve burs sorularını onaylı bilgilerle yanıtlarız.'),
        dict(icon='cal', name='Kampüs ziyareti randevusu', text='Tanıtım günleri ve birebir ziyaretler için randevu verir, bir gün önce teyit alırız.'),
        dict(icon='out', name='Web ve reklam taleplerini arama', text='Bilgi formu dolduran velileri aynı gün arar, ihtiyacı netleştiririz.'),
        dict(icon='clock', name='Kayıt hatırlatma', text='Ön kayıt yapan ya da görüşmeye gelen ailelere kayıt tarihlerini hatırlatırız.'),
        dict(icon='users', name='Etkinlik davetleri', text='Açık gün, seminer ve sınav etkinlikleri için izinli kişileri davet ederiz.'),
        dict(icon='star', name='Veli memnuniyeti', text='Dönem içinde veli memnuniyeti anketleri yapar, sonuçları raporlarız.'),
    ],
    flow_title='Bir aday talebi bizde böyle ilerler',
    flow=[
        dict(name='Talep gelir', text='Telefon, form ya da reklam talebi Karelima CRM\'e kaydedilir.'),
        dict(name='Bilgilendirme', text='Kademe, program ve beklentiler konuşulur.'),
        dict(name='Randevu', text='Kampüs ziyareti ya da kayıt görüşmesi planlanır.'),
        dict(name='Teyit', text='Ziyaret öncesi hatırlatma yapılır.'),
        dict(name='Rapor', text='Talep, ziyaret ve kayıt sayıları kaynak bazında raporlanır.'),
    ],
    qa=[
        dict(q='Kayıt döneminde telefon yoğunluğu nasıl yönetilir?', p=[
            'Kayıt dönemlerinde çağrı ve form talepleri kısa sürede katlanır; kayıt ofisi hem ziyaretçilerle hem telefonla ilgilenmekte zorlanır. Bu dönemlerde hattı bize yönlendirdiğinizde her veli aynı gün dönüş alır.',
            'Dönem bitince ekip normal hacme göre küçülür; yalnızca ihtiyaç duyduğunuz kapasiteye ödeme yaparsınız.']),
        dict(q='Temsilciler ücret ve burs bilgisi veriyor mu?', p=[
            'Hangi bilgilerin telefonda paylaşılacağını siz belirlersiniz. Ücret, burs ve indirim bilgileri sizin onayladığınız güncel metinlerle verilir; değerlendirme gerektiren konular kayıt ofisinize aktarılır.']),
        dict(q='Reklamdan gelen taleplerin kayda dönüşü nasıl artar?', p=[
            'Formu dolduran veli o an araştırma yapıyordur ve birden fazla kuruma başvurmuş olabilir. Talebi aynı gün aramak ve kampüs ziyaretini hemen planlamak, ailenin kurumunuzu yerinde görmesini sağlar.']),
    ],
    law=dict(title='İzinli iletişim', text=IYS),
    why=['Kayıt döneminde esnek kapasite', 'Aynı gün geri dönüş', 'Ziyaret randevusu ve teyit', 'Kaynak bazlı kayıt raporu'],
    faq_title='Eğitim kurumları için çağrı merkezi hakkında',
    faq=[
        dict(q='Sadece kayıt dönemi için hizmet alabilir miyiz?', a='Evet. Dönemsel proje modeliyle yalnızca kayıt dönemlerinde çalışabiliriz.'),
        dict(q='Birden fazla kampüs için çalışır mısınız?', a='Evet. Talepleri kampüs ve kademe bazında ayırır, her kampüsün takvimine ayrı randevu veririz.'),
        dict(q='Mevcut velilere duyuru araması yapıyor musunuz?', a='Evet. Etkinlik, toplantı ve önemli duyurular için mevcut velilerinizi arayabiliriz.'),
        dict(q='Yurt dışı eğitim ve dil okulları için uygun mu?', a='Evet. Danışmanlık görüşmesi randevusu ve bilgilendirme süreçlerini aynı şekilde yönetiyoruz.'),
        faq_kurulum(),
    ],
    related=[dict(url='/hizmetler/randevu-ve-rezervasyon-yonetimi/', name='Randevu yönetimi'), dict(url='/hizmetler/lead-ve-talep-yonetimi/', name='Form talebi geri arama'), dict(url='/hizmetler/memnuniyet-ve-anket-aramalari/', name='Veli memnuniyeti'), FIYAT, TEKLIF],
    cta_title='Kayıt döneminde hiçbir veli beklemesin.', cta_text='Kampüs sayınızı ve dönemsel talep hacminizi paylaşın; çalışma planımızı iletelim.')),

# ---------------------------------------------------------------- Telekom
dict(path=S + 'telekom-ve-abonelik/telekom-ve-abonelik-cagri-merkezi/', name='Telekom ve abonelik çağrı merkezi', sector='Telekom ve abonelik', og_image='operasyon-merkezi',
     audience='İnternet, TV, yayın ve abonelik hizmeti sunan firmalar',
     title='Telekom ve Abonelik Satışı için Çağrı Merkezi | Karelima',
     description='Yeni abonelik satışı, başvuru teyidi, kurulum takibi ve taahhüt bitimi aramaları. Digitürk ve Türksat iş ortaklığıyla her gün sahada kanıtlanmış ekip.',
     d=dict(
    eyebrow='Sektörler · Telekom ve abonelik', h1='Telekom ve abonelik hizmetleri için çağrı merkezi',
    answer='Karelima, Digitürk ve Türksat\'ın satış iş ortağı olarak yüksek hacimli abonelik satışını her gün kendi ekibiyle yürütür. Aynı deneyimle internet, TV, yayın ve diğer abonelik hizmetleri için başvuru karşılama, satış, başvuru teyidi, kurulum takibi ve taahhüt bitimi aramaları yapar.',
    facts=['Abonelik satışında deneyim', 'Başvuru teyidi', 'Kurulum takibi', 'Taahhüt bitimi aramaları'],
    illus='illus/telekom.svg',
    tasks_title='Abonelik operasyonunda üstlendiğimiz işler', tasks_sub='Başvurudan kuruluma ve yenilemeye kadar abonelik yaşam döngüsünün her adımı.',
    tasks=[
        dict(icon='phone', name='Başvuru karşılama ve satış', text='Web ve reklam başvurularını saniyeler içinde arar, uygun paketi anlatır ve satışı tamamlarız.'),
        dict(icon='shield', name='Başvuru teyidi', text='Başvuru bilgilerini ve müşteri onayını kayıtlı görüşmeyle teyit ederiz.'),
        dict(icon='cal', name='Kurulum randevusu ve takibi', text='Kurulum randevusunu planlar, gerçekleşene kadar takip ederiz.'),
        dict(icon='clock', name='Taahhüt bitimi aramaları', text='Taahhüdü sona eren mevcut abonelerinizi yenileme seçenekleriyle ararız.'),
        dict(icon='users', name='Kayıp abone geri kazanımı', text='Hizmetten ayrılan abonelerle ayrılma nedenini konuşur, geri dönüş teklifinizi iletiriz.'),
        dict(icon='chart', name='Satış ve iptal raporu', text='Satış, kurulum ve iptal oranlarını kaynak bazında raporlarız.'),
    ],
    flow_title='Bir abonelik başvurusu bizde böyle ilerler',
    flow=[
        dict(name='Başvuru', text='Başvuru Karelima CRM\'e düşer ve saniyeler içinde aranır.'),
        dict(name='İhtiyaç ve paket', text='Adres uygunluğu ve ihtiyaç konuşulur, uygun paket anlatılır.'),
        dict(name='Teyit', text='Bilgiler ve onay kayıtlı görüşmeyle teyit edilir.'),
        dict(name='Kurulum', text='Kurulum randevusu planlanır ve takip edilir.'),
        dict(name='Rapor', text='Satış, kurulum ve iptal sonuçları raporlanır.'),
    ],
    qa=[
        dict(q='Abonelik satışında hız neden belirleyici?', p=[
            'İnternet ya da TV başvurusu bırakan kişi çoğunlukla aynı anda birden fazla firmaya başvurur. İlk arayan ve süreci en net anlatan firma genellikle satışı alır.',
            'Bu yüzden başvuruları düştüğü anda arıyoruz. Telekom iş ortaklarımız için yürüttüğümüz operasyonda bu disiplini her gün uyguluyoruz.']),
        dict(q='Başvuru teyidi ve iptal oranı nasıl ilişkili?', p=[
            'Eksik ya da yanlış anlaşılmış bir satış, kurulum aşamasında iptale dönüşür. Satış sonrası kayıtlı teyit görüşmesi, müşterinin paket ve taahhüt koşullarını doğru anladığını garanti altına alır ve iptalleri azaltır.']),
        dict(q='Hangi aramalar mevzuata uygundur?', p=[
            'Telekom sektöründe tanıtım aramaları sıkı kurallara bağlıdır. BTK düzenlemeleri, işletmecilerin ve bayilerin başka operatörlerin abonelerini tanıtım amacıyla aramasını yasaklar. Projelerimizde yalnızca başvuru bırakan kişilerle, mevcut müşterilerinizle ve İYS onayı bulunan kişilerle görüşülür.']),
    ],
    law=dict(title='BTK ve İYS kurallarına uygun', text='Tanıtım aramaları yalnızca başvuru bırakan, mevcut müşteriniz olan ya da İYS onayı bulunan kişilere yapılır. Başka operatörün abonelerine yönelik izinsiz arama yapılmaz.'),
    why=['Her gün abonelik satışı yapan ekip', 'Saniyeler içinde başvuru dönüşü', 'Kayıtlı teyit ile düşük iptal', 'Kurulum takibi'],
    faq_title='Telekom ve abonelik çağrı merkezi hakkında',
    faq=[
        dict(q='Bireysel Digitürk ya da Türksat başvurusu yapmak istiyorum.', a='Bireysel abonelik başvuruları için iş ortaklarımız sayfasındaki bağlantıları kullanabilirsiniz. Bu sayfa, abonelik hizmeti sunan firmalara yönelik çağrı merkezi hizmetimizi anlatır.'),
        dict(q='Bölgesel internet servis sağlayıcıları için çalışır mısınız?', a='Evet. Altyapı uygunluk kontrolü, başvuru ve kurulum süreçlerini sizin sistemlerinize göre kurarız.'),
        dict(q='Satış primli çalışma mümkün mü?', a='Evet. Sabit ücretle birlikte satış başına prim içeren karma modeller sunabiliyoruz.'),
        dict(q='Müşteri hizmetleri hattınızı da devralabilir misiniz?', a='Evet. Fatura, arıza kaydı ve paket değişikliği gibi gelen çağrıları da karşılıyoruz.'),
        faq_kurulum(),
    ],
    related=[dict(url='/is-ortaklarimiz/', name='İş ortaklarımız'), dict(url='/hizmetler/dis-arama-ve-telesatis/', name='Telesatış'), dict(url='/hizmetler/lead-ve-talep-yonetimi/', name='Başvuru geri arama'), FIYAT, TEKLIF],
    cta_title='Abonelik satışınızı kanıtlanmış bir ekiple büyütün.', cta_text='Aylık başvuru hacminizi ve hizmet bölgenizi paylaşın; çalışma modelimizi iletelim.')),

# ---------------------------------------------------------------- Teknoloji
dict(path=S + 'teknoloji-ve-yazilim/yazilim-firmalari-icin-cagri-merkezi/', name='Yazılım firmaları için çağrı merkezi', sector='Teknoloji ve yazılım', og_image='temsilci-ofis',
     audience='SaaS, yazılım ve donanım firmaları',
     title='Yazılım ve SaaS Firmaları için Çağrı Merkezi | Karelima',
     description='Birinci seviye destek, demo randevusu, deneme kullanıcısı aramaları ve abonelik yenileme. Yazılım ve SaaS firmaları için 7/24 müşteri hizmetleri.',
     d=dict(
    eyebrow='Sektörler · Teknoloji ve yazılım', h1='Yazılım ve SaaS firmaları için çağrı merkezi',
    answer='Karelima; yazılım, SaaS ve donanım firmalarının birinci seviye destek hattını karşılar, demo taleplerini arayıp satış ekibine randevu verir, deneme kullanıcılarına ulaşarak kurulumda yardımcı olur ve abonelik yenileme dönemlerinde müşterilerinizi arar. Ürün ekibiniz geliştirmeye, satış ekibiniz kapanışa odaklanır.',
    facts=['1. seviye destek', 'Demo randevusu', 'Deneme kullanıcısı aramaları', 'Yenileme takibi'],
    illus='illus/teknoloji.svg',
    tasks_title='Yazılım firmalarında üstlendiğimiz işler', tasks_sub='Satış öncesinden yenilemeye kadar müşteri temasının telefon ve mesaj tarafı.',
    tasks=[
        dict(icon='cal', name='Demo talebi ve randevu', text='Demo isteyen firmayı arar, ihtiyacı netleştirir ve satış ekibinize toplantı ayarlarız.'),
        dict(icon='users', name='Deneme kullanıcısı aramaları', text='Deneme sürümüne kaydolan kullanıcıyı arayarak ilk kurulumda yardımcı oluruz.'),
        dict(icon='phone', name='Birinci seviye destek', text='Giriş, kurulum ve kullanım sorularını çözüm kütüphanesiyle yanıtlarız.'),
        dict(icon='doc', name='Arıza kaydı', text='Çözülemeyen sorunu eksiksiz kayıtla geliştirme ekibinize aktarırız.'),
        dict(icon='clock', name='Abonelik yenileme', text='Yenileme tarihi yaklaşan müşterileri arar, memnuniyeti ve yenileme kararını öğreniriz.'),
        dict(icon='chart', name='Ürün geri bildirimi', text='Destek ve görüşmelerden gelen talepleri ürün ekibiniz için raporlarız.'),
    ],
    flow_title='Bir demo talebi bizde böyle ilerler',
    flow=[
        dict(name='Talep', text='Web sitesinden demo talebi Karelima CRM\'e düşer.'),
        dict(name='Hızlı arama', text='Firma yetkilisi saniyeler içinde aranır.'),
        dict(name='Ön eleme', text='Firma büyüklüğü, ihtiyaç ve zamanlama sorulur.'),
        dict(name='Toplantı', text='Satış ekibinizin takvimine demo toplantısı işlenir.'),
        dict(name='Rapor', text='Demo ve dönüşüm oranları kaynak bazında raporlanır.'),
    ],
    qa=[
        dict(q='Deneme kullanıcılarını aramak neden işe yarar?', p=[
            'Deneme sürümüne kaydolan kullanıcıların bir kısmı ilk kurulumda takılır ve ürünü bırakır. Kayıttan kısa süre sonra yapılan bir yardım araması, kullanıcının ürünün değerini görmesini sağlar.',
            'Görüşmede öğrenilen ihtiyaçlar satış ekibinize aktarılır; ücretli kullanıma geçişte doğru teklif yapılır.']),
        dict(q='Teknik destek ile satış aynı ekipte olabilir mi?', p=[
            'Birinci seviye destek ve satış öncesi görüşmeler farklı uzmanlık ister; bu yüzden projelerde ayrı akışlar ve gerekirse ayrı temsilciler tanımlarız. Ortak nokta, tüm temasların aynı müşteri kaydında birleşmesidir.']),
        dict(q='Hangi araçlarla çalışırsınız?', p=[
            'Kullandığınız CRM ve destek sistemine yetkili kullanıcı olarak erişebilir, toplantıları satış ekibinizin takvimine doğrudan işleyebiliriz.']),
    ],
    why=['Demo talebine saniyeler içinde dönüş', 'Deneme kullanıcısı aktivasyonu', 'Çözüm kütüphanesiyle destek', 'Ürün ekibine geri bildirim'],
    faq_title='Yazılım firmaları için çağrı merkezi hakkında',
    faq=[
        dict(q='Kurumsal müşterilere hizmet verebilir misiniz?', a='Evet. B2B müşteri yapınıza göre karşılama, öncelik ve eskalasyon kuralları tanımlarız.'),
        dict(q='Temsilciler ürünümüzü nasıl öğreniyor?', a='Kurulum sürecinde ürün eğitimi, dokümantasyon ve çözüm kütüphanesiyle eğitilir; sınavdan geçmeden hatta çıkmaz.'),
        dict(q='İngilizce destek veriyor musunuz?', a='Ekibimiz şu anda Türkçe hizmet veriyor. Yabancı dil ihtiyacınızı keşif görüşmesinde konuşalım.'),
        dict(q='Donanım firmaları için de uygun mu?', a='Evet. Kurulum desteği, arıza kaydı ve servis yönlendirmesi süreçlerini yönetiyoruz.'),
        faq_kurulum(),
    ],
    related=[dict(url='/hizmetler/teknik-destek-hatti/', name='Teknik destek hattı'), dict(url='/hizmetler/lead-ve-talep-yonetimi/', name='Demo talebi geri arama'), dict(url='/hizmetler/whatsapp-ve-canli-destek/', name='Canlı destek'), FIYAT, TEKLIF],
    cta_title='Destek ve satış hattınızı birlikte kuralım.', cta_text='Ürününüzü ve aylık talep hacminizi paylaşın; ekip önerimizi iletelim.')),

# ---------------------------------------------------------------- Teknik servis
dict(path=S + 'teknik-servis/teknik-servis-cagri-merkezi/', name='Teknik servis çağrı merkezi', sector='Teknik servis', og_image='temsilci-ofis',
     audience='Yetkili servisler, kombi ve klima servisleri, kurulum ekipleri',
     title='Teknik Servis Çağrı Merkezi ve Arıza Kaydı Hattı | Karelima',
     description='Arıza kaydı, servis randevusu, periyodik bakım hatırlatma ve servis sonrası memnuniyet. Kombi, klima ve beyaz eşya servisleri için 7/24 hat.',
     d=dict(
    eyebrow='Sektörler · Teknik servis', h1='Teknik servisler için çağrı merkezi ve arıza kaydı hattı',
    answer='Karelima; yetkili servisler, kombi, klima ve beyaz eşya servisleri ile kurulum ekiplerinin arıza kaydı ve servis randevu hattını 7/24 karşılar. Arızayı doğru bilgilerle kaydeder, teknisyen takvimine göre randevu verir, servis öncesi teyit alır ve periyodik bakım zamanı gelen müşterileri arar.',
    facts=['7/24 arıza kaydı', 'Teknisyen takvimine randevu', 'Bakım hatırlatma', 'Servis sonrası memnuniyet'],
    illus='illus/teknik-servis.svg',
    tasks_title='Teknik serviste üstlendiğimiz işler', tasks_sub='Teknisyenleriniz sahada işe odaklanırken telefon trafiği bizde.',
    tasks=[
        dict(icon='doc', name='Arıza kaydı', text='Cihaz, model, arıza belirtisi ve adres bilgilerini eksiksiz kaydederiz.'),
        dict(icon='cal', name='Servis randevusu', text='Teknisyen takvimi ve bölgesine göre uygun randevuyu veririz.'),
        dict(icon='clock', name='Periyodik bakım hatırlatma', text='Yıllık bakımı yaklaşan müşterilerinizi arayarak randevu öneririz.'),
        dict(icon='phone', name='Servis öncesi teyit', text='Ziyaretten önce müşteriyi arar, adres ve saati teyit ederiz.'),
        dict(icon='star', name='Servis sonrası memnuniyet', text='Servis sonrası memnuniyeti ölçer, sorunları aynı gün size iletiriz.'),
        dict(icon='moon', name='Mesai dışı acil hat', text='Gece ve hafta sonu gelen acil arızaları nöbetçi teknisyeninize yönlendiririz.'),
    ],
    flow_title='Bir arıza kaydı bizde böyle ilerler',
    flow=[
        dict(name='Arama', text='Müşteri servisinizin adıyla karşılanır.'),
        dict(name='Kayıt', text='Cihaz, arıza ve adres bilgileri eksiksiz alınır.'),
        dict(name='Randevu', text='Teknisyen takvimine göre randevu verilir.'),
        dict(name='Teyit', text='Ziyaret öncesi müşteriden teyit alınır.'),
        dict(name='Kapanış', text='Servis sonrası memnuniyet sorulur, kayıt kapanır.'),
    ],
    qa=[
        dict(q='Arıza kaydını doğru almak neden önemli?', p=[
            'Eksik ya da yanlış alınan arıza bilgisi, teknisyenin yanlış parçayla gitmesine ve ikinci bir ziyarete neden olur. Model, seri numarası ve arıza belirtisini kontrol listesiyle alan bir hat, ilk ziyarette çözüm oranını artırır.']),
        dict(q='Periyodik bakım aramaları nasıl planlanır?', p=[
            'Kombi ve klima gibi cihazlarda yıllık bakım hem güvenlik hem verim için önemlidir. Servis kayıtlarınızdan bakım zamanı gelen müşteriler listelenir, sezon yoğunluğundan önce aranarak randevu verilir.',
            'Mevcut müşteriye kullandığı ürünün bakımıyla ilgili yapılan bu aramalar, kampanya aramalarından ayrı tutulur.']),
        dict(q='Sezon yoğunluğu nasıl karşılanır?', p=[
            'Kış başında kombi, yaz başında klima arızaları kısa sürede artar. Bu dönemlerde ekibi hacme göre büyütür, telefonda bekleme süresini düşük tutarız.']),
    ],
    why=['7/24 arıza kaydı', 'Kontrol listesiyle eksiksiz kayıt', 'Sezonda esnek kapasite', 'Bakım hatırlatmayla düzenli iş'],
    faq_title='Teknik servis çağrı merkezi hakkında',
    faq=[
        dict(q='Servis yazılımımızı kullanabilir misiniz?', a='Evet. Servis takip yazılımınıza yetkili kullanıcı olarak erişir, kayıtları doğrudan sisteminize açarız.'),
        dict(q='Birden fazla bölge ve bayi için çalışır mısınız?', a='Evet. Kayıtları adrese göre doğru bölgeye ya da yetkili servise yönlendiririz.'),
        dict(q='Ücretli servis bilgisini telefonda veriyor musunuz?', a='Sizin belirlediğiniz servis ücreti ve garanti kurallarını müşteriye net bir şekilde iletiriz.'),
        dict(q='Garanti kayıtlarını kontrol edebilir misiniz?', a='Erişim verdiğiniz sistemlerden garanti durumunu kontrol edebiliriz.'),
        faq_kurulum(),
    ],
    related=[dict(url='/hizmetler/teknik-destek-hatti/', name='Teknik destek hattı'), dict(url='/hizmetler/randevu-ve-rezervasyon-yonetimi/', name='Randevu yönetimi'), dict(url='/hizmetler/memnuniyet-ve-anket-aramalari/', name='Servis memnuniyeti'), FIYAT, TEKLIF],
    cta_title='Arıza hattınız sezon boyunca açık kalsın.', cta_text='Teknisyen sayınızı ve aylık arıza kaydı hacminizi paylaşın; teklifimizi iletelim.')),

# ---------------------------------------------------------------- Restoran
dict(path=S + 'restoran-ve-franchise/restoran-siparis-ve-franchise-cagri-merkezi/', name='Restoran ve franchise çağrı merkezi', sector='Restoran ve franchise', og_image='hero-temsilci',
     audience='Zincir restoranlar ve franchise merkezleri',
     title='Restoran Sipariş Hattı ve Franchise Çağrı Merkezi | Karelima',
     description='Zincir restoranlar için merkezi sipariş hattı, şikâyet ve şube memnuniyeti aramaları; franchise merkezleri için bayilik başvurusu karşılama.',
     d=dict(
    eyebrow='Sektörler · Restoran ve franchise', h1='Zincir restoranlar ve franchise merkezleri için çağrı merkezi',
    answer='Karelima; zincir restoranlar için merkezi sipariş ve rezervasyon hattını, şikâyet ve öneri hattını yönetir, şube bazlı memnuniyet aramaları yapar. Franchise merkezleri için bayilik başvurularını karşılar, ön bilgileri toplar ve görüşme randevusu verir. Tüm şubelerin geri bildirimleri tek raporda toplanır.',
    facts=['Merkezi sipariş hattı', 'Şikâyet ve öneri hattı', 'Şube memnuniyeti', 'Franchise başvuruları'],
    illus='illus/restoran.svg',
    tasks_title='Restoran ve franchise ağında üstlendiğimiz işler', tasks_sub='Şubeleriniz mutfağa ve servise odaklanırken telefon tarafı merkezi ve tutarlı yönetilir.',
    tasks=[
        dict(icon='phone', name='Merkezi sipariş hattı', text='Telefon siparişlerini alır, müşterinin adresine en yakın şubeye iletiriz.'),
        dict(icon='cal', name='Rezervasyon', text='Masa ve grup rezervasyonlarını şube takvimine işleriz.'),
        dict(icon='chat', name='Şikâyet ve öneri hattı', text='Şikâyetleri kayda alır, şubeye ve merkeze aynı gün iletir, çözümü takip ederiz.'),
        dict(icon='star', name='Şube memnuniyet aramaları', text='Sipariş sonrası kısa memnuniyet aramalarıyla şube performansını ölçeriz.'),
        dict(icon='users', name='Franchise başvuruları', text='Bayilik başvurusu yapan adayların ön bilgilerini toplar, görüşme randevusu veririz.'),
        dict(icon='chart', name='Şube raporu', text='Şikâyet, memnuniyet ve sipariş verilerini şube bazında raporlarız.'),
    ],
    flow_title='Bir şikâyet bizde böyle ilerler',
    flow=[
        dict(name='Kayıt', text='Müşterinin şikâyeti, şube ve sipariş bilgisiyle kaydedilir.'),
        dict(name='İletim', text='Kayıt aynı gün şubeye ve merkeze iletilir.'),
        dict(name='Geri dönüş', text='Belirlenen sürede müşteriye çözümle dönülür.'),
        dict(name='Takip', text='Çözüm sonrası müşteri memnuniyeti sorulur.'),
        dict(name='Rapor', text='Şube bazında tekrar eden sorunlar raporlanır.'),
    ],
    qa=[
        dict(q='Merkezi sipariş hattı neden işe yarar?', p=[
            'Şubeler yoğun saatlerde telefonu açmakta zorlanır; çalan telefon hem siparişi kaçırır hem mutfağın düzenini bozar. Merkezi bir hat, siparişi doğru şubeye ileterek şubelerin yalnızca hazırlığa odaklanmasını sağlar.']),
        dict(q='Şube memnuniyetini telefonla ölçmek neden önemli?', p=[
            'Olumsuz deneyim yaşayan müşterilerin çoğu şikâyet etmez, yalnızca bir daha gelmez ya da internette yorum yazar. Düzenli memnuniyet aramaları sorunları yorumlara yansımadan önce yakalamanızı ve şubeler arasında karşılaştırma yapmanızı sağlar.']),
        dict(q='Franchise başvurularını nasıl yönetiyorsunuz?', p=[
            'Bayilik başvurusu yapan adaylar hızlı ve profesyonel bir dönüş bekler. Adayı arar; bölge, yatırım bütçesi, lokasyon ve deneyim bilgilerini toplar, uygun adaylar için franchise ekibinize görüşme randevusu veririz.']),
    ],
    why=['Tüm şubeler için tek hat', 'Şikâyete aynı gün aksiyon', 'Şube bazlı karşılaştırmalı rapor', 'Franchise adaylarına hızlı dönüş'],
    faq_title='Restoran ve franchise çağrı merkezi hakkında',
    faq=[
        dict(q='Sipariş sistemimize kayıt yapabilir misiniz?', a='Evet. Sipariş ve şube yönetim sisteminize yetkili kullanıcı olarak erişebilir ya da siparişi şubeye anlık iletebiliriz.'),
        dict(q='Kaç şube için hizmet verebilirsiniz?', a='Şube sayısından bağımsız olarak çalışırız; hacme göre ekip büyüklüğünü belirleriz.'),
        dict(q='Yemek siparişi platformlarındaki yorumları takip ediyor musunuz?', a='Platform panellerine erişim verirseniz yorumları takip edip şikâyetleri kayda alabiliriz.'),
        dict(q='Kampanya duyuruları için arama yapıyor musunuz?', a='Yalnızca İYS onayı bulunan müşterilerinizi kampanya ve açılış duyuruları için arayabiliriz.'),
        faq_kurulum(),
    ],
    related=[dict(url='/hizmetler/memnuniyet-ve-anket-aramalari/', name='Memnuniyet aramaları'), dict(url='/hizmetler/whatsapp-ve-canli-destek/', name='WhatsApp sipariş ve destek'), dict(url='/hizmetler/gelen-cagri-yonetimi/', name='Gelen çağrı yönetimi'), FIYAT, TEKLIF],
    cta_title='Tüm şubeleriniz için tek, tutarlı bir hat.', cta_text='Şube sayınızı ve günlük çağrı hacminizi paylaşın; çalışma planımızı iletelim.')),

# ---------------------------------------------------------------- Enerji
dict(path=S + 'enerji/ges-ve-enerji-firmalari-cagri-merkezi/', name='GES ve enerji firmaları çağrı merkezi', sector='Enerji', og_image='operasyon-merkezi',
     audience='GES kurulum firmaları, enerji tedarikçileri, tesisat firmaları',
     title='GES Kurulum ve Enerji Firmaları için Çağrı Merkezi | Karelima',
     description='Güneş enerjisi (GES) taleplerini arıyor, keşif randevusu veriyor, teklif takibi yapıyoruz. Enerji tedarikçileri için abone hizmetleri hattı.',
     d=dict(
    eyebrow='Sektörler · Enerji', h1='GES kurulum ve enerji firmaları için çağrı merkezi',
    answer='Karelima; güneş enerjisi (GES) kurulum firmalarına gelen talepleri arar, çatı, tüketim ve bütçe bilgileriyle ön eleme yapar ve keşif randevusu verir. Teklif sonrası takip aramalarıyla kararı hızlandırır. Enerji tedarik ve tesisat firmaları için abone hizmetleri ve randevu hattını yönetir.',
    facts=['Talebe hızlı dönüş', 'Ön eleme', 'Keşif randevusu', 'Teklif takibi'],
    illus='illus/enerji.svg',
    tasks_title='Enerji sektöründe üstlendiğimiz işler', tasks_sub='Satış mühendisleriniz keşif ve projeye odaklanırken ilk temas bizde.',
    tasks=[
        dict(icon='phone', name='GES talebi arama', text='Web ve reklamdan gelen talepleri saniyeler içinde arar, ihtiyacı netleştiririz.'),
        dict(icon='doc', name='Ön eleme', text='Mülk tipi, çatı alanı, aylık fatura ve bütçe gibi bilgileri toplarız.'),
        dict(icon='cal', name='Keşif randevusu', text='Uygun talepler için keşif ekibinizin takvimine randevu veririz.'),
        dict(icon='clock', name='Teklif takibi', text='Teklif verilen müşteriyi belirlenen aralıklarla arar, soruları ve kararı öğreniriz.'),
        dict(icon='users', name='Abone hizmetleri hattı', text='Enerji tedarik firmalarının abone başvuru, fatura ve bilgi çağrılarını karşılarız.'),
        dict(icon='chart', name='Kaynak bazlı rapor', text='Talep, keşif ve sözleşme sayılarını kaynak bazında raporlarız.'),
    ],
    flow_title='Bir GES talebi bizde böyle ilerler',
    flow=[
        dict(name='Talep', text='Form ya da reklam talebi Karelima CRM\'e düşer.'),
        dict(name='Hızlı arama', text='Kişi saniyeler içinde aranır.'),
        dict(name='Ön eleme', text='Mülk, tüketim ve bütçe bilgileri alınır.'),
        dict(name='Keşif', text='Uygun talep için keşif randevusu verilir.'),
        dict(name='Takip', text='Teklif sonrası takip aramaları yapılır, sonuç raporlanır.'),
    ],
    qa=[
        dict(q='GES taleplerinde ön eleme neden önemli?', p=[
            'Güneş enerjisi talebi bırakan herkes kurulum için uygun değildir: kiracı olabilir, çatı uygun olmayabilir ya da yalnızca fiyat araştırıyor olabilir. Keşif ekibini her talebe göndermek zaman ve maliyet kaybıdır.',
            'Kısa bir ön eleme görüşmesi, keşif ekibinizin yalnızca gerçekten uygun projelere gitmesini sağlar.']),
        dict(q='Teklif takibi neden satışı artırır?', p=[
            'Yüksek tutarlı yatırımlarda müşteri kararını vermeden önce birden fazla teklif karşılaştırır. Teklif sonrası düzenli ve bilgilendirici takip aramaları, soruların cevapsız kalmasını önler ve kararın sizin lehinize verilmesine yardımcı olur.']),
        dict(q='Enerji tedarik firmaları için hangi hizmetleri veriyorsunuz?', p=[
            'Abone başvurusu, fatura bilgilendirme ve genel bilgi çağrılarını karşılarız. Bu alanda EPDK\'nın tüketici hizmetlerine ilişkin düzenlemeleri çağrı merkezi hizmet seviyesi ve kayıt konularında yükümlülükler getirebilir; hizmet seviyesi hedeflerini bu yükümlülüklere göre birlikte belirleriz.']),
    ],
    law=dict(title='İzinli iletişim', text=IYS),
    why=['Talebe saniyeler içinde dönüş', 'Keşif ekibinin zamanı korunur', 'Düzenli teklif takibi', 'Kaynak bazlı rapor'],
    faq_title='Enerji sektörü çağrı merkezi hakkında',
    faq=[
        dict(q='Temsilciler teknik GES sorularını yanıtlayabilir mi?', a='Temel bilgilendirme sorularını onaylı yanıtlarla karşılarız; teknik ve fiyat detayları mühendislerinize aktarılır.'),
        dict(q='Birden fazla il için keşif planlayabilir misiniz?', a='Evet. Talepleri bölgeye göre ayırır, her bölgenin keşif ekibine ayrı randevu veririz.'),
        dict(q='Tarımsal ve sanayi GES projeleri için de çalışır mısınız?', a='Evet. Ön eleme sorularını konut, tarım ve sanayi projelerine göre ayrı ayrı hazırlarız.'),
        dict(q='Fiyatlandırma nasıl?', a='Talep başı, temsilci başı ya da randevu başı prim içeren karma modeller sunuyoruz.'),
        faq_kurulum(),
    ],
    related=[dict(url='/hizmetler/lead-ve-talep-yonetimi/', name='Lead ve talep yönetimi'), dict(url='/hizmetler/randevu-ve-rezervasyon-yonetimi/', name='Keşif randevusu'), dict(url='/hizmetler/dis-arama-ve-telesatis/', name='Teklif takibi'), FIYAT, TEKLIF],
    cta_title='GES taleplerinizi aynı gün keşfe çevirelim.', cta_text='Aylık talep hacminizi ve hizmet bölgelerinizi paylaşın; teklifimizi iletelim.')),

# ---------------------------------------------------------------- Lojistik
dict(path=S + 'lojistik-ve-kargo/lojistik-ve-kargo-cagri-merkezi/', name='Lojistik ve kargo çağrı merkezi', sector='Lojistik ve kargo', og_image='operasyon-merkezi',
     audience='Kargo, nakliye, kurye ve beyaz eşya/mobilya teslimat firmaları',
     title='Lojistik ve Kargo Firmaları için Çağrı Merkezi | Karelima',
     description='Gönderi sorgulama, teslimat randevusu, hasar ve şikâyet kaydı. Kargo, nakliye ve kurye firmaları için 7/24 müşteri hizmetleri hattı.',
     d=dict(
    eyebrow='Sektörler · Lojistik ve kargo', h1='Lojistik, kargo ve nakliye firmaları için çağrı merkezi',
    answer='Karelima; kargo, nakliye ve kurye firmalarının gönderi sorgulama, teslimat randevusu, adres değişikliği, hasar ve şikâyet çağrılarını 7/24 karşılar. Takip sisteminizden gönderinin durumunu kontrol eder, büyük ve hacimli teslimatlarda müşteriyle randevu planlar, şikâyetleri takip numarasıyla yönetir.',
    facts=['Gönderi sorgulama', 'Teslimat randevusu', 'Hasar ve şikâyet kaydı', '7/24 hat'],
    illus='illus/lojistik.svg',
    tasks_title='Lojistikte üstlendiğimiz işler', tasks_sub='Operasyon ekibiniz dağıtıma odaklanırken müşteri soruları bizde.',
    tasks=[
        dict(icon='doc', name='Gönderi sorgulama', text='Takip numarasıyla gönderinin durumunu sisteminizden kontrol eder, müşteriyi bilgilendiririz.'),
        dict(icon='cal', name='Teslimat randevusu', text='Beyaz eşya, mobilya ve hacimli gönderilerde müşteriyle teslimat günü ve saatini planlarız.'),
        dict(icon='in', name='Adres ve teslimat değişikliği', text='Adres ya da teslimat tercihi değişikliklerini kurallarınıza göre işleriz.'),
        dict(icon='shield', name='Hasar ve kayıp kaydı', text='Hasarlı ya da kayıp gönderi bildirimlerini eksiksiz kaydeder, süreci takip ederiz.'),
        dict(icon='out', name='Teslim edilemeyen gönderiler', text='Teslim edilemeyen gönderiler için alıcıyı arar, yeni teslimat planlarız.'),
        dict(icon='chart', name='Şikâyet raporu', text='Şikâyet konularını bölge ve şube bazında raporlarız.'),
    ],
    flow_title='Bir teslimat randevusu bizde böyle ilerler',
    flow=[
        dict(name='Liste', text='Randevu gerektiren gönderiler günlük olarak paylaşılır.'),
        dict(name='Arama', text='Alıcı aranır, uygun gün ve saat aralığı alınır.'),
        dict(name='Planlama', text='Randevu dağıtım planınıza işlenir.'),
        dict(name='Teyit', text='Teslimattan önce alıcıya hatırlatma yapılır.'),
        dict(name='Rapor', text='Teslim ve başarısız teslim oranları raporlanır.'),
    ],
    qa=[
        dict(q='Teslimat randevusu neden önemli?', p=[
            'Hacimli gönderilerde alıcı evde olmadığında araç boşuna gider, teslimat ertesi güne kalır ve maliyet artar. Önceden planlanan ve teyit edilen teslimat randevusu, başarısız teslimat sayısını azaltır.']),
        dict(q='Kampanya dönemlerinde çağrı yoğunluğu nasıl karşılanır?', p=[
            'E-ticaret kampanya dönemlerinde gönderi sayısıyla birlikte sorgulama çağrıları da artar. Bu dönemlerde ekibi hacme göre büyütür, bekleme süresini düşük tutarız.']),
        dict(q='Hangi sistemlerle çalışırsınız?', p=[
            'Gönderi takip ve operasyon sistemlerinize yetkili kullanıcı olarak erişebiliriz. Gerekirse kayıtları API ile sisteminize aktarırız.']),
    ],
    why=['7/24 gönderi sorgulama', 'Daha az başarısız teslimat', 'Takip numaralı şikâyet yönetimi', 'Kampanya döneminde esnek kapasite'],
    faq_title='Lojistik çağrı merkezi hakkında',
    faq=[
        dict(q='Kurumsal göndericilere destek veriyor musunuz?', a='Evet. Kurumsal müşterileriniz için ayrı karşılama ve öncelik kuralları tanımlayabiliriz.'),
        dict(q='Hasar tazmin sürecini yürütüyor musunuz?', a='Hasar bildirimini kaydeder ve süreci takip ederiz; tazmin kararı sizin yetkili biriminizde kalır.'),
        dict(q='Kuryelerle iletişim kurabilir misiniz?', a='Tanımlı kurallar çerçevesinde dağıtım ekibinize ya da şubeye bilgi iletebiliriz.'),
        dict(q='Sadece mesai dışı hizmet alabilir miyiz?', a='Evet. Gece ve hafta sonu hattı için ayrıca hizmet alabilirsiniz.'),
        faq_kurulum(),
    ],
    related=[dict(url='/sektorler/e-ticaret-ve-perakende/e-ticaret-cagri-merkezi/', name='E-ticaret çağrı merkezi'), dict(url='/hizmetler/randevu-ve-rezervasyon-yonetimi/', name='Teslimat randevusu'), dict(url='/hizmetler/gelen-cagri-yonetimi/', name='Gelen çağrı yönetimi'), FIYAT, TEKLIF],
    cta_title='Gönderi sorularınızı 7/24 karşılayalım.', cta_text='Günlük gönderi ve çağrı hacminizi paylaşın; çalışma planımızı iletelim.')),

# ---------------------------------------------------------------- Finans
dict(path=S + 'finans/finans-cagri-merkezi/', name='Finans çağrı merkezi', sector='Finans', og_image='operasyon-merkezi',
     audience='Ödeme kuruluşları, finansman ve leasing şirketleri, aracı kurumlar',
     title='Finans Sektörü için Çağrı Merkezi Hizmeti | Karelima',
     description='Ödeme kuruluşları, finansman ve leasing şirketleri için bilgi hattı, başvuru takibi, ödeme hatırlatma ve memnuniyet aramaları. Kayıtlı ve denetlenebilir süreç.',
     d=dict(
    eyebrow='Sektörler · Finans', h1='Finans sektörü için çağrı merkezi hizmeti',
    answer='Karelima; ödeme kuruluşları, finansman ve leasing şirketleri ile aracı kurumlar için bilgi hattı, başvuru takibi, eksik belge tamamlama, ödeme hatırlatma ve memnuniyet aramaları yapar. Tüm görüşmeler kayıt altındadır; yetki, erişim ve bilgi güvenliği kuralları sözleşmeyle tanımlanır.',
    facts=['Bilgi hattı', 'Başvuru ve belge takibi', 'Ödeme hatırlatma', 'Kayıtlı ve denetlenebilir'],
    illus='illus/finans.svg',
    tasks_title='Finans sektöründe üstlendiğimiz işler', tasks_sub='Müşteri temasının kurallı, kayıtlı ve tutarlı yürüdüğü bir operasyon.',
    tasks=[
        dict(icon='phone', name='Bilgi hattı', text='Ürün, başvuru koşulları ve süreç sorularını onaylı metinlerle yanıtlarız.'),
        dict(icon='doc', name='Başvuru ve belge takibi', text='Başvurusu eksik olan müşteriyi arar, belge ve bilgileri tamamlatırız.'),
        dict(icon='clock', name='Ödeme hatırlatma', text='Vadesi yaklaşan ve geciken ödemeler için kibar ve kayıtlı hatırlatma yaparız.'),
        dict(icon='shield', name='Kimlik doğrulama adımları', text='Görüşmelerde sizin belirlediğiniz doğrulama adımlarını eksiksiz uygularız.'),
        dict(icon='star', name='Memnuniyet aramaları', text='Başvuru ve hizmet sonrası müşteri memnuniyetini ölçeriz.'),
        dict(icon='chart', name='Denetim raporları', text='Görüşme kayıtları, sonuçlar ve hizmet seviyeleri denetime hazır şekilde raporlanır.'),
    ],
    flow_title='Bir başvuru takibi bizde böyle ilerler',
    flow=[
        dict(name='Liste', text='Eksik başvurular günlük olarak paylaşılır.'),
        dict(name='Doğrulama', text='Müşteri aranır, kimlik doğrulama adımları uygulanır.'),
        dict(name='Tamamlama', text='Eksik bilgi ve belgeler için yönlendirme yapılır.'),
        dict(name='İletim', text='Tamamlanan başvuru ilgili birime iletilir.'),
        dict(name='Rapor', text='Tamamlanma oranları ve süreler raporlanır.'),
    ],
    qa=[
        dict(q='Finans kuruluşları çağrı merkezi hizmetini dışarıdan alabilir mi?', p=[
            'Alabilir; ancak bankalar ve ödeme kuruluşları gibi düzenlemeye tabi kurumların dış hizmet alımı, BDDK ve TCMB gibi otoritelerin ilgili düzenlemelerine tabi olabilir. Destek hizmeti alımına ilişkin bu kurallar; sözleşme, denetim, bilgi güvenliği ve hizmet seviyesi konularında yükümlülükler getirir.',
            'Projeye başlamadan önce kurumunuzun uyum ekibiyle bu gereklilikleri birlikte değerlendirir, çalışma modelini buna göre kurarız.']),
        dict(q='Görüşmelerde hangi bilgiler paylaşılır?', p=[
            'Temsilciler yalnızca sizin onayladığınız ürün ve süreç bilgilerini paylaşır. Kişiye özel bilgiler, tanımlı kimlik doğrulama adımları tamamlanmadan konuşulmaz; kart ve şifre bilgisi telefonda alınmaz.']),
        dict(q='Kayıt ve denetim nasıl sağlanıyor?', p=[
            'Tüm görüşmeler kaydedilir, saklama süreleri sözleşmede belirlenir. Kalite ekibimiz görüşmeleri düzenli dinler; denetim ve inceleme taleplerinde kayıtlar ve raporlar sizinle paylaşılır.']),
    ],
    law=dict(title='Uyum ve bilgi güvenliği', text='Düzenlemeye tabi kurumların dış hizmet alımında ilgili otorite düzenlemeleri esas alınır. Kart ve şifre bilgisi telefonda alınmaz; kişisel veriler KVKK\'ya uygun işlenir.'),
    why=['Kayıtlı ve denetlenebilir süreç', 'Onaylı metinlerle tutarlı bilgi', 'Kimlik doğrulama disiplini', 'Uyum ekibinizle birlikte kurulum'],
    faq_title='Finans çağrı merkezi hakkında',
    faq=[
        dict(q='Bankalar için de hizmet veriyor musunuz?', a='Bankaların dış hizmet alımı özel düzenlemelere tabidir. Kapsamı ve uygunluğu bankanın uyum ekibiyle birlikte değerlendiriyoruz.'),
        dict(q='Telefonda ödeme alıyor musunuz?', a='Hayır. Kart bilgisi telefonda alınmaz; müşteriye kurumunuzun güvenli ödeme kanalları iletilir.'),
        dict(q='Kredi ya da yatırım tavsiyesi veriyor musunuz?', a='Hayır. Temsilcilerimiz tavsiye vermez; yalnızca onaylı ürün ve süreç bilgilerini paylaşır.'),
        dict(q='Görüşme kayıtları ne kadar saklanıyor?', a='Saklama süreleri mevzuat ve sizin politikanıza göre sözleşmede belirlenir.'),
        faq_kurulum('Uyum değerlendirmesinin ardından standart kurulum ve eğitim 10 iş gününde tamamlanır.'),
    ],
    related=[dict(url='/hizmetler/odeme-hatirlatma/', name='Ödeme hatırlatma'), dict(url='/hizmetler/back-office-operasyonlari/', name='Back office'), dict(url='/sektorler/sigorta/sigorta-cagri-merkezi/', name='Sigorta çağrı merkezi'), FIYAT, TEKLIF],
    cta_title='Kurallı ve kayıtlı bir müşteri hattı kuralım.', cta_text='Hizmet kapsamınızı ve uyum gerekliliklerinizi paylaşın; çalışma modelimizi birlikte belirleyelim.')),
]
