import os
import re
from collections import Counter

from src.utils import get_json_file

list_transactions = get_json_file(os.path.join("../data/operations.json"))


def return_list_dicts_with_transaction(list_dict: list, search_str: str) -> list:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    check_list = []
    for transaction in list_dict:
        if "description" in transaction and re.findall(search_str, transaction["description"]):
            check_list.append(transaction)
    return check_list


def sort_transactions(list_dict_select: list, categories: list) -> dict:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории
    """
    list_categories_transaction = []
    for transaction in list_dict_select:
        if "description" in transaction and transaction["description"] in categories:
            list_categories_transaction.append(transaction["description"])
    sort_transaction = Counter(list_categories_transaction)
    return dict(sort_transaction)


if __name__ == "__main__":
    categories_operations = [
        "Перевод организации",
        "Перевод с карты на карту",
        "Перевод с карты на счет",
        "Перевод со счета на счет",
        "Открытие вклада",
    ]
