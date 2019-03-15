
import time
import random
import multiprocessing
from numba import double
from numba.decorators import jit, autojit
import numpy as np



class EvolutionaryAlgorithm():

    list_pop = []

    def __init__(self):
        pass


    def gera_pop(self, COD, POP, D, bounds=None,seed=None):
        """
        COD param: str, 'bin','int', 'int-perm', 'real'
        bounds param: tuple, (lim_inferior,lim_superior)
        POP: int, tamanho da população
        D: int, tamanho do cromossomo (número de variáveis)
        """
        if POP <= 0:
            raise ValueError("Tamanho de população inválido")

        if COD not in ["bin","int","int-perm","real"]:
            raise ValueError("Codificação inválida ou não suportada")

        if self.params_are_valid(COD=COD,D=D,bounds=bounds):
            for _ in range(POP):
                self.list_pop.append(Individual(COD=COD,D=D,bounds=bounds))
        else:
            raise Exception("Combinação de parâmetros inválida")

    def print_pop(self):
        for i in range(0,len(self.list_pop)):
            print ("Individual ", i+1, ":",self.list_pop[i].chromossome)
        return

    def params_are_valid(self,COD, D, bounds):
        if COD in ['int','real']:
            if (bounds is None) or (bounds[0] >= bounds[1]) or (not isinstance(bounds,tuple)) or (len(bounds)>2):
                return (False)
        elif COD == 'int-perm':
            if (bounds is None) or len(list(range(bounds[0],bounds[1])))!=D:
                return (False)
        elif COD == 'bin':
            if bounds is not None:
                return (False)
        
        return (True)



class Individual():


    def __init__(self,COD,D,bounds,seed=None):
        self.chromossome = np.array
        if seed != None:
            random.seed(seed)
        self.chromossome = self.gera_cromossomo(COD,D,bounds)
        pass

    def gera_cromossomo(self, COD,D, bounds=None):
        """
        Gera as variáveis do individuo
        """
        if COD == 'bin':
            chromossome = np.random.choice(a=[False, True], size=D)

        elif COD == 'int':
            chromossome = np.random.randint(bounds[0],bounds[1],D)

        elif COD == 'int-perm':
            chromossome = np.arange(bounds[0],bounds[1])
            np.random.shuffle(chromossome)
            
        elif COD == 'real':
            chromossome = np.random.uniform(bounds[0],bounds[1],D)

        return (chromossome)

    def print_individual(self):
        print (self.chromossome)
        return



if __name__ == "__main__":
    
    ae = EvolutionaryAlgorithm()

    start = time.time()
    ae.gera_pop('bin',D=10,POP=10)
    ae.gera_pop('int',D=10,POP=10,bounds=(-5,5))
    ae.gera_pop('int-perm',D=10,POP=10,bounds=(0,10))
    ae.gera_pop('real',D=10,POP=10,bounds=(-10,10))
    end = time.time() - start 

    ae.print_pop()
    
    print ("Tima taken: ",end," seconds")
  
