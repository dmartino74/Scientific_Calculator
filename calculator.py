import logging
import pandas as pd
import os
from dotenv import load_dotenv
from operations.dispatcher import get_operation
from operations.history import HistoryManager
from operations.calculator_memento import CalculationMemento
from operations.logging_observer import LoggingObserver
from operations.autosave_observer import AutoSaveObserver

# 🌱 Load environment variables
load_dotenv()
LOG_FILE = os.getenv("CALCULATOR_LOG_DIR", "calculator.log")
HISTORY_FILE = os.getenv("CALCULATOR_HISTORY_FILE", "calculation_history.csv")
SESSION_FILE = os.getenv("CALCULATOR_SESSION_FILE", "session_results.csv")
AUTOSAVE_FILE = os.getenv("AUTOSAVE_FILE", "autosave_history.csv")

# 🔍 Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 🧾 Store session results
session_results = []
history = HistoryManager()

# 👀 Register observers
observers = [LoggingObserver(), AutoSaveObserver(filepath=AUTOSAVE_FILE)]
def notify_observers(state: dict):
    for observer in observers:
        observer.update(state)

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
            action = input("Type 'undo', 'redo', or press Enter to continue: ").strip().lower()

            if action == 'undo':
                m = history.undo()
                if m:
                    state = m.get_state()
                    print(f"↩️ Undone: {state['Operation']}({state['a']}, {state['b']}) = {state['Result']}")
                else:
                    print("⚠️ Nothing to undo.")
                continue

            elif action == 'redo':
                m = history.redo()
                if m:
                    state = m.get_state()
                    print(f"↪️ Redone: {state['Operation']}({state['a']}, {state['b']}) = {state['Result']}")
                else:
                    print("⚠️ Nothing to redo.")
                continue

            a = float(input("Enter first number: "))
            operator = input("Enter operation (+, -, *, /, ^, sqrt, log, sin, cos, tan): ").strip()
            logging.info(f"User input: a={a}, operator={operator}")

            if operator in ['sqrt', 'sin', 'cos', 'tan']:
                result = calculate(a, operator=operator)
                print(f"{operator}({a}) = {result}")
                state = {'Operation': operator, 'a': a, 'b': None, 'Result': result}
                session_results.append(state)
                history.save(CalculationMemento(operator, a, None, result))
                notify_observers(state)

            elif operator == 'log':
                base_input = input("Enter base (optional, press Enter for natural log): ").strip()
                base = float(base_input) if base_input else None
                result = calculate(a, base, operator)
                print(f"log base {base if base else 'e'} of {a} = {result}")
                state = {'Operation': 'log', 'a': a, 'b': base, 'Result': result}
                session_results.append(state)
                history.save(CalculationMemento('log', a, base, result))
                notify_observers(state)

            else:
                b = float(input("Enter second number: "))
                result = calculate(a, b, operator)
                print(f"{a} {operator} {b} = {result}")
                state = {'Operation': operator, 'a': a, 'b': b, 'Result': result}
                session_results.append(state)
                history.save(CalculationMemento(operator, a, b, result))
                notify_observers(state)

        except Exception as e:
            print(f"❌ Error: {e}")
            logging.error(f"Exception occurred: {e}")

        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            logging.info("User exited the calculator.")
            print("👋 Goodbye!")

            # 💾 Export results to CSV
            if session_results:
                pd.DataFrame(session_results).to_csv(SESSION_FILE, index=False)
                print(f"📁 Session results saved to '{SESSION_FILE}'")

            # 🧠 Export full history
            if history.get_all():
                pd.DataFrame(history.get_all()).to_csv(HISTORY_FILE, index=False)
                print(f"📁 Full history saved to '{HISTORY_FILE}'")
            break
