import json
from typing import Any


def get_json_file(file_opener: str) -> Any:
    """Функция принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях"""
    with open(file_opener) as operations:
        try:
            transaction_list = json.load(operations)
            return transaction_list

        except:
            return []


print(get_json_file(r"C:\Users\Ivan\PycharmProjects\home_project_three\data\operations.json"))
