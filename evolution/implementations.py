from .algorithm import EvolutionaryAlgorithm
from optimization.core.problem import OptimizationProblem
from typing import List
from .solution import EvolutionarySolution
from .selection import SelectionStrategy
import random


class SteadyGeneticAlgorithm(EvolutionaryAlgorithm):
    problem: OptimizationProblem
    solution_class: EvolutionarySolution

    population: List[EvolutionarySolution]
    population_size: int

    mutation_chance: float
    crossover_chance: float

    max_iteration_without_improvement: int = 100
    max_iterations: int = 10_000

    selection_strategy: SelectionStrategy

    _iterations = 0
    _iteration_without_improvement = 0

    def perform(self) -> None:
        self.initialize_population()
        while self.should_iterate():
            self._iterations += 1

            sol1, sol2 = self.select_good_solutions(2)

            if self.should_crossover():
                sol1, sol2 = sol1.crossover(sol2)

            if self.should_mutate():
                sol1.mutate()

            if self.should_mutate():
                sol2.mutate()

            if (
                sol1.fitness > self.best_solution.fitness
                or sol2.fitness > self.best_solution.fitness
            ):
                self._iteration_without_improvement = 0
                self.best_solution = max(sol1, sol2, key=lambda x: x.fitness)

            else:
                self._iteration_without_improvement += 1

    def initialize_population(self) -> List[EvolutionarySolution]:
        return [
            self.solution_class.from_optimization_solution(
                self.problem.get_random_solution()
            )
            for _ in range(self.population_size)
        ]

    def should_iterate(self) -> bool:
        return (
            self._iterations < self.max_iterations
            and self._iteration_without_improvement
            < self.max_iteration_without_improvement
        )

    def select_good_solutions(self, no: int) -> List[EvolutionarySolution]:
        good_solutions = [self.selection_strategy.select_and_remove(self.population)]
        while len(good_solutions) < no:
            solution = self.selection_strategy.select_and_remove(self.population)
            if solution not in good_solutions:
                good_solutions.append(solution)

        return good_solutions

    def should_mutate(self) -> bool:
        return random.random() < self.mutation_chance

    def should_crossover(self) -> bool:
        return random.random() < self.crossover_chance
