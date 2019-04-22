import matplotlib.pyplot as plt

class Report():
    def __init__(self, generations):
        self.data = generations

    def basic(self):
        pass

    def intermediary(self):
        pass

    def complete(self):
        pass

    def plot_convergence(self):
        generation = list(range(0, len(self.data)))
        best_fitness = [gen.best.fitness for gen in self.data]
        print(best_fitness)
        worst_fitness = [gen.worst.fitness for gen in self.data]
        print(worst_fitness)
        average_fitness = [gen.average for gen in self.data]
        print(average_fitness)


        plt.plot(generation,best_fitness,"blue")
        plt.plot(generation,average_fitness,"black")
        plt.plot(generation,worst_fitness,"red")
        plt.grid(axis='both')
        plt.xlabel('Geração')
        plt.ylabel('Fitness')
        plt.show()