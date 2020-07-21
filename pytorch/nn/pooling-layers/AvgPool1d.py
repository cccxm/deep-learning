from torch import tensor, float32
from torch.nn import AvgPool1d


def avg_pool1d():
    """
    一维均值池化器
    @:param kernel_size – the size of the window
    @:param stride – the stride of the window. Default value is kernel_size
    @:param padding – implicit zero padding to be added on both sides
    @:param ceil_mode – when True, will use ceil instead of floor to compute the output shape
    @:param count_include_pad – when True, will include the zero-padding in the averaging calculation
    """
    pool = AvgPool1d(kernel_size=3, stride=1)
    input = tensor([[[0, 1, 2, 2, 3, 3, 3, 4, 4, 4]]], dtype=float32)
    output = pool(input)
    print(output)
    # tensor([[[1.0000, 1.6667, 2.3333, 2.6667, 3.0000, 3.3333, 3.6667, 4.0000]]])
