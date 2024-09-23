from typing import Any, Iterator

transactions_info = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions_info: list[dict], currency_info: str) -> Iterator[Any]:
    """Функция принимает список словарей, представляющих транзакции.
    а возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    for transaction in transactions_info:
        if transaction["operationAmount"]["currency"]["code"] == currency_info:
            yield transaction
        elif transactions_info == [] :
            yield "Введен пустой список"


usd_transactions = filter_by_currency(transactions_info, "USD")
for _ in range(2):
    print(next(usd_transactions))


def transaction_descriptions(transactions_info: list[dict], descriptions: str) -> Iterator[Any]:
    """Генератор, который принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""
  #  for descriptions in range(len(transactions_info)):
   #     yield transactions_info[descriptions]["description"]
    for d in transactions_info:
        if d.get("description") == descriptions:
            yield d
        elif d.get("description") != descriptions:
            yield "Перевед не был осуществлен"


for descriptions in range(len(transactions_info)):
    print(transactions_info[descriptions]["description"])


def card_number_generator(start: Any, end: Any) -> Iterator[Any]:
    """Генератор, который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX, где X — цифра номера карты"""
    while start < end:
            start += 1

            card_number = str(start)
            while len(card_number) < 16:
                card_number = "0" + card_number
                formatted_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[-8:-4]} {card_number[-4:]}"
            yield formatted_card_number


for card_number in card_number_generator(0, 9):
    print(card_number)
