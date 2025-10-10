# dispatcher.py

from operations.arithmetic import Add, Subtract, Multiply, Divide
from operations.scientific import Power, Sqrt, Log, Sin, Cos, Tan

def get_operation(operator):
    return {
        '+': Add(),
        '-': Subtract(),
        '*': Multiply(),
        '/': Divide(),
        '^': Power(),
        'sqrt': Sqrt(),
        'log': Log(),
        'sin': Sin(),
        'cos': Cos(),
        'tan': Tan()
    }.get(operator)
