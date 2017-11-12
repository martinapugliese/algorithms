import numpy as np


class FFN(object):
    """
    A (non-deep) feedforward neural network.
    """

    def __init__(self, n_input, n_hidden, n_output):
        """
        Constructor takes:
            - number of neurons in input layer
            - number of neurons in hidden layer
            - number of neurons in output layer
        Initialises weights and biases at random from a uniform distribution for all neurons.
        """

        self.input_neurons = [
            {
                'w': np.random.uniform(0, 1),
                'b': np.random.uniform(0, 1)
            }
            for item in range(n_input)
        ]
        self.hidden_neurons = [
            {
                'w': [np.random.uniform(0, 1, n_input)],
                'b': np.random.uniform(0, 1)
            }
            for item in range(n_hidden)
        ]
        self.output_neurons = [
            {
                'w': [np.random.uniform(0, 1, n_hidden)],
                'b': np.random.uniform(0, 1)
            }
            for item in range(n_output)
        ]


    def return_neuron_output(self, neuron, neuron_input):
        """
        Computes the output of a single neuron via logistic function.
        """
        return self._logistic_function(
            np.dot(neuron['w'], neuron_input) + neuron['b'])


    def compute_layer_output(self, layer_input, layer_neurons):
        """
        Computes the output the output of the whole layer of neurons given the input vector and the layer itself.
        """

        output = []
        for i in range(len(layer_neurons)):
            neuron = layer_neurons[i]
            neuron_output = self.return_neuron_output(neuron, layer_input[i])
            output.append(neuron_output)

        return output


    def _logistic_function(self, x):

        return 1 / (1 + np.exp(-x))
