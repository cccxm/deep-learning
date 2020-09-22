import numpy as np


def rand(depth: int) -> np.ndarray:
    """
    随机正态分布参数向量
    :param depth:
    :return:
    """
    return np.random.randn(depth)
