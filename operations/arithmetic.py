# operations/arithmetic.py

from operations.base import Operation

class Add(Operation):
    """Performs addition of two numbers."""
    def execute(self, a: float, b: float) -> float:
        return a + b

class Subtract(Operation):
    """Performs subtraction of two numbers."""
    def execute(self, a: float, b: float) -> float:
        return a - b

class Multiply(Operation):
    """Performs multiplication of two numbers."""
    def execute(self, a: float, b: float) -> float:
        return a * b

class Divide(Operation):
    """Performs division of two numbers, with zero-division check."""
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
