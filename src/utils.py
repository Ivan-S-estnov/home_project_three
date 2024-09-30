import json


def get_transaction() -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    try:
        with open("operations.json") as operations:
            try:
                transactions = json.loads(operations)
                return transactions
            except json.JSONDecodeError:
                print("Invalid JSON data")

    except FileNotFoundError as e:
        print(e)

    return transactions
