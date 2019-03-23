# -*- coding: utf8 -*-
import time
import random
import os
import numpy as np
import individual as ind
import fitness as fit


class IndvidualFactory():
    types = {'bin':ind.Binary,
            'int':ind.Integer,
            'int-perm':ind.PermutedInteger,
            'real':ind.Real}
 
    @staticmethod
    def create_individual(cod, **kwargs):
            print (cod)
            return IndvidualFactory.types[cod](**kwargs)


class EvolutionaryAlgorithm():

    def __init__(self,input_params):
        """
        COD param: str, ('bin','int', 'int-perm', 'real') codificações possiveis
        D: int, tamanho do cromossomo (número de variáveis)
        POP: int, tamanho da população
        bounds param: tuple, (lim_inferior,lim_superior)
        seed param: int, seed para geração de números aleatórios
        """
        
        for key, value in input_params.items(): 
            print ("%s = %s" %(key, value)) 
            
        print ("Gerando População inicial...")
        self.list_pop = []
        self.COD = input_params["COD"]
        self.POP = int(input_params["POP"])
        self.D = int(input_params["D"])
        self.gera_pop(input_params)

    def gera_pop(self, input_params):
        """
        Gera a população com base nos parametros de inicialização
        """
        for _ in range(self.POP):
            self.list_pop.append(IndvidualFactory.create_individual(self.COD,**input_params))

    def info(self):
        print ("[Info]")
        print (" - COD: "+str(self.COD))
        print (" - D: "+str(self.D))
        print (" - POP: "+str(self.POP))
        #print (" - bounds: ["+str(self.low_bound)+","+str(self.high_bound)+"]")

    def print_pop(self):
        print ("[Population = "+str(self.POP)+"]")
        for i in range(0,len(self.list_pop)):
            print (" - " + str(i) + " ->",self.list_pop[i].chromossome)
        return






