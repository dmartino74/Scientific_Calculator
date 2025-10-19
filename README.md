Thanks for the update, Daniel! Here's your fully updated and polished `README.md` with the correct GitHub repo name: `Scientific_Calculator`. This version reflects your final structure, features, and submission details.

---

```markdown
# 🧮 Enhanced Scientific Calculator CLI (Midterm Project)

This project is a modular, object-oriented command-line calculator built in Python. It supports both basic arithmetic and advanced scientific operations, with integrated logging, undo/redo functionality, autosave, and data management using pandas. Designed for a midterm assessment, it demonstrates key software engineering principles including design patterns, environment configuration, unit testing, and version control.

---

## 🚀 Features

- **Arithmetic Operations**: `+`, `-`, `*`, `/`, `^` (power)
- **Scientific Functions**: `sqrt`, `log`, `sin`, `cos`, `tan`
- **Error Handling**: Division by zero, invalid inputs, negative roots
- **Undo/Redo**: Powered by the Memento pattern
- **Logging**: Configurable log levels, input/output/error tracking
- **Autosave**: Observer pattern saves session history to CSV automatically
- **Environment Configuration**: `.env` file for toggles and paths
- **Data Management**: Session history stored in pandas DataFrame
- **Export Options**: Save results to CSV or Excel
- **Unit Testing**: 98%+ coverage with `pytest` and `pytest-cov`
- **Version Control**: Git workflow with feature branches and commits

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/dmartino74/Scientific_Calculator.git
cd Scientific_Calculator
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
LOG_LEVEL=INFO
CSV_OUTPUT_PATH=session_results.csv
EXCEL_OUTPUT_PATH=session_results.xlsx
ENABLE_SCIENTIFIC_MODE=true
```

---

## 🧪 Running the Calculator

```bash
python calculator.py
```

Follow the prompts to enter numbers and choose operations. Results are logged and stored in session history. You can undo or redo operations using the CLI commands.

---

## 📁 Exporting Results

At the end of a session, results are automatically saved to:

- CSV: `session_results.csv`
- Excel: `session_results.xlsx` (if enabled)

Autosave is triggered after each operation via the Observer pattern.

---

## 🧪 Running Tests

```bash
pytest --cov=operations --cov-report=term-missing
```

Includes tests for:
- Arithmetic and scientific operations
- Error handling and edge cases
- Dispatcher logic
- Observer behavior (logging and autosave)
- Undo/redo via Memento pattern
- CSV export and pandas integration

---

## 🧼 Project Structure

```
Scientific_Calculator/
├── calculator.py
├── operations/
│   ├── __init__.py
│   ├── arithmetic.py
│   ├── scientific.py
│   ├── base.py
│   ├── dispatcher.py
│   ├── operation.py
│   ├── history.py
│   ├── calculator_memento.py
│   ├── observer.py
│   ├── logging_observer.py
│   └── autosave_observer.py
├── tests/
│   ├── test_operation.py
│   ├── test_dispatcher.py
│   ├── test_history.py
│   └── test_observers.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🧠 Design Patterns Used

- **Factory**: Centralized creation of operation objects via dispatcher
- **Strategy**: Dynamic selection of operation logic
- **Memento**: Undo/redo functionality using state snapshots
- **Observer**: Logging and autosave triggered after each operation

---

## 📌 Version Control Workflow

```bash
git checkout -b feature/logging
# make changes
git commit -m "Add logging configuration via .env"
git push origin feature/logging
```

---

## 📬 Submission Notes

- ✅ All tests pass (37/37)
- ✅ Coverage: 98%+
- ✅ GitHub repo: [github.com/dmartino74/Scientific_Calculator](https://github.com/dmartino74/Scientific_Calculator)
- ✅ README and `.env` included
- ✅ Modular structure and design patterns implemented

---

## 📚 Credits

Developed by Daniel Martino  
Midterm Project — NJIT Informatics  
Fall 2025
```

---

Let me know if you want to add GitHub Actions CI or a help menu next. You're ready to submit!