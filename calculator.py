# calculator.py

from dispatcher import get_operation

def calculate(a, b=None, operator=None):
    operation = get_operation(operator)
    if not operation:
        raise ValueError(f"Unsupported operator: {operator}")

    # Use polymorphism to execute the operation
    if operator in ['sqrt', 'sin', 'cos', 'tan']:
        return operation.execute(a)
    elif operator == 'log':
        return operation.execute(a, b if b else None)
    else:
        return operation.execute(a, b)

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
