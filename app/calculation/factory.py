# Author: Ishan Rehan | Date: 2025-09-29
from typing import Dict, Callable, List
from app.calculation.models import Calculation
from app.operation.basic import add, sub, mul, div

_OPERATIONS: Dict[str, Callable[[float, float], float]] = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
}

_HISTORY: List[Calculation] = []

def operations_map() -> Dict[str, Callable[[float, float], float]]:
    return dict(_OPERATIONS)

def history() -> List[Calculation]:
    return list(_HISTORY)

class CalculationFactory:
    @staticmethod
    def from_parts(key: str, a: float, b: float) -> Calculation:
        if key not in _OPERATIONS:
            raise ValueError(f"Unknown operation: {key}")
        calc = Calculation(op_name=key, a=a, b=b, func=_OPERATIONS[key])
        _HISTORY.append(calc)
        return calc

# -------- test-only utility --------
def _reset_history_for_tests() -> None:  # pragma: no cover
    """Clear session history (used by tests)."""
    _HISTORY.clear()
