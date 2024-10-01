import json
import os

import requests
from dotenv import load_dotenv

load_dotenv("../.env")
API_KEY = json.loads(os.getenv("API_KEY"))


def currency_conversion(transaction_data: dict) -> float:
    """Функция, которая конвертирует остальную валюту в рубли"""
    amount = transaction_data["operationAmount"]["amount"]
    code = transaction_data["operationAmount"]["currency"]["code"]
    if transaction_data["operationAmount"]["currency"]["code"] == "RUB":
        return amount
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from{code}&amount={amount}"
        response = requests.get(url, headers=API_KEY)
        result = response.json()
        data = result.get("result")
        return data
