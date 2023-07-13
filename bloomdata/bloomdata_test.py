import pytest
import bloomdata.helper_functions as hf


def test_bowling_score():
    """
    Tests to ensure the randomly generated 
    bowling score is above 0 and below
    301
    """
    assert hf.random_bowling_score() > 0
    assert hf.random_bowling_score() <= 300


def test_random_phrase():
    """
    Tests to affirm that randomly generated phrase is a string
    """
    assert isinstance(hf.random_phrase(), str)


def test_silly_tuple():
    """
    Tests to see if the return value of the function:silly_tuple()
    is in fact a Tuple
    """
    assert isinstance(hf.silly_tuple(), tuple)