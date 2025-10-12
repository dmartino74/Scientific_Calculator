# test_operation.py

import sys
import os
import pytest
import math
import pandas as pd

# 🔧 Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from operations.operation import *






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

def test_sin():
    assert round(sin(90), 5) == 1.0

def test_cos():
    assert round(cos(0), 5) == 1.0

def test_tan():
    assert round(tan(45), 5) == 1.0

def test_csv_export(tmp_path):
    # Sample session data
    results = [
        {'Operation': '+', 'a': 2, 'b': 3, 'Result': 5},
        {'Operation': 'sqrt', 'a': 16, 'b': None, 'Result': 4}
    ]

    # Path to temporary CSV file
    csv_file = tmp_path / "test_results.csv"

    # Export using pandas
    pd.DataFrame(results).to_csv(csv_file, index=False)

    # Read back and verify
    df = pd.read_csv(csv_file)
    assert len(df) == 2
    assert df.iloc[0]['Operation'] == '+'
    assert df.iloc[1]['Result'] == 4
