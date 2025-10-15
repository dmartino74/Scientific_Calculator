

# 🧮 Enhanced Scientific Calculator CLI (Midterm Project)

This project is a modular, object-oriented command-line calculator built in Python. It supports both basic arithmetic and advanced scientific operations, with integrated logging, configuration via environment variables, and data management using pandas. Designed as part of a midterm assessment, it demonstrates key software engineering principles including design patterns, testing, and version control.

---

## 🚀 Features

- **Arithmetic Operations**: `+`, `-`, `*`, `/`, `^` (power)
- **Scientific Functions**: `sqrt`, `log`, `sin`, `cos`, `tan`
- **Error Handling**: Division by zero, invalid inputs, negative roots
- **Logging**: Configurable log levels, input/output/error tracking
- **Environment Configuration**: `.env` file for toggles and paths
- **Data Management**: Session history stored in pandas DataFrame
- **Export Options**: Save results to CSV or Excel
- **Unit Testing**: Comprehensive test suite with `pytest`
- **Version Control**: Git workflow with feature branches and commits

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/dmartino74/Midterm_Project.git
cd Midterm_Project
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

Follow the prompts to enter numbers and choose operations. Results are logged and stored in session history.

---

## 📁 Exporting Results

At the end of a session, results are automatically saved to:

- CSV: `session_results.csv`
- Excel: `session_results.xlsx` (if enabled)

---

## 🧪 Running Tests

```bash
pytest --cov
```

Includes tests for:
- Arithmetic and scientific operations
- Error handling
- CSV export
- Edge cases (e.g., divide by zero, invalid log input)

---

## 🧼 Project Structure

```
Midterm_Project/
├── calculator.py
├── operations/
│   ├── base.py
│   ├── arithmetic.py
│   ├── scientific.py
│   └── dispatcher.py
├── test_operation.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🧠 Design Patterns Used

- **Strategy**: Dynamic selection of operation logic
- **Factory**: Centralized creation of operation objects
- **Memento** (optional): For undo/redo history snapshots

---

## 📌 Version Control Workflow

```bash
git checkout -b feature/logging
# make changes
git commit -m "Add logging configuration via .env"
git push origin feature/logging
```

---

## 📚 Credits

