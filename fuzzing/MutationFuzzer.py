import random

from BaseFuzzer import BaseFuzzer


class MutationFuzzer(BaseFuzzer):
    """Base class for mutational fuzzing"""

    def __init__(self, seed: list[str], min_mutations: int = 1, max_mutations: int = 5) -> None:
        """Constructor.
        `seed` - a list of (input) strings to mutate.
        `min_mutations` - the minimum number of mutations to apply.
        `max_mutations` - the maximum number of mutations to apply.
        """
        self.seed = seed
        self.population = self.seed
        self.seed_index = 0

        self.min_mutations = min_mutations
        self.max_mutations = max_mutations

    def create_candidate(self) -> str:
        """Create a new candidate by mutating a population member"""
        candidate = random.choice(self.population)
        trials = random.randint(self.min_mutations, self.max_mutations)

        for i in range(trials):
            candidate = self.mutate(candidate)

        return candidate

    def fuzz(self) -> str:
        if self.seed_index < len(self.seed):
            # Still seeding
            self.inp = self.seed[self.seed_index]
            self.seed_index += 1
        else:
            # Mutating
            self.inp = self.create_candidate()
        return self.inp

    def mutate(self, inp: str) -> str:
        """Apply a random mutation to the JSON input string"""

        # TODO: Add your mutations here
        mutators = [
            self.mutation1,
            self.mutation2,
            self.mutation3
        ]

        mutator = random.choice(mutators)
        return mutator(inp)

    # TODO: Delete and create your own
    # def example_mutation(self, inp: str) -> str:
    #     """Example of mutation definition"""
    #     return inp + "a"
    
    def mutation1(self, inp: str) -> str:
        if len(inp) == 0:
            return inp
        chars = list(inp)
        random.shuffle(chars)
        return ''.join(chars)
    
    def mutation2(self, inp: str) -> str:
        if len(inp) == 0:
            return inp
        index = random.randint(0, len(inp) - 1)
        char = chr(random.randint(32, 126)) 
        return inp[:index] + char + inp[index:]
    
    def mutation3(self, inp: str) -> str:
        if len(inp) == 0:
            return inp
        index = random.randint(0, len(inp) - 1)
        return inp[:index] + inp[index].upper() + inp[index:]
