# Title     : SOM Demo
# Objective : show process of SOM algorithm
# Created by: chen
# Created on: 2020/9/5

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
        self.depth = depth
        self.width = width
        self.height = height
        self.length = width * height
        self.nodes = [Node(weight) for weight in [np.random.randn(depth) for _ in range(width * height)]]
        for i in range(len(self.nodes)):
            self.nodes[i].position = np.array([int(i % width), int(i / width)], np.float64)
        self.distance = None
        self.neighborhood = lambda r, i, c: np.linalg.norm(i - c) <= r
        self.update = lambda U: np.array([np.mean([u[d] for u in U]) for d in range(depth)], dtype=np.float64)

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

    def train(self, X: list, radius: float):
        """
        单个输入训练
        :param X: list of ndarray
        :param alpha: 学习率
        :param radius: 邻域半径
        :return: is stop
        """
        # 生成Voronoi集
        V = [(self.nodes.index(self.winner(x)), x) for x in X]
        # 生成邻域集
        N = [[self.nodes.index(node) for node in self.nodes if
              self.neighborhood(radius, node.position, self.nodes[i].position)]
             for i in range(self.length)]
        # 生成并集U
        U = [union([[v[1] for v in V if v[0] == n] for n in N[i]]) for i in range(self.length)]
        # 更新m
        for i in range(self.length):
            node = self.nodes[i]
            node.weight = self.update(U[i])


def union(data: list) -> list:
    n = []
    for d in data:
        n += d
    return n


def euclidean(v1: ndarray, v2: ndarray) -> float:
    """
    欧氏距离计算
    :param v1:
    :param v2:
    :return:
    """
    return np.linalg.norm(v1 - v2)
