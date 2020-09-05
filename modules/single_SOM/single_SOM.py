# Title     : SOM Demo
# Objective : show process of SOM algorithm
# Created by: chen
# Created on: 2020/9/4

import numpy as np
from numpy import ndarray


class Node(object):
    def __init__(self, weight: ndarray):
        """
        SOM节点对象
        :param weight: 权重初值
        """
        self.weight = weight
        # x,y
        self.position = np.array([0, 0], dtype=np.float64)


class Model(object):
    def __init__(self, depth: int, width: int, height: int):
        """
        SOM模型
        :param depth: 权重的深度
        :param width: 图的宽度
        :param height: 图的高度
        """
        self.width = width
        self.height = height
        self.length = width * height
        self.nodes = [Node(weight) for weight in [np.random.randn(depth) for _ in range(width * height)]]
        for i in range(len(self.nodes)):
            self.nodes[i].position = np.array([int(i % width), int(i / width)], np.float64)
        self.distance = None
        self.neighborhood = None

    def winner(self, x) -> Node:
        """
        查找优胜节点
        :param x:
        :return:
        """
        centre = self.nodes[0]
        min_d = self.distance(centre.weight, x)
        for node in self.nodes:
            d = np.linalg.norm(node.weight - x)
            if d < min_d:
                centre = node
                min_d = d
        return centre

    def train(self, x: ndarray, alpha: float, radius: float) -> bool:
        """
        单个输入训练
        :param x:
        :param alpha: 学习率
        :param radius: 邻域半径
        :return: is stop
        """
        # 查找优胜节点
        centre = self.winner(x)
        # 利用邻域函数更新全部节点的权值
        for node in self.nodes:
            node.weight = node.weight + self.neighborhood(alpha, radius, node.position, centre.position) * (
                    x - node.weight)
        return False


def euclidean(v1: ndarray, v2: ndarray) -> float:
    """
    欧氏距离计算
    :param v1:
    :param v2:
    :return:
    """
    return np.linalg.norm(v1 - v2)


def gaussian(alpha: float, radius: float, i: ndarray, c: ndarray) -> float:
    """
    邻域函数 - 简化高斯函数
    :param alpha: 学习率
    :param c: 获胜中心节点的位置向量
    :param i: 给定节点的位置向量
    :param radius: 给定邻域半径
    :return:
    """
    if np.linalg.norm(i - c) <= radius:
        return alpha
    else:
        return 0.0
