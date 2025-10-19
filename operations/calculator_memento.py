# calculator_memento.py

class CalculationMemento:
    """
    Stores the state of a single calculation for undo/redo functionality.
    """
    def __init__(self, operation, a, b, result):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result

    def get_state(self):
        return {
            'Operation': self.operation,
            'a': self.a,
            'b': self.b,
            'Result': self.result
        }
