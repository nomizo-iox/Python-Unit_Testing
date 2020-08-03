import math_func
import pytest
import sys


@pytest.mark.number
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(5, 10) != 11


@pytest.mark.skipif(sys.version_info > (3, 3), reason='do not run float product test')
def test_add_float():
    assert math_func.add(5.0, 5.7) == 25


@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(10, 29) != 49


@pytest.mark.skip(reason='do not run float product test')
def test_product_float():
    assert math_func.product(5.0, 5.7) == 25


@pytest.mark.strings
def test_add_strings():
    result = math_func.add('Hello ', 'World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldo' not in result


@pytest.mark.strings
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result
