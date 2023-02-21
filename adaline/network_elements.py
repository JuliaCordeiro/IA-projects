import numpy as np
import math

class Neuron:
    weights = np.random.uniform(low=-0.5, high=0.5, size=21)

    def update_weight(self, index, new_weight):
        self.weights[index] = new_weight
    
    def get_weight(self, index):
        return self.weights[index]

    def __str__(self):
        return f'Neuron:[Weights:{self.weights}]'
    
class Madaline:
    neurons = []
    bias = np.random.uniform(low=-0.5, high=0.5, size=21)
    output_layer = np.zeros(21, dtype=float)
    def __init__(self):
        i = 0
        while i < 63:
            self.neurons.append(Neuron())
    

    






    




