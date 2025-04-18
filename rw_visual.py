import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # 创建一个random实例
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 将所有点都绘制出来
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(12, 8), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=1)  # edgecolors='none'表示删除每个点的轮廓
    ax.set_aspect('equal')  # 设置坐标轴的比例相等

    # 突出起点和终点
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)  # 链式引用
    ax.get_yaxis().set_visible(False)

    plt.show()

    if input("是否继续？(y/n): ") == 'n':
        break
