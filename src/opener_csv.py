import csv
import logging
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / "pandas_file" / "transactions.csv"
excel_path = BASE_DIR / "pandas_file" / "transactions_excel.xlsx"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../logs/transaction.log",
    filemode="w",
    encoding="utf-8",
)
csv_xlsx_logger = logging.getLogger("transactions.logs")


def open_csv(csv_path: Path) -> list[dict]:
    """Функция считывает финансовые операции из csv-файла и выдает список словарей с транзакциями"""
    remittance = []
    csv_xlsx_logger.info("Открываем csv-файл для чтения")
    try:
        with open(csv_path, encoding="utf-8") as file_csv:
            reader = csv.reader(file_csv, delimiter=";")
            next(reader)
            csv_xlsx_logger.info("Считали csv-файл")
            for row in reader:
                if row:
                    id_, state, date, amount, currence_name, currency_code, from_, to, description = row
                    remittance.append(
                        {
                            "id": str(id_),
                            "state": state,
                            "date": date,
                            "operationAmount": {
                                "amount": str(amount),
                                "currency": {"name": currence_name, "code": currency_code},
                            },
                            "description": description,
                            "from": from_,
                            "to": to,
                        }
                    )

    except Exception as e:
        csv_xlsx_logger.error(f"Произошла ошибка {e}")
        return []
    return remittance


print(open_csv(BASE_DIR / "pandas_file" / "transactions.csv"))


def open_xlsx(excel_path: Path) -> list[dict]:
    """Функция считывает финансовые операции из excel-файла и выдает список словарей с транзакциями"""
    remittance = []
    csv_xlsx_logger.info("Открываем excel-файл для чтения")
    try:
        excel_data = pd.read_excel(excel_path)
        len_, b = excel_data.shape
        csv_xlsx_logger.info("Считали excel-файл")
        for i in range(len_):
            if excel_data["id"][i]:
                remittance.append(
                    {
                        "id": str(excel_data["id"][i]),
                        "state": excel_data["state"][i],
                        "date": excel_data["date"][i],
                        "operationAmount": {
                            "amount": str(excel_data["amount"][i]),
                            "currency": {
                                "name": excel_data["currency_name"][i],
                                "code": excel_data["currency_code"][i],
                            },
                        },
                        "description": excel_data["description"][i],
                        "from": excel_data["from"][i],
                        "to": excel_data["to"][i],
                    }
                )
            else:
                continue
    except Exception as e:
        csv_xlsx_logger.error(f"Произошла ошибка {e}")
        return []
    return remittance


print(open_xlsx(BASE_DIR / "pandas_file" / "transactions_excel.xlsx"))
