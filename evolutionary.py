
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


        for i in range(0,POP):
            self.list_pop.append(Individual('bin',D=D,bounds=bounds))

    def print_pop(self):
        for i in range(0,len(self.list_pop)):
            print (self.list_pop[i].chromossome)
        return



class Individual():

    chromossome = []

    def __init__(self,COD,D,bounds,seed=None):
        if seed != None:
            random.random.seed(seed)
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
                    gene = random.randint(bounds[0],bounds[1])
                    self.chromossome.append(gene)
            elif COD == 'int-perm':
                for i in range(0,D):
                    gene = random.randint(bounds[0],bounds[1])
                    self.chromossome.append(gene)
            elif COD == 'real':
                for i in range(0,D):
                    gene = random.uniform(bounds[0],bounds[1])
                    self.chromossome.append(gene)
        else:
            raise Exception("Combinação de parâmetros inválida")
        return

    def params_are_valid(self,COD, D, bounds):
        return (True)
        """
        if COD in ['int','int-perm','real']:
            if (bounds is None) or (bounds[0] => bounds[1]) or (not isinstance(tuple,bounds)) or (len(bounds)>2):
                return (False)
        elif COD == 'bin':
            if bounds is not None:
                return (False)
        """





    def print_individual(self):
        print (chromossome)
        return

if __name__ == "__main__":
    start = time.time()
    ae = EvolutionaryAlgorithm()
    ae.gera_pop('bin',D=10,POP=500)
    ae.print_pop()
    end = time.time() - start 
    print ("Tima taken: ",end," seconds")