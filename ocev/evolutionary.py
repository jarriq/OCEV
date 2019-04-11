# -*- coding: utf8 -*-
import time
import random
import os
import numpy as np
import ocev.creators as cr
import ocev.fitness as fit
import ocev.selection as sel


class EvolutionaryAlgorithm():

    def __init__(self, ga_args, ind_args, sel_args, op_args):
        """
        COD param: str, ('bin','int', 'int-perm', 'real') codificações possiveis
        D: int, tamanho do cromossomo (número de variáveis)
        pop: int, tamanho da população
        bounds param: tuple, (lim_inferior,lim_superior)
        seed param: int, seed para geração de números aleatórios
        """ 
            
        print ("Gerando população inicial...")
        self.population = []
        self.cod = ga_args["cod"]
        self.pop = ga_args["pop"]
        self.gen = ga_args["gen"]
        self.dim = ind_args['dim']
        self.fitness_func = eval("fit." + ind_args["fitness"])

        self.gerenerate_population(ind_args)
        self.get_fitness()
        self.info()
        self.print_pop(self.population)
        print ("selected")
        selected = sel.stochastic_sampling_with_replacement(self.population)
        self.print_pop(selected)
        

    def gerenerate_population(self, ind_args):
        """
        Gera a população com base nos parametros de inicialização
        """
        for _ in range(self.pop):
            self.population.append(cr.IndvidualCreator.create(self.cod, ind_args))

    def get_fitness(self):
        """
        TODO DOC
        """
        best = -1
        worst = 9999
        start = time.time()
        for ind in self.population:
            ind.fitness = self.fitness_func(ind.chromossome)
            if ind.fitness > best:
                best = ind.fitness
            if ind.fitness < worst:
                worst = ind.fitness
        end = time.time() - start
        print ("time:", end)
        print ("best: ", best, "worst:", worst)


    def info(self):
        """
        TODO DOC
        """
        print ("[Info]")
        print (" - COD: "+str(self.cod))
        print (" - D: "+str(self.dim))
        print (" - pop: "+str(self.pop))
        #print (" - bounds: ["+str(self.low_bound)+","+str(self.high_bound)+"]")

    def print_pop(self,pop):
        """
        TODO DOC
        """
        print ("[population = "+str(self.pop)+"]")
        for i in range(0,len(pop)):
            print (" " + str(i + 1) + " ->",pop[i].chromossome,
                   "-> fit: ", round(pop[i].fitness,5))
        return






