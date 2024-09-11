import pytest
import poly_match_rs


def test_sum_as_string():
    assert poly_match_rs.sum_as_string(1, 1) == "2"
