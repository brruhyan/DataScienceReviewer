# ---------- pytorch relu functions ----------

# implementing reLU
relu_pytorch = nn.ReLU()
x = torch.tensor(-1.0, requires_grad = True)
y = relu.pytorch(x)
y.backward # updating the weights and biases using relu

# implementing leaky relu
leaky_relu = nn.LeakyReLU(negative_slope = 0.05)
x = torch.tensor(-2.0)

# ---------- model architecture advanced ----------

model = nn.Sequential(nn.Linear(n_features, 8),
                      nn.Linear(8,4),
                      nn.Linear(4, n_classes))

# INFO: the input layer depends on the n_features
# INFO: the output layer depends on the n_classes (categories)

# calculating the number of learnable parameters
total = 0 
for parameter in model.parameters():
  total += parameter.numel()
print(total)

# learning rates and momentum 
sgd = optim.SGD(model.parameters(), lr = 0.01, momentum = 0.95)

# INFO: momentum allows the learnign to overcome dips in the gradient

# ---------- tensor dataset ----------

# selecting x and y
features = torch.tensor(student_data[['Course', 'Name', 'Age']].to_numpy()).float()
target = torch.tensor(student_data['Passed'].to_numpy()).float()

# creating the dataset from the selected
dataset = TensorDataset(features, target)
# creating the dataloader (allows the data to be passed through the network)
dataloader = DataLoader(dataset, shuffle = True, batch_size = 2)
x, y = next(iter(dataloader))

# ---------- evaluating model ----------

# setting the model to evaluate mode
model.eval()
validation_loss = 0.0

with torch.no_grad():
  for data in validationloader:
    outputs = model(data[0])
    loss = criterion(outputs, data[1])

    validation_loss += loss.item()

# mean loss
validation_loss_epoch = validation_loss / len(validationloader)
print(validation_loss_epoch)
# Set the model back to training mode
model.train()

# accuracy
metric = torchmetrics.Accuracy(task="multiclass", num_classes=3)
for data in dataloader:
    features, labels = data
    outputs = model(features)
  
    # Calculate accuracy 
    acc = metric(outputs, labels.argmax(dim=-1))
