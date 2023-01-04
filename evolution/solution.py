from __future__ import annotations
from abc import abstractmethod
from optimization.core.solution import OptimizationSolution
from typing import Any, Tuple
from dataclasses import dataclass

print(sklearn.__version__)


@dataclass
class EvolutionarySolution(OptimizationSolution):
    value: Any
    fitness: float
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
        return cls(value=solution.value, fitness=solution.fitness)
