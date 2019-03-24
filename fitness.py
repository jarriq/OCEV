import math
from numba import jit,njit
from numba import int64,float32
import numpy as np

@njit(float32(int64[:]),parallel=True)
def n_queens(chromosome):
    clashes = abs(len(chromosome) - len(np.unique(chromosome)))

    for i in range(len(chromosome)):
        for j in range(len(chromosome)):
            if ( i != j):
                dx = abs(i-j)
                dy = abs(chromosome[i] - chromosome[j])
                if(dx == dy):
                    clashes += 1
    return (1/(1+clashes))

@njit(float32(float32),parallel=True)
def max_f_alg_exer(x):
    return (4 + math.cos(20*x) - abs(x)/2 + (x**3)/4)

@njit(float32(float32),parallel=True)
def min_f_alg_exer(x):
    return (math.cos(20*x) - abs(x)/2 + (x**3)/4)