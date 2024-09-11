import pytest
import poly_match


def test_sum_as_string():
    assert poly_match.sum_as_string(1, 1) == "2"
