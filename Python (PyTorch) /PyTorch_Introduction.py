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

# ---------- pytorch training neural network ----------

# FORWARD PASS: input data is passed forward and propagated through the network
# BACKPROPAGATION: the weights and biases are updated during training

# implementing forward pass
n_classes = 3 
model = nn.Sequential(
  nn.Linear(6,4), 
  nn.Linear(4, n_classes), 
  nn.Softmax(dim = -1)
)

# regression with forward pass
model = nn.Sequential(
  nn.Linear(6,4),
  nn.Linear(4,1)
)
output = model(input_data)

# ---------- pytorch loss functions ----------

# one hot encoding concepts
import torch.nn.functional as F
F.one_hot(torch_tensor(0), num_classes = 3) # tensor([1,0,0])
F.one_hot(torch_tensor(1), num_classes = 3) # tensor([0,1,0])

# cross entropy loss in pytorch
from torch.nn import CrossEntropyLoss
scores = tensors([[-0.1211, 0.1059]])
one_hot_target = tensor([[1,0]]) # output must be predicted in the first class
criterion = CrossEntropyLoss()
criterion(scores.double(), one_hot_target.double())

# LOSS FUNCTION: takes the scores, aka the model prediction before the softmax function 
# LOSS FUNCTION: and takes the one_hot_target, which is the desired output. the lower the loss the better 
