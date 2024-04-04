from kafka import KafkaConsumer
from kafka import TopicPartition
import json
import sys
import base64
import os

bootstrap_server = '{provide kafka broker address and port number}'

# Define the partition numbers you want to consume from
partition_numbers = [0,1]  # Change Plzz. [0,1] [1,2] [2,3]

# Initialize consumer variable and manually assign the partitions
consumer = KafkaConsumer(
    bootstrap_servers=bootstrap_server,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id="Consumer_Group_0"  # Change Plzz...
)

# Manually assign the partitions to consume from based on partition_numbers
topic = 'hello_world.'  # Replace with your Kafka topic name

partitions_to_assign = [TopicPartition(topic, partition_number) for partition_number in partition_numbers]
consumer.assign(partitions_to_assign)

data_dir = os.path.join(os.getcwd(), "data")

metadata_list = []  # List to store metadata entries

# Read and print messages from the assigned partitions
for msg in consumer:
    file_name = msg.value['name']
    img_data = base64.b64decode(msg.value['img'])

    # Store metadata in a dictionary
    metadata = {
        'filename': file_name,
        'topic': topic,
        'consumer_group': "Consumer_Group_0",  # Change Plzzz.
        'partition_number': msg.partition
    }

    # Append metadata to the list
    # metadata_list.append(metadata)

    with open(os.path.join(data_dir, file_name), mode='wb') as file:
        file.write(img_data)

    # Print metadata and a message indicating the file is saved
    print('Metadata:', metadata)
    # print('{} File saved'.format(file_name))
    metadata_file_path = os.path.join(data_dir, 'metadata.json')
    with open(metadata_file_path, 'a') as metadata_file:
        json.dump(metadata, metadata_file, indent=4)

# Terminate the script
sys.exit()
