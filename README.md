<<<<<<< HEAD
# Homework 8.01: MongoDB, RabbitMQ, and Redis

## Introduction

# Homework 8.01: MongoDB, RabbitMQ, and Redis

## Introduction

This project focuses on integrating MongoDB Atlas for cloud-based data storage, RabbitMQ for message queuing, and Redis for caching. The task is divided into two main parts:

...

### Installation and Dependencies

Before running the scripts, ensure you have the following components installed and configured:

#### MongoDB Atlas

1. Set up a cloud-based MongoDB instance on [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. Obtain the connection details.

#### RabbitMQ

1. Install RabbitMQ locally or set it up on a server. Refer to the [official installation guide](https://www.rabbitmq.com/download.html).
2. Configure RabbitMQ credentials.

#### Redis

1. Install and configure Redis locally. Follow the instructions [here](https://redis.io/download).

#### Python Packages

Install the required Python packages using the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. **Start MongoDB and Redis services.**

2. **Run the application:**

    ```bash
    python main.py
    ```

3. **Enter search commands:**

   - To search by author name: `name:author_name`
   - To search by tags: `tags:tag1,tag2`
   - To search by a single tag: `tag:tag_name`
   
   Type `exit` to quit the application.

## Functions

### find_by_tag

- **Input:** `tag: str`
- **Output:** `List[str | None]`
- Finds quotes based on a single tag.

### find_by_tags

- **Input:** `tags: str`
- **Output:** `List[str | None]`
- Finds quotes based on multiple tags.

### find_by_author

- **Input:** `author: str`
- **Output:** `List[List[Any]]`
- Finds quotes by a specific author.

### search_quotes

- **Input:** `command: str`
- **Output:** Displays search results.
- Accepts user input commands and performs the corresponding search.

## How to Run

1. **Start MongoDB:**

    ```bash
    # Example command, adjust as needed
    mongod --dbpath /path/to/data/directory
    ```

2. **Start Redis:**

    ```bash
    # Example command, adjust as needed
    redis-server
    ```

3. **Run the application:**

    ```bash
    python main.py
    ```

## Additional Features (Optional)

### Shortened Commands

In the search script, you can use shortened commands for user convenience:

- `name:st` for `name:Steve Martin`
- `tag:li` for `tag:life`

### Caching with Redis

To enable caching of search results using Redis, uncomment the relevant sections in the search script (`search_quotes.py`). Ensure that Redis is running before executing the script.


