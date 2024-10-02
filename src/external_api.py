import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.utils import get_json_file, json_way

load_dotenv("../.env")


def currency_conversion() -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    transaction_data = get_json_file(json_way)
    amount = transaction_data["operationAmount"]["amount"]
    code = transaction_data["operationAmount"]["currency"]["code"]
    if transaction_data["operationAmount"]["currency"]["code"] == "RUB":
        return amount
    else:
        API_KEY = os.getenv("API_KEY")
        url = f"https://api.apilayer.com/currency_data/convert?base=RUB&symbols={code}&amount={amount}/"
        header = {"apikey": API_KEY}
        response = requests.get(url, headers=header)
        result = response.json()
        return result
