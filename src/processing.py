from typing import Any

info_input = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(info_input: list[dict[str, Any]], state_id: str = "EXECUTED") -> Any:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ соответствует указанному значению"""
    state_list = []
    for key in info_input:
        if key.get("state") == state_id:
            state_list.append(key)

    return state_list


print(filter_by_state(info_input))


def sort_by_date(info_input: list[dict[str, Any]], revers: bool = True) -> Any:
    """Функция должна возвращать новый список, отсортированный по дате"""
    sorted_info = sorted(info_input, key=lambda a: a["date"], reverse=revers)
    return sorted_info


print(sort_by_date(info_input))
