import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.utils import get_json_file, json_way

load_dotenv("../.env")
API_KEY = os.getenv("API_KEY")

payment = get_json_file(json_way)


def valuta_conversion(convert_from, amount) -> Any:
    """Функция, в которой происходит обращение к внешнему API для получения
    текущего курса валют и конвертации суммы операции в рубли"""
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={convert_from}&amount={amount}"

    headers = {"apikey": API_KEY}
    response = requests.request("GET", url, headers=headers)
    result = response.text
    return result


print(valuta_conversion("USD", "100000"))


def get_sum_amount() -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount_check = []
    convert_result = []
    for i in payment:
        if len(i) > 0:

            if i["operationAmount"]["currency"]["code"] != "RUB":
                convert_valuta = valuta_conversion(
                    i["operationAmount"]["currency"]["code"], i["operationAmount"]["amount"]
                )
                convert_result.append(convert_valuta)
            else:
                continue
        else:
            break

    for j in convert_result:
        if len(j) > 0:
            amount_check.append(float(j))
        else:
            break

    return sum(amount_check)


print(get_sum_amount())
