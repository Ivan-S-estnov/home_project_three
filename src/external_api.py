import os

import requests
from dotenv import load_dotenv

load_dotenv()


def currency_conversion(transaction: dict) -> float:
    """Функция, которая переводит остальную валюту в рубли"""
    amount = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]
    if code == "RUB":
        return amount
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from{code}&amount={amount}"
        token_exchange = os.getenv("API_KEY_exchange")
        headers = {"apikey": token_exchange}
        response = requests.get(url, headers=headers)
        result = dict(response.json())
        return float(result["result"])
