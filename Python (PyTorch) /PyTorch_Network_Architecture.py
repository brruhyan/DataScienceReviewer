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
