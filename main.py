# ───────────────────────────────────────────────────────────────────────────────
# 1. Initialize Network
# ───────────────────────────────────────────────────────────────────────────────
#
# Each neuron has a set of weights that need to be maintained. One weight for each
# input connection and an additional weight for the bias. We will need to store
# additional properties for a neuron during training, therefore we will use a
# dictionary to represent each neuron and store properties by names such as
# 'weights' for the weights.
#
# A neural network is organized into layers. We will organize layers as arrays of
# dictionaries and treat the whole network as an array of layers.

from random import random, seed

# %%


def initialize_network(n_inputs, n_hidden, n_outputs):
    """Initialize a neural network with random weights.

    Args:
        n_inputs (int): Number of inputs to the network.
        n_hidden (int): Number of neurons in the hidden layer.
        n_outputs (int): Number of neurons in the output layer.

    Returns:
        list: A list of layers, where each layer is a list of neuron
            dictionaries with initialized weights (including bias).
    """
    network = []
    hidden_layer = [
        {"weights": [random() for i in range(n_inputs + 1)]} for i in range(n_hidden)
    ]
    output_layer = [
        {"weights": [random() for i in range(n_hidden + 1)]} for i in range(n_outputs)
    ]
    network.append(hidden_layer)
    network.append(output_layer)
    return network


# %%

seed(1)
network = initialize_network(2, 1, 2)
for layer in network:
    print(layer)


# %%

# ───────────────────────────────────────────────────────────────────────────────
# 1. Initialize Network
# ───────────────────────────────────────────────────────────────────────────────
#
# We can calculate an output from a neural network by propagating an input signal
# through each layer until the output layer outputs its values.
#
# 1. Neuron Activation
# 2. Neuron Transfer
# 3. Forward Propagation


# %%


# %%

