import torch


def reflection_pad1d():
    """
    1维对称填充
    @:param padding (int, tuple) – the size of the padding.
    :return: Tensor
    """
    m = torch.nn.ReflectionPad1d(2)
    input = torch.tensor([[[1, 2, 3, 4]]], dtype=torch.float32)
    print(input)
    # tensor([[[1., 2., 3., 4.]]])
    output = m(input)
    print(output)
    # tensor([[[3., 2., 1., 2., 3., 4., 3., 2.]]])
