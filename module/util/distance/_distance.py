import numpy as np


def euclidean(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    计算两个向量的欧氏距离
    :return: float
    """
    return np.linalg.norm(v1 - v2)


def pearson(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    计算两个向量的皮尔逊相关系数
    :return: 相关系数的倒数
    """
    from scipy.stats import pearsonr
    return 1 / pearsonr(v1, v2)[0]


def fast_dtw(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    fast_dtw
    :return: 距离
    """
    import fastdtw
    from scipy.spatial.distance import euclidean
    # noinspection PyTypeChecker,PyUnresolvedReferences
    return fastdtw.fastdtw(v1, v2, dist=euclidean)[0]


def dtw(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    fast_dtw
    :return: 距离
    """
    import fastdtw
    from scipy.spatial.distance import euclidean
    # noinspection PyTypeChecker,PyUnresolvedReferences
    return fastdtw.dtw(v1, v2, dist=euclidean)[0]
