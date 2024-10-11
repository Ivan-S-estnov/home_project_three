import json
import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

BASE_DIR = Path(__file__).resolve().parent.parent
join_path = BASE_DIR / "data" / "operations.json"


def get_json_file(file_path: Path) -> Optional[list]:
    """Функция принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях"""

    try:
        logger.info("Принимаем путь до JSON-файла")
        with open(file_path, "r", encoding="utf-8") as json_file:
            try:
                transaction_list = json.load(json_file)
                if isinstance(transaction_list, list):
                    logger.info("Функция возвращает список словарей с данными о финансовых транзакциях")
                    return transaction_list
                else:
                    return []
            except json.JSONDecodeError as ex:
                logger.error(f"Произошла ошибка: {ex}")
                return []

    except FileNotFoundError as ex:
        logger.error(f"Файл не найден: {ex}")
        return []


print(get_json_file(file_path=BASE_DIR / "data" / "operations.json"))
