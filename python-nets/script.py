import numpy as np

from classes import FFN


# Create the network
network = FFN(3, 1, 2)

print('input layer', network.input_neurons)

print('hidden layer', network.hidden_neurons)

print('output layer', network.output_neurons)

# Starting input data: one value per input neuron
# (extract from a uniform distribution)
starting_input = np.random.uniform(0, 1, len(network.input_neurons))


print('\nstarting input', starting_input)

input_layer_output = \
    network.compute_layer_output(starting_input, network.input_neurons)

print('\ninput layer output', input_layer_output)

hidden_layer_output = \
    network.compute_layer_output([input_layer_output for item in network.hidden_neurons], network.hidden_neurons)

print('\nhidden layer output', hidden_layer_output)

output_layer_output = \
    network.compute_layer_output([hidden_layer_output for item in network.output_neurons], network.output_neurons)

print('\noutput layer output', output_layer_output)
