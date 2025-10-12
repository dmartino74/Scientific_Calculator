# calculator.py

import logging
from operations.dispatcher import get_operation

# 🔍 Configure logging
logging.basicConfig(
    filename='calculator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def calculate(a, b=None, operator=None):
    logging.info(f"Requested operation: {operator} with a={a}, b={b}")
    op = get_operation(operator)
    if not op:
        logging.error(f"Unsupported operator: {operator}")
        raise ValueError(f"Unsupported operator: {operator}")
    try:
        if operator in ['sqrt', 'sin', 'cos', 'tan']:
            result = op.execute(a)
        elif operator == 'log':
            result = op.execute(a, b if b else None)
        else:
            result = op.execute(a, b)
        logging.info(f"Result: {result}")
        return result
    except Exception as e:
        logging.exception("Error during calculation")
        raise

if __name__ == "__main__":
    print("🔬 Scientific Calculator")
    while True:
        try:
            a = float(input("Enter first number: "))
            operator = input("Enter operation (+, -, *, /, ^, sqrt, log, sin, cos, tan): ").strip()
            logging.info(f"User input: a={a}, operator={operator}")

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
            logging.error(f"Exception occurred: {e}")

        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            logging.info("User exited the calculator.")
            print("👋 Goodbye!")
            break
