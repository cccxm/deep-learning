import torch


def reflection_pad2d():
    """
    2维对称填充
    @:param padding (int, tuple) – the size of the padding.
    :return: Tensor
    """
    m = torch.nn.ReflectionPad2d((1, 2, 1, 2))
    input = torch.tensor([[[[1, 2, 3, 4],
                            [5, 6, 7, 8],
                            [9, 10, 11, 12]]]], dtype=torch.float32)
    print(input)
    # tensor([[[[ 1.,  2.,  3.,  4.],
    #           [ 5.,  6.,  7.,  8.],
    #           [ 9., 10., 11., 12.]]]])
    output = m(input)
    print(output)
    # tensor([[[[ 6.,  5.,  6.,  7.,  8.,  7.,  6.],
    #           [ 2.,  1.,  2.,  3.,  4.,  3.,  2.],
    #           [ 6.,  5.,  6.,  7.,  8.,  7.,  6.],
    #           [10.,  9., 10., 11., 12., 11., 10.],
    #           [ 6.,  5.,  6.,  7.,  8.,  7.,  6.],
    #           [ 2.,  1.,  2.,  3.,  4.,  3.,  2.]]]])
