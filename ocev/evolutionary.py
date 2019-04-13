# -*- coding: utf8 -*-
import time
import random
import os
import numpy as np
import ocev.creators as cr
import ocev.fitness as fit
import ocev.selection as sel
import ocev.operators as op
import ocev.report as rep

class Generation():

    def __init__(self):
        self.population = []
        
        self.best = None
        self.worst = None
        self.mean = None
        self.n_rest_broken = None

    def get_n_rest_broken(self):
        cont = 0
        for ind in self.population:
            if not ind.bounds_ok():
                cont += 1
        self.n_rest_broken = cont

    def set_values(self):
        list_fit = [ind.fitness for ind in self.population]
        self.best = self.population[list_fit.index(max(list_fit))]
        self.worst = self.population[list_fit.index(min(list_fit))]
        self.mean = sum(list_fit)/len(list_fit)
        self.get_n_rest_broken()

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
        self.cod = ga_args["cod"]
        self.pop_size = ga_args["pop"]
        self.n_gen = ga_args["gen"]
        self.elite = ga_args["elite"]
        self.generations = [Generation()]*self.n_gen
        self.dim = ind_args['dim']
        self.fitness_func = eval("fit." + ind_args["fitness"])

        self.population = self.gerenerate_population(ind_args)

        self.operator = cr.OperatorCreator.get_operator(self.cod)
        
        for i, gen in enumerate(self.generations):
            gen.population = self.population
            self.get_fitness()
            gen.set_values()
            print("GEN:",i)
            print(gen.best.chromossome, gen.worst.chromossome)
            print(gen.best.fitness, gen.worst.fitness)

            self.population = eval("sel." + sel_args["selection"])
            self.population = eval("self.operator." + op_args["crossover"])
            self.population = eval("self.operator." + op_args["mutation"])

            if self.elite:
                self.save_elite()
            
        self.print_pop(self.population)
        print(gen.best_fitness, gen.worst_fitness)

    def gerenerate_population(self, ind_args):
        """
        Gera a população com base nos parametros de inicialização
        """
        population = []
        for _ in range(self.pop_size):
            population.append(cr.IndvidualCreator.create(self.cod, ind_args))
        
        return population

    def save_elite(self):
        list_fit = [ind.fitness for ind in self.population]
        min_pos = list_fit.index(min(list_fit))
        max_pos = list_fit.index(max(list_fit))
        self.population[min_pos] = self.population[max_pos]

    def get_fitness(self):
        """
        TODO DOC
        """
        start = time.time()
        for ind in self.population:
            ind.fitness = round(self.fitness_func(np.array(ind.chromossome)),5)
        end = time.time() - start
        print ("time:", end)

    def info(self):
        """
        TODO DOC
        """
        print ("[Info]")
        print (" - COD: "+str(self.cod))
        print (" - D: "+str(self.dim))
        print (" - pop_size: "+str(self.pop_size))
        #print (" - bounds: ["+str(self.low_bound)+","+str(self.high_bound)+"]")

    def print_pop(self,pop):
        """
        TODO DOC
        """
        print ("[population = "+str(self.pop_size)+"]")
        for i in range(0,len(pop)):
            print (" " + str(i + 1) + " ->",pop[i].chromossome,
                   "-> fit: ", round(pop[i].fitness,5))
        return






