# operations/history.py

from .calculator_memento import CalculationMemento

class HistoryManager:
    def __init__(self):
        self._history = []
        self._undo_stack = []
        self._redo_stack = []

    def save(self, memento: CalculationMemento):
        self._history.append(memento)
        self._undo_stack.append(memento)
        self._redo_stack.clear()

    def get_all(self):
        return [m.get_state() for m in self._history]

    def undo(self):
        if not self._undo_stack:
            return None
        m = self._undo_stack.pop()
        self._redo_stack.append(m)
        return m

    def redo(self):
        if not self._redo_stack:
            return None
        m = self._redo_stack.pop()
        self._undo_stack.append(m)
        return m

    def clear(self):
        self._history.clear()
        self._undo_stack.clear()
        self._redo_stack.clear()

