import random
import copy
import time
import numpy as np
import deap.tools.crossover as deap_cros
import deap.tools.mutation as deap_mut

def binary_crossover(population, ratio=1.0, method="1-point"):
    """
    Applies cx to the population
    param population: list(Binary(Individual))
    param ratio: float, best between 0.8 and 1.0
    param method: "1-point","2-point"
    """
    population = [copy.deepcopy(p) for p in population]
    
    for k in population:
        print(id(k))
    for i in range(0,len(population),2):
        if random.random() <= ratio:
            ind1 = list(population[i].b_chromossome)
            ind2 = list(population[i+1].b_chromossome)
            print(">>>>>>>")
            print(population[i].b_chromossome,population[i].chromossome)
            print(population[i+1].b_chromossome,population[i+1].chromossome)
            print("----")
            if method == "1-point":
                c1, c2 = deap_cros.cxOnePoint(ind1,ind2)
            elif method == "2-point":
                c1, c2 = deap_cros.cxTwoPoint(ind1,ind2)
            else:
                raise ValueError("Método inválido", method)
            
            population[i].b_chromossome = "".join(c1)
            population[i+1].b_chromossome = "".join(c2)
            population[i].reajust()
            population[i+1].reajust()
            print(population[i].b_chromossome,population[i].chromossome)
            print(population[i+1].b_chromossome,population[i+1].chromossome)
    

    return population
        
def binary_mutation(population, perc=0.05):
    population = [copy.deepcopy(p) for p in population]

    for i in range(0,len(population)):
        if random.random() <= perc:
            print(population[i].chromossome)
            print(population[i].b_chromossome)
            for bit_pos, bit in enumerate(population[i].b_chromossome):
                rand = random.choice([True,False])
                if rand == True:
                    aux = population[i].b_chromossome
                    if aux[bit_pos] == '1':
                        population[i].b_chromossome = copy.deepcopy(aux[:bit_pos] + '0' + aux[bit_pos+1:])
                    else:
                        population[i].b_chromossome = copy.deepcopy(aux[:bit_pos] + '1' + aux[bit_pos+1:])
                    
            population[i].reajust()        
            print("reaj:",population[i].chromossome, i)
            print("a:",population[i].b_chromossome)
    

    return population

def integer_crossover(population, ratio=1.0, method="1-point"):
    """
    Applies cx to the population
    param population: list(Integer(Individual))
    param ratio: float, best between 0.8 and 1.0
    param method: "1-point","2-point"
    """
    
    for i in range(0,len(population),2):
        if i <= ratio*len(population):
            ind1 = list(population[i].b_chromossome)
            ind2 = list(population[i+1].b_chromossome)
            if method == "1-point":
                c1, c2 = deap_cros.cxOnePoint(ind1,ind2)
            elif method == "2-point":
                c1, c2 = deap_cros.cxTwoPoint(ind1,ind2)
            else:
                raise ValueError("Método inválido", method)
            
            population[i].b_chromossome = c1
            population[i+1].b_chromossome = c2
        else:
            break
    return population

def integer_mutation(population, perc=0.05):
    n_mutations = int(len(population)*perc)

    i_to_mutate = random.sample(range(0,len(population)), n_mutations)

    for i in i_to_mutate:
        for bit_pos, bit in enumerate(population[i].chromossome):
            rand = random.choice([True,False])
            if rand == True:
                population[i].chromossome[bit_pos] = random.randint(population[i].bounds['low'],population[i].bounds['high'])

    return population


def permuted_crossover(ind1, ind2, ratio=1.0):
    """
    Applies PMX to the population
    """
    childs = []
    c1, c2 = deap_cros.cxPartialyMatched(ind1,ind2)
    childs.append(c1)
    childs.append(c2)
    #print("=============================")
    #print("before cross:")
    #print(ind1)
    #print(ind2)
    #print("after cross:")
    #print(c1)
    #print(c2)

    
    return childs

def permuted_mutation(chromosome, rate=0.05):
    """
    Inversion mutation
    """
    for gene in range(len(chromosome)):
        prob = np.random.uniform(0, 1)
        if prob < rate:
            pos = np.random.randint(0, len(chromosome))
            aux = chromosome[pos]
            chromosome[pos] = chromosome[gene]
            chromosome[gene] = aux

