from typing import Protocol
from .solution import OptimizationSolution
from .algorithm import OptimizationAlgorithm


class OptimizationProblem(Protocol):

    optimization_algorithm: OptimizationAlgorithm

    def set_optimization_algorithm(self, optimization_algorithm: OptimizationAlgorithm) -> None:
        pass

    def evaluate_fitness(self, solution: OptimizationSolution) -> float:
        ...

    def holds_constraints(self, solution: OptimizationSolution) -> bool:
        return True

    def get_random_solution(self) -> OptimizationSolution:
        ...
