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

    def __init__(self, pop):
        self.population = pop
        
        self.best = None
        self.worst = None
        self.mean = None
        self.n_rest_broken = None     
        self.set_values()

    def get_n_rest_broken(self):
        cont = 0
        for ind in self.population:
            if not ind.bounds_ok():
                cont += 1
        self.n_rest_broken = cont

    def set_values(self):
        list_fit = [ind.fitness for ind in self.population]
        print ("max:", max(list_fit), "I:",list_fit.index(max(list_fit)))
        print ("max:", min(list_fit), "I:", list_fit.index(min(list_fit)))
        self.best = self.population[list_fit.index(max(list_fit))]
        print("setvalues", self.best.fitness)
        self.worst = self.population[list_fit.index(min(list_fit))]
        self.mean = round(sum(list_fit)/len(list_fit),5)
        self.get_n_rest_broken()

    def print(self):
        #print("pop: ",self.population)
        print("best_fit: ",self.best.fitness)
        print("worst_fit: ",self.worst.fitness)
        print("mean_fit: ",self.mean)
        print("broken: ",self.n_rest_broken)

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
        self.generations = []
        self.dim = ind_args['dim']
        self.fitness_func = eval("fit." + ind_args["fitness"])

        self.population = self.gerenerate_population(ind_args)

        self.operator = cr.OperatorCreator.get_operator(self.cod)

        for i in range(0,self.n_gen):
            if i == 0:
                gen = Generation(self.population)
            else:
                if self.elite:
                    final_pop[0] = self.generations[i-1].best
                gen = Generation(final_pop)

            self.generations.append(gen)
            print("---------------------------------------")
            print("GEN:",i)
            print(gen.best.chromossome, gen.worst.chromossome)
            print(gen.best.fitness, gen.worst.fitness)
            print("Start")
            self.get_fitness(self.generations[i].population, self.fitness_func)
            self.print_pop(self.generations[i].population)
            selected = eval("sel." + sel_args["selection"])
            print("SELECTION")
            self.get_fitness(selected, self.fitness_func)
            self.print_pop(selected)
            crossed = eval("self.operator." + op_args["crossover"])
            print("CROSSOVER")
            self.get_fitness(crossed, self.fitness_func)
            self.print_pop(crossed)
            mutated = eval("self.operator." + op_args["mutation"])
            print("MUTATION")
            self.get_fitness(mutated, self.fitness_func)
            self.print_pop(mutated)
            gen.print()

            final_pop = mutated
            #self.print_pop(new_population)
            
            self.generations.append(gen)
            
        self.print_pop(self.population)
        print(gen.best.fitness, gen.worst.fitness)
        report = rep.Report(self.generations)
        report.plot_convergence()

    def gerenerate_population(self, ind_args):
        """
        Gera a população com base nos parametros de inicialização
        """
        population = []
        for _ in range(self.pop_size):
            population.append(cr.IndvidualCreator.create(self.cod, ind_args))
        
        return population

    def get_fitness(self, pop, fitness_func):
        """
        TODO DOC
        """
        start = time.time()
        for ind in pop:
            ind.fitness = round(fitness_func(np.array(ind.chromossome)),5)
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






