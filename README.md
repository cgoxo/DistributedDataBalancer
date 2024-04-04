# DistributedDataBalancer

## Description
This project is a distributed system that enables low storage devices to train image data on the device itself, without requiring large amounts of local storage. The system utilizes Apache Kafka to distribute batches of images to worker nodes, which then send the images to a head node for model training.

## Installation
- Clone the repository
- Install dependencies using `pip3 install kafka-python`
- Download and setup kafka locally and use RedPanda to create consumer groups

## Usage
- Run the consumer nodes using `python consumer.py`
- Run the head node using `python producer.py`

## Technologies Used
- Apache Kafka
- Redpanda
- Machine Learning
- Image Processing
- Distributed Systems

## Architecture
The system consists of three consumer nodes with one kafka broker and one head node. The consumer nodes read images from the local device and send them to the Kafka broker based on the read write speeds in the consumer nodes, which distributes the images to the head node for training.
