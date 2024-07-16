#code_to_test.py
def my_sum(a,b):
    return a + b

def my_upper(my_str):
    if not isinstance(my_str, str):
        raise TypeError()
    return my_str.upper()


import pytest

def test_upper_type_exception():
    with pytest.raises(TypeError):
        my_upper(10)

def test_upper():
    result = my_upper('hello world')
    assert result == 'HELLO WORLD'

def test_my_sum():
    result = my_sum(5, 2)
    expected_result = 7
    # pytest.fail()
    assert result == expected_result

def test_dict_contains():
    data = {"key1": "value"}
    assert data["key"] == "value"

def test_key_error():
    with pytest.raises(KeyError):
        some_dict = {'nonexistent_key': 'bla'}
        value = some_dict['nonexistent_key2']
