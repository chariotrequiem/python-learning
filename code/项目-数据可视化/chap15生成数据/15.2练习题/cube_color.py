# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/27 17:45
import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# 设置图表标题并给坐标加上标签
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 5100, 0, 140000000000])
plt.show()