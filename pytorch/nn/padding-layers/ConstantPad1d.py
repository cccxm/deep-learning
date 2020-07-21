import torch

input = torch.tensor([[[2, 2, 2]]], dtype=torch.float32)
print(input)
# tensor([[[1., 2., 3., 4.]]])

m = torch.nn.ConstantPad1d(1, 1)
output = m(input)
print(output)
# tensor([[[1., 2., 2., 2., 1.]]])
