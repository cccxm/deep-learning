import torch

input = torch.tensor([[[[[0, 0],
                         [0, 0]],
                        [[2, 2],
                         [3, 3]]]]], dtype=torch.float32)
pool = torch.nn.AdaptiveMaxPool3d(1)
output = pool(input)
print(output)
# tensor([[[[[3.]]]]])
