from kafka import KafkaProducer
import json
import os
import base64

class MessageProducer:
    broker = ""
    topic = ""
    producer = None

    def __init__(self, broker, topic):
        self.broker = broker
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=self.broker,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            acks='all',
            retries=3
        )

    def send_msg(self, msg):
        print("Sending message...")
        try:
            future = self.producer.send(self.topic, msg)
            self.producer.flush()
            future.get(timeout=60)
            print("Message sent successfully...")
            return {'status_code': 200, 'error': None}
        except Exception as ex:
            return ex

def publish_images_in_folder(broker, topic1, topic2, folder_path):
    message_producer_topic1 = MessageProducer(broker, topic1)
    message_producer_topic2 = MessageProducer(broker, topic2)

    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, mode='rb') as file:
                img = file.read()
                data = {'name': filename}
                data['img'] = base64.encodebytes(img).decode('utf-8')

                # Send the image twice to topic1
                resp = message_producer_topic1.send_msg(data)
                resp = message_producer_topic1.send_msg(data)
                print(f"Published in topic_1: {filename}")
                print(resp)

                # Send the image once to topic2
                resp = message_producer_topic2.send_msg(data)
                print(f"Published in topic_2: {filename}")
                print(resp)

if __name__ == "__main__":
    broker = 'IP of kafka broker'
    topic1 = '{provide topic1 name}'
    topic2 = '{provide topic2 name}'
    folder_path = 'path/to/data'
    publish_images_in_folder(broker, topic1, topic2, folder_path)
