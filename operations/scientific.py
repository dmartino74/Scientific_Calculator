# operations/scientific.py

import math
from operations.base import Operation

class Power(Operation):
    def execute(self, a, b):
        return a ** b

class Sqrt(Operation):
    def execute(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of negative number.")
        return math.sqrt(a)

class Log(Operation):
    def execute(self, a, base=math.e):
        if a <= 0:
            raise ValueError("Logarithm undefined for non-positive values.")
        return math.log(a, base)

class Sin(Operation):
    def execute(self, a):
        return math.sin(math.radians(a))

class Cos(Operation):
    def execute(self, a):
        return math.cos(math.radians(a))

class Tan(Operation):
    def execute(self, a):
        return math.tan(math.radians(a))
