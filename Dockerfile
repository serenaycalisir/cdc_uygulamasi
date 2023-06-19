# Base image
FROM python:3.9-slim

# Gerekli kütüphaneleri yükleme
RUN pip install pymongo kafka-python

# Uygulama dosyalarını imaj içine kopyalama
COPY app_a.py /app/app_a.py
COPY app_b.py /app/app_b.py

# Çalışma dizini ayarlama
WORKDIR /app

# Uygulamaları çalıştırma
CMD ["python", "app_a.py"]
