from abc import ABC
from typing import Any


class OptimizationSolution(ABC):
    value: Any
    fitness: float
