import torch


def conv_transpose_1d():
    """
    一维转置卷积
    @:param in_channels (int) – 输入通道数
    @:param out_channels (int) – 输出通道数
    @:param kernel_size (int or tuple) – 卷积核数
    @:param stride (int or tuple, optional) – 卷积步长
    @:param padding (int or tuple, optional) – dilation * (kernel_size - 1) - 填充Default: 0
    @:param output_padding (int or tuple, optional) – 输出填充Default: 0
    @:param groups (int, optional) – 从输入到输出的卷积分组Default: 1
    @:param bias (bool, optional) – If True, adds a learnable bias to the output. Default: True
    @:param dilation (int or tuple, optional) – 卷积核内部间距Default: 1
    """

    input = torch.tensor([[[.8, 1.4, 2., 2.6, 3.2, 3.8, 4.4, 5.]]])
    convt1d = torch.nn.ConvTranspose1d(in_channels=1, out_channels=1, kernel_size=3)
    convt1d.bias = torch.nn.Parameter(torch.zeros(1))
    convt1d.weight = torch.nn.Parameter(torch.tensor([[[.1, .2, .3]]]))
    output = convt1d(input)
    print(output)
    # tensor([[[0.0800, 0.3000, 0.8000, 1.2200, 1.6400, 2.0600, 2.4800, 2.9000,
    #           2.7600, 2.0000]]], grad_fn=<SqueezeBackward1>)
