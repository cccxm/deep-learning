# 数据工具

[TOC]

## torch.utils.data.Dataset[CLASS]

是数据集的抽象类，所有的数据集都要继承自此类。所有的子类都要重写`__getitem__()`用于给定键获取样本。

