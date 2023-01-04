from abc import abstractmethod

from optimization.core.algorithm import OptimizationAlgorithm
from optimization.core.problem import OptimizationProblem
from .solution import EvolutionarySolution
from typing import List


class EvolutionaryAlgorithm(OptimizationAlgorithm):
    best_solution: EvolutionarySolution
    population: List[EvolutionarySolution]
    problem: OptimizationProblem

    @abstractmethod
    def get_random_solution(self) -> EvolutionarySolution:
        pass
