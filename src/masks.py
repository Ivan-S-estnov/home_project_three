import logging
from venv import logger

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='masks.log',
                    filemode='w')
masks_logger = logging.getLogger('app.masks')



def get_mask_card_number(card_numb: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    try:
        masks_logger.info("Ввод номена карты")
        return f"{card_numb[:4]} {card_numb[4:6]}** **** {card_numb[-4:]}"
    except Exception as e:
        masks_logger.error(f"Произошла ошибка: {e}")


print(get_mask_card_number("7000792289606361"))


def get_mask_account(mask_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    try:
        masks_logger.info("Ввод номера счета")
        return f"**{mask_account[-4:]}"
    except Exception as e:
        masks_logger.error(f"Произошла ошибка: {e}")


print(get_mask_account("73654108430135874305"))
