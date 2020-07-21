import torch

"""
一维数据的最大值池化器
@:param kernel_size (int) – 池化器窗口大小
@:param stride (int) – 池化器滑动步长. Default value is kernel_size
@:param padding (int) – 边缘0填充,default 0
@:param dilation (int)– 控制窗口内元素的跨度
@:param return_indices (bool) – if True, 则返回结果是最大值的索引. Useful for torch.nn.MaxUnpool1d later
@:param ceil_mode (bool) – when True, 向上取整
"""
pool = torch.nn.MaxPool1d(kernel_size=3, stride=1)
input = torch.tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9]]], dtype=torch.float32)
output = pool(input)
print(output)
# tensor([[[3., 4., 5., 6., 7., 8., 9.]]])
