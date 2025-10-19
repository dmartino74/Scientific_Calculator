# operations/observer.py

class Observer:
    def update(self, calculation_state: dict):
        raise NotImplementedError("Subclasses must implement update()")
