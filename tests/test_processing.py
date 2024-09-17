from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def test_filter_by_state(processing_input: list[dict[str, Any]], processing_result_1: list[dict[str, Any]]) -> Any:
    assert filter_by_state(processing_input) == processing_result_1


@pytest.mark.parametrize(
    "user_input, reverse_date, result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]
        ),
    ],
)
def test_sort_by_date(user_input: Any, reverse_date: Any, result: Any) -> Any:
    assert sort_by_date(user_input, reverse_date) == result
