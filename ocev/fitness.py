import math
from numba import jit,njit
from numba import int64,float32,float64
import numpy as np

@njit(float32(int64[:]),parallel=True)
def n_queens(chromosome):
    clashes = 1
    for i in range(0, len(chromosome)):
        for j in range(1, len(chromosome)):
            if (i != j):
                dx = abs(i-j)
                dy = abs(chromosome[i] - chromosome[j])
                if(dx == dy):
                    clashes += 1
    

    return (1/clashes)


@njit(float32(float32),parallel=True)
def max_f_alg_exer(x):
    return (4 + math.cos(20*x) - abs(x)/2 + (x**3)/4)

@njit(float32(float32),parallel=True)
def min_f_alg_exer(x):
    return (4 + math.cos(20*x) - abs(x)/2 + (x**3)/4)

@njit(float32(float64[:]),parallel=True)
def fab_radios(chromosome):
    fit = (30*chromosome[0] + 40*chromosome[1])/1360
    restr = max(0,(chromosome[0] + 2*chromosome[1]-40)/16)
    return (fit - restr)

if __name__ == "__main__":
    a = np.arange(0,32)
    np.random.shuffle(a)
    print(n_queens0(a))