import torch

input = torch.tensor([-2, -1, 0, 1, 2], dtype=torch.float32)
m = torch.nn.Hardtanh(1)
output = m(input)
print(output)
# tensor([-2.,  0.,  0.,  0.,  2.])
