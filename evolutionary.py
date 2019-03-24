# -*- coding: utf8 -*-
import time
import random
import os
import numpy as np
import individual as ind
import fitness as fit


class IndvidualFactory():
    types = {'bin':ind.Binary,
            'int':ind.Integer,
            'int-perm':ind.PermutedInteger,
            'real':ind.Real}
 
    @staticmethod
    def create_individual(cod, **kwargs):
            return IndvidualFactory.types[cod](**kwargs)


class EvolutionaryAlgorithm():

    def __init__(self,input_params):
        """
        COD param: str, ('bin','int', 'int-perm', 'real') codificações possiveis
        D: int, tamanho do cromossomo (número de variáveis)
        POP: int, tamanho da população
        bounds param: tuple, (lim_inferior,lim_superior)
        seed param: int, seed para geração de números aleatórios
        """ 
            
        print ("Gerando População inicial...")
        self.list_pop = []
        self.COD = input_params["COD"]
        self.POP = int(input_params["POP"])
        self.D = int(input_params["D"])
        self.fitness_func = eval("fit." + input_params["fitness"])
        self.gerenerate_population(input_params)
        best,worst = self.get_fitness()
        self.info()
        self.print_pop()
        print ("best:",best,"worst:",worst)

    def gerenerate_population(self, input_params):
        """
        Gera a população com base nos parametros de inicialização
        """
        for _ in range(self.POP):
            self.list_pop.append(IndvidualFactory.create_individual(self.COD,**input_params))

    def get_fitness(self):
        start = time.time()
        best = -1
        worst = 100000
        for ind in self.list_pop:
            ind.fitness = self.fitness_func(ind.chromossome)
            if ind.fitness > best:
                best = ind.fitness
            if ind.fitness < worst:
                worst = ind.fitness

        end = time.time() - start
        print ("time:", end)
        return (best,worst)

    def info(self):
        print ("[Info]")
        print (" - COD: "+str(self.COD))
        print (" - D: "+str(self.D))
        print (" - POP: "+str(self.POP))
        #print (" - bounds: ["+str(self.low_bound)+","+str(self.high_bound)+"]")

    def print_pop(self):
        print ("[Population = "+str(self.POP)+"]")
        for i in range(0,len(self.list_pop)):
            print (" - " + str(i + 1) + " ->",self.list_pop[i].chromossome, "-> fit: ", round(self.list_pop[i].fitness,5) )
        return






