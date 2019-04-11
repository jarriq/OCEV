import time
import random
import numpy as np
import ocev.utils as utils

class Individual():

    def __init__(self):
        self.dim = None
        self.bounds = None
        self.precision = None
        self.chromossome = None

        self.fitness = None

    def info(self):
        print(type(self))
        print("--------------------------")
        print("-Dimension: ",self.dim)
        print("-Chromossome: ",self.chromossome)
        print("-Fitness: ",self.fitness)
        print("-Precision: ",self.precision) 
        return

class Binary(Individual):

    def __init__(self, ind_args): 
        super().__init__()
        self.bounds = ind_args['bounds']
        self.nvars = len(ind_args['bounds']['high'])
        self.precision = 10**-(ind_args["precision"])
        
        self.L = utils.find_L(self.nvars, self.bounds, self.precision)
        print(self.L)
        self.dim = sum(self.L)
        print(self.dim)
        self.b_chromossome = self.generate_chromossome(self.dim)
        print(self.b_chromossome)
        self.chromossome = utils.scale_adjust(self.b_chromossome, self.bounds, self.L, self.precision)
        print(self.chromossome)

    def generate_chromossome(self, dim):
        return ("".join(str(random.choice("01")) for i in range(int(dim))))


class Integer(Individual):

    def __init__(self,ind_args):
        super().__init__()
        self.dim = ind_args['dim']
        self.bounds = ind_args['bounds']
        self.chromossome = self.generate_chromossome(self.dim,self.bounds)

    def generate_chromossome(self,dim,bounds):
        return (np.random.randint(bounds['low'],bounds['high'],dim))

class PermutedInteger(Individual):

    def __init__(self,ind_args):
        super().__init__()
        self.dim = ind_args['dim']
        self.chromossome = self.generate_chromossome(self.dim,self.bounds)


    def generate_chromossome(self,D,bounds):
        chromossome = np.arange(bounds['low'],bounds['high'])
        np.random.shuffle(chromossome)
        return (chromossome)

class Real(Individual):

    def __init__(self,ind_args):
        super().__init__()
        self.dim = ind_args['dim']
        self.bounds = ind_args['bounds']
        self.chromossome = self.generate_chromossome(self.dim, self.bounds)

    def generate_chromossome(self,dim,bounds):
        return (np.random.uniform(bounds['low'],bounds['high'],dim))


