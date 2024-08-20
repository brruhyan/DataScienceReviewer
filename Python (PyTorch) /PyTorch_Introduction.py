# ---------- pytorch basics ----------

# loading from a list
import torch
list = [[1,2,3,4,5], [6,7,8,9,10]]
tensor = torch.tensor(list) # tensors are the building blocks for pytorch

# loading from a numpy array
np_array = np.array(array)
np_tensor = torch.from_numpy(np_array)

# tensor attributes
tensor.shape
tensor.dtype
tensor.device

# ---------- pytorch neural network basics ----------

# creating a neural network with pytorch
import torch.nn as nn
input_tensor = torch.tensor(
  [[0.3471, 0.4547, -0.2356]])
# defining the first linear layer
linear_layer = nn.Linear(in_features = 3, out_features = 2)
# passing the input through the linear layer
output = linear_layer(input_tensor)
print(output)

# linear layer attributes
linear_layer.weight
linear_layer.bias

# EXTRA INFO: the linear layer operation performs matrix multiplication of input_tensor and the weights and then added by the bias 
# EXTRA INFO: when we call the nn.Linear, the weights and biases are initialized randomly

# creating a network using pytorch sequential
model = nn.Sequential(
  nn.Linear(10,5), # the parameters represent input and output respectively
  nn.Linear(5,20), # notice that the next node input is equal to the prior node's output
  nn.Linear(20,5)
)
model(input_tensor)

# ---------- pytorch activation functions ----------

# SIGMOID: primarily used for binary classification (0 and 1) 
# SIGMOID: we take thge pre-activation (class parameters) and pass it to the sigmoid and we can obtain a value between 0 and 1

# implemeting sigmoid function
model = nn.Sequential(
  nn.Linear(10,5), 
  nn.Linear(5,20), 
  nn.Linear(20,5)
  nn.Sigmoid()
)

# SOFTMAX: takes the class vector as the input and outputs the same size
# SOFTMAX: primariliy used for multiple classification

probability = nn.Softmax(dim = -1)
output = probability(input_tensor)
