import json
import time
from kafka import KafkaProducer
from pymongo import MongoClient

# MongoDB bağlantısı
mongo_client = MongoClient("mongodb://localhost:27017")
db = mongo_client["mydatabase"]
collection = db["mycollection"]

# Kafka bağlantısı
bootstrap_servers = ['localhost:9092']
topic = 'mytopic'
producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Son işlenen dökümanın id'sini takip etmek için değişken
last_processed_id = None

while True:
    # MongoDB'de yeni dökümanları sorgula
    new_documents = collection.find({'_id': {'$gt': last_processed_id}})
    for document in new_documents:
        # Kafka'ya JSON mesajı publish et
        producer.send(topic, document)
        print("Yeni döküman Kafka'ya gönderildi:", document)

        # Son işlenen dökümanın id'sini güncelle
        last_processed_id = document['_id']
    
    # 10 saniye bekle
    time.sleep(10)
