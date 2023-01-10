from abc import ABC, abstractmethod
from typing import Optional, Callable, Any
from .solution import OptimizationSolution


class OptimizationAlgorithm(ABC):
    best_solution: OptimizationSolution
    fitness_function: Optional[Callable[[OptimizationSolution], float]] = None

    @abstractmethod
    def perform(self) -> None:
        pass
