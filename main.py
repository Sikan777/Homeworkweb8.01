# Імпорт необхідних бібліотек та класів
from typing import List, Any
import redis
from redis_lru import RedisLRU
from models import Author, Quote

# Підключення до Redis та створення об'єкту RedisLRU для кешування
client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

# Декоратор для кешування результатів функцій
@cache
def find_by_tag(tag: str) -> list[str | None]:
    # Вивід інформації про пошук за тегом
    print(f"Find by {tag}")
    # Знаходження цитат за тегом
    quotes = Quote.objects(tags__iregex=tag)
    # Формування списку цитат
    result = [q.quote for q in quotes]
    return result

# Декоратор для кешування результатів функцій
@cache
def find_by_tags(tags: str) -> list[str | None]:
    # Вивід інформації про пошук за тегами
    print(f"Find by {tags}")
    results = []
    tags = tags.split(",")
    for a in tags:
        # Знаходження цитат за кожним тегом
        quotes = Quote.objects(tags__iregex=a)
        # Формування списку цитат для кожного тегу
        result = [q.quote for q in quotes]
        results.append(result)
    return results

# Декоратор для кешування результатів функцій
@cache
def find_by_author(author: str) -> list[list[Any]]:
    # Вивід інформації про пошук за автором
    print(f"Find by {author}")
    # Знаходження авторів за іменем або початковими літерами
    authors = Author.objects(fullname__iregex=author)
    result = {}
    for a in authors:
        # Знаходження цитат автора
        quotes = Quote.objects(author=a)
        # Формування списку цитат для кожного автора
        result[a.fullname] = [q.quote for q in quotes]
    return result

# Функція для виконання пошуку цитат за введеним користувачем запитом
def search_quotes(command):
    # Розділення команди на ключ та значення
    parts = command.split(":", 1)
    if len(parts) != 2:
        return

    key, value = parts
    key = key.strip()
    value = value.strip()

    # Виклик функції залежно від отриманого ключа
    if key == "name":
        result = find_by_author(value)
    elif key == "tags":
        result = find_by_tags(value)
    elif key == "tag":
        result = find_by_tag(value)
    else:
        print("Invalid command format. Use 'name:', 'tag:', or 'tags:'.")
        return

    # Виведення результату пошуку
    if result:
        print(f"RESULT:{result}")
    else:
        print("No value found for this query")

# Виконання пошуку цитат за користувацькими командами
if __name__ == "__main__":
    while True:
        command = input(
            "Invalid command format. Use 'name:', 'tag:', or 'tags:\nEnter command 'exit' to quit:\n>>>"
        )
        if command.lower() == "exit":
            break
        search_quotes(command)
