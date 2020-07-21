import torch

input = torch.tensor([[[[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12]]]], dtype=torch.float32)
print(input)
# tensor([[[[ 1.,  2.,  3.,  4.],
#           [ 5.,  6.,  7.,  8.],
#           [ 9., 10., 11., 12.]]]])

m = torch.nn.ConstantPad2d((1, 1, 1, 1), 0)
output = m(input)
print(output)
# tensor([[[[ 0.,  0.,  0.,  0.,  0.,  0.],
#           [ 0.,  1.,  2.,  3.,  4.,  0.],
#           [ 0.,  5.,  6.,  7.,  8.,  0.],
#           [ 0.,  9., 10., 11., 12.,  0.],
#           [ 0.,  0.,  0.,  0.,  0.,  0.]]]])
