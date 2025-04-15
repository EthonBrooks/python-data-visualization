import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.style.use('Solarize_Light2')  # 更改网格的样式

fig, ax = plt.subplots()  # subplots()函数可在一个图形中绘制一个或多个绘图。变量fig表示由多个绘图绘成的整个图形，变量ax表示图形中的绘图
ax.plot(input_values, squares, linewidth=3)  # linewidth参数设置线条的宽度

# 设置图形的标题和坐标轴标签
ax.set_title('Square Number', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Squares of Value', fontsize=14)

# 设置刻度标记的大小
ax.tick_params(labelsize=14)

plt.show()
