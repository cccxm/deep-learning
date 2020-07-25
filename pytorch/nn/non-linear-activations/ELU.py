import torch

input = torch.tensor([-2, 0, 2], dtype=torch.float32)
m = torch.nn.ELU()
output = m(input)
print(output)
# tensor([-0.8647,  0.0000,  2.0000])
