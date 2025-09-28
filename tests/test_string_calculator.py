import pytest
from string_calculator import add

def test_empty_string_returns_zero():
    assert add("") == 0

def test_single_number_returns_value():
    assert add("1") == 1

def test_two_numbers_comma_separated():
    assert add("1,5") == 6

def test_many_numbers():
    assert add("1,2,3,4,5") == 15

def test_newlines_between_numbers():
    assert add("1\n2,3") == 6

# def test_custom_single_char_delimiter():
#     assert add("//;\n1;2") == 3

# def test_negative_raises_single():
#     with pytest.raises(ValueError) as exc:
#         add("1,-2,3")
#     assert "negative numbers not allowed -2" in str(exc.value)

# def test_negative_raises_multiple():
#     with pytest.raises(ValueError) as exc:
#         add("1,-2,-5,3")
#     assert "negative numbers not allowed -2,-5" in str(exc.value)
