import os
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv

from src.utils import get_json_file

BASE_DIR = Path(__file__).resolve().parent.parent
join_path = BASE_DIR / "data" / "operations.json"

load_dotenv("../.env")
API_KEY = os.getenv("API_KEY")

payment = get_json_file(file_path=BASE_DIR / "data" / "operations.json")


def valuta_conversion(payment: Any):
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для
    получения текущего курса валют и конвертации суммы операции в рубли
    """
    valuta_code = payment["operationAmount"]["currency"]["code"]
    amount_check = payment["operationAmount"]["amount"]
    if valuta_code == "RUB":
        return round(float(amount_check),2)
    elif valuta_code != "RUB":
        response = requests.get(f"https://currate.ru/api/?get=rates&pairs={valuta_code}RUB&key={API_KEY}")
        result = response.json()
        transaction_result = result["data"]["USDRUB"]
        return round(float(amount_check) * float(transaction_result),2)


# convert_result = valuta_conversion(
#     {
#         "id": 41428829,
#         "state": "EXECUTED",
#         "date": "2019-07-03T18:35:29.512364",
#         "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
#     }
# )
#
#
# print(convert_result)
