# startegy pattern for selection method
from abc import ABC, abstractmethod
from typing import List
from .solution import EvolutionarySolution
import random


class SelectionStrategy(ABC):
    @abstractmethod
    def select_and_remove(
        self, population: List[EvolutionarySolution]
    ) -> EvolutionarySolution:
        pass


class Tournament(SelectionStrategy):
    def __init__(self, tournament_size: int = 3):
        self.tournament_size = tournament_size

    def select_and_remove(
        self, population: List[EvolutionarySolution]
    ) -> EvolutionarySolution:

        participants = [
            population.pop(random.randrange(len(population)))
            for _ in range(self.tournament_size)
        ]

        return max(participants, key=lambda x: x.fitness)
