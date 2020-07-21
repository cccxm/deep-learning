import torch


def conv_transpose_3d():
    """
    三维转置卷积
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

    input = torch.tensor([[[[[6.0000, 6.8000],
                             [8.4000, 9.2000]],
                            [[13.2000, 14.0000],
                             [15.6000, 16.4000]]]]])
    convt3 = torch.nn.ConvTranspose3d(1, 1, kernel_size=2)
    convt3.bias = torch.nn.Parameter(torch.zeros(1))
    convt3.weight = torch.nn.Parameter(torch.tensor([[[[[.1, .1],
                                                        [.1, .1]],
                                                       [[.1, .1],
                                                        [.1, .1]]]]]))
    output = convt3(input)
    print(output)
    # tensor([[[[[0.6000, 1.2800, 0.6800],
    #            [1.4400, 3.0400, 1.6000],
    #            [0.8400, 1.7600, 0.9200]],
    #
    #           [[1.9200, 4.0000, 2.0800],
    #            [4.3200, 8.9600, 4.6400],
    #            [2.4000, 4.9600, 2.5600]],
    #
    #           [[1.3200, 2.7200, 1.4000],
    #            [2.8800, 5.9200, 3.0400],
    #            [1.5600, 3.2000, 1.6400]]]]], grad_fn=<SlowConvTranspose3DBackward>)
