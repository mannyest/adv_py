

import pytest
import mymod as mm


def test_addthese_success():
    assert mm.addthese(5, 10) == 15
    assert mm.addthese(5.0, 10.5) == 15.5


def test_addthese_failure():
    with pytest.raises(TypeError):
        mm.addthese('5', 10)

