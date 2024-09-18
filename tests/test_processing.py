import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(processing_input, processing_result_two):
    assert filter_by_state(processing_input) == processing_result_two


def test_sort_by_date(processing_input, processing_result_one):
    assert sort_by_date(processing_input) == processing_result_one
