import torch


def conv1d():
    """
    Applies a 1D convolution over an input signal composed of several input planes.
    @:param in_channels (int) -输入图像中的通道数
    @:param out_channels（int）–卷积产生的通道数
    @:param kernel_size（int或tuple）–卷积内核的大小
    @:param stride（int or tuple，optional）–卷积的步幅,默认值：1
    @:param padding（int or tuple，optional）–将零填充添加到输入的两侧,默认值：0
    @:param padding_mode (string, optional) – 'zeros', 'reflect', 'replicate' or 'circular'. Default: 'zeros'
    @:param dilation (int or tuple, optional) – 内核元素之间的间距. Default: 1
    @:param groups (int, optional) – 从输入通道到输出通道的连接数. Default: 1
    @:param bias (bool, optional) – If True, 给输出增加可学习的偏置. Default: True
    """

    in_data = torch.tensor([[[0., 1., 2., 3., 4., 5., 6., 7., 8., 9.]]])
    print("input size is {}".format(in_data.size()))
    # input size is torch.Size([1, 1, 10])
    conv1d = torch.nn.Conv1d(in_channels=1, out_channels=1, kernel_size=3)
    conv1d.bias = torch.nn.Parameter(torch.zeros(1))
    print("bias size is {}".format(conv1d.bias.size()))
    # bias size is torch.Size([1])
    conv1d.weight = torch.nn.Parameter(torch.tensor([[[.1, .2, .3]]]))
    print("weight size is {}".format(conv1d.weight.size()))
    # weight size is torch.Size([1, 1, 3])
    out_data = conv1d(in_data)
    print("output size is {}".format(out_data.size()))
    # output size is torch.Size([1, 1, 8])
    print("output data is {}".format(out_data))
    # output data is tensor([[[0.8000, 1.4000, 2.0000, 2.6000, 3.2000, 3.8000, 4.4000, 5.0000]]],
    #        grad_fn=<SqueezeBackward1>)
