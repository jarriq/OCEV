import os
import evolutionary as ga

"""
Default input format:
    COD='bin','int','int-perm','real'
    D=int
    POP=int
    low_bound=float,int
    high_bound=float,int
    fitness=str
"""


def read_input(input_path):
    dic_params = {
        "COD":None,
        "D":None,
        "POP":None,
        "low_bound":None,
        "high_bound":None}
    
    with open(input_path, "r") as f:
        for line in f:
            p_name,p_value = line.strip("\n").split("=")
            try:
                dic_params[p_name] = p_value
            except:
                print ("Parâmetro não interpretado: ",p_name)

    dic_params = {k: v for k, v in dic_params.items() if v is not None}

    return (dic_params)




if __name__ == "__main__":
    
    input_params = read_input(os.path.dirname(os.path.abspath(__file__))+"/input.txt")


    ga.EvolutionaryAlgorithm(COD=input_params["COD"],POP=input_params["POP"],**(input_params.pop("COD").pop("POP")))