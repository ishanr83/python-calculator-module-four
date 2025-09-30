# Professional Python Calculator (Module 4)

Author: Ishan Rehan  
Date: 2025-09-29

# Run
```bash
python -m app.calculator

# Professional Python Calculator (Module 4)

**Author:** Ishan Rehan  
**Date:** 2025-09-29

# Overview
A modular command-line calculator in Python. It uses a clean architecture (operations, calculation factory, REPL), strong error handling (LBYL + EAFP), full unit/parameterized tests, and a GitHub Actions workflow that **fails** if coverage is below **100%**.

# Features
- REPL interface (`add|sub|mul|div <a> <b>`, `history`, `help`, `exit|quit|q`)
- Input validation (LBYL) and safe exception handling (EAFP for division by zero)
- `CalculationFactory` creates immutable calculations and saves session history
- Unit + parameterized tests with **100% coverage** enforced locally and in CI

# Project Structure
python-calculator-module-four/
├── app/
│ ├── calculator/ # REPL (entry: python -m app.calculator)
│ ├── calculation/ # Calculation model, factory, history
│ └── operation/ # Arithmetic operations
├── tests/ # Unit + parameterized tests (100% coverage)
├── .github/workflows/ # GitHub Actions CI (coverage gate)
├── README.md
├── pytest.ini
├── requirements.txt

# Setup
```bash
python -m venv .venv
# Windows Git Bash:
source .venv/Scripts/activate
# Ensure imports match CI:
export PYTHONPATH=.
pip install -r requirements.txt

# Example session:
Calculator REPL. Commands: add|sub|mul|div <a> <b> | history | help | exit
> help
> add 2 3
Result: 5
> div 5 0
Error: Division by zero
> history
1. add(2, 3) = 5
> q
Bye!

# Continuous Integration (GitHub Actions)

Every push runs tests with coverage on Ubuntu. The build fails if coverage < 100%.
Workflow file: .github/workflows/python-app.yml
Main steps:
Set PYTHONPATH=. for imports
Install deps
Run tests with coverage
Fail if coverage < 100%
