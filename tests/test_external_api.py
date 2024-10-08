import json
import os
from unittest.mock import Mock, patch
from pathlib import Path
import requests
from dotenv import load_dotenv

from src.external_api import valuta_conversion

load_dotenv("../.env")
API_KEY = os.getenv("API_KEY")


@patch("requests.get")
def test_valuta_conversion(mock_get: Mock, pawn_path: Path):
    mock_get.return_value =
    assert (
        valuta_conversion(
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            }
        )
        ==
    )
