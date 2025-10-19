import sys
import os
import pytest
import math
import pandas as pd

# 🔧 Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from operations.operation import (
    add, subtract, multiply, divide,
    power, sqrt, log, sin, cos, tan
)
from operations.scientific import Log, Tan
from operations.base import Operation

# 🧪 Arithmetic Tests
def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

# 🧪 Scientific Tests
def test_power():
    assert power(2, 3) == 8

def test_sqrt():
    assert sqrt(16) == 4

def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-9)

def test_log_default():
    assert round(log(math.e), 5) == 1.0

def test_log_base10():
    assert round(log(100, 10), 5) == 2.0

def test_log_invalid():
    with pytest.raises(ValueError):
        log(0)

def test_log_negative():
    with pytest.raises(ValueError):
        Log().execute(-1)

def test_sin():
    assert round(sin(90), 5) == 1.0

def test_cos():
    assert round(cos(0), 5) == 1.0

def test_tan():
    assert round(tan(45), 5) == 1.0

def test_tan_90():
    result = Tan().execute(89.999)
    assert abs(result) > 1000

# 🧪 Base Class Behavior
def test_base_operation_not_implemented():
    op = Operation()
    with pytest.raises(NotImplementedError):
        op.execute(1, 2)

# 🧪 CSV Export Test
def test_csv_export(tmp_path):
    results = [
        {'Operation': '+', 'a': 2, 'b': 3, 'Result': 5},
        {'Operation': 'sqrt', 'a': 16, 'b': None, 'Result': 4}
    ]
    csv_file = tmp_path / "test_results.csv"
    pd.DataFrame(results).to_csv(csv_file, index=False)
    df = pd.read_csv(csv_file)

    assert len(df) == 2
    assert df.iloc[0]['Operation'] == '+'
    assert df.iloc[1]['Result'] == 4
