import numpy as np

RANDOM_LOWER_LIMIT = -0.5
RANDOM_UPPER_LIMIT = 0.5

class Neuron:
    bias = 0.0
    weights = []

    def __init__(self, bias, num_weights):
        self.bias = bias
        self.weights = []
        for i in range(num_weights):
            self.weights.append(np.random.uniform(low=RANDOM_LOWER_LIMIT, high=RANDOM_UPPER_LIMIT))
    
    def update_weight(self, index, new_weight):
        self.weights[index] = new_weight

    def get_num_weights(self):
        return len(self.weights)

class Layer:
    neurons = []

    def __init__(self, num_neurons, num_weights):
        self.neurons = []
        for i in range(num_neurons):
            neuron = Neuron(np.random.uniform(low=RANDOM_LOWER_LIMIT, high=RANDOM_UPPER_LIMIT),num_weights)
            self.neurons.append(neuron)
    
    def __str__(self):
        return f'Layer: neurons={len(self.neurons)} weights={len(self.neurons[0].weights)}'
    
    def get_bias(self):
        bias = []
        for neuron in self.neurons:
            bias.append(neuron.bias)
        return bias
        
class InputLayer:
    neurons = []

    def __init__(self, num_neurons, num_weights):
        self.neurons = []
        for i in range(num_neurons):
            neuron = Neuron(0.0,num_weights)
            self.neurons.append(neuron)
        
    def __str__(self):
        return f'InputLayer: neurons={len(self.neurons)} weights={len(self.neurons[0].weights)}'

class MultilayerPerceptron:
    layers = []

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
            new_layer = InputLayer(num_neurons, num_weights)
            self.layers.append(new_layer)
            print(f'[INFO] New input layer added: {new_layer}')
    
    def generate_output(self, _input):
        result = _input
        for layer in self.layers:
            print(f'Step {layer}')
            print(f'\tInput: {result}')
            result = layer.propagate(result) #TODO implement propagate inside MLP
            print(f'\tIntermediary Output: {result}')
        print(f'Output: {result}')

mlp = MultilayerPerceptron()
mlp.add_layer(5,10)
mlp.add_layer(10,5)

mlp.generate_output([1,2,3,4,5])