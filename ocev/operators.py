import random
from ocev.individual import Binary, Integer, PermutedInteger, Real
#--------------------------
#BINARY
#--------------------------
class BinaryOperator():

    def __init__(self, population, operator_args):
        if operator_args['crossover'] is not None:
            eval("self."+operator_args['crossover'])

        if operator_args['mutation'] is not None:
            eval("self."+operator_args['mutation'])


    def binary_crossover(self, population, method="1-point"):
        """
        param population: list(Binary(Individual))
        param method: "1-point","2-point","uniform"
        """
        pair_population = [(population[i],population[i+1]) for i in range(0,len(population),2)]

        for i, pair in enumerate(pair_population):
            if method == "1-point":
                cut = random.randint(0,len(population))
                aux = pair[0][:cut]
                pair[0][:cut] = pair[1][:cut]
                pair[1][:cut] = aux

            elif method == "2-point":
                cut = random.sample(list(range(0,len(population))),2)
                aux = pair[0][cut[0]:cut[1]]
                pair[0][cut:cut+1] = pair[1][cut:cut+1]
                pair[1][cut:cut+1] = aux

            elif method == "uniform":
                for j in range(0,pair[0]):
                    rand = random.choice([True,False])
                    if rand == True:
                        aux = pair[0][j]
                        pair[0][j] = pair[1][j]
                        pair[1][j] = pair[0][j]
            

def mutation():
    pass


#--------------------------
#INT
#--------------------------


#--------------------------
#INT-PERM
#--------------------------
def cycle_crossover(population):
    for i in range(0,len(population),2):
        ind1 = population[i]
        ind2 = population[i+1]

