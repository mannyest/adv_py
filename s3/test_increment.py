from s3ex import increment
import pytest

def test_increment_int():
    """ tests incrementing a value & if it's an integer"""
    assert increment(4) == 5
    assert isinstance(increment(8), int)

def test_increment_float():
    """ tests incrementing a float """
    assert increment(7.0) == 8.0
    assert isinstance(increment(2.5), float)

def test_increment_str():
    """ tests incrementing a str """
    with pytest.raises(TypeError):                  ##read this as 'assuming a TypeError is raised,' do what raises the error
        increment('4')