"""
Задание
Условие: Добавить в задание с REST API ещё один тест,
в котором создаётся новый пост, а потом проверяется его наличие на сервере по полю «описание».
Подсказка: создание поста выполняется запросом к
https://test-stand.gb.ru/api/posts с передачей параметров title, description, content.

Что ещё можно почитать:
• Описание Wikipedia API
• Пример использования zeep
"""
import requests

import yaml

with open("config.yaml") as f:
    data = yaml.safe_load(f)


def get_notMe(token):
    resource = requests.get(data["url_posts"],
                            headers={"X-Auth-Token": token},
                            params={"owner": "notMe"})
    return resource.json()

def get_Me(token):
    resource = requests.get(data["url_posts"],
                            headers={"X-Auth-Token": token},
                           )
    return resource.json()