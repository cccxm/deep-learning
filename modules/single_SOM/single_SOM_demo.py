import matplotlib.pyplot as plt
import numpy as np
import time

from modules.single_SOM.single_SOM import Model, euclidean, gaussian

# 新建SOM模型，设置位深为2,图的尺寸为3x3
model = Model(depth=2, width=3, height=3)
# 设置距离算法为欧氏距离
model.distance = euclidean
# 设置邻域算法为简化高斯函数
model.neighborhood = gaussian

# 创建200个深度为2的随机向量作为输入
X = [(np.random.randn(2) * 5 + 10) for _ in range(100)]
[X.append(np.random.randn(2) * -5 - 10) for _ in range(100)]

# 显示原始向量的分布
plt.plot([x[0] for x in X], [x[1] for x in X], color="white", linestyle='dashed', marker="o", markerfacecolor='black')
plt.show()

marker_colors = ["#00BFFF", "#87CEFA", "#DC143C",
                 "#1E90FF", "#BA55D3", "#FF7F50",
                 "#0000FF", "#4B0082", "#FF0000"]

# 初始化学习率，邻域半径
alpha = 0.5
radius = 3.0
step = 0
# 开始训练，直到学习率降低到0.001时结束
while alpha > 0.001:
    step += 1
    print("step {}: alpha - {}; radius - {}".format(step, alpha, radius))
    time.sleep(0.5)

    for x in X:
        model.train(x, alpha, radius)
    alpha *= 0.9
    radius *= 0.95

    color_list = [marker_colors[model.nodes.index(model.winner(x))] for x in X]
    for i in range(len(X)):
        plt.plot([X[i][0]], [X[i][1]], color="white", linestyle='dashed', marker="o",
                 markerfacecolor=color_list[i])
    plt.show()
