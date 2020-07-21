import torch


def conv2d():
    """
    Applies a 2D convolution over an input signal composed of several input planes.
    @:param in_channels (int) – 输入图片的通道数
    @:param out_channels (int) – 卷积层产生的通道数
    @:param kernel_size (int or tuple) – 卷积核尺寸
    @:param stride (int or tuple, optional) – 卷积步长Default: 1
    @:param padding (int or tuple, optional) – 边缘填充Default: 0
    @:param padding_mode (string, optional) – 填充模式：'zeros', 'reflect', 'replicate' or 'circular'. Default: 'zeros'
    @:param dilation (int or tuple, optional) – 内核间距Default: 1
    @:param groups (int, optional) – 从输入通道到输出通道的连接分组数Default: 1
    @:param bias (bool, optional) – If True, adds a learnable bias to the output. Default: True
    """

    in_data = torch.tensor([[[[0., 1., 2.],
                              [3., 4., 5.],
                              [6., 7., 8.]]]])
    print("input data size is {}".format(in_data.size()))
    # input data size is torch.Size([1, 1, 3, 3])
    conv2 = torch.nn.Conv2d(in_channels=1, out_channels=1, kernel_size=2)
    conv2.bias = torch.nn.Parameter(torch.zeros(1))
    conv2.weight = torch.nn.Parameter(torch.tensor([[[[.1, .1], [.1, .1]]]]))
    out_data = conv2(in_data)
    print(out_data.size())
    # torch.Size([1, 1, 2, 2])
    print(out_data)
    # tensor([[[[0.8000, 1.2000],
    #           [2.0000, 2.4000]]]], grad_fn=<MkldnnConvolutionBackward>)


conv2d()
