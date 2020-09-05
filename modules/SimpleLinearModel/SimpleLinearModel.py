import torch
from torch import Tensor
from torch.nn import Module, Parameter


class SimpleLinearModel(Module):
    def __init__(self, ndim: int):
        """
        初始化线性回归模型
        :param ndim: 特征数量
        """
        Module.__init__(self)
        self.ndim = ndim
        self.weight = Parameter(torch.randn(ndim, 1), requires_grad=True)
        self.bias = Parameter(torch.randn(1), requires_grad=True)

    def forward(self, x: Tensor) -> Tensor:
        """
        定义前向传播
        :param x: input
        :return: 'y = Wx + bias'
        """
        return x @ self.weight + self.bias


lm = SimpleLinearModel(5)
x = torch.randn(5, 5)
print(lm(x))
