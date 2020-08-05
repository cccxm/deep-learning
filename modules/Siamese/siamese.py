import random

import PIL
from PIL.Image import Image
import numpy
import torch
from torch.nn import Module
import torchvision
from matplotlib import pyplot
from torch import Tensor
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from torchvision.datasets.folder import ImageFolder


def show_image(img: Tensor, text: str = None) -> None:
    """
    显示图片
    :param img: shape is (C,H,W)
    :param text: 展示文字说明
    :return: None
    """
    np_image = img.numpy()
    pyplot.axis("off")  # 设置坐标轴关闭
    if text:
        pyplot.text(75, 8, text)
    pyplot.imshow(numpy.transpose(np_image, (1, 2, 0)))  # 转换为(H,W,C)
    pyplot.show()


def show_loss_plot(iteration: list, loss: list) -> None:
    """
    绘制损失变化图
    :param iteration: list<int> 迭代次数
    :param loss: list<int> 损失值
    """
    pyplot.plot(iteration, loss)
    pyplot.show()


class SiameseNetworkDataset(Dataset):

    def __init__(self,
                 image_folder_dataset: ImageFolder,
                 transform: transforms.Compose = None) -> None:
        """
        表示ORL数据集的对象
        :param image_folder_dataset: 图片数据集文件夹对象
        :param transform: 数据集转换方式对象
        """
        self.image_folder_dataset = image_folder_dataset
        self.transform = transform

    def __getitem__(self, index: int) -> (Image, Image, Tensor):
        """
        提供使用索引访问数据集的方式，这里使用随机获取图片的方式
        :param index: 访问元素索引
        :return: (Image.Image, Image.Image, Tensor)
        """
        img0_tuple = random.choice(self.image_folder_dataset.imgs)
        should_get_same_class = random.randint(0, 1)  # 保证同类样本约占一半
        if should_get_same_class:
            while True:
                # 直到找到同一类别
                img1_tuple = random.choice(self.image_folder_dataset.imgs)
                if img0_tuple[1] == img1_tuple[1]:
                    break
        else:
            while True:
                # 直到找到非同一类别
                img1_tuple = random.choice(self.image_folder_dataset.imgs)
                if img0_tuple[1] != img1_tuple[1]:
                    break
        # 随机从数据集中抽出两张图片
        img0: Image = PIL.Image.open(img0_tuple[0]).convert("L")
        img1: Image = PIL.Image.open(img1_tuple[0]).convert("L")
        # 将原始图像转换为灰度图像 L
        if self.transform is not None:
            # 按照指定的方式对图像进行转换
            img0 = self.transform(img0)
            img1 = self.transform(img1)

        return img0, img1, torch.from_numpy(numpy.array([int(img0_tuple[1] != img1_tuple[1])], dtype=numpy.float))

    def __len__(self) -> int:
        """
        数据集长度
        :return: int
        """
        return len(self.image_folder_dataset.imgs)


class SiameseNetwork(Module):

    def __init__(self) -> None:
        """
        孪生网络模型对象
        """
        Module.__init__(self)
        # 卷积神经网络顺序容器，能够按照指定顺序执行操作
        self.cnn = torch.nn.Sequential(
            torch.nn.ReflectionPad2d(1),
            torch.nn.Conv2d(1, 4, kernel_size=3),
            torch.nn.ReLU(inplace=True),
            torch.nn.BatchNorm2d(4),

            torch.nn.ReflectionPad2d(1),
            torch.nn.Conv2d(4, 8, kernel_size=3),
            torch.nn.ReLU(inplace=True),
            torch.nn.BatchNorm2d(8),

            torch.nn.ReflectionPad2d(1),
            torch.nn.Conv2d(8, 8, kernel_size=3),
            torch.nn.ReLU(inplace=True),
            torch.nn.BatchNorm2d(8),
        )

        self.fc = torch.nn.Sequential(
            torch.nn.Linear(8 * 100 * 100, 500),
            torch.nn.ReLU(inplace=True),

            torch.nn.Linear(500, 500),
            torch.nn.ReLU(inplace=True),

            torch.nn.Linear(500, 5),
        )

    def forward_once(self, x: Tensor) -> Tensor:
        """
        一次前向传播
        :param x: Tensor
        :return: Tensor
        """
        output = self.cnn(x)
        output = output.view(output.size()[0], -1)
        output = self.fc(output)
        return output

    def forward(self, input1: Tensor, input2: Tensor) -> (Tensor, Tensor):
        """
        前向传播，同时讲两个输入通过同样的网络结构
        :param input1: Tensor
        :param input2: Tensor
        :return: Tensor, Tensor
        """
        output1 = self.forward_once(input1)
        output2 = self.forward_once(input2)
        return output1, output2


