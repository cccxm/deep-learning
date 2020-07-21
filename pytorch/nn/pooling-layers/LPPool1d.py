import torch

input = torch.tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9]]], dtype=torch.float32)
m = torch.nn.LPPool1d(2, kernel_size=2)
output = m(input)
print(output)
# tensor([[[ 2.2361,  5.0000,  7.8102, 10.6301]]])
