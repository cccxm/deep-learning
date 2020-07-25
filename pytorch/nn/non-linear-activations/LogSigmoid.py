import torch

input = torch.tensor([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2], dtype=torch.float32)
m = torch.nn.LogSigmoid()
output = m(input)
print(output)
# tensor([-2.1269, -1.7014, -1.3133, -0.9741, -0.6931, -0.4741, -0.3133, -0.2014,
#         -0.1269])
