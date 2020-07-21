from torch import tensor, float32
from torch.nn import MaxPool3d, MaxUnpool3d

"""
二维的最大值池化逆转操作
*注意*：该操作是有损操作
"""
pool = MaxPool3d(kernel_size=2, stride=1, return_indices=True)
input = tensor([[[[[1, 1, 2],
                   [1, 2, 3],
                   [2, 3, 4]],
                  [[1, 2, 3],
                   [2, 3, 4],
                   [3, 4, 5]],
                  [[2, 3, 4],
                   [3, 4, 5],
                   [4, 5, 6]]]]], dtype=float32)
output, indices = pool(input)
print(output)
# tensor([[[[[3., 4.],
#            [4., 5.]],
#
#           [[4., 5.],
#            [5., 6.]]]]])
print(indices)
# tensor([[[[[13, 14],
#            [16, 17]],
#
#           [[22, 23],
#            [25, 26]]]]])
unpool = MaxUnpool3d(kernel_size=2, stride=1)
unpool_out = unpool(output, indices)
print(unpool_out)
# tensor([[[[[0., 0., 0.],
#            [0., 0., 0.],
#            [0., 0., 0.]],
#
#           [[0., 0., 0.],
#            [0., 3., 4.],
#            [0., 4., 5.]],
#
#           [[0., 0., 0.],
#            [0., 4., 5.],
#            [0., 5., 6.]]]]])
