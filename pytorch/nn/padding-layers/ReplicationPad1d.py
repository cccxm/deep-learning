import torch

input = torch.tensor([[[1, 2, 3, 4, 5]]], dtype=torch.float32)
print(input)
# tensor([[[1., 2., 3., 4., 5.]]])

m = torch.nn.ReplicationPad1d(2)
output = m(input)
print(output)
# tensor([[[1., 1., 1., 2., 3., 4., 5., 5., 5.]]])

m = torch.nn.ReplicationPad1d((1, 2))
output = m(input)
print(output)
# tensor([[[1., 1., 2., 3., 4., 5., 5., 5.]]])
