from optimization.core.algorithm import OptimizationAlgorithm
from .solution import EvolutionarySolution
from typing import List


class EvolutionaryAlgorithm(OptimizationAlgorithm):
    population: List[EvolutionarySolution]

    
