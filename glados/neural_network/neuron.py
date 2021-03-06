#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
The Neuron module
It contains all the necessary to define an artificial neuron
"""


from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING
from random import random

import numpy as np

if TYPE_CHECKING:
    from glados.neural_network.activations import ActivationFunction
    from glados.neural_network.loss import Loss
    from glados.neural_network.optimizers import Optimizer


class Neuron:
    """
    Class that act as an artificial neuron
    """

    def __init__(self, num_inputs: int, activation: ActivationFunction, loss: Loss,
                 optimizer: Optimizer, learning_rate=0.01):
        """
        Initialize the neuron class with random weight and given loss and activation function
        :param num_inputs: The number of inputs that the neuron will have
        :param activation: The activation function that the neuron will use
        :param loss: The loss function to use to calculate the error
        :param learning_rate: The learning rate to use
        """
        self.weights = np.array([random() for _ in range(num_inputs)])
        self.bias = random()
        self.activation = activation
        self.loss = loss
        self.optimizer = optimizer
        self.learning_rate = learning_rate

    def learn(self, x_train: np.ndarray, y_train: np.ndarray, x_val: Optional[np.ndarray] = None,
              y_val: Optional[np.ndarray] = None, iteration=100, batch_size=32, verbose=True) -> None:
        """
        Make the neuron learn from the data (Basically just a wrapper around the optimizer)
        :param x_train: The learning data
        :param y_train: The learning prediction
        :param x_val: The validation data
        :param y_val: The validation prediction
        :param iteration: The number of iteration for the neuron to learn
        :param batch_size: The number of randomly picked element to take at each iteration
        :param verbose: If the learning process should print information about his status
        """
        self.optimizer.compute(self, x_train, y_train, x_val, y_val, iteration, batch_size, verbose)

    def forward(self, inputs: List[float]) -> float:
        """
        Do a forward pass on the neuron (aka sum of the inputs weighted plus the bias)
        :param inputs: The list of inputs data to predict from
        :return: The value returned by the activation function
        """
        act = self.bias + np.dot(inputs, self.weights)
        return self.activation(act)

    predict = forward  # Alias for the forward function
