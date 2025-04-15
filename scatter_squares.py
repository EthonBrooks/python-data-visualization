import matplotlib.pyplot as plt

x_value = range(1, 1001)
y_value = [value ** 2 for value in x_value]

plt.style.use('seaborn-v0_8')  # 更改网格的样式
fig, ax = plt.subplots()

ax.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, s=10)  # s参数设置
ax.set_title('Square Number', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Squares of Value', fontsize=14)
ax.tick_params(labelsize=14)  # 设置刻度标记的样式
ax.axis([0, 1100, 0, 1_100_000])  # 设置坐标轴的范围,参数是一个列表

plt.show()
