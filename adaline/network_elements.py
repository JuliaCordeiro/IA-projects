import numpy as np

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
    output_layer_pure = np.zeros(21, dtype=float)
    output_layer_liquid = np.zeros(21, dtype=int)
    error_history = []
    def __init__(self):
        i = 0
        while i < 63:
            self.neurons.append(Neuron())
    
    def generate_output(self, input):
        for output_index in range(21):
            self.output_layer_pure[output_index] = self.bias[output_index]
            for input_index in range(63):
                self.output_layer_pure[output_index] += input[input_index]*self.neurons[input_index].get_weight(output_index)
            if self.output_layer_pure[output_index] >= 0.0:
                self.output_layer_liquid[output_index] = 1
            else:
                self.output_layer_liquid[output_index] = -1

    def calculate_error(self, target):
        error = 0.0
        for output_index in range(21):
            error += 0.5*((target[output_index] - self.output_layer_liquid[output_index])**2.0)
        return error

    def train(self, inputs, targets, learning_rate, max_epoch, minimum_error):
        epoch = 1
        error = 1.0
        while epoch <= max_epoch and error > minimum_error:
            error = 0.0
            for input_index in range(21):
                #Process input in the network
                self.generate_output(inputs[input_index])
                #Calculate error
                error = self.calculate_error(targets[input_index])
                #Adjust weights
                for neuron_index in range(63):
                    for output_index in range(21):
                        new_weight = self.neurons[neuron_index].get_weight(output_index) + learning_rate * (targets[input_index][output_index] - self.output_layer_liquid[output_index]) * inputs[input_index][neuron_index]
                        self.neurons[neuron_index].update_weight(output_index, new_weight)
            #Save error for history
            self.error_history.append(error)
            #Increment epochs
            epoch += 1
            print(f'[LOG] Training... E:{epoch} error:{error * 100}%')

    def get_error_history(self):
        return self.error_history


    

    






    




