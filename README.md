# Scientific Calculator Project
Here’s a clean, professional `README.md` tailored for your **Scientific Calculator** project — modular, testable, and midterm-ready:

---

## 🧮 Scientific Calculator

A modular Python-based scientific calculator designed for clarity, reproducibility, and full test coverage. Built by **dmartino74** for midterm evaluation and instructional use.

---

### 📁 Project Structure

```
Scientific_Calculator/
├── calculator.py          # Main interface and dispatcher
├── operation.py           # Core arithmetic and scientific functions
├── test_operation.py      # Pytest suite for all operations
├── README.md              # Project documentation
```

---

### ⚙️ Features

- Basic operations: `+`, `-`, `*`, `/`, `^`
- Scientific functions: `sqrt`, `log`, `sin`, `cos`, `tan`
- Input validation and error handling
- CLI interface for interactive use
- Modular design for easy grading and extension
- Pytest-based test suite with edge case coverage

---

### 🚀 How to Run

```bash
python3 calculator.py
```

Follow the prompts to enter numbers and choose operations interactively.

---

### 🧪 How to Test

Make sure `pytest` is installed:
```bash
pip install pytest
```

Then run:
```bash
pytest test_operation.py
```

All tests should pass, including:
- Division by zero
- Square root of negative numbers
- Logarithm of non-positive values

---

### 🧠 Educational Value

This project emphasizes:
- Clean separation of logic
- Robust exception handling
- Reproducible workflows
- Transparent testing for grading and review

---

### 📌 Author

**Daniel Martino**  
GitHub: [dmartino74](https://github.com/dmartino74)  
Focus: Modular Python systems, reproducible workflows, clarity in grading

