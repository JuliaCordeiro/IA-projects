import numpy as np
import math
import common_files.graph_generator as graph

FULL_DEBUG = False
LIMIT = 0.0
MAX_VALUE = 1
MIN_VALUE = -1


def euclidean_distance(arr1, arr2):
    distance = 0.0
    for i in range(7):
        distance += (arr1[i] - arr2[i]) ** 2.0
    distance = math.sqrt(distance)
    print(f'Distance between: {arr1}, {arr2} = {distance}')
    return distance


class Neuron:
    weights = []

    def __init__(self):
        self.weights = np.random.uniform(low=-0.5, high=0.5, size=7)

    def update_weight(self, index, new_weight):
        self.weights[index] = new_weight

    def get_weight(self, index):
        return self.weights[index]

    def __str__(self):
        return f'Neuron:[Weights:{self.weights}]'


class Madaline:
    neurons = []
    bias = np.random.uniform(low=-0.5, high=0.5, size=7)
    output_layer_pure = np.zeros(7, dtype=float)
    output_layer_liquid = np.zeros(7, dtype=int)
    error_history = []
    inputs = np.loadtxt(open("docs/x.csv", "rb"), delimiter=",", skiprows=0)
    targets = np.loadtxt(open("docs/targets.csv", "rb"), delimiter=",", skiprows=0)

    def __init__(self):
        self.neurons = [Neuron() for i in range(63)]

    def generate_output(self, input_data):
        for output_index in range(7):
            self.output_layer_pure[output_index] = self.bias[output_index]
            for input_index in range(63):
                self.output_layer_pure[output_index] += input_data[input_index] \
                                                        * self.neurons[input_index].get_weight(output_index)

            if self.output_layer_pure[output_index] >= LIMIT:
                self.output_layer_liquid[output_index] = MAX_VALUE
            else:
                self.output_layer_liquid[output_index] = MIN_VALUE

    def classify(self, input_id):
        input_data = self.inputs[input_id]
        self.generate_output(input_data)
        output = self.output_layer_liquid
        min_dist = 0.0
        min_dist_id = -1
        for i in range(7):
            target = self.targets[i]
            distance = euclidean_distance(output, target)
            if distance < min_dist or min_dist_id == -1:
                min_dist = distance
                min_dist_id = i
        print(f'Classified as id={min_dist_id}')

        if min_dist_id == 0:
            return 'A'
        if min_dist_id == 1:
            return 'B'
        if min_dist_id == 2:
            return 'C'
        if min_dist_id == 3:
            return 'D'
        if min_dist_id == 4:
            return 'E'
        if min_dist_id == 5:
            return 'J'
        if min_dist_id == 6:
            return 'K'

    def calculate_error(self, target_data):
        error_calculated = 0.0
        for output_index in range(7):
            error_calculated += 0.5 * (
                math.pow((target_data[output_index] - self.output_layer_liquid[output_index]), 2.0))
        return error_calculated

    def train(self, window, inputs, targets, learning_rate, max_epoch, minimum_error):
        self.error_history.clear()
        epoch = 1
        error = 1000.0
        while epoch <= max_epoch and error > minimum_error:
            error = 0.0
            for input_sample_index in range(21):
                # Process input in the network
                self.generate_output(inputs[input_sample_index])

                # Calculate error
                error += self.calculate_error(targets[int(input_sample_index / 3)])
                # Divides by 3 and truncates to map every 3 positions
                # from input array into a single position from targets array

                # Adjust weights
                for neuron_index in range(63):
                    for output_index in range(7):
                        new_weight = self.neurons[neuron_index].get_weight(output_index) + learning_rate \
                                     * (targets[int(input_sample_index/3)][output_index]
                                        - self.output_layer_liquid[output_index]) \
                                     * inputs[input_sample_index][neuron_index]
                        self.neurons[neuron_index].update_weight(output_index, new_weight)
                # Adjust Bias
                for output_index in range(7):
                    self.bias[output_index] = self.bias[output_index] + learning_rate \
                                              * (targets[int(input_sample_index/3)][output_index]
                                                 - self.output_layer_liquid[output_index])

                # DEBUG PRINTS
                if FULL_DEBUG:
                    print(f'[LOG] Epoch [{epoch}] Sample: {input_sample_index}')
                    print(f'\tTarget: {targets[int(input_sample_index/3)]}')
                    print(f'\tMadaline output liquid: {self.output_layer_liquid}')
                    print(f'\tMadaline output pure: {self.output_layer_pure}')
                    print(f'\tBias: {self.bias}')
                    print(f'\tError: {error}')
                    print(f'\tLearning Rate: {learning_rate}')
                    print(f'\tNeuron0: {self.neurons[0]}')
                    input("Press Enter to run next epoch...")

            if not FULL_DEBUG:
                print(f'[LOG] Training... E:{epoch} error:{error}')

            # Save error for history
            self.error_history.append(error)

            # Update graph every epoch
            graph.update_graph(window['-CANVAS-'].TKCanvas, self.error_history)
            window.refresh()

            epoch += 1

    def get_error_history(self):
        return self.error_history


def train(window, learning_rate, max_epochs, minimum_error):
    madaline: Madaline = Madaline()
    madaline.train(window, madaline.inputs, madaline.targets, learning_rate, max_epochs, minimum_error)
    return madaline


def test_madaline():
    madaline = Madaline()
    for i in range(63):
        print(f'[{i}]: {madaline.neurons[i]}')
        if i % 10 == 0:
            input("Press Enter to continue...")
    print(f'bias: {madaline.bias}')
