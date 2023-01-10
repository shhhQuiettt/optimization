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

        participants_indexes = random.sample(
            range(len(population)), self.tournament_size
        )
        best_participant_index = max(
            participants_indexes, key=lambda idx: population[idx].fitness
        )
        population.pop(best_participant_index)
        return population[best_participant_index]
