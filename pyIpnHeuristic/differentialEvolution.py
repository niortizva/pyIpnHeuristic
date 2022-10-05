from typing import List

from . import PopulationBasedHeuristics
import random


class DifferentialEvolution(PopulationBasedHeuristics):
    """
    Differential Evolution Algorithm
    """
    
    def __init__(self, *args, **params):
        super().__init__(*args, **params)
        # Differential Evolution parameters
        self.f = params.get("f", 0.5)
        self.cr = params.get("cr", 0.8)
        # Types: rand-1, best-1, current-to-best-1, best-2, rand-2
        self.type = params.get("type", "rand-1")
        self.index_list = [i for i in range(self.population_size)]
        
        # Check if population has enough size
        if self.population_size <= 3:
            raise ValueError("""
            Population size is not valid. Population size
            must be greater than 3
            """)
        
    def mutation(self) -> List[dict]:
        """
        Mutation Heuristic

        - For each x_i in population
            - Select x_r1, x_r2, x_r3 such as r1 != r2 != r3 != i
            - m_i = x_r1 + F * (x_r2 - x_r3)
            - add m_i to Mutation Matrix
        :return list: Mutation Matrix
        """
        mutation_matrix: List[dict] = []
        if self.type == "rand-1":
            for i in range(self.population_size):
                # Get Different Random Indexes
                r1 = random.choice(list(set(self.index_list) - {i}))
                r2 = random.choice(list(set(self.index_list) - {i, r1}))
                r3 = random.choice(list(set(self.index_list) - {i, r1, r2}))
                # Get associated vectors
                x1 = self.population[r1]["x"]
                x2 = self.population[r2]["x"]
                x3 = self.population[r3]["x"]
                mutation_matrix.append(self.fix_ranges({"x": [x1[j] + self.f * (x2[j] - x3[j])
                                                              for j in range(self.dimension)]}))
        elif self.type == "best-1":
            for i in range(self.population_size):
                # Get best vector
                fx_matrix = [vector["fx"] for vector in self.population]
                x_best = self.population[fx_matrix.index(min(fx_matrix))]["x"]
                # Get Different Random Indexes
                r1 = random.choice(list(set(self.index_list) - {i}))
                r2 = random.choice(list(set(self.index_list) - {i, r1}))
                # Get associated vectors
                x1 = self.population[r1]["x"]
                x2 = self.population[r2]["x"]
                mutation_matrix.append(self.fix_ranges({"x": [x_best[j] + self.f * (x1[j] - x2[j])
                                                              for j in range(self.dimension)]}))
        elif self.type == "current-to-best-1":
            for i in range(self.population_size):
                # Get best vector
                fx_matrix = [vector["fx"] for vector in self.population]
                x_best = self.population[fx_matrix.index(min(fx_matrix))]["x"]
                x_current = self.population[i]["x"]
                # Get Different Random Indexes
                r1 = random.choice(list(set(self.index_list) - {i}))
                r2 = random.choice(list(set(self.index_list) - {i, r1}))
                # Get associated vectors
                x1 = self.population[r1]["x"]
                x2 = self.population[r2]["x"]
                mutation_matrix.append(self.fix_ranges({"x": [
                    x_current[j] + self.f * (x_best[j] - x_current[j]) + self.f * (x1[j] - x2[j])
                    for j in range(self.dimension)
                ]}))
        elif self.type == "best-2":
            for i in range(self.population_size):
                # Get best vector
                fx_matrix = [vector["fx"] for vector in self.population]
                x_best = self.population[fx_matrix.index(min(fx_matrix))]["x"]
                # Get Different Random Indexes
                r1 = random.choice(list(set(self.index_list) - {i}))
                r2 = random.choice(list(set(self.index_list) - {i, r1}))
                r3 = random.choice(list(set(self.index_list) - {i, r1, r2}))
                r4 = random.choice(list(set(self.index_list) - {i, r1, r2, r3}))
                # Get associated vectors
                x1 = self.population[r1]["x"]
                x2 = self.population[r2]["x"]
                x3 = self.population[r3]["x"]
                x4 = self.population[r4]["x"]
                mutation_matrix.append(self.fix_ranges({"x": [
                    x_best[j] + self.f * (x1[j] - x2[j]) + self.f * (x3[j] - x4[j])
                    for j in range(self.dimension)
                ]}))
        elif self.type == "rand-2":
            for i in range(self.population_size):
                # Get best vector
                fx_matrix = [vector["fx"] for vector in self.population]
                # Get Different Random Indexes
                r0 = random.choice(list(set(self.index_list) - {i}))
                r1 = random.choice(list(set(self.index_list) - {i, r0}))
                r2 = random.choice(list(set(self.index_list) - {i, r0, r1}))
                r3 = random.choice(list(set(self.index_list) - {i, r0, r1, r2}))
                r4 = random.choice(list(set(self.index_list) - {i, r0, r1, r2, r3}))
                # Get associated vectors
                x0 = self.population[r0]["x"]
                x1 = self.population[r1]["x"]
                x2 = self.population[r2]["x"]
                x3 = self.population[r3]["x"]
                x4 = self.population[r4]["x"]
                mutation_matrix.append(self.fix_ranges({"x": [
                    x0[j] + self.f * (x1[j] - x2[j]) + self.f * (x3[j] - x4[j])
                    for j in range(self.dimension)
                ]}))
        else:
            raise TypeError("¡Differential Evolution variant type is not defined!")
        
        return mutation_matrix
    
    def recombination(self, mutation_matrix: List[dict]) -> List[dict]:
        """
        Recombination Heuristic

        - For each x_i in population
            - Select random number rnd in [0, 1]
            - Select random population index rnd_index
            - Select random xr, vr from population and mutation matrix
            - For each x_i,j in x_i
                - if rnd <= CR or j = rnd_index, u_i,j = v_r,j else u_i,j = x_r,j
            - add u_i to Recombination Matrix
        :param list mutation_matrix: Mutation Matrix
        :return list: Recombination Matrix
        """
        recombination_matrix: List[dict] = []
        for i in range(self.population_size):
            xr = self.population[i]["x"]
            vr = mutation_matrix[i]["x"]
            recombination_matrix.append({"x": [
                vr[j] if random.random() <= self.cr or j == random.choice(self.index_list)
                else xr[j] for j in range(self.dimension)]})
        
        return self.evaluate_population(recombination_matrix)
    
    def selection(self, recombination_matrix: List[dict]) -> List[dict]:
        """
        Selection Heuristic

        - For each x_i in population
            - Select best between x_i and u_i from population and recombination matrix
            - Add the best to the new population
        :param list recombination_matrix: Recombination Matrix
        :return list: Selection Matrix
        """
        return [self.comparison(recombination_matrix[i], self.population[i])
                for i in range(self.population_size)]
        
    def population_enhancement(self) -> None:
        """
        Population Enhancement Method
        :return None:
        """
        # Step 1: Mutation
        mutation_matrix = self.mutation()
        # Step 2: Recombination
        recombination_matrix = self.recombination(mutation_matrix)
        # Step 3: Selection
        self.population = self.selection(recombination_matrix)
        
    def stop_condition(self) -> bool:
        return False


if __name__ == "__main__":
    pass
