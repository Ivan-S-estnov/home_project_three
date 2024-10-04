from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_exceptions(generators_input: Any) -> Any:
    assert filter_by_currency(generators_input, "RUB")
    assert filter_by_currency("Введен пустой список", "")


def test_transaction_descriptions(generators_input: Any) -> Any:
    assert transaction_descriptions(generators_input, "Перевод со счета на счет")
    assert transaction_descriptions(generators_input, "Перевед не был осуществлен")


@pytest.mark.parametrize(
    "start, end",
    [("0", "5"), ("0", "0"), ("9999999999999998", "9999999999999999")],
)
def test_card_number_generator(start: Any, end: Any) -> Any:
    assert card_number_generator(start, end)
