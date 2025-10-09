# test_operation.py

import pytest
from operation import *

def test_add(): assert add(2, 3) == 5
def test_subtract(): assert subtract(5, 2) == 3
def test_multiply(): assert multiply(4, 3) == 12
def test_divide(): assert divide(10, 2) == 5
def test_divide_by_zero():
    with pytest.raises(ValueError): divide(5, 0)

def test_power(): assert power(2, 3) == 8
def test_sqrt(): assert sqrt(16) == 4
def test_sqrt_negative():
    with pytest.raises(ValueError): sqrt(-9)

def test_log_default(): assert round(log(math.e), 5) == 1.0
def test_log_base10(): assert round(log(100, 10), 5) == 2.0
def test_log_invalid():
    with pytest.raises(ValueError): log(0)

def test_sin(): assert round(sin(90), 5) == 1.0
def test_cos(): assert round(cos(0), 5) == 1.0
def test_tan(): assert round(tan(45), 5) == 1.0
