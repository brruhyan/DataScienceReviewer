# ---------- image recognition in pytorch ----------

# binary classification (two distinct categories)
class BinaryCNN(nn.Module): # for multiple classes use MultiClassCNN
  def __init__(self):
    super(BinaryCNN, self).__init__() # for multiple classes use MultiClassCNN
    self.conv1 = nn.Conv2d(3,16, 
      kernel_size = 3, stride = 1, padding = 1)
    self.relu = nn.ReLU()
    self.pool = nn.Maxpool2d(kernel_size = 2, stride = 2)
    self.flatten = nn.Flatten()
    self.fc1 = nn.Linear(16 * 112 * 112, 1)
    self.sigmoid = nn.Signmoid() # for multiple classes use softmax instead with dim = 1

  def forward(self,x):
    x = self.pool(self.relu(self.conv1(x)))
    x = self.fc1(self.flatten(x))
    x = self.sigmoid(x)]
    return x

