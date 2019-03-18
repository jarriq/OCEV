
import time
import random
import multiprocessing
from numba import double
from numba.decorators import jit, autojit
import numpy as np



class EvolutionaryAlgorithm():

    def __init__(self,COD=None,D=None,POP=None,bounds=None,seed=None):
        """
        COD param: str, ('bin','int', 'int-perm', 'real') codificações possiveis
        D: int, tamanho do cromossomo (número de variáveis)
        POP: int, tamanho da população
        bounds param: tuple, (lim_inferior,lim_superior)
        seed param: int, seed para geração de números aleatórios
        """
        self.params_are_valid(COD=COD,D=D,POP=POP,bounds=bounds)
        
        self.list_pop = []
        self.COD = COD
        self.D = D
        self.POP = POP 
        self.bounds = bounds
        self.seed = seed

        self.gera_pop()


    def gera_pop(self, seed=None):
        """
        Gera a população com base nos parametros de inicialização
        """
        for _ in range(self.POP):
            self.list_pop.append(Individual(COD=self.COD,D=self.D,bounds=self.bounds,seed=self.seed))

    def info(self):
        print ("[Info]")
        print (" - COD: "+str(self.COD))
        print (" - D: "+str(self.D))
        print (" - POP: "+str(self.POP))
        print (" - bounds: "+str(self.bounds))
        print (" - seed: "+str(self.seed))

    def print_pop(self):
        print ("[Population = "+str(self.POP)+"]")
        for i in range(0,len(self.list_pop)):
            print (" - " + str(i+1) + " ->",self.list_pop[i].chromossome)
        return

    def params_are_valid(self,COD, D, POP, bounds):
        if POP <= 0:
            raise ValueError(POP + ": Tamanho de população inválido")

        if COD not in ["bin","int","int-perm","real"]:
            raise ValueError(COD + ": Codificação inválida ou não suportada") 

        if COD in ['int','real']:
            if (bounds is None) or (bounds[0] >= bounds[1]) or (not isinstance(bounds,tuple)) or (len(bounds)>2):
                raise ValueError(COD + ": Combinação de parâmetros inválida")
        elif COD == 'int-perm':
            if (bounds is None) or len(list(range(bounds[0],bounds[1])))!=D:
                raise ValueError(COD + ": Combinação de parâmetros inválida")
        elif COD == 'bin':
            if bounds is not None:
                raise ValueError(COD + ": Combinação de parâmetros inválida")
        
        return True



class Individual():


    def __init__(self,COD,D,bounds,seed=None):
        self.chromossome = np.array
        if seed != None:
            random.seed(seed)
        self.chromossome = self.gera_cromossomo(COD,D,bounds)


    def gera_cromossomo(self, COD,D, bounds=None):
        """
        Gera as genes(variáveis) do individuo
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
    
    

    start = time.time()
    ae = EvolutionaryAlgorithm('bin',D=10,POP=10)
    ae.info()
    ae.print_pop()
    
    ae = EvolutionaryAlgorithm('int',D=10,POP=10,bounds=(-5,5))
    ae.info()
    ae.print_pop()
    
    ae = EvolutionaryAlgorithm('int-perm',D=10,POP=10,bounds=(0,10))
    ae.info()
    ae.print_pop()
    
    ae = EvolutionaryAlgorithm('real',D=10,POP=10,bounds=(-10,10))
    ae.info()
    ae.print_pop()
    
    end = time.time() - start 
    
    print ("Tima taken: ",end," seconds")
  
