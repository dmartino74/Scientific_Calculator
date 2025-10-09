# calculator.py

from operation import add, subtract, multiply, divide, power, sqrt, log, sin, cos, tan

def calculate(a, b=None, operator=None):
    if operator == '+': return add(a, b)
    elif operator == '-': return subtract(a, b)
    elif operator == '*': return multiply(a, b)
    elif operator == '/': return divide(a, b)
    elif operator == '^': return power(a, b)
    elif operator == 'sqrt': return sqrt(a)
    elif operator == 'log': return log(a, b if b else None)
    elif operator == 'sin': return sin(a)
    elif operator == 'cos': return cos(a)
    elif operator == 'tan': return tan(a)
    else: raise ValueError(f"Unsupported operator: {operator}")

if __name__ == "__main__":
    print("🔬 Scientific Calculator")
    try:
        a = float(input("Enter first number: "))
        operator = input("Enter operation (+, -, *, /, ^, sqrt, log, sin, cos, tan): ").strip()

        if operator in ['sqrt', 'sin', 'cos', 'tan']:
            result = calculate(a, operator=operator)
            print(f"{operator}({a}) = {result}")
        elif operator == 'log':
            base_input = input("Enter base (optional, press Enter for natural log): ").strip()
            base = float(base_input) if base_input else None
            result = calculate(a, base, operator)
            print(f"log base {base if base else 'e'} of {a} = {result}")
        else:
            b = float(input("Enter second number: "))
            result = calculate(a, b, operator)
            print(f"{a} {operator} {b} = {result}")

    except Exception as e:
        print(f"❌ Error: {e}")

