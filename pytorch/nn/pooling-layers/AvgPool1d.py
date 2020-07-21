from torch import tensor, float32
from torch.nn import AvgPool1d

pool = AvgPool1d(kernel_size=3, stride=1)
input = tensor([[[0, 1, 2, 2, 3, 3, 3, 4, 4, 4]]], dtype=float32)
output = pool(input)
print(output)
# tensor([[[1.0000, 1.6667, 2.3333, 2.6667, 3.0000, 3.3333, 3.6667, 4.0000]]])
