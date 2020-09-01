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

~~~python
gpu_tensor = torch.randn(2, 2, device='cuda:0')
print(gpu_tensor.device)
# cuda:0
~~~

### 2.3 张量转移

张量可以在CPU和GPU之间相互转移

~~~python
gpu_tensor = torch.randn(2, 2, device='cuda:0')

cpu_tensor = gpu_tensor.cpu()
print(cpu_tensor.device)
# cpu
gpu_tensor = cpu_tensor.cuda(0)
print(gpu_tensor.device)
# cuda:0
~~~

## 三、张量的形状

### 3.1 获取维度信息

~~~Python
import torch
t = torch.randn(2,3,4)
t.ndimension()
# 3
~~~

### 3.2 获取元素数量

~~~Python
t.nelement()
# 24
~~~

## 四、张量的运算

### 4.1 独立张量的运算

~~~python
import torch

t1 = torch.tensor([[2, 4, 8, 10],
                   [0.1, 0.2, 0.4, 0.8]], dtype=torch.float)
print(t1)
# tensor([[ 2.0000,  4.0000,  8.0000, 10.0000],
#         [ 0.1000,  0.2000,  0.4000,  0.8000]])

# 求平方根
t2 = t1.sqrt()
# t2 = torch.sqrt(t1)
print(t2)
# tensor([[1.4142, 2.0000, 2.8284, 3.1623],
#         [0.3162, 0.4472, 0.6325, 0.8944]])
print(t1)
# tensor([[ 2.0000,  4.0000,  8.0000, 10.0000],
#         [ 0.1000,  0.2000,  0.4000,  0.8000]])

# inplace operator
t1.sqrt_()
print(t1)
# tensor([[1.4142, 2.0000, 2.8284, 3.1623],
#         [0.3162, 0.4472, 0.6325, 0.8944]])

sum = t1.sum()
print(sum)
# tensor(11.6952)

mean = t1.mean()
print(mean)
# tensor(1.4619)
~~~

**注意**：这些操作会消除原始数据的维度，如果需要保留维度可以设置参数`keepDim=True`.

### 4.2 多张量运算

~~~python
import torch

t1 = torch.tensor([[1, 2],
                   [3, 4]], dtype=torch.float32)
t2 = torch.tensor([[0, -1],
                   [-1, 0]], dtype=torch.float32)

sum = t1 + t2
# sum = torch.add(t1, t2)
# sum = t1.add(t2)
print(sum)
# tensor([[1., 1.],
#         [2., 4.]])
t1.add_(t2)
print(t1)
# tensor([[1., 1.],
#         [2., 4.]])
~~~

其他运算包括`add`,`torch.add`,`tensor.add`,`tensor.add_`,以及`sub`,`mul`,`div`等。

### 4.3 极值和排序

**获取某个方向的极值位置**

~~~python
import torch

t = torch.randn(3, 3)
print(t)
# tensor([[ 0.0815,  1.4848,  1.0463],
#         [ 0.5863, -0.3132, -2.3847],
#         [ 0.9891, -0.2270, -0.7129]])
print(t.argmax(0))
# tensor([2, 0, 0])
print(torch.argmin(t, 1))
# tensor([0, 2, 2])
~~~

**获取张量极值**

~~~python
import torch

t = torch.randn(3, 3)
print(t)
# tensor([[ 0.5689,  0.0272, -1.0228],
#         [ 0.1595, -0.9023,  0.4352],
#         [ 1.1611,  0.1746, -1.1886]])
print(t.min())
# tensor(-1.1886)
print(torch.max(t))
# tensor(1.1611)
~~~

**张量按维度排序**

~~~python
import torch

t = torch.randn(2, 2, 2)
print(t)
# tensor([[[-1.1862,  0.6807],
#          [ 0.4622, -0.2585]],
# 
#         [[ 1.1917,  2.2841],
#          [ 0.3277,  1.2513]]])
values, indices = t.sort(0)
print(values)
# tensor([[[-1.1862,  0.6807],
#          [ 0.3277, -0.2585]],
# 
#         [[ 1.1917,  2.2841],
#          [ 0.4622,  1.2513]]])
print(indices)
# tensor([[[0, 0],
#          [1, 0]],
# 
#         [[1, 1],
#          [0, 1]]])
~~~

### 4.4 矩阵乘法

~~~python
import torch

a = torch.randn(1, 2)
# tensor([[-0.6390,  0.0263]])
print(a)
b = torch.randn(2, 4)
print(b)
# tensor([[ 0.9777,  0.3342, -1.6471, -0.8226],
#         [-0.5891, -2.2091,  0.1889,  0.7874]])
c = torch.randn(4, 1)
print(c)
# tensor([[ 0.3100],
#         [-0.0155],
#         [-0.6403],
#         [-0.8830]])

d = a @ b @ c
# d = a.mm(b).mm(c)
print(d)
# tensor([[-1.3538]])
~~~

