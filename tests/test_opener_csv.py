from unittest.mock import patch
from src.opener_csv import open_csv, open_xlsx


@patch("src.opener_csv.pd.open_csv")
def test_open_csv(mock_read, csv_xlsx_for_test):
    mock_read.return_value = csv_xlsx_for_test
    assert open_csv('transactions.csv') == csv_xlsx_for_test.to_dict(orient='records')
    mock_read.assert_called_once_with('transactions.csv', delimiter=';')


@patch("src.opener_csv.pd.open_xlsx")
def test_open_xlsx(mock_read, csv_xlsx_for_test):
    mock_read.return_value = csv_xlsx_for_test
    assert open_xlsx('transactions_excel.xlsx') == csv_xlsx_for_test.to_dict(orient='records')
    mock_read.assert_called_once_with('transactions_excel.xlsx')