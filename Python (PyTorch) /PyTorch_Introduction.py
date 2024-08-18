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

# extra info: the linear layer operation performs matrix multiplication of input_tensor and the weights and then added by the bias 
