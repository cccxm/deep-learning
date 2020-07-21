import torch


def conv_transpose_2d():
    """
    二维转置卷积
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

    input = torch.tensor([[[[1., 2.], [3., 4.]]]])
    convt2d = torch.nn.ConvTranspose2d(in_channels=1, out_channels=1, kernel_size=2)
    convt2d.bias = torch.nn.Parameter(torch.zeros(1))
    convt2d.weight = torch.nn.Parameter(torch.tensor([[[[.1, .1], [.1, .1]]]]))
    output = convt2d(input)
    print(output)
    # tensor([[[[0.1000, 0.3000, 0.2000],
    #           [0.4000, 1.0000, 0.6000],
    #           [0.3000, 0.7000, 0.4000]]]], grad_fn=<SlowConvTranspose2DBackward>)
