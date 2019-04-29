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
from operator import attrgetter
import numpy as np
from copy import copy, deepcopy

class Generation():

    def __init__(self, pop):
        self.population = pop

        self.best = None
        self.worst = None
        self.mean = None
        self.n_rest_broken = None
        self.get_n_rest_broken()
        self.set_values()   

    def get_n_rest_broken(self):
        cont = 0
        for ind in self.population:
            if not ind.bounds_ok():
                cont += 1
        self.n_rest_broken = cont

    def set_values(self):
        #print([ind.fitness for ind in self.population])
        self.best = max(self.population, key=attrgetter('fitness'))
        self.worst = min(self.population, key=attrgetter('fitness'))
        self.average = np.average([ind.fitness for ind in self.population])

    def print(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        #print("pop: ",self.population)
        print("best_fit: ",self.best.fitness)
        print("worst_fit: ",self.worst.fitness)
        print("average_fit: ",self.average)
        print("broken: ",self.n_rest_broken)

class EvolutionaryAlgorithm():

    def __init__(self, ga_args, ind_args, sel_args, cros_args, mut_args):
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
        self.dim = ind_args['dim']
        self.fitness_func = eval("fit." + ind_args["fitness"])
        self.selection_func = eval("sel." + sel_args["selection"])
        sel_args.pop("selection")
        
        self.operator = cr.OperatorCreator.get_operator(self.cod)
        self.crossover_func = eval("self.operator." + cros_args["crossover"])
        cros_args.pop("crossover")
        print(cros_args)

        self.mutation_func = eval("self.operator." + mut_args["mutation"])
        mut_args.pop("mutation")
        print(mut_args)

        self.generations = []
        self.population = self.gerenerate_population(ind_args)
        

        self.get_fitness(self.population, self.fitness_func)
        gen = Generation(self.population)
        pop = gen.population[:]
        self.generations.append(gen)
        try:
            while len(self.generations) < self.n_gen:

                pop = deepcopy([deepcopy(p) for p in pop])

                pop2 = self.get_fitness(pop, self.fitness_func)
                if self.elite:
                    best = deepcopy(max(pop, key=attrgetter('fitness')))
                    print("BEST:",best.fitness)
                    

                
                print("SELECTION ----------------------------------------")
                print("before:")
                print([p.chromossome for p in pop])
                print([p.fitness for p in pop])
                print(np.mean([p.fitness for p in pop]))
                
                selected = self.selection_func(pop2,**sel_args)

                
                print("after:")
                print([sel.chromossome for sel in selected])
                print([sel.fitness for sel in selected])
                print(np.mean([sel.fitness for sel in selected]))
                
                #print("CROSSOVER --------")
                #print("before:")
                #print([sel.chromossome for sel in selected])

                crossed = self.crossover_func(selected, **cros_args)
                #for s in range(0,len(selected)):
                ##    if selected[s].chromossome != crossed[s]:
                #       raise ValueError("Deu certo") 
                    
                 

                cont = 0 
                for s,c in zip(selected,crossed):
                    if not np.array_equal(s.chromossome,c.chromossome):
                        pass
                        #raise ValueError("BUSTED")
                        cont += 1

                print("CHANGEEEEEEEEEEEED", cont)
                #print("after:")
                #print([cr.chromossome for cr in crossed])
                
                #print("MUTATION --------")
                #print("before:")
                #print([cros.chromossome for cros in crossed])
                mutated = self.mutation_func(crossed, **mut_args)
                #print("after:")
                #print([mut.chromossome for mut in mutated])
                
                pop = mutated
                pop = self.get_fitness(pop, self.fitness_func)
                if self.elite:
                    pop[-1] = best
                gen = Generation(pop)
                
                #gen.print()
                print("GEN:", len(self.generations))
                self.generations.append(gen)
        except KeyboardInterrupt:
            pass
        


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
        for i in range(0,len(pop)):
            pop[i].fitness = round(fitness_func(np.array(pop[i].chromossome)),5)
        end = time.time() - start
        #print ("time:", end)
        return deepcopy([deepcopy(p) for p in pop])

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






