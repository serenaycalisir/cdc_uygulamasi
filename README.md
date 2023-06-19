# cdc_uygulamasi
# Apache Kafka ile Basit CDC Uygulaması Geliştirme Projesi

Bu proje, MongoDB veritabanında belirli bir koleksiyonda oluşan yeni dökümanları sorgulayarak Apache Kafka'ya JSON mesajları üreten ve bu mesajları tüketen basit bir CDC (Change Data Capture) uygulamasıdır. 
Uygulama Python programlama dili kullanılarak yazılmıştır.

## Gereksinimler

- Docker
- Docker Compose veya Kubernetes

## Kurulum

1. Bu Github repository'sini klonlayın.
2. Terminalde proje klasörüne gidin.
3. Docker Compose ile çalıştırmak için: 
docker-compose up
4. Kubernetes ortamına deploy etmek için: 
helm install my-cdc-app ./cdc-app-chart

## Kullanım

Uygulama başarıyla çalıştığında, A uygulaması belirli bir süre aralığında MongoDB'deki koleksiyonu sorgulayarak yeni dökümanları Kafka'ya publish eder. B uygulaması ise Kafka'dan gelen mesajları konsola yazdırır.

- A uygulaması (Mesaj Üreten Uygulama): app_a.py
- B uygulaması (Mesaj Tüketen Uygulama): app_b.py


## Katkıda Bulunma

1. Bu repository'yi fork edin.
2. Yeni bir branch oluşturun: `git checkout -b feature/your-feature`
3. Değişikliklerinizi commit edin: `git commit -m 'Add some feature'`
4. Branch'inize push yapın: `git push origin feature/your-feature`
5. Bir pull request oluşturun.

## Lisans

Bu proje [MIT Lisansı](LICENSE.md) altında lisanslanmıştır.
