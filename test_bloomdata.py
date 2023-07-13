import pytest
import bloomdata-pace.bloomdata


def test_increment_int():
    assert bloomdata.increment(3) == 4
    assert bloomdata.increment(3) == 2
