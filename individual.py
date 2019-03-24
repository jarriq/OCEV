import time
import random
import numpy as np

class Individual():

    def __init__(self):
        self.D = None
        self.low_bound = None
        self.high_bound = None
        self.chromossome = None
        self.fitness = None

    def print_individual(self):
        print (self.chromossome)
        return


class Binary(Individual):

    def __init__(self,**kwargs): 
        super().__init__()
        self.validade_params(kwargs)
        self.D = int(kwargs["D"])
        self.chromossome = self.generate_chromossome(self.D)
        
    def validade_params(self,params):
        if int(params["D"]) < 0:
            raise Exception("Valor para D menor que 0")
        return

    def generate_chromossome(self,D):
        return ("".join(str(random.choice("01")) for i in range(int(D))))


class Integer(Individual):

    def __init__(self,**kwargs):
        super().__init__()
        self.validade_params(kwargs)
        self.D = int(kwargs["D"])
        self.low_bound = int(kwargs["low_bound"])
        self.high_bound = int(kwargs["high_bound"])
        self.chromossome = self.generate_chromossome(self.D,self.low_bound,self.high_bound)

    def validade_params(self,params):
        if int(params["D"]) < 0:
            raise Exception("Valor para D menor que 0")
        if int(params["low_bound"]) > int(params["high_bound"]):
            raise Exception("Valor para bounds inválido")
        return

    def generate_chromossome(self,D,low_bound,high_bound):
        return (np.random.randint(low_bound,high_bound,D))

class PermutedInteger(Individual):

    def __init__(self,**kwargs):
        super().__init__()
        self.validade_params(kwargs)
        self.D = int(kwargs["D"])
        self.low_bound = int(kwargs["low_bound"])
        self.high_bound = int(kwargs["high_bound"])
        self.chromossome = self.generate_chromossome(self.D,self.low_bound,self.high_bound)


    def validade_params(self,params):
        if int(params["D"]) < 0:
            raise Exception("Valor para D menor que 0")
        if int(params["low_bound"]) > int(params["high_bound"]):
            raise Exception("Valor para bounds inválido")
        if len(range(int(params["low_bound"]),int(params["high_bound"]))) + 1 != int(params["D"]):
            raise Exception("Tamabho de bounds diferente de tamanho de cromossomo")
        return

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

