from torch import tensor, float32
from torch.nn import MaxPool1d, MaxUnpool1d

"""
一维的最大值池化逆转操作
*注意*：该操作是有损操作
"""
pool = MaxPool1d(kernel_size=3, stride=1, return_indices=True)
input = tensor([[[5, 1, 2, 3, 4, 5, 6, 7, 8]]], dtype=float32)
output, indices = pool(input)
print(output)
# tensor([[[5., 3., 4., 5., 6., 7., 8.]]])
print(indices)
# tensor([[[0, 3, 4, 5, 6, 7, 8]]])
unpool = MaxUnpool1d(kernel_size=3, stride=1)
unpool_out = unpool(output, indices)
print(unpool_out)
# tensor([[[5., 0., 0., 3., 4., 5., 6., 7., 8.]]])
