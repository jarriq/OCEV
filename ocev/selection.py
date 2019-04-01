import random
import numpy as np

def stochastic_sampling_with_replacement(list_pop):
    """
    Implementa método da roleta 1
    """
    list_raw_fitness = [ind.fitness for ind in list_pop]
    sum_fitness = np.sum(list_raw_fitness)
    list_rel_fitness = [rf/sum_fitness for rf in list_raw_fitness]
    
    for i,f in enumerate(list_rel_fitness):
        print (i, str(round(f*100,3)) + '%')

    selected_pop = []
    for _ in range(len(list_pop)):
        rand = random.random()
        sum1 = 0
        for index,j in enumerate(list_rel_fitness):
            sum1 += j
            if sum1 > rand:
               selected_pop.append(list_pop[index])
               break

    return selected_pop

def stochastic_universal_sampling(list_pop):
    """
    Implementa método da roleta 2

    TODO lembrar de arrumar for /2
    """
    list_raw_fitness = [ind.fitness for ind in list_pop]
    sum_fitness = np.sum(list_raw_fitness)
    list_rel_fitness = [rf/sum_fitness for rf in list_raw_fitness]

    for i,f in enumerate(list_rel_fitness):
        print (i, str(round(f*100,3)) + '%')

    selected_pop = []
    for _ in range(int(len(list_pop)/2)):
        rand1 = random.random()
        rand2 = 1 - random.random()

        sum1 = 0
        sum2 = 0
        for index,j in enumerate(list_rel_fitness):
            sum1 += j
            if sum1 > rand1:
               selected_pop.append(list_pop[index])
               break
        for index,k in enumerate(list_rel_fitness):
            sum2 += k
            if sum2 > rand2:
               selected_pop.append(list_pop[index])
               break

    return selected_pop

def uniform_rank(list_pop):
    """
    Seleciona baseado no algoritmo de ranking uniforme
    """
    pop_sorted = sorted(list_pop, key=lambda x: x.fitness,reverse=True)

    list_rank = [(i+1)/((len(list_pop)*(len(list_pop) + 1))/2) for i,ind in enumerate(pop_sorted)]

    print (np.sum(list_rank))
    for i,f in enumerate(list_rank):
        print (i, str(round(f*100,3)) + '%')

    selected_pop = []
    for _ in range(len(list_pop)):
        rand = random.random()
        sum1 = 0
        for index,j in enumerate(list_rank):
            sum1 += j
            if sum1 > rand:
               selected_pop.append(pop_sorted[index])
               break

    return selected_pop

def stochastic_tourney(list_pop):
    """
    TODO DOC
    """
    pass

def local_selection(list_pop):
    """
    TODO DOC
    """
    pass