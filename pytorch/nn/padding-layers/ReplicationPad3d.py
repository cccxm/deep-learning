import torch

input = torch.tensor([[[[[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]],
                        [[10, 11, 12],
                         [13, 14, 15],
                         [16, 17, 18]],
                        [[19, 20, 21],
                         [22, 23, 24],
                         [25, 26, 27]]]]], dtype=torch.float32)
print(input)
# tensor([[[[[ 1.,  2.,  3.],
#            [ 4.,  5.,  6.],
#            [ 7.,  8.,  9.]],
#
#           [[10., 11., 12.],
#            [13., 14., 15.],
#            [16., 17., 18.]],
#
#           [[19., 20., 21.],
#            [22., 23., 24.],
#            [25., 26., 27.]]]]])

m = torch.nn.ReplicationPad3d(1)
output = m(input)
print(output)
# tensor([[[[[ 1.,  1.,  2.,  3.,  3.],
#            [ 1.,  1.,  2.,  3.,  3.],
#            [ 4.,  4.,  5.,  6.,  6.],
#            [ 7.,  7.,  8.,  9.,  9.],
#            [ 7.,  7.,  8.,  9.,  9.]],
#
#           [[ 1.,  1.,  2.,  3.,  3.],
#            [ 1.,  1.,  2.,  3.,  3.],
#            [ 4.,  4.,  5.,  6.,  6.],
#            [ 7.,  7.,  8.,  9.,  9.],
#            [ 7.,  7.,  8.,  9.,  9.]],
#
#           [[10., 10., 11., 12., 12.],
#            [10., 10., 11., 12., 12.],
#            [13., 13., 14., 15., 15.],
#            [16., 16., 17., 18., 18.],
#            [16., 16., 17., 18., 18.]],
#
#           [[19., 19., 20., 21., 21.],
#            [19., 19., 20., 21., 21.],
#            [22., 22., 23., 24., 24.],
#            [25., 25., 26., 27., 27.],
#            [25., 25., 26., 27., 27.]],
#
#           [[19., 19., 20., 21., 21.],
#            [19., 19., 20., 21., 21.],
#            [22., 22., 23., 24., 24.],
#            [25., 25., 26., 27., 27.],
#            [25., 25., 26., 27., 27.]]]]])