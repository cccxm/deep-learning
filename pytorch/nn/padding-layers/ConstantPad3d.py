import torch

input = torch.tensor([[[[[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]],
                        [[10, 11, 12],
                         [13, 14, 15],
                         [16, 17, 18]]]]], dtype=torch.float32)
print(input)
# tensor([[[[[ 1.,  2.,  3.],
#            [ 4.,  5.,  6.],
#            [ 7.,  8.,  9.]],
#
#           [[10., 11., 12.],
#            [13., 14., 15.],
#            [16., 17., 18.]]]]])

m = torch.nn.ConstantPad3d(1, 0)
output = m(input)
print(output)
# tensor([[[[[ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.]],
#
#           [[ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  1.,  2.,  3.,  0.],
#            [ 0.,  4.,  5.,  6.,  0.],
#            [ 0.,  7.,  8.,  9.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.]],
#
#           [[ 0.,  0.,  0.,  0.,  0.],
#            [ 0., 10., 11., 12.,  0.],
#            [ 0., 13., 14., 15.,  0.],
#            [ 0., 16., 17., 18.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.]],
#
#           [[ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.],
#            [ 0.,  0.,  0.,  0.,  0.]]]]])