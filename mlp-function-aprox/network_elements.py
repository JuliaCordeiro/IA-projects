import numpy as np
import activation_functions as af

RANDOM_LOWER_LIMIT = -0.5
RANDOM_UPPER_LIMIT = 0.5
ACTIVATION_FUNCTION = "tanh"


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


class Layer:
    neurons = []

    def __init__(self, num_neurons, num_weights):
        self.neurons = []
        for i in range(num_neurons):
            neuron = Neuron(np.random.uniform(low=RANDOM_LOWER_LIMIT, high=RANDOM_UPPER_LIMIT), num_weights)
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
            neuron = Neuron(0.0, num_weights)
            self.neurons.append(neuron)
        
    def __str__(self):
        return f'InputLayer: neurons={len(self.neurons)} weights={len(self.neurons[0].weights)}'

class OutputLayer:
    neurons = []

    def __init__(self, num_neurons):
        self.neurons = []
        for i in range(num_neurons):
            neuron = Neuron(np.random.uniform(low=RANDOM_LOWER_LIMIT, high=RANDOM_UPPER_LIMIT), 0)
            self.neurons.append(neuron)
    
    def __str__(self):
        return f'OutputLayer: neurons={len(self.neurons)}'

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
                print(f'[ERROR] Couldn\'t add new layer! num_neurons was expected to be '
                      f'{len(self.layers[layers_len-1].neurons[0].weights)} but is {num_neurons}!')
        else:
            new_layer = InputLayer(num_neurons, num_weights)
            self.layers.append(new_layer)
            print(f'[INFO] New input layer added: {new_layer}')

    #Add more activations, using pre-made functions from activation_functions.py as needed
    def activate(self, input, activation_function):
        output = []
        if activation_function == "tanh":
            for x in input:
                y = af.tanh(x, 1.0)
                output.append(y)

        return output

    def add_output_layer(self):
        layers_len = len(self.layers)
        new_output_layer = OutputLayer(len(self.layers[layers_len-1].neurons[0].weights))
        self.layers.append(new_output_layer)
        print(f'[INFO] Auto-generated output layer: {new_output_layer}')
    
    def propagate(self, layer, next_layer, _input):
        result = []
        for i in range(len(next_layer.neurons)):
            output = next_layer.neurons[i].bias
            for j in range(len(layer.neurons)):
                output += _input[j] * layer.neurons[j].weights[i]
            result.append(output)
        result = self.activate(result, "tanh") #ACTIVATION
        return result

    def generate_output(self, _input):
        result = _input
        for i in range(len(self.layers)-1):
            print(f'Step {self.layers[i]}')
            print(f'\tInput: {result}')
            result = self.propagate(self.layers[i], self.layers[i+1], result)
            print(f'\tIntermediary Output: {result}')
        result = self.activate(result, "tanh")
        print(f'\tFinal Output: {result}')
        return result


mlp = MultilayerPerceptron()
mlp.add_layer(5, 10)
mlp.add_layer(10, 1)
mlp.add_output_layer()

mlp.generate_output([1, 2, 3, 4, 5])
