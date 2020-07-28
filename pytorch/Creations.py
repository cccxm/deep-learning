import torch


def fun1():
    """
    创建一个Tensor对象
    @:param data (array_like) – 初始化数据，可以是list, tuple, NumPy ndarray, scalar, 或其他类型
    @:param dtype (torch.dtype, optional) – 描述数据的类型，默认于[data]相同
    @:param device (torch.device, optional) – 期望得到的张量计算设备
    @:param requires_grad (bool, optional) – 记录梯度 Default: False.
    @:param pin_memory (bool, optional) – 锁页内存，锁页内存中的数据将加速转义到GPU. Default False.
    """
    tensor = torch.tensor([[1, 2, 3],
                           [2, 4, 6]], dtype=torch.float32)
    print(tensor)
    # tensor([[1., 2., 3.],
    #         [2., 4., 6.]])
