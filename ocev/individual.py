import time
import random
import numpy as np
import ocev.utils as utils


class Individual():

    def __init__(self, chromossome):
        self.chromossome = chromossome
        self.fitness = 0

def binary(pop_size, dim, lower_bound=0, upper_bound=0):
    chromos = []
    for ind in range(pop_size):
        chromos.append("".join(str(random.choice("01")) for i in range(int(dim))))
    return [Individual(chromo) for chromo in chromos]


def integer(pop_size, dim, lower_bound=0, upper_bound=10):
    chromos = []
    for ind in range(pop_size):
        chromos.append(np.random.randint(lower_bound, upper_bound, size=dim))
    return [Individual(chromo) for chromo in chromos]


def int_perm(pop_size, dim, lower_bound=0, upper_bound=10):
    chromos = []
    for ind in range(pop_size):
        chromos.append(np.random.permutation(dim))
    return [Individual(chromo) for chromo in chromos]


def real(pop_size, dim, lower_bound=0, upper_bound=10):
    chromos = []
    for ind in range(pop_size):
        chromos.append(
            np.random.uniform(lower_bound, upper_bound, size=dim)
        )
    return [Individual(chromo) for chromo in chromos]
