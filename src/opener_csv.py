import logging
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / "pandas_file" / "transactions.csv"
xlsx_path = BASE_DIR / "pandas_file" / "transactions_excel.xlsx"


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/transaction.log",
    filemode="w",
)
csv_xlsx_logger = logging.getLogger("transactions logs")


def transaction_csv_xlsx(path_file: Path) -> Any:
    """Функция считывает финансовые операции из csv-файла и excel-файла
    и выдает список словарей с транзакциями"""
    time_start = datetime.now()
    try:
        if path_file == "transactions.csv":
            with open(path_file):
                result_transaction_csv = pd.DictReader()
                csv_xlsx_logger.info("Считали csv-файл")
                return result_transaction_csv

        elif path_file == "transactions_excel.xlsx":
            result_transaction_xlsx = pd.read_excel(path_file)
            csv_xlsx_logger.info("Считали excel-файл")
            return result_transaction_xlsx

    except Exception as e:
        csv_xlsx_logger.error(f"Произошла ошибка {e}")
        return []

    finally:
        time_stop = datetime.now()
        csv_xlsx_logger.debug(f"Функция обработала данные за время {time_stop-time_start}")

    print(transaction_csv_xlsx(path_file))
