# 简单线性回归模型

[TOC]

## Step 1. 创建模型

继承`torch.nn.Module`实现`forward`函数 

~~~python
class SimpleLinearModel(Module):
    def __init__(self, ndim: int):
        """
        初始化线性回归模型
        :param ndim: 特征数量
        """
        Module.__init__(self)
        self.ndim = ndim
        self.weight = Parameter(torch.randn(ndim, 1))
        self.bias = Parameter(torch.randn(1))

    def forward(self, x: Tensor) -> Tensor:
        """
        定义前向传播
        :param x: input
        :return: 'y = Wx + bias'
        """
        return x @ self.weight + self.bias
~~~

