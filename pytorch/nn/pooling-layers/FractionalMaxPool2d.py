import torch

m = torch.nn.FractionalMaxPool2d(kernel_size=2, output_size=1)
input = torch.tensor([[[[1, 2, 4],
                        [4, 2, 1],
                        [1, 1, 1]]]], dtype=torch.float32)
output = m(input)
print(output)
