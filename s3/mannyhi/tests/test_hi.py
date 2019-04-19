import pytest
import mannyhi

def test_greet():
    assert mannyhi.greet() == 'hi, world!'