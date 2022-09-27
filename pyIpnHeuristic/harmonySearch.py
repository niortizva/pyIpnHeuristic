from . import PopulationBasedHeuristics
import random


class HarmonySearch(PopulationBasedHeuristics):
    """
    Harmony Search Algorithm
    """
    
    def __init__(self, *args, **params):
        super().__init__(*args, **params)
        self.hcmr = params.get("hcmr", 0.95)
        self.par = params.get("par", 0.10)
        self.alpha = params.get("alpha", 1.)
        
    def create_from_population(self) -> dict:
        """
        Create New Harmony from the current population

        - For j in [0, dimension]
            - Select random x_i,j from population
            - Get new harmony nh_i,j = x_i,j
        :return dict: New harmony
        """
        x = [self.population[i]["x"] for i in range(self.population_size)]
        return {
            "x": [
                random.choice([x[i][j] for i in range(self.population_size)]) 
                for j in range(self.dimension)
            ],
            "fx": None,
            "gx": None,
            "hx": None
        }
    
    def add_noise(self, harmony: dict) -> dict:
        """
        Add noise to a given harmony

        - For each j in [0, dimension]
            - Set random number U in [-1, 1]
            - h_i,j = x_i,j + alpha * U
        :param dict harmony: Harmony
        :return dict: Noisy Harmony
        """
        harmony["x"] = [
            harmony["x"][j] + self.alpha * random.uniform(-1, 1)
            for j in range(self.dimension)
        ]
        return harmony
        
    def population_enhancement(self) -> None:
        """
        Population Enhancement Method
        :return None:
        """
        fx = [self.population[i]["fx"] for i in range(self.population_size)]
        worst_index = fx.index(max(fx))
        worst_harmony = self.population[worst_index]
        rnd = random.random()
        
        # Create new Harmony
        if rnd <= self.hcmr:
            rnd = random.random()
            new_harmony = self.create_from_population()
            if rnd <= self.par:
                new_harmony = self.add_noise(new_harmony)
            new_harmony = self.fix_ranges(new_harmony)
        else:
            new_harmony = self.create_individual()
        new_harmony = self.evaluate_individual(new_harmony)
        
        # Select best harmony between worst and new
        self.population[worst_index] = self.comparison(worst_harmony, new_harmony)
        
    def stop_condition(self) -> bool:
        return False


if __name__ == "__main__":
    pass
