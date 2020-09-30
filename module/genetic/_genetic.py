class Node(object):
    pass


def index_random(pr: list) -> int:
    """
    随机一个根据概率的索引
    :param pr:
    :return: 索引
    """
    import random
    r = random.random()
    for i in range(len(pr)):
        if pr[i] > r:
            return i
    return len(pr) - 1


def alive(group: list, fit_score: list, alive_num: int) -> list:
    """
    选择存活个体
    :param group: 当前种群
    :param fit_score: 种群个体的适应度得分
    :param alive_num: 能够存活的个体个数
    :return: 存活个体集合
    """
    pr = fit_score
    a = []
    while len(a) != alive_num:
        s = sum(pr) + 0.000000001
        pr = [p / s for p in pr]
        for i in range(1, len(pr)):
            pr[i] += pr[i - 1]
        index = index_random(pr)
        a.append(group[index])
        group = [group[i] for i in range(len(group)) if i != index]
        pr = [pr[i] for i in range(len(pr)) if i != index]
    return a


def generate_next(group: list, fit_score: list, n: int, crossover) -> list:
    """
    产生新的后代
    :param group: 双亲
    :param fit_score: 种群个体的适应度得分
    :param n: 产生后代个数
    :param crossover: 节点交叉函数
    :return: 产生的后代
    """
    pr = fit_score
    a = []
    while len(a) != n:
        s = sum(pr) + 0.00000000001
        pr = [p / s for p in pr]
        for i in range(1, len(pr)):
            pr[i] += pr[i - 1]
        index = index_random(pr)
        a.append(group[index])
        group = [group[i] for i in range(len(group)) if i != index]
        pr = [pr[i] for i in range(len(pr)) if i != index]
    for i in range(len(a) - 1):
        a[i], a[i + 1] = crossover(a[i], a[i + 1])
    return a


class Model(object):
    def __init__(self, n: int, replace: float, mutation: float):
        """
        遗传算法模型
        :param n: 种群中个体的数量
        :param replace: 每次淘汰的比例(0.-1.)
        :param mutation: 种群内个体变异的比例(0.-1.)
        """
        self.n = n
        self.replace = replace
        self.mutation = mutation

    def search(self, generator, crossover, mutation, fitness, fitness_threshold: float) -> Node:
        """
        搜索假设
        :param generator: 种群初始化函数 lambda n:int -> list of Node
        :param crossover: 产生后代函数 lambda Node,Node -> Node,Node
        :param mutation: 变异函数 lambda Node -> Node
        :param fitness: 个体适应度函数 lambda Node -> float
        :param fitness_threshold: 适应度阈值，当有个体的适应度达到此阈值时，训练结束
        :return: 满足适应度阈值的节点
        """
        # 初始化种群
        import numpy as np
        group = generator(self.n)
        while True:
            # 评估每一个个体的适应度
            fit_score = []
            for unit in group:
                fit_score.append(fitness(unit))
            if max(fit_score) < fitness_threshold:
                # 如果没有产生目标个体
                # 按照概率公式pr选择哪些个体活到下一代，得分越高，活着的概率越大
                alive_group = alive(group, fit_score, int(self.n * (1 - self.replace)))
                # 根据概率公式pr选择n*r个双亲，产生n*r个后代
                next_generation = generate_next(group, fit_score, int(self.n * self.replace), crossover)
                # 生成新的种群
                group = alive_group + next_generation
                # 根据变异系数选择变异个体随机变异
                for i in range(len(group)):
                    if np.random.random() < self.mutation:
                        group[i] = mutation(group[i])
            else:
                # 返回适应度最高的个体
                return group[int(np.argmax(fit_score))]
