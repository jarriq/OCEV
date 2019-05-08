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

    '''
    for i,f in enumerate(list_rel_fitness):
        print (i, str(round(f*100,3)) + '%')
    '''
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

def stochastic_tourney(list_pop, k=2, kp=1, method='random'):
    """
    param int k [0,N] = numero de individus do torneio 
    param float [0,1] kp = probabilidade de escolher o primero
    param str method =  worst - o segundo escolhido é o pior
                        random - o segundo escolhido é aleatorio fora o melhor
    """
    selected = []
    for _ in range(len(list_pop)):
        tourney = []
        for _ in range(k):
            rand = random.randint(0,len(list_pop)-1)
            tourney.append(list_pop[rand])
        rand = random.random()
        tourney = sorted(tourney, key=lambda x: x.fitness,reverse=True)
        if kp >= rand:
            selected.append(tourney[0])
        else:
            if method == 'worst':
                selected.append(tourney[-1])
            elif method == 'random':
                rand = random.randint(1,len(list_pop))
                selected.append(tourney[rand])
            else:
                raise ValueError("Método inválido")

    return selected
            

def local_selection(list_pop, r=2, method='best'):
    """
    param int r: raio da vizinhança
    param str method: metodo pra selecao do segundo
                        'best': melhor da vizinhanca
                        'random': aleatorio da vizinhaca
                        'fitness-prop': roleta proporcional ao fitness
    """
    selected = []
    for _ in range(int(len(list_pop)/2)):
        rand = random.randint(0,len(list_pop)-1)
        selected.append(list_pop[rand])
        neighbourhood = []
        for i in range(-r,r):
            if i != rand:
                if rand+i >= len(list_pop):
                   neighbourhood.append(list_pop[rand+i-len(list_pop)])
                else:
                    neighbourhood.append(list_pop[rand+i])
        neighbourhood = sorted(neighbourhood, key=lambda x: x.fitness,reverse=True)
        if method == 'best':
            selected.append(neighbourhood[0])
        elif method == 'random':
            rand = random.randint(0,len(neighbourhood)-1)
            selected.append(neighbourhood[rand])
        elif method == 'fitness-prop':
            rand = random.random()
            list_raw_fitness = [ind.fitness for ind in neighbourhood]
            sum_fitness = np.sum(list_raw_fitness)
            list_rel_fitness = [rf/sum_fitness for rf in list_raw_fitness]
            sum_r = 0
            for index,j in enumerate(list_rel_fitness):
                sum_r += j
                if sum_r > rand:
                    selected.append(neighbourhood[index])
                    break
        else:
            raise ValueError("Método inválido")
    return selected

def roulette(individuals):
    pop_size = len(individuals)
    list_fitness = [ind.fitness for ind in individuals]
    sum_fitness = np.sum(list_fitness)
    list_fitness = list_fitness / sum_fitness
    indexes = np.random.choice(pop_size, pop_size, p=list_fitness)
    parents = [individuals[i] for i in indexes]
    
    return parents


def tournment(individuals, tournment_size=2):
    pop_size = len(individuals)
    winners = []
    for i in range(pop_size):
        gladiators = random.sample(individuals, tournment_size)
        sorted_gladiators = sorted(gladiators, key=lambda ind: ind.fitness)
        winners.append(sorted_gladiators[tournment_size - 1])
    
    return winners