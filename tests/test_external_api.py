from unittest.mock import patch
import os
from dotenv import load_dotenv
from src.external_api import get_sum_amount


def test_get_sum_amount(utils_result):

    assert get_sum_amount(json_way) == utils_result


