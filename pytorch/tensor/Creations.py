import torch
import numpy as np

# 1 通过tensor函数创建

tensor = torch.tensor([1, 2, 3, 4])
print(tensor)
# tensor([1, 2, 3, 4])
print(tensor.dtype)
# torch.int64

tensor = torch.tensor([.1, .2, .3])
print(tensor)
# tensor([0.1000, 0.2000, 0.3000])
print(tensor.dtype)
# torch.float32

tensor = torch.tensor(np.array([.1, .2, .3]))  # numpy默认为小数为双精度浮点型
print(tensor)
# tensor([0.1000, 0.2000, 0.3000], dtype=torch.float64)
print(tensor.dtype)
# torch.float64

tensor = tensor.to(dtype=torch.int)
print(tensor.dtype)
# torch.int32

np_array: np.ndarray = tensor.numpy()
print(type(np_array))
# <class 'numpy.ndarray'>

# 2 通过内置函数创建

torch.rand(3, 3)  # 矩阵元素为随机均匀分布的浮点型[0,1]

torch.randn(1, 2, 3)  # 矩阵元素为服从正态分布的随机浮点型

torch.zeros(2, 2)  # 生成2x2的元素全为0的矩阵

torch.ones(3, 3)  # 生成3x3的元素全为1的矩阵

torch.eye(3)  # 生成3x3的单位矩阵

print(torch.randint(0, 10, (2, 4)))  # 生成整数随机矩阵
# tensor([[2, 2, 6, 0],
#         [2, 0, 8, 9]])

# 3 创建形状相同的张量

t = torch.randn(3, 4)
print(t.shape)
# torch.Size([3, 4])
t2 = torch.ones_like(t)
print(t2.shape)
# torch.Size([3, 4])

# 4 创建类型相同的张量
print(t.dtype)
# torch.float32
nt = t.new_tensor([2, 2])
print(nt)
# tensor([2., 2.])
