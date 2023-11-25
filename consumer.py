from kafka import KafkaConsumer
from kafka import TopicPartition
import json
import sys
import base64
import time
import os



drive_name = "/dev/sda2"
def get_write_speed():
        st_to_write="faferfvjhgrf,bu,ferfreuu4fr37fbv,e8qlf83l8rqT@6ikg"
        start_timer=time.time()
        try:
            f=open('wrtcheck.txt','w')
            for k in range(0,100000):
                for q in st_to_write:
                    f.write(q)
            f.close()
            end_timer=time.time()
            size=os.stat("wrtcheck.txt")
            d=size.st_size//(end_timer-start_timer)
            os.remove('wrtcheck.txt')
            d=int(d)
            return (d)
        except:
            return "error"


bootstrap_server = '10.70.33.117:9092'

# Define the partition numbers you want to consume from
partition_numbers = [0]  # Change Plzz. [0,1] [1,2] [0,2]

# drive_name = "C:" # for windows
disk_speed = get_write_speed()

# Determine the topic based on disk_speed
if disk_speed >= 1000000:
    topic = 'hello_world.'
else:
    topic = 'topic_2'

# Initialize consumer variable and manually assign the partitions
consumer = KafkaConsumer(
    bootstrap_servers=bootstrap_server,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id="Consumer_Group_1"  # Change Plzz...
)

# Manually assign the partitions to consume from based on partition_numbers
partitions_to_assign = [TopicPartition(topic, partition_number) for partition_number in partition_numbers]
consumer.assign(partitions_to_assign)

data_dir = os.path.join(os.getcwd(), "data")

# Read and print messages from the assigned partitions
for msg in consumer:
    file_name = msg.value['name']
    img_data = base64.b64decode(msg.value['img'])

    # Store metadata in a dictionary
    metadata = {
        'filename': file_name,
        'topic': topic,
        'consumer_group': "Consumer_Group_1",  # Change Plzzz.
        'partition_number': msg.partition
    }

    with open(os.path.join(data_dir, file_name), mode='wb') as file:
        file.write(img_data)

    # Print metadata and a message indicating the file is saved
    print('Metadata:', metadata)

# Terminate the script
sys.exit()
