import random
import sys

from module.genetic import Genetic, Unit

operators = [
    ('plus', lambda x: x[0] + x[1]),
    ('multi', lambda x: x[0] * x[1]),
    ('minus', lambda x: x[0] - x[1]),
    ('dev', lambda x: [x[0] / x[1] if x[1] != 0 else sys.maxsize][0])
]
X = [
    ((0, 10), 10),
    ((1, 9), 6.4),
    ((2, 8), 3.6),
    ((3, 7), 1.6),
    ((4, 6), 0.4),
    ((5, 5), 0)
]


class ProgramingNode(Unit):
    def __init__(self, name: str, operator):
        """
        程序树节点，表示一个操作对象
        :param name:节点名
        :param operator: 操作
        """
        self.operator = operator
        self.name = name
        self.left = None
        self.right = None
        self.parent = None

    def copy(self):
        node = ProgramingNode(self.name, self.operator)
        if self.left is not None:
            node.left = self.left.copy()
            node.left.parent = node
        if self.right is not None:
            node.right = self.right.copy()
            node.right.parent = node
        return node

    def to_list(self) -> list:
        nodes = [self]
        if self.left is not None:
            [nodes.append(node) for node in self.left.to_list()]
        if self.right is not None:
            [nodes.append(node) for node in self.right.to_list()]
        return nodes

    def execute(self, x: tuple) -> float:
        if self.left is None or self.right is None:
            return self.operator(x)
        else:
            return self.operator((self.left.execute(x), self.right.execute(x)))

    def __str__(self) -> str:
        if self.left is None or self.right is None:
            return self.name
        else:
            return "{}:({}:{})".format(self.name, self.left.__str__(), self.right.__str__())


def generator(n: int) -> list:
    """
    生成初始化节点
    """
    population = []
    for i in range(n):
        random.shuffle(operators)
        nodes = [ProgramingNode(op[0], op[1]) for op in random.sample(operators, 3)]
        nodes[0].left = nodes[1]
        nodes[0].right = nodes[2]
        nodes[1].parent = nodes[2].parent = nodes[0]
        population.append(nodes[0])
    return population


def crossover(parent1: ProgramingNode, parent2: ProgramingNode) -> tuple:
    """
    交叉算子
    """
    node1 = parent1.copy()
    node2 = parent2.copy()
    r1: ProgramingNode = random.choice(node1.to_list())
    r2: ProgramingNode = random.choice(node2.to_list())
    if r1.parent is not None and r2.parent is not None:
        if r1.parent.left == r1:
            r1.parent.left = r2.copy()
            r1.parent.left.parent = r1.parent
        if r1.parent.right == r1:
            r1.parent.right = r2.copy()
            r1.parent.right.parent = r1.parent
        if r2.parent.left == r2:
            r2.parent.left = r1.copy()
            r2.parent.left.parent = r2.parent
        if r2.parent.right == r2:
            r2.parent.right = r1.copy()
            r2.parent.right.parent = r2.parent
    elif r2.parent is not None:
        if r2.parent.left == r2:
            r2.parent.left = node1
        if r2.parent.right == r2:
            r2.parent.right = node1
        node1.parent = r2.parent
        node1 = r2.copy()
        node1.parent = None
    elif r1.parent is not None:
        if r1.parent.left == r1:
            r1.parent.left = node2
        if r1.parent.right == r1:
            r1.parent.right = node2
        node2.parent = r1.parent
        node2 = r1.copy()
        node2.parent = None
    return node1, node2


def mutation(node: ProgramingNode) -> Unit:
    """
    变异
    """
    operator = random.choice(operators)
    n = random.choice(node.to_list())
    n.name = operator[0]
    n.operator = operator[1]
    return node


def fitness(node: ProgramingNode) -> float:
    """
    适应度
    :param node:
    :return:
    """
    return 1 - min(100, sum([abs(y - node.execute(x)) for x, y in X])) / 100


model = Genetic(100, 0.02, 0.01)
target = model.search(generator, crossover, mutation, fitness, 1.)
print(target.__str__())
# multi:(dev:(minus:plus):minus)
# dev:(minus:dev:(plus:minus))
# multi:(minus:dev:(minus:plus))
