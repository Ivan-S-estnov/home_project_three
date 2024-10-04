def get_mask_card_number(card_numb: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    return f"{card_numb[:4]} {card_numb[4:6]}** **** {card_numb[-4:]}"


print(get_mask_card_number("7000792289606361"))


def get_mask_account(mask_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f"**{mask_account[-4:]}"


print(get_mask_account("73654108430135874305"))
