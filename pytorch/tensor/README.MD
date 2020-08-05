# Tensor模块

[TOC]

torch.Tensor模块定义了torch中的张量类型。张量具有不同的数值类型。张量中的方法命名通常有如下规则，若一个函数或方法带有下划线后缀，则此方法是原地的。

张量一共支持9中数据类型，每种数据类型都对应有CPU和GPU版本。

## 一、张量的创建方式

在Pytorch中，张量有四种创建方式。

### 1.1 通过torch.tensor函数创建

 ~~~python
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
 ~~~

### 1.2 通过内置函数创建

通过内置函数可以生成指定形状的张量

~~~python
torch.rand(3, 3)  # 矩阵元素为随机均匀分布的浮点型[0,1]

torch.randn(1, 2, 3)  # 矩阵元素为服从正态分布的随机浮点型

torch.zeros(2, 2)  # 生成2x2的元素全为0的矩阵

torch.ones(3, 3)  # 生成3x3的元素全为1的矩阵

torch.eye(3)  # 生成3x3的单位矩阵

print(torch.randint(0, 10, (2, 4)))  # 生成整数随机矩阵
# tensor([[2, 2, 6, 0],
#         [2, 0, 8, 9]])
~~~

### 1.3 创建形状相同的张量

创建与已知张量形状相同的张量

~~~python
t = torch.randn(3, 4)
print(t.shape)
# torch.Size([3, 4])
t2 = torch.ones_like(t)
print(t2.shape)
# torch.Size([3, 4])
~~~

### 1.4 创建类型相同的张量

~~~python
print(t.dtype)
# torch.float32
nt = t.new_tensor([2, 2])
print(nt)
# tensor([2., 2.])
~~~

## 二、张量的存储

### 2.1 CPU存储

PyTorch会默认将张量存储在CPU中。也可以通过参数指定为CPU存储。

~~~python
default_tensor = torch.randn(3, 3)
print(default_tensor.device)
# cpu

cpu_tensor = torch.tensor([1, 2, 3], dtype=torch.float, device='cpu')
print(cpu_tensor.device)
# cpu
~~~

### 2.2 GPU存储

使用`cude:id`形式指定存储在哪一块GPU上。

