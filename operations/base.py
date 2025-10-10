# operations/base.py

class Operation:
    def execute(self, *args):
        raise NotImplementedError("Subclasses must implement execute()")
