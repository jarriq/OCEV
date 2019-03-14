
import time
import random



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

        print (bounds)
        for _ in range(0,POP):
            #new_individual = Individual('bin',D=D,bounds=bounds)
            self.list_pop.append(Individual(COD=COD,D=D,bounds=bounds))

    def print_pop(self):
        for i in range(0,len(self.list_pop)):
            print ("Individual ", i+1, ":",self.list_pop[i].chromossome)
        return



class Individual():

    

    def __init__(self,COD,D,bounds,seed=None):
        self.chromossome = []
        if seed != None:
            random.seed(seed)
        self.gera_cromossomo(COD,D,bounds)
        pass

    def gera_cromossomo(self, COD,D, bounds=None):
        """
        Gera as variáveis do individuo
        """
        if self.params_are_valid(COD,D,bounds):
            if COD == 'bin':
                for i in range(0,D):
                    gene = random.randint(0,1)
                    self.chromossome.append(gene)
            elif COD == 'int':
                for i in range(0,D):
                    gene = random.randrange(bounds[0],bounds[1])
                    self.chromossome.append(gene)
            elif COD == 'int-perm':
                for i in range(0,D):
                    gene = random.randrange(bounds[0],bounds[1])
                    self.chromossome.append(gene)
            elif COD == 'real':
                for i in range(0,D):
                    gene = random.random(bounds[0],bounds[1])
                    self.chromossome.append(gene)
        else:
            raise Exception("Combinação de parâmetros inválida")

        return

    def params_are_valid(self,COD, D, bounds):
        if COD in ['int','int-perm','real']:
            if (bounds is None) or (bounds[0] >= bounds[1]) or (not isinstance(bounds,tuple)) or (len(bounds)>2):
                return (False)
        elif COD == 'bin':
            if bounds is not None:
                print ("AAAAAAAAAA")
                return (False)
        
        return (True)

    def print_individual(self):
        print (self.chromossome)
        return

if __name__ == "__main__":
    start = time.time()
    ae = EvolutionaryAlgorithm()
    ae.gera_pop('int',D=30,POP=5000,bounds=(-50,50))
    ae.print_pop()
    end = time.time() - start 
    print ("Tima taken: ",end," seconds")
