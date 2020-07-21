from torch import tensor, float32
from torch.nn import MaxPool3d

"""
@:param kernel_size (int) – 池化器窗口大小
@:param stride (int) – 池化器滑动步长. Default value is kernel_size
@:param padding (int) – 边缘0填充,default 0
@:param dilation (int)– 控制窗口内元素的跨度
@:param return_indices (bool) – if True, 则返回结果是最大值的索引. Useful for torch.nn.MaxUnpool1d later
@:param ceil_mode (bool) – when True, 向上取整
"""
pool = MaxPool3d(kernel_size=2, stride=1)
input = tensor([[[[[0, 1, 2],
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
# tensor([[[[[3., 4.],
#            [4., 5.]],
#
#           [[4., 5.],
#            [5., 6.]]]]])
