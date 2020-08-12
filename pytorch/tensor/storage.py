import torch

default_tensor = torch.randn(3, 3)
print(default_tensor.device)
# cpu

cpu_tensor = torch.tensor([1, 2, 3], dtype=torch.float, device='cpu')
print(cpu_tensor.device)
# cpu

gpu_tensor = torch.randn(2, 2, device='cuda:0')
print(gpu_tensor.device)
# cuda:0

gpu_tensor = torch.randn(2, 2, device='cuda:0')

cpu_tensor = gpu_tensor.cpu()
print(cpu_tensor.device)
# cpu
gpu_tensor = cpu_tensor.cuda(0)
print(gpu_tensor.device)
# cuda:0
