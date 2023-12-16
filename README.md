## Homework 8.01: MongoDB, RabbitMQ, and Redis
Introduction
This project focuses on integrating MongoDB Atlas for cloud-based data storage, RabbitMQ for message queuing, and Redis for caching. The task is divided into two main parts:

Part 1: MongoDB Integration
1.1 MongoDB Setup
Create a MongoDB Atlas cloud database.
Utilize the ODM Mongoengine to define models for storing data from provided JSON files (authors.json and quotes.json).
Ensure that the "author" field in the "quotes" collection references the "authors" collection via the ObjectID.
1.2 Data Loading Scripts
Develop scripts for loading data from JSON files into the MongoDB Atlas database.
1.3 Search Script
Implement a script allowing users to search for quotes based on author names, tags, or a combination of tags.
The script should run in an infinite loop, accepting input commands.
Additional Task (Optional)
Implement shortened versions for the search commands, e.g., "name:st" for "name:Steve Martin" and "tag:li" for "tag:life."
Part 2: RabbitMQ Integration
2.1 Contact Model
Create a model for storing contact information, including full name, email, and a boolean field indicating whether a message has been sent.
2.2 Producer Script
Develop a script (producer.py) that generates fake contacts, saves them to the MongoDB database, and places messages containing ObjectIDs into a RabbitMQ queue.
2.3 Consumer Script
Implement a consumer script (consumer.py) that retrieves messages from the RabbitMQ queue, simulates sending email messages, and updates the "message_sent" field in the MongoDB database.
Additional Task (Optional)
Introduce additional contact details like phone numbers and a field indicating the preferred method of communication (SMS or email).
Create separate consumer scripts (consumer_sms.py and consumer_email.py) for handling SMS and email messages.
Installation and Dependencies
MongoDB Atlas: Set up a cloud-based MongoDB instance and obtain connection details.
RabbitMQ: Install RabbitMQ locally and configure credentials.
Redis: Install and configure Redis locally.
Python Packages: Install required Python packages using pip install -r requirements.txt.
Usage
Execute MongoDB and RabbitMQ services.
Run data loading scripts for MongoDB (load_mongo.py).
Run the search script for MongoDB (search_quotes.py).
Run the producer script for RabbitMQ (producer.py).
Run the consumer script for RabbitMQ (consumer.py).
Additional Features (Optional)
Shortened commands in search script for user convenience.
Caching search results using Redis.
