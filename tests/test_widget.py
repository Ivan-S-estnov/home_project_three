import pytest

from conftest import widget_input
from src.widget import get_date, mask_account_card


def test_mask_account_card(widget_input, widget_result_one):
    return mask_account_card(widget_input)
    assert test_mask_account_card(widget_input, widget_result_one)


@pytest.mark.parametrize(
    "user_date, repair_date",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
    ],
)
def test_get_date(user_date: str, repair_date: str):
    assert get_date(user_date) == repair_date