class ContrastiveLoss(Module):

    def __init__(self, margin: float = 2.0) -> None:
        """
        定义对比损失函数模型
        :param margin:
        """
        super(ContrastiveLoss, self).__init__()
        self.margin = margin

    def forward(self, output1: Tensor, output2: Tensor, label: Tensor) -> Tensor:
        """
        计算两个输出的对比损失
        :param output1: Tensor
        :param output2: Tensor
        :param label: Tensor 表示类别的张量，长度为1,使用整数表示T and F
        :return: Tensor
        """
        euclidean_distance: Tensor = torch.nn.functional.pairwise_distance(output1, output2, keepdim=True)
        # 欧氏距离
        loss_contrastive: Tensor = torch.mean((1 - label) * torch.pow(euclidean_distance, 2) +
                                              label * torch.pow(torch.clamp(self.margin - euclidean_distance, min=0.0),
                                                                2))
        # 对比损失
        return loss_contrastive


BATCH_SIZE = 32
EPOCHS = 50

# 创建数据集对象SIAMESE_DATASET
SIAMESE_DATASET = SiameseNetworkDataset(
    image_folder_dataset=torchvision.datasets.ImageFolder(root="./datasets/ORL_Faces/"),
    # 图像数据集文件夹 生成一个图片数组对象
    transform=torchvision.transforms.Compose([
        transforms.Resize((100, 100)),
        transforms.ToTensor()])
    # 设置数据压缩方式 1,调整大小为100x100，并保存为Tensor格式
)

# 创建一个能够从数据集中遍历加载数据的方式
TRAIN_DATA_LOADER = torch.utils.data.dataloader.DataLoader(dataset=SIAMESE_DATASET,
                                                           shuffle=True,
                                                           batch_size=BATCH_SIZE)
RUN_WITH_CUDA = torch.cuda.is_available()
if RUN_WITH_CUDA:
    NET = SiameseNetwork().cuda()
else:
    NET = SiameseNetwork()
CRITERION = ContrastiveLoss()
OPTIMIZER = torch.optim.Adam(NET.parameters(), lr=0.0005)
COUNTER = []
LOSS_HISTORY = []
ITERATION_NUMBER = 0
for EPOCH in range(0, EPOCHS):
    for INDEX, DATA in enumerate(TRAIN_DATA_LOADER):
        IMG_0, IMG_1, LABEL = DATA
        if RUN_WITH_CUDA:
            IMG_0, IMG_1, LABEL = IMG_0.cuda(), IMG_1.cuda(), LABEL.cuda()
        OPTIMIZER.zero_grad()  # 清除梯度
        OUTPUT_1, OUTPUT_2 = NET(IMG_0, IMG_1)
        LOSS_CONTRASTIVE = CRITERION(OUTPUT_1, OUTPUT_2, LABEL)
        LOSS_CONTRASTIVE.backward()
        OPTIMIZER.step()  # 更新参数
        if INDEX % 10 == 0:
            ITERATION_NUMBER += 10
            COUNTER.append(ITERATION_NUMBER)
            LOSS_HISTORY.append(LOSS_CONTRASTIVE.item())
    # noinspection PyUnboundLocalVariable
    print("Epoch number:{}, Current loss:{:.4f}".format(EPOCH, LOSS_CONTRASTIVE.item()))

show_loss_plot(COUNTER, LOSS_HISTORY)
