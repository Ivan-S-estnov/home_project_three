import json
from unittest.mock import MagicMock, patch
from pathlib import Path
from src.utils import get_json_file


@patch("builtins.open")
def test_get_json_file(mock_open: MagicMock, path_name: Path) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps([{"test", "test"}])
    assert get_json_file(path_name) == [{"test", "test"}]
   # mock_file.read.return_value = json.dumps({})
    #assert get_json_file(path_name) == []
  #  mock_file.read.return_value = json.dumps("testtest")
   # assert get_json_file(path_name) == []
   # mock_file.read.return_value = json.dumps("")
    #assert get_json_file(path_name) == []
