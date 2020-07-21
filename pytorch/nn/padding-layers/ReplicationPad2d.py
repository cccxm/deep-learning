import torch

input = torch.tensor([[[[1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 0]]]], dtype=torch.float32)
print(input)
# tensor([[[[1., 2., 3., 4., 5.],
#           [6., 7., 8., 9., 0.]]]])

m = torch.nn.ReplicationPad2d(1)
output = m(input)
print(output)
# tensor([[[[1., 1., 2., 3., 4., 5., 5.],
#           [1., 1., 2., 3., 4., 5., 5.],
#           [6., 6., 7., 8., 9., 0., 0.],
#           [6., 6., 7., 8., 9., 0., 0.]]]])

m = torch.nn.ReplicationPad2d((1, 1, 2, 2))
output = m(input)
print(output)
# tensor([[[[1., 1., 2., 3., 4., 5., 5.],
#           [1., 1., 2., 3., 4., 5., 5.],
#           [1., 1., 2., 3., 4., 5., 5.],
#           [6., 6., 7., 8., 9., 0., 0.],
#           [6., 6., 7., 8., 9., 0., 0.],
#           [6., 6., 7., 8., 9., 0., 0.]]]])
