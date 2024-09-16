import pytest
from typing import Any
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parmetrize(
    "list_dictionaries, state",
    [
        ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}], "EXECUTED"),
        ([{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}], "EXECUTED"),
    ],
)
def test_filter_by_state(list_dictionaries: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    assert filter_by_state(list_dictionaries) == state


@pytest.mark.parametrize(
    "date_dictionaries, sorted_date",
    [
        ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}], "EXECUTED"),
        ([{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}], "EXECUTED"),
    ],
)
def test_sort_by_date(date_dictionaries: list[dict[str, Any]], sorted_date: bool = True) -> Any:
    assert sort_by_date(date_dictionaries) == sorted_date
