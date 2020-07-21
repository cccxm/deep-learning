import torch

input = torch.tensor([[[1, 2, 3, 4, 5]]], dtype=torch.float32)
pool = torch.nn.AdaptiveMaxPool1d(2)
output = pool(input)
print(output)
# tensor([[[3., 5.]]])

# pool = torch.nn.AdaptiveMaxPool1d(3)
# output = pool(input)
# print(output)
# tensor([[[2., 4., 5.]]])
