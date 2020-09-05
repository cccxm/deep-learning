import matplotlib.pyplot as plt
import numpy as np
import time

from modules.batch_SOM.batch_SOM import Model, euclidean

# 新建SOM模型，设置位深为2,图的尺寸为3x3
model = Model(depth=2, width=3, height=3)
# 设置距离算法为欧氏距离
model.distance = euclidean

# 创建深度为2的随机向量作为输入
X = [(np.random.randn(2)) for _ in range(100)]
[X.append(np.random.randn(2) + [0, 5]) for _ in range(100)]
[X.append(np.random.randn(2) + [-5, 0]) for _ in range(100)]
[X.append(np.random.randn(2) * [2, 0.8] + [5, 5]) for _ in range(100)]
[X.append(np.random.randn(2) * [2, 0.8] - [10, 10]) for _ in range(100)]
[X.append(np.random.randn(2) * [0.8, 2] + [10, 10]) for _ in range(100)]
[X.append(np.random.randn(2) * [0.8, 2] - [5, 5]) for _ in range(100)]
[X.append(np.random.randn(2) * 3 + [10, -10]) for _ in range(100)]
[X.append(np.random.randn(2) * 3 + [-10, 10]) for _ in range(100)]

# 显示原始向量的分布
plt.plot([x[0] for x in X], [x[1] for x in X], color="white", linestyle='dashed', marker="o", markerfacecolor='black')
plt.show()

marker_colors = ["#FF0000", "#000000", "#DC143C",
                 "#1E90FF", "#BA55D3", "#FF7F50",
                 "#0000FF", "#4B0082", "#00BFFF"]

# 初始化学习率，邻域半径
radius = 2.8
# 开始训练
step = 1
while radius > 0.1:
    print("step:{},radius: {}".format(step, radius))

    model.train(X, radius)
    radius *= 0.8

    color_list = [marker_colors[model.nodes.index(model.winner(x))] for x in X]
    for i in range(len(X)):
        plt.plot([X[i][0]], [X[i][1]], color="white", linestyle='dashed', marker="o",
                 markerfacecolor=color_list[i])
    plt.savefig("{}.jpg".format(step))
    plt.show()
    step += 1
