import sys
import os
import logging
import pandas as pd
import pytest

# 🔧 Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from operations.logging_observer import LoggingObserver
from operations.autosave_observer import AutoSaveObserver
from operations.observer import Observer

def test_logging_observer(caplog):
    observer = LoggingObserver()
    state = {'Operation': '+', 'a': 2, 'b': 3, 'Result': 5}

    with caplog.at_level(logging.INFO):
        observer.update(state)

    assert any("LoggingObserver" in message for message in caplog.messages)

def test_autosave_observer(tmp_path):
    filepath = tmp_path / "autosave.csv"
    observer = AutoSaveObserver(filepath=str(filepath))
    state = {'Operation': '*', 'a': 4, 'b': 5, 'Result': 20}
    observer.update(state)

    df = pd.read_csv(filepath)
    assert df.iloc[0]['Operation'] == '*'
    assert df.iloc[0]['Result'] == 20

def test_abstract_observer_not_implemented():
    obs = Observer()
    with pytest.raises(NotImplementedError):
        obs.update({'Operation': '+', 'a': 1, 'b': 2, 'Result': 3})

