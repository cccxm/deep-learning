import torch

input = torch.tensor([-2, -1, 0, 1, 2], dtype=torch.float32)
m = torch.nn.LeakyReLU(0.5)
output = m(input)
print(output)
# tensor([-1.0000, -0.5000,  0.0000,  1.0000,  2.0000])
