import json
import os

import requests
from dotenv import load_dotenv

from src.utils import get_json_file

load_dotenv("../.env")


def currency_conversion() -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    transaction_data = get_json_file(r"C:\Users\Ivan\PycharmProjects\home_project_three\data\operations.json")
    amount = transaction_data["operationAmount"]["amount"]
    code = transaction_data["operationAmount"]["currency"]["code"]
    if transaction_data["operationAmount"]["currency"]["code"] == "RUB":
        return amount
    else:
        api_opener = os.getenv("API_KEY")
        headers = {"apikey": api_opener}
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from{code}&amount={amount}"
        response = requests.get(url, headers=headers)
        result = response.json()
        return result
