from torch import tensor, float32
from torch.nn import AvgPool2d

pool = AvgPool2d(kernel_size=2, stride=1)
input = tensor([[[[1, 2, 3],
                  [3, 2, 1],
                  [1, 1, 1]]]], dtype=float32)
output = pool(input)
print(output)
# tensor([[[[2.0000, 2.0000],
#           [1.7500, 1.2500]]]])
