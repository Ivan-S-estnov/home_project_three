from unittest.mock import Mock, patch
from src.external_api import valuta_conversion


@patch("requests.get")
def test_one_valuta_conversion(mock_get: Mock, transaction_one):
    mock_get.return_value.json.return_value = {"status": 200, "message": "test", "data": {"USDRUB": "99.99"}}
    assert valuta_conversion(transaction_one) == 9999
    mock_get.assert_called_once()


def test_two_valuta_conversion(transaction_two):
    assert valuta_conversion(transaction_two) == 31957.58
