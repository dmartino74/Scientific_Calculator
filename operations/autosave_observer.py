# operations/autosave_observer.py

import pandas as pd
import os
from operations.observer import Observer

class AutoSaveObserver(Observer):
    def __init__(self, filepath='autosave_history.csv'):
        self.filepath = filepath
        self._initialized = False

    def update(self, calculation_state: dict):
        df = pd.DataFrame([calculation_state])
        if not self._initialized or not os.path.exists(self.filepath):
            df.to_csv(self.filepath, index=False)
            self._initialized = True
        else:
            df.to_csv(self.filepath, mode='a', header=False, index=False)
