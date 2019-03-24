"""
Utilitary functions
"""

def scale_adjust(b_chromossome, low_bound, high_bound, D,L):
    """
    Adjusts the scale of a binary chromossome
    to its equivalent decimal counterpart
    """
    scale_adjusted = low_bound+((high_bound-low_bound)/(2**L - 1)) \
                     *int(b_chromossome,2)
    return (scale_adjusted)

def find_L(low_bound, high_bound,precision=None):
    """
    Finds L, which is equivalent to the number
    of bits necessary to convert genotype to fenotype
    """
    if precision is None:
        precision = 1
    
    for L in range(1,20):
        if 2**(L-1) < (high_bound - low_bound)/precision <= 2**L:
            print (L)
            return (L)



    raise Exception("Não foi possível encontrar o valor de L")


