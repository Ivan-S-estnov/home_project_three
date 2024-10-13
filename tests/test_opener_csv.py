import csv
from pathlib import Path
from unittest.mock import MagicMock, patch
from src.opener_csv import open_csv, open_xlsx


@patch("builtins.open")
def test_open_csv(mock_open: MagicMock, csv_for_test: Path) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = csv.DictReader({"test": "test"})
    assert open_csv(csv_for_test) == [{"test": "test"}]
