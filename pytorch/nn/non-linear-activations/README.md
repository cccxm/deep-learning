# 非线性激活函数

[TOC]

## torch.nn.ELU

激活函数定义
$$
ELU(x)=\max(0,x)+\min(0,\alpha\times(e^x-1))
$$
![ELU activation function](ELU.png)

ELU可以缓解梯度消失的问题，其存在负值，可以将激活单元的输出均值靠近0。

> 参数列表：
>
> **alpha**: 默认为1.0
>
> **inplace**: 是否使用原地算法，默认为False。若选择True表示直接将计算结果覆盖输入，否则将创建新的对象存放输出结果。

~~~python
import torch

input = torch.tensor([-2, 0, 2], dtype=torch.float32)
m = torch.nn.ELU()
output = m(input)
print(output)
# tensor([-0.8647,  0.0000,  2.0000])

~~~

