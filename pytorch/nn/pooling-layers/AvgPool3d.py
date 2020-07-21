from torch import tensor, float32
from torch.nn import AvgPool3d

pool = AvgPool3d(kernel_size=2, stride=1)
input = tensor([[[[[2, 1, 2],
                   [1, 2, 3],
                   [2, 3, 4]],
                  [[1, 2, 3],
                   [2, 3, 4],
                   [3, 4, 5]],
                  [[2, 3, 4],
                   [3, 4, 5],
                   [4, 5, 6]]]]], dtype=float32)
output = pool(input)
print(output)
# tensor([[[[[1.7500, 2.5000],
#            [2.5000, 3.5000]],
#
#           [[2.5000, 3.5000],
#            [3.5000, 4.5000]]]]])
