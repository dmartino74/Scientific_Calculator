import sys
import os

# 🔧 Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from operations.dispatcher import get_operation

def test_dispatcher_add():
    op = get_operation('+')
    assert op.execute(2, 3) == 5

def test_dispatcher_subtract():
    op = get_operation('-')
    assert op.execute(5, 2) == 3

def test_dispatcher_multiply():
    op = get_operation('*')
    assert op.execute(4, 3) == 12

def test_dispatcher_divide():
    op = get_operation('/')
    assert op.execute(10, 2) == 5

def test_dispatcher_power():
    op = get_operation('^')
    assert op.execute(2, 3) == 8

def test_dispatcher_sqrt():
    op = get_operation('sqrt')
    assert op.execute(16) == 4

def test_dispatcher_log():
    op = get_operation('log')
    assert round(op.execute(100, 10), 5) == 2.0

def test_dispatcher_sin():
    op = get_operation('sin')
    assert round(op.execute(90), 5) == 1.0

def test_dispatcher_cos():
    op = get_operation('cos')
    assert round(op.execute(0), 5) == 1.0

def test_dispatcher_tan():
    op = get_operation('tan')
    assert round(op.execute(45), 5) == 1.0

def test_dispatcher_invalid():
    assert get_operation('invalid') is None
