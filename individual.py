import time
import random
import numpy as np

class Individual():

    def __init__(self):
        self.D = None
        self.chromossome = None

    def print_individual(self):
        print (self.chromossome)
        return


class Binary(Individual):

    def __init__(self,**kwargs): 
        super().__init__()
        self.validade_params(kwargs)
        self.chromossome = self.generate_chromossome(kwargs["D"])
        
    def validade_params(self,D):
        pass

    def generate_chromossome(self,D):
        return ("".join(str(random.choice("01")) for i in range(int(D))))


class Integer(Individual):

    def __init__(self,D,low_bound,high_bound):
        super().__init__()
        self.validade_params(D)
        self.chromossome = self.generate_chromossome(D,low_bound,high_bound)

    def validade_params(self,D):
        pass

    def generate_chromossome(self,D,low_bound,high_bound):
        return (np.random.randint(low_bound,high_bound,D))

class PermutedInteger(Individual):

    def __init__(self,D,low_bound,high_bound):
        super().__init__()
        self.validade_params(D,low_bound,high_bound)
        self.chromossome = self.generate_chromossome(D,low_bound,high_bound)

    def validade_params(self,D,low_bound,high_bound):
        pass

    def generate_chromossome(self,D,low_bound,high_bound):
        chromossome = np.arange(low_bound,high_bound)
        np.random.shuffle(chromossome)
        return (chromossome)

class Real(Individual):

    def __init__(self,D,low_bound,high_bound):
        super().__init__()
        self.validade_params(D,low_bound,high_bound)
        self.chromossome = self.generate_chromossome(D,low_bound,high_bound)

    def validade_params(self,D,low_bound,high_bound):
        pass

    def generate_chromossome(self,D,low_bound,high_bound):
        return (np.random.uniform(low_bound,high_bound,D))

