import torch

input = torch.tensor([[[[1, 2, 3],
                        [2, 5, 4],
                        [3, 4, 3]]]], dtype=torch.float32)
pool = torch.nn.AdaptiveMaxPool2d(2)
output = pool(input)
print(output)
# tensor([[[[5., 5.],
#           [5., 5.]]]])
