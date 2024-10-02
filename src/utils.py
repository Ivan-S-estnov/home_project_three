import json
from typing import Any

json_way = r"C:\Users\Ivan\PycharmProjects\home_project_three\data\operations.json"


def get_json_file(json_way) -> Any:
    """Функция принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях"""
    try:
        with open(json_way, encoding="utf-8") as json_file:
            transaction_list = json.load(json_file)
    except json.JSONDecodeError as j:
        print(j)
    except FileNotFoundError as e:
        print(e)

    return transaction_list


print(get_json_file(json_way))