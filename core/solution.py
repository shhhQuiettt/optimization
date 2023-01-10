from abc import ABC, abstractmethod
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any, Optional


@dataclass(kw_only=True)
class OptimizationSolution(ABC):
    value: Any
    _fitness: Optional[float] = None

    @abstractmethod
    def evaluate_fitness(self) -> float:
        pass

    @property
    def fitness(self):
        if self._fitness is None:
            self._fitness = self.evaluate_fitness()
        return self._fitness
