import torch

input = torch.tensor([[[[1, 2, 3, 4],
                        [5, 6, 7, 8]]]], dtype=torch.float32)
print(input)
# tensor([[[[1., 2., 3., 4.],
#           [5., 6., 7., 8.]]]])

m = torch.nn.ZeroPad2d((1, 1, 2, 2))
output = m(input)
print(output)
# tensor([[[[0., 0., 0., 0., 0., 0.],
#           [0., 0., 0., 0., 0., 0.],
#           [0., 1., 2., 3., 4., 0.],
#           [0., 5., 6., 7., 8., 0.],
#           [0., 0., 0., 0., 0., 0.],
#           [0., 0., 0., 0., 0., 0.]]]])
