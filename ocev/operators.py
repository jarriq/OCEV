import random
import deap.tools.crossover as deap_cros
import deap.tools.mutation as deap_mut
from ocev.individual import Binary, Integer, PermutedInteger, Real

class BinaryOperator():

    def __init__(self):
        print("Binary Operator")

    def binary_crossover(self, population, ratio=1.0, method="1-point"):
        """
        Applies cx to the population
        param population: list(Binary(Individual))
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
                
                population[i].b_chromossome = "".join(c1)
                population[i+1].b_chromossome = "".join(c2)
            else:
                break

        return population
            
    def binary_mutation(self, population, perc=0.05):
        n_mutations = int(len(population)*perc)

        i_to_mutate = random.sample(range(0,len(population)), n_mutations)

        for i in i_to_mutate:
            for bit_pos, bit in enumerate(population[i].b_chromossome):
                rand = random.choice([True,False])
                if rand == True:
                    aux = population[i].b_chromossome
                    if aux[bit_pos] == '1':
                        population[i].b_chromossome = aux[:bit_pos] + '0' + aux[bit_pos+1:]
                    else:
                        population[i].b_chromossome = aux[:bit_pos] + '1' + aux[bit_pos+1:]
        
        return population
    
class IntegerOperator():

    def __init__(self):
        print("Integer Operator")

    def integer_crossover(self, population, ratio=1.0, method="1-point"):
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

    def integer_mutation(self, population, perc=0.05):
        n_mutations = int(len(population)*perc)

        i_to_mutate = random.sample(range(0,len(population)), n_mutations)

        for i in i_to_mutate:
            for bit_pos, bit in enumerate(population[i].chromossome):
                rand = random.choice([True,False])
                if rand == True:
                    population[i].chromossome[bit_pos] = random.randint(population[i].bounds['low'],population[i].bounds['high'])

        return population

class PermutedIntegerOperator():

    def __init__(self):
        print("PermutedInteger Operator")

    def permuted_crossover(self, population, ratio=1.0):
        """
        Applies PMX to the population
        """
        for i in range(0,len(population),2):
            if i <= ratio*len(population):
                ind1 = list(population[i].chromossome)
                ind2 = list(population[i+1].chromossome)
                c1, c2 = deap_cros.cxPartialyMatched(ind1,ind2)
                
                population[i].chromossome = c1
                population[i+1].chromossome = c2
            else:
                break

        return population

    def permuted_mutation(self, population, perc=0.05):
        n_mutations = int(len(population)*perc)
        
        i_to_mutate = random.sample(range(0,len(population)), n_mutations)

        for i in i_to_mutate:
            rand = random.sample(range(0,len(population[i].chromossome)),2)

            aux = population[i].chromossome[rand[0]] 
            population[i].chromossome[rand[0]] = population[i].chromossome[rand[1]]
            population[i].chromossome[rand[1]] = aux

        return population

class RealOperator():

    def __init__(self):
        print("Real Operator")


if __name__ == '__main__':
    pass