import numpy as np
from numpy import ndarray
from .util.rand import PARAMETER_RAND_NORM
from .util.distance import EUCLIDEAN
from .util.neighborhood import GAUSSIAN


class Node(object):
    def __init__(self, weight: ndarray):
        """
        图节点
        :param weight: 权重
        """
        self.weight = weight
        self.position = np.array([0, 0], dtype=np.float64)


class Model(object):
    def __init__(self, depth: int, width: int, height: int,
                 param_init=PARAMETER_RAND_NORM,
                 distance=EUCLIDEAN,
                 neighborhood=GAUSSIAN
                 ):
        """
        SOM 模型
        :param depth: 深度
        :param width: 图 宽度
        :param height: 图 高度
        :param param_init: 标签初始化函数，默认为正态分布
        :param distance: 距离函数，默认为欧氏距离
        :param neighborhood: 邻域函数，默认为简化高斯函数
        """
        self.width = width
        self.height = height
        self.length = width * height
        self.nodes = [Node(weight) for weight in [param_init(depth) for _ in range(width * height)]]
        for i in range(len(self.nodes)):
            self.nodes[i].position = np.array([int(i % width), int(i / width)], np.float64)
        self.distance = distance
        self.neighborhood = neighborhood

    def __len__(self):
        return self.length

    def winner(self, x) -> Node:
        """
        获胜节点计算函数
        :param x: 单个输入
        :return: 获胜节点
        """
        centre = self.nodes[0]
        min_d = self.distance(centre.weight, x)
        for node in self.nodes:
            d = self.distance(node.weight, x)
            if d < min_d:
                centre = node
                min_d = d
        return centre

    def train(self, x: ndarray, alpha: float, radius: float):
        """
        模型训练
        :param x: 单个输入
        :param alpha: 学习率 [0.-1.]
        :param radius: 邻域半径
        :return: None
        """
        # 查找优胜节点
        centre = self.winner(x)
        # 利用邻域函数更新全部节点的权值
        for node in self.nodes:
            node.weight = node.weight + self.neighborhood(alpha, radius, node.position, centre.position) * (
                    x - node.weight)
