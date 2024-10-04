from src.utils import get_json_file, json_way


def test_get_json_file(utils_input):
    assert get_json_file(json_way) == utils_input
