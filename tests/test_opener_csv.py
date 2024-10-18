import os
from unittest.mock import patch

from src.opener_csv import open_csv, open_xlsx

@patch('csv.reader')
def test_open_csv_1(mock_reader):
  mock_reader.return_value = iter([
    ['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description'],
    ['650703', 'EXECUTED', '2023-09-05T11:30:32Z', '16210', 'SoL', 'PEN', 'Счет 58803664651298323391', 'Счет 39746506635466619397', 'Перевод организации']
  ])

  result = open_csv(os.path.join('csv_path', 'transactions.csv'))
  expected_result = [
    {
      "id": "650703",
      "state": "EXECUTED",
      "date": "2023-09-05T11:30:32Z",
      "amount": "16210",
      "currency_name": "SoL",
      "currency_code": "PEN",
      "from": "Счет 58803664651298323391",
      "to": "Счет 39746506635466619397",
      "description": "Перевод организации"
    }
  ]

@patch("csv.reader")
def test_open_csv_2(mock_reader):
    mock_reader.return_value = []
    assert open_csv(os.path.join("csv_path")) == []


@patch("pandas.read_excel")
def test_open_xlsx_1(mock_reader):
    mock_reader.return_value = [
        {
            "id": 3598919.0,
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        }
    ]
    result = open_xlsx(os.path.join("excel_path"))
    expected_result = [
        {
            "id": 3598919.0,
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        }
    ]


@patch("pandas.read_excel")
def test_open_xlsx_2(mock_reader):
    mock_reader.return_value = []
    assert open_xlsx(os.path.join("excel_path")) == []
