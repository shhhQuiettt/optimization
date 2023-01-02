from typing import Protocol
from solution import OptimizationSolution
from algorithm import OptimizationAlgorithm


class OptimizationProblem(Protocol):

    optimization_algorithm: OptimizationAlgorithm

    def evaluate_fitness(self, solution: OptimizationSolution) -> float:
        ...

    def holds_constraints(self, solution: OptimizationSolution) -> bool:
        return True
