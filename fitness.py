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