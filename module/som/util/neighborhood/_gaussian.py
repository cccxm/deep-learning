import numpy as np
from numpy import ndarray


def gaussian(alpha: float, radius: float, i: ndarray, c: ndarray) -> float:
    """
    简化高斯函数
    :param alpha: 学习率
    :param radius: 邻域半径
    :param i: 位置
    :param c: 中心位置
    :return: 距离
    """
    if np.linalg.norm(i - c) <= radius:
        return alpha
    else:
        return 0.0
