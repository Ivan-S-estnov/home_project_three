from src.masks import get_mask_account, get_mask_card_number

# Примеры входных данных для проверки функции:
account_and_card_numb = """ Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305 """


def mask_account_card(user_info: str) -> str:
    """Функция для маскировки номера карты/счета"""
    split_user_info = user_info.split()
    new_name = []
    card_and_account = []
    for numb_or_name in split_user_info:
        if numb_or_name.isalpha():
            card_and_account.append(numb_or_name)
        elif numb_or_name.isdigit():
            if len(numb_or_name) == 16:
                mask_card_numb = get_mask_card_number(numb_or_name)
                card_and_account.append(mask_card_numb)
                new_name.append(card_and_account)
                card_and_account = list()
            elif len(numb_or_name) == 20:
                mask_account_numb = get_mask_account(numb_or_name)
                card_and_account.append(mask_account_numb)
                new_name.append(card_and_account)
                card_and_account = list()
        else:
            continue
    ready_data = ""
    for card_info in new_name:
        make_a_line = " ".join(card_info)
        ready_data += make_a_line + "\n"
    return ready_data


date_input = "2018-07-11T02:26:18.671407"


def get_date(date_input: str) -> str:
    """Функция, принимающая строку с датой и модифоцирующая её в формат "ДД.ММ.ГГГГ" """
    date = date_input.split("T")[0]
    date_format = f"{date[-2:]}.{date[5:7]}.{date[:4]}"

    return date_format


if __name__ == "__main__":
    print(mask_account_card(account_and_card_numb))
    print(get_date(date_input))
