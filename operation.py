# operation.py

import math

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a, b): return a ** b
def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return math.sqrt(a)

def log(a, base=math.e):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log(a, base)

def sin(a): return math.sin(math.radians(a))
def cos(a): return math.cos(math.radians(a))
def tan(a): return math.tan(math.radians(a))
