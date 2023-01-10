from __future__ import annotations
from abc import abstractmethod, ABC
from optimization.core.solution import OptimizationSolution
from typing import Any, Tuple, Callable
from dataclasses import dataclass


@dataclass(kw_only=True)
class EvolutionarySolution(OptimizationSolution):
    value: Any
    age: int = 0

    @abstractmethod
    def mutate(self) -> None:
        pass

    @abstractmethod
    def crossover(
        self, other_solution: EvolutionarySolution
    ) -> Tuple[EvolutionarySolution, EvolutionarySolution]:
        pass

    @classmethod
    def from_optimization_solution(
        cls, solution: OptimizationSolution
    ) -> EvolutionarySolution:
        return cls(value=solution.value)


class RandomSolutionStrategy(ABC):
    @abstractmethod
    def get(self) -> EvolutionarySolution:
        pass
