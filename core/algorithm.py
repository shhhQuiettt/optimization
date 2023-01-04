from abc import ABC, abstractmethod


class OptimizationAlgorithm(ABC):

    best_solution = None
    problem = None

    @abstractmethod
    def perform(self) -> None:
        pass
