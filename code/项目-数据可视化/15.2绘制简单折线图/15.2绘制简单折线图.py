# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/27 11:50
import matplotlib.pyplot as plt  # matplotlib.pyplot模块：绘图

# 2.1修改标签文字和线条粗细
"""
参数linewidth决定了plot()绘制的线条的粗细。函数title()给图表指定标题。
参数fontsize指定了图表中文字的大小。函数xlabel()和ylabel()让你能够为每条轴设置标题；
函数tick_params()设置刻度的样式，其中指定的实参将影响x轴和y轴上的刻度（axes='both' ），
并将刻度标记的字号设置为14（labelsize=14）。
squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()
"""

# 2.2校正图形
# 当你向plot()提供一系列数字时，它假设第一个数据点对应的x坐标值为0，
# 但我们的第一个点对应的x值为1。为改变这种默认行为，我们可以给plot()同时提供输入值和输出值：
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()

# 2.3使用scatter()绘制散点图并设置其样式
"""
有时候，需要绘制散点图并设置各个数据点的样式。
例如，你可能想以一种颜色显示较小的值，而用另一种颜色显示较大的值。
绘制大型数据集时，你还可以对每个点都设置同样的样式，再使用不同的样式选项重新绘制某些点，以突出它们。 

要绘制单个点，可使用函数scatter()，并向它传递一对x和y坐标，它将在指定位置绘制一个点：
"""
plt.scatter(2, 4, s=200)

# 设置图表标题并给坐标加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()

# 2.4使用scatter()绘制一系列点
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values, s=100)

# 设置图表标题并给坐标加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()

# 2.5自动计算数据
# 手工计算列表要包含的值可能效率低下，需要绘制的点很多时尤其如此。
# 可以不必手工计算包含点坐标的列表，而让Python循环来替我们完成这种计算。下面是绘制1000个点的代码：
"""
我们首先创建了一个包含x值的列表，其中包含数字1~1000。
接下来是一个生成y值的列表解析，它遍历x值（for x in x_values），计算其平方值（x**2），并将结果存储到列表y_values中。
然后，将输入列表和输出列表传递给scatter()。

由于这个数据集较大，我们将点设置得较小，并使用函数axis()指定了每个坐标轴的取值范围。
函数axis()要求提供四个值: x和y坐标轴的最小值和最大值。在这里，我们将x坐标轴的取值范围设置为0~1100，
并将y坐标轴的取值范围设置为0~1 100 000。
"""
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
# 设置图表标题并给坐标加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
plt.show()

# 2.6删除数据点的轮廓
"""
matplotlib允许你给散点图中的各个点指定颜色。
默认为蓝色点和黑色轮廓，在散点图包含的数据点不多时效果很好。但绘制很多点时，黑色轮廓可能会粘连在一起。
要删除数据点的轮廓，可在调用scatter()时传递实参edgecolor='none'
"""

# 2.7自定义颜色
"""
要修改数据点的颜色，可向scatter()传递参数c ，并将其设置为要使用的颜色的名称

还可以使用RGB颜色模式自定义颜色。
要指定自定义颜色，可传递参数c，并将其设置为一个元组，其中包含三个0~1之间的小数值，它们分别表示红色、绿色和蓝色分量。
"""

# 2.8使用颜色映射
"""
颜色映射（colormap）是一系列颜色，它们从起始颜色渐变到结束颜色。
在可视化中，颜色映射用于突出数据的规律，例如，你可能用较浅的颜色来显示较小的值，并使用较深的颜色来显示较大的值。 

模块pyplot内置了一组颜色映射。要使用这些颜色映射，你需要告诉pyplot该如何设置数据集中每个点的颜色。
下面演示了如何根据每个点的y值来设置其颜色：
我们将参数c设置成了一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射。
这些代码将y值较小的点显示为浅蓝色，并将y值较大的点显示为深蓝色，
"""
x_values = list(range(1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

# 设置图表标题并给坐标加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')

# 2.9自动保存图表
# 要让程序自动将图表保存到文件中，可将对plt.show()的调用替换为对plt.savefig()的调用：
# 第一个实参指定要以什么样的文件名保存图表，这个文件将存储到.py所在的目录中；
# 第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空白区域，可省略这个实参。
