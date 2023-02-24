import numpy as np

RANDOM_LOWER_LIMIT = -0.5
RANDOM_UPPER_LIMIT = 0.5

class Neuron:
    bias = 0.0
    weights = []

    def __init__(self, bias, num_weights):
        self.bias = bias
        for i in range(num_weights):
            self.weights.append(np.random.uniform(low=RANDOM_LOWER_LIMIT, high=RANDOM_UPPER_LIMIT))
    
    def update_weight(self, index, new_weight):
        self.weights[index] = new_weight

    def get_num_weights(self):
        return self.weights.shape[0]

class Layer:
    neurons = []

    def __init__(self, num_neurons, num_weights):
        for i in range(num_neurons):
            self.neurons.append(Neuron(np.random.uniform(low=RANDOM_LOWER_LIMIT, high=RANDOM_UPPER_LIMIT),num_weights))
    
    def propagate(self, input):
        result = []
        if input.shape[0] == len(self.neurons):
            for i in range(self.neurons.get_num_weights()):
                output = 0.0
                for j in range(len(self.neurons)):
                    output += self.neurons[j].weights[i] * input[j] + self.neurons[j].bias
                result.append(output)
            return result
        else:
            print(f'[ERROR] Input shape ({input.shape[0]}) != neurons shape ({len(self.neurons)})')
            return result
        
    def __str__(self):
        return f'Layer: neurons={len(self.neurons)} weights={len(self.neurons[0].weights)}'
        
class MultilayerPerceptron:
    layers = []

    #TODO fix add layer using wrong weight (is it multiplying neurons x weight ?!?)
    def add_layer(self, num_neurons, num_weights):
        layers_len = len(self.layers)
        if layers_len != 0:
            if len(self.layers[layers_len-1].neurons[0].weights) == num_neurons:
                new_layer = Layer(num_neurons, num_weights)
                self.layers.append(new_layer)
                print(f'[INFO] New layer added: {new_layer}')
            else:
                print(f'[ERROR] Couldn\'t add new layer! num_neurons was expected to be {len(self.layers[layers_len-1].neurons[0].weights)} but is {num_neurons}!')
        else:
            new_layer = Layer(num_neurons, num_weights)
            self.layers.append(new_layer)
            print(f'[INFO] New layer added: {new_layer}')

mlp = MultilayerPerceptron()
mlp.add_layer(5,10)
mlp.add_layer(10,1)