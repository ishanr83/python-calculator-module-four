# Author: Ishan Rehan | Date: 2025-09-29

def add(a: float, b: float) -> float:
    return a + b

def sub(a: float, b: float) -> float:
    return a - b

def mul(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> float:
    # EAFP friendly: allow caller to catch ZeroDivisionError
    return a / b
