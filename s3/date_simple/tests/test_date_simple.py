import pytest
import date_simple as ds
import datetime

def test_get_date_object():
    assert ds.get_date_object() == datetime.datetime.today().date()
    assert ds.get_date_object(date='2018-02-26') == datetime.datetime.strptime('2018-02-26', '%Y-%m-%d').date()
    with pytest.raises(ValueError):
        ds.get_date_object(date='208-29-26')
    with pytest.raises(TypeError):
        ds.get_date_object(date = 5)

def test_get_date_string():
    assert ds.get_date_string() == datetime.datetime.today().strftime('%Y-%m-%d')

    dateobj = datetime.datetime.strptime('2018-02-26', '%Y-%m-%d')
    assert ds.get_date_string(date_object=dateobj) == '2018-02-26'

    with pytest.raises(AttributeError):
        ds.get_date_string(date_object = '2018-02-26')

