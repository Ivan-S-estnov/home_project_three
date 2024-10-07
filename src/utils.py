import json
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).resolve().parent.parent
join_path = BASE_DIR / "data" / "operations.json"


def get_json_file(file_path: Path) -> Optional[list]:
    """Функция принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях"""

    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            try:
                transaction_list = json.load(json_file)
                if isinstance(transaction_list, list):
                    return transaction_list
                else:
                    return []
            except json.JSONDecodeError:
                return []

    except FileNotFoundError:
        return []


print(get_json_file(file_path=BASE_DIR / "data" / "operations.json"))
