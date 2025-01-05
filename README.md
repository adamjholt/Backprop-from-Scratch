# Backprop from Scratch

## Overview

* **Backpropagation** is a **supervised learning algorithm** used to train **multilayer feed-forward neural networks**.
* A neural network consists of **neurons (nodes)** connected by **weights**. The weights determine how strongly each input affects the output.
* During training:

  1. **Forward pass:** Input data moves through the network to produce an output.
  2. **Calculate error:** The predicted output is compared with the **known/expected output**.
  3. **Backward pass:** The error is propagated backward through the network.
  4. **Update weights:** The weights are adjusted to reduce the error.
* This process is repeated many times until the network produces sufficiently accurate predictions.
* A typical network has an **input layer → hidden layer(s) → output layer**.
* Backpropagation can be used for **classification and regression**.

### For Classification

For a problem with two classes, such as **A and B**, the output can use **one-hot encoding**:

* **A → [1, 0]**
* **B → [0, 1]**

So, the output neuron with the higher value indicates the predicted class.

**In one sentence:**

> **Backpropagation trains a neural network by calculating the output error and propagating it backward to adjust the weights and improve future predictions.**


## Dataset

* The **Wheat Seeds dataset** contains **201 samples (records)**.
* Each sample has **7 numerical input features**, such as measurements of the wheat seeds.
* The goal is to classify each seed into **one of 3 species**.
* Because the features have **different numerical scales**, **normalization** may be needed before using algorithms such as backpropagation.
* **Zero Rule (ZeroR)** is a simple baseline algorithm that always predicts the **most common class**.
* For this dataset, Zero Rule achieves **28.095% accuracy**.

