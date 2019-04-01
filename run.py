import os
import ocev.evolutionary as ga

"""
Default input format:
    COD='bin','int','int-perm','real'
    D=int
    POP=int
    low_bound=float,int
    high_bound=float,int
    fitness=str,
    precision=0.1,0.01,0.001 ... para codificação binária
"""

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
    dic_params = {
        "COD":None,
        "D":None,
        "POP":None,
        "low_bound":None,
        "high_bound":None,
        "fitness":None,
        "precision":None}
    
    with open(input_path, "r") as f:
        for line in f:
            p_name,p_value = line.strip("\n").split("=")
            try:
                dic_params[p_name] = p_value
            except:
                print ("Parâmetro não interpretado: ",p_name)

    return (dic_params)


if __name__ == "__main__":
    file = select_input_files()
    input_params = read_input(file)
    ga.EvolutionaryAlgorithm(input_params)