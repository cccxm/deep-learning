import numpy as np
from numpy import ndarray
from .util.rand import PARAMETER_RAND_NORM
from .util.distance import EUCLIDEAN
from .util.neighborhood import GAUSSIAN


class Node(object):
    def __init__(self, label, weight: ndarray):
        """
        图节点
        :param label: 标签
        :param weight: 权重
        """
        self.weight = weight
        self.position = np.array([0, 0], dtype=np.float)
        self.label = label


class Model(object):
    def __init__(self, depth: int, width: int, height: int, labels: list,
                 param_init=PARAMETER_RAND_NORM,
                 distance=EUCLIDEAN,
                 neighborhood=GAUSSIAN):
        """
        学习向量量化 LVQ 模型
        需要额外设置
        :param depth: 位深，对应节点权值深度
        :param width: 图的宽度
        :param height: 图的高度
        :param labels: 标签初始节点标签列表，长度不能小于节点数量
        :param param_init: 标签初始化函数，默认为正态分布
        :param distance: 距离函数，默认为欧氏距离
        :param neighborhood: 邻域函数，默认为简化高斯函数
        """
        self.width = width
        self.height = height
        self.length = width * height
        self.nodes = [Node(label, weight) for weight, label in
                      [(param_init(depth), labels[i]) for i in range(width * height)]]
        for i in range(len(self.nodes)):
            self.nodes[i].position = np.array([int(i % width), int(i / width)], np.float)
        self.distance = distance
        self.neighborhood = neighborhood

    def __len__(self):
        return self.length

    def winner(self, x: ndarray) -> Node:
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

    def train(self, X: list, y, alpha: float, radius: float) -> None:
        """
        模型训练
        :param X: 输入列表（要求属于同一个标签）
        :param y: 标签
        :param alpha: 学习率 [0.-1.]
        :param radius: 邻域半径
        :return: None
        """
        winners = []
        for _, x in X:
            # 查找优胜节点
            centre = self.winner(x)
            winners.append(self.nodes.index(centre))
            # 利用邻域函数更新全部节点的权值
            for node in self.nodes:
                node.weight = node.weight + self.neighborhood(alpha, radius, node.position, centre.position) * (
                        x - node.weight)
        # 更新选中节点的标签
        max_label = max(winners, key=winners.count)
        self.nodes[max_label].label = y

    def validate(self, test_sets: list) -> float:
        """
        评估模型正确率
        :param test_sets:输入列表（标签可以不相同）
        :return: 模型正确率[0.-1.]
        """
        return sum([1 for (label, test) in test_sets if self.winner(test).label == label]) / len(test_sets)
