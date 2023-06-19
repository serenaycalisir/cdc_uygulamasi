from kafka import KafkaConsumer

# Kafka bağlantısı
bootstrap_servers = ['localhost:9092']
topic = 'mytopic'
consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers)

# Mesajları tüket
for message in consumer:
    print("Kafka'dan gelen mesaj:", message.value)
