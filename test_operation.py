import pytest
import math

from operations import Add, Subtract, Multiply, Divide, Power, Sqrt, Log, Sin, Cos, Tan

def test_add(): assert Add().execute(2, 3) == 5
def test_subtract(): assert Subtract().execute(5, 2) == 3
def test_multiply(): assert Multiply().execute(4, 3) == 12
def test_divide(): assert Divide().execute(10, 2) == 5

def test_divide_by_zero():
    try:
        Divide().execute(5, 0)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_power(): assert Power().execute(2, 3) == 8
def test_sqrt(): assert Sqrt().execute(16) == 4

def test_sqrt_negative():
    try:
        Sqrt().execute(-9)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_log_default():
    assert round(Log().execute(math.e), 5) == 1.0

def test_log_base10():
    assert round(Log().execute(100, 10), 5) == 2.0

def test_log_invalid():
    try:
        Log().execute(0)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_sin(): assert round(Sin().execute(90), 5) == 1.0
def test_cos(): assert round(Cos().execute(0), 5) == 1.0
def test_tan(): assert round(Tan().execute(45), 5) == 1.0
