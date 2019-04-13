"""
Parses input files and executes the GA
"""

import os
import ocev.evolutionary as GA

def select_input_files():
    folder = os.path.dirname(os.path.abspath(__file__))+"/inputs/"

    files = []
    # r=root, d=directories, f=files
    for r, d, f in os.walk(folder):
        for file in f:
            if '.txt' in file:
                files.append(os.path.join(r, file))

    print ("Arquivos de input")
    print ("-----------------------")
    for i, f in enumerate(files):
        print(i, "->", f.rsplit("/")[-1])
    
    print ("-----------------------")
    n = input("Digite o número do arquivo desejado: ")
    return (files[int(n)])

def read_input(input_path):
    ga_args = {"cod":None,
                "gen":None,
                "pop":None,
                "elite":False}
    
    individual_args = {"dim":None,
                        "bounds":None,
                        "fitness":None,
                        "precision":0}

    selection_args = {"selection":None}

    operators_args = {"crossover"
    :None,
                        "mutation":None}
            
    with open(input_path, "r") as f:
        for line in f:
            line = line.rstrip('\n')
            if str(line).endswith(":"):
                step = eval(line.split(":")[0] + "_args")
                continue
            print (line)
            p_name,p_value = line.split("=",1)
            try:
                if p_name not in step.keys():
                    raise ValueError("Parâmetro inválido: ",p_name)
                else:
                    if p_name not in ["fitness","selection","crossover","mutation"]:
                        step[p_name] = eval(p_value)
                    else:
                        step[p_name] = p_value
            except:
                raise ValueError("Parâmetro não interpretado: ",p_name)

    return (ga_args,individual_args,selection_args,operators_args)


if __name__ == "__main__":
    file = select_input_files()
    ga,ind,sel,opr = read_input(file)
    print(ga)
    print(ind)
    print(sel)
    print(opr)
    GA.EvolutionaryAlgorithm(ga,ind,sel,opr)