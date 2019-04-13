"""
Utilitary functions
"""

def scale_adjust(b_chromossome, bounds, L, precision):
    """
    Adjusts the scale of a binary chromossome
    to its equivalent decimal counterpart
    """
    scale_adjusted = []
    cont = 0
    for var in range(0,len(L)):
        scale_adjusted.append(round(bounds['low'][var] \
                            +((bounds['high'][var]-bounds['low'][var])/(2**L[var] - 1)) \
                            *int(b_chromossome[cont:cont+L[var]],2),len(str(precision))-1))
        cont += L[var]
    
    return (scale_adjusted)

def find_L(nvars, bounds, precision=None):
    """
    Finds L, which is equivalent to the number
    of bits necessary to convert genotype to fenotype
    """
    if precision is None:
        precision = 1
    
    _L = []
    for var in range(0,nvars):
        for L in range(1,20):
            if 2**(L-1) < (bounds['high'][var] - bounds['low'][var] + 1)/precision <= 2**L:
                _L.append(L)
                break
    if len(_L) == nvars:
        return (_L)
    else:
        raise Exception("Não foi possível encontrar o valor de L")


if __name__ == "__main__":
    print (find_L(2,{'high':[16,24],'low':[0,0]},1))

