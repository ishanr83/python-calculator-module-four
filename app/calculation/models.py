# Author: Ishan Rehan | Date: 2025-09-29
from dataclasses import dataclass
from typing import Callable

@dataclass(frozen=True)
class Calculation:
    op_name: str
    a: float
    b: float
    func: Callable[[float, float], float]

    def execute(self) -> float:
        return self.func(self.a, self.b)
