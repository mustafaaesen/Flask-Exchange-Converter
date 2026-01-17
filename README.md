

# Flask Döviz Çevirici

Flask Döviz Çevirici, Flask REST API kullanılarak geliştirilmiş bir döviz çevirme uygulamasıdır.
Uygulama, Frankfurter API üzerinden Euro (EUR) bazlı döviz kurlarını alır ve 30 farklı para birimi arasında çapraz kur hesaplaması yaparak dönüşüm sağlar.
Ayrıca güncel döviz kurlarını kullanıcıya tablo halinde sunar.

Projenin canlı çalışan halini görmek için aşağıdaki bağlantıyı ziyaret edebilirsiniz:
FlaskDövizÇevirici → https://exchangeconverter.pythonanywhere.com

---

## Proje Mimarisi

![Proje Mimarisi](screenshots/dovizcevirici.png)


## Proje Klasör Yapısı

```text
DÖVİZ ÇEVİRİCİ
│
├── app.py
├── .env
├── .gitignore
│
├── templates
│   └── index.html
│
├── static
│   ├── css
│   │   └── style.css
│   ├── js
│   │   └── main.js
│   └── images
│       ├── favicon.png
│       └── waves-bg.png
│
├── screenshots
│   └── dovizceviriciarch.png
│
└── __pycache__
```

## Proje Mimarisi

Bu proje frontend, backend ve harici API olmak üzere üç ana bileşenden oluşur.

Frontend katmanı HTML, CSS ve JavaScript kullanılarak geliştirilmiştir.
Kullanıcı frontend üzerinden güncel döviz kurlarını tablo halinde görebilir, istediği iki para birimini seçebilir ve girdiği tutara göre döviz dönüşümünü hesaplatabilir.
Kullanıcı etkileşimlerine bağlı olarak frontend, backend’e REST API isteği gönderir ve gelen sonucu arayüzde gösterir.

Backend katmanı Flask REST API mimarisi ile geliştirilmiştir.
Frontend’den gelen istekleri alır, Frankfurter API üzerinden EUR bazlı güncel döviz kurlarını çeker, seçilen para birimleri arasında çapraz kur hesaplamasını yapar ve hesaplanan sonucu JSON formatında frontend’e geri döndürür.

Harici veri kaynağı olarak Frankfurter API kullanılmıştır.
Frankfurter API Euro bazlı çalışır, ücretsizdir, API anahtarı gerektirmez ve güvenilir döviz kuru verisi sağlar.

---

## Çalışma Akışı

Kullanıcı frontend üzerinden döviz dönüşümü yapmak ister.
Frontend backend’e REST API isteği gönderir.
Backend Frankfurter API’den EUR bazlı döviz kurlarını alır.
Çapraz kur hesaplaması backend tarafında yapılır.
Hesaplanan sonuç frontend’e gönderilir.
Sonuç kullanıcıya arayüzde gösterilir.

---

## Kurulum ve Çalıştırma

Projeyi GitHub’dan klonlayın ve proje dizinine girin.

.env dosyası oluşturun ve içine yalnızca SECRET_KEY değişkenini ekleyin.

Uygulamayı python app.py komutu ile çalıştırın.

Tarayıcıdan http://127.0.0.1:5000 adresine giderek uygulamaya erişin.

---

## Notlar

Bu projede veritabanı kullanılmamaktadır.
API anahtarı gerektirmez.
.env dosyası GitHub’a eklenmez.
Proje eğitim ve portföy amaçlı geliştirilmiştir.


