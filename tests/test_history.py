# tests/test_history.py

import pytest
import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from operations.calculator_memento import CalculationMemento
from operations.history import HistoryManager

def test_save_and_get_all():
    history = HistoryManager()
    m1 = CalculationMemento('+', 2, 3, 5)
    m2 = CalculationMemento('sqrt', 16, None, 4)

    history.save(m1)
    history.save(m2)

    all_history = history.get_all()
    assert len(all_history) == 2
    assert all_history[0]['Result'] == 5
    assert all_history[1]['Operation'] == 'sqrt'

def test_undo_redo():
    history = HistoryManager()
    m1 = CalculationMemento('-', 10, 4, 6)
    m2 = CalculationMemento('*', 3, 3, 9)

    history.save(m1)
    history.save(m2)

    undone = history.undo()
    assert undone.get_state()['Result'] == 9

    redone = history.redo()
    assert redone.get_state()['Operation'] == '*'

def test_undo_empty():
    history = HistoryManager()
    assert history.undo() is None

def test_redo_empty():
    history = HistoryManager()
    assert history.redo() is None

def test_clear_history():
    history = HistoryManager()
    history.save(CalculationMemento('/', 8, 2, 4))
    history.clear()
    assert history.get_all() == []
    assert history.undo() is None
    assert history.redo() is None

