# -*- coding: utf8 -*-
import time
import random
import os
import numpy as np
import ocev.fitness as fit
import ocev.selection as sel
import ocev.operators as op
import ocev.report as rep
from ocev.individual import Individual, binary, integer, int_perm, real

from operator import attrgetter
import numpy as np
from copy import copy, deepcopy

class Generation():

    def __init__(self, pop):

        self.pop = pop
        self.best = None
        self.worst = None
        self.average = None
        self.set_values(pop)

    def set_values(self, pop):
        #print([ind.fitness for ind in self.population])
        self.best = max(pop, key=attrgetter('fitness'))
        self.worst = min(pop, key=attrgetter('fitness'))
        self.average = np.average([ind.fitness for ind in pop])


class Population():

    def __init__(self, ga_args, ind_args, sel_args, cros_args, mut_args):
        """
        COD param: str, ('bin','int', 'int-perm', 'real') codificações possiveis
        D: int, tamanho do cromossomo (número de variáveis)
        pop: int, tamanho da população
        bounds param: tuple, (lim_inferior,lim_superior)
        seed param: int, seed para geração de números aleatórios
        """ 
        self.ind_args = ind_args
        self.sel_args = sel_args
        self.cros_args = cros_args
        self.mut_args = mut_args



        print ("Gerando população inicial...")
        self.cod = ga_args["cod"]
        self.pop_size = ind_args["pop_size"]
        self.n_gen = ga_args["gen"]
        self.elite = ga_args["elite"]
        #self.n_exec = ga_args["n_exec"]

        self.fitness_func = eval("fit." + ga_args["fitness"])
        self.selection_func = eval("sel." + sel_args["selection"])
        sel_args.pop("selection")
        

        self.crossover_func = eval("op." + cros_args["crossover"])
        cros_args.pop("crossover")
        print(cros_args)

        self.mutation_func = eval("op." + mut_args["mutation"])
        mut_args.pop("mutation")
        print(mut_args)

        self.generations = []
        self.individuals = eval(self.cod)(**ind_args)

        self.best_individual = None
        try:
            self.evolve()
        except KeyboardInterrupt:
            pass
        


        report = rep.Report(self.generations)
        report.plot_convergence()

    def evolve(self):
        generation = 0
        self.get_fitness(self.individuals)
        self.generations.append(Generation(self.individuals))
        while generation < self.n_gen:
            #self.get_diversity()
            parents = self.selection_func(self.individuals)
            next_generation = self.crossover(parents)
            self.mutation(next_generation)
            self.generations.append(Generation(self.individuals))
            self.individuals = next_generation
            
            generation += 1
        #self.show_best(self.best_individual)

    def get_diversity(self):
        chromos = np.array([ind.chromossome for ind in self.individuals])
        ci = np.sum(chromos, axis=0) / self.pop_size
        div = np.sum((chromos - ci) ** 2)
        #self.diversity.append(div)

    def get_fitness(self, individuals):
        max_fitness = 0.0
        for ind in individuals:
            ind.fitness = round(self.fitness_func(ind.chromossome),5)
            if ind.fitness > max_fitness:
                max_fitness = ind.fitness
                if self.best_individual is None:
                    self.best_individual = deepcopy(ind)
                if ind.fitness > self.best_individual.fitness:
                    self.best_individual = deepcopy(ind)

    def crossover(self, parents):
        next_generation = []
        for ind in range(0, self.pop_size, 2):
            ctax = np.random.uniform(0, 1)
            if ctax < self.cros_args["ratio"]:
                childs = self.crossover_func(
                    parents[ind].chromossome, parents[ind+1].chromossome,
                    **self.cros_args
                )
                next_generation.append(Individual(childs[0]))
                next_generation.append(Individual(childs[1]))
            else:
                next_generation.append(Individual(parents[ind].chromossome))
                next_generation.append(
                    Individual(parents[ind+1].chromossome)
                )
        self.get_fitness(next_generation)
        next_generation = sorted(next_generation, key=lambda ind: ind.fitness)
        print (next_generation[0].chromossome, next_generation[0].fitness)
        next_generation[0] = deepcopy(self.best_individual)
        return next_generation

    def mutation(self, individuals):
        for ind in individuals:
            self.mutation_func(
                ind.chromossome, **self.mut_args
                )

