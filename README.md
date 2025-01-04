# Backprop from Scratch

## Overview

Backpropagation is a supervised learning algorithm that trains multilayer feed-forward neural networks by adjusting weights to minimize the error between predicted and expected outputs.

A typical network consists of input, hidden, and output layers. It can be used for classification and regression; for classification, each class is typically represented by an output neuron using one-hot encoding (e.g., A = [1, 0], B = [0, 1]).

## Dataset

The Wheat Seeds dataset contains 201 records with 7 numerical input variables used to classify wheat seeds into 3 species. Since the input variables have different scales, normalization may be required for algorithms such as backpropagation.

Using the Zero Rule algorithm, which predicts the most common class, the baseline accuracy is 28.095%.

