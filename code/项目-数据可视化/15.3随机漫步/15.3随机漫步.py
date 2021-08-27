# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/27 19:07
"""
在本节中，我们将使用Python来生成随机漫步数据，再使用matplotlib以引人瞩目的方式将这些数据呈现出来。
随机漫步是这样行走得到的路径：每次行走都完全是随机的，没有明确的方向，结果是由一系列随机决策决定的。
你可以这样认为，随机漫步就是蚂蚁在晕头转向的情况下，每次都沿随机的方向前行所经过的路径。

在自然界、物理学、生物学、化学和经济领域，随机漫步都有其实际用途。
例如，漂浮在水滴上的花粉因不断受到水分子的挤压而在水面上移动。水滴中的分子运动是随机的，
因此花粉在水面上的运动路径犹如随机漫步。我们稍后将编写的代码模拟了现实世界的很多情形。
"""
# 3.1创建RandomWalk()类
"""
为模拟随机漫步，我们将创建一个名为RandomWalk 的类，它随机地选择前进方向。
这个类需要三个属性，其中一个是存储随机漫步次数的变量，其他两个是列表，分别存储随机漫步经过的每个点的x和y坐标。 

RandomWalk 类只包含两个方法：__init__()和fill_walk()，其中后者计算随机漫步经过的所有点。下面先来看看__init__() ，如下所示：
from random import choice

class RandomWalk:
    
    def __init__(self, num_points=5000):
        self.num_points = num_points
        
        # 所有随机漫步都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]
为做出随机决策，将所有可能的选择都存储在一个列表中，并在每次做决策时都使用choice()来决定使用哪种选择。
接下来，将随机漫步包含的默认点数设置为5000，这大到足以生成有趣的模式，同时又足够小，可确保能够快速地模拟随机漫步。
然后，创建了两个用于存储x和y值的列表，并让每次漫步都从点(0, 0)出发。
"""
# 3.2选择方向
"""
我们将使用fill_walk()来生成漫步包含的点，并决定每次漫步的方向，如下所示:
    def fill_walk(self):
        #计算随机漫步包含的所有点
        
        # 不断漫步，直到列表到达指定的长度
        while len(self.x_values) < self.num_points:     
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_distance * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_distance
            
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
                
            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
我们建立了一个循环，这个循环不断运行，直到漫步包含所需数量的点。
这个方法的主要部分告诉Python如何模拟四种漫步决定：向右走还是向左走？沿指定的方向走多远？向上走还是向下走？沿选定的方向走多远？
我们使用choice([1, -1])给x_direction选择一个值，结果要么是表示向右走的1，要么是表示向左走的-1。接下来，choice([0, 1, 2, 3, 4])
随机地选择一个0~4之间的整数，告诉Python沿指定的方向走多远（x_distance）。（通过包含0，我们不仅能够沿两个轴移动，还能够沿y 轴移动。） 

我们将移动方向乘以移动距离，以确定沿x和y轴移动的距离。如果x_step为正，将向右移动，为负将向左移动，而为零将垂直移动；
如果y_step 为正，就意味着向上移动，为负意味着向下移动，而为零意味着水平移动。
如果x_step 和y_step 都为零，则意味着原地踏步，我们拒绝这样的情况，接着执行下一次循环。 

为获取漫步中下一个点的x值，我们将x_step与x_values中的最后一个值相加，对于y值也做相同的处理。
获得下一个点的x值和y值后，我们将它们分别附加到列表x_values和y_values的末尾。
"""

# 3.3绘制随机漫步图
"""
下面的代码将随机漫步的所有点都绘制出来：
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 创建一个RandomWalk实例，并将其包含的点都绘制出来
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()

首先导入了模块pyplot和RandomWalk类，然后创建了一个RandomWalk实例，并将其存储到rw中，再调用fill_walk()。
将随机漫步包含的x和y值传递给scatter()，并选择了合适的点尺寸。
"""

# 3.4模拟多次随机漫步
"""
每次随机漫步都不同，因此探索可能生成的各种模式很有趣。
要在不多次运行程序的情况下使用前面的代码模拟多次随机漫步，一种办法是将这些代码放在一个while循环中，如下所示：
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n)): ")
    if keep_running == 'n':
        break
        
这些代码模拟一次随机漫步，在matplotlib查看器中显示结果，再在不关闭查看器的情况下暂停。
如果你关闭查看器，程序将询问你是否要再模拟一次随机漫步。如果你输入y，可模拟多次随机漫步：
这些随机漫步都在起点附近进行，大多沿特定方向偏离起点，漫步点分布不均匀等。要结束程序，请输入n 。
"""

# 3.5设置随机漫步图的样式
"""
在本节中，我们将定制图表，以突出每次漫步的重要特征，并让分散注意力的元素不那么显眼。
为此，我们确定要突出的元素，如漫步的起点、终点和经过的路径。接下来确定 要使其不那么显眼的元素，如刻度标记和标签。
最终的结果是简单的可视化表示，清楚地指出了每次漫步经过的路径。
"""
# 3.6给点着色
"""
我们将使用颜色映射来指出漫步中各点的先后顺序，并删除每个点的黑色轮廓，让它们的颜色更明显。
为根据漫步中各点的先后顺序进行着色，我们传递参数c，并将其设置为 一个列表，其中包含各点的先后顺序。
由于这些点是按顺序绘制的，因此给参数c指定的列表只需包含数字1~5000，如下所示：
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n)): ")
    if keep_running == 'n':
        break
        
使用range()生成了一个数字列表，其中包含的数字个数与漫步包含的点数相同。
接下来，将这个列表存储在point_numbers中，以便后面使用它来设置每个漫步点的颜色。
将参数c设置为point_numbers，指定使用颜色映射Blues，并传递实参edgecolor=none以删除每个点周围的轮廓。
最终的随机漫步图从浅蓝色渐变为深蓝色
"""

# 3.7重新绘制起点和终点
"""
除了给随机漫步的各个点着色，以指出它们的先后顺序外，如果还能呈现随机漫步的起点和终点就更好了。
为此，可在绘制随机漫步图后重新绘制起点和终点。我们让起点和终点变得更大，并显示为不同的颜色，以突出它们，如下所示：
--snip--
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.show()
    --snip--
为突出起点，我们使用绿色绘制点(0, 0)，并使其比其他点大（s=100 ）。
为突出终点，我们在漫步包含的最后一个x和y值处绘制一个点，将其颜色设置为红色，并将尺寸设置为100。
请务必将这些代码放在调用plt.show()的代码前面，确保在其他点的上面绘制起点和终点。
"""

# 3.8隐藏坐标轴
"""
下面来隐藏这个图表中的坐标轴，以免我们注意的是坐标轴而不是随机漫步路径。
要隐藏坐标轴，可使用如下代码：
     plt.gca().get_xaxis().set_visible(False)
     plt.gca().get_yaxis().set_visible(False)
"""

# 3.9增加点数
"""
下面来增加点数，以提供更多的数据。为此，我们在创建RandomWalk实例时增大num_points的值，并在绘图时调整每个点的大小，
如下所示：

这个示例模拟了一次包含50 000个点的随机漫步（以模拟现实情况），并将每个点的大小都设置为1。
最终的随机漫步图更纤细，犹如云朵。
"""

# 3.10调整尺寸以适合屏幕
"""
图表适合屏幕大小时，更能有效地将数据中的规律呈现出来。为让绘图窗口更适合屏幕大小，可像下面这样调整matplotlib输出的尺寸：
# 设置绘图窗口的尺寸
    plt.figure(figsize=(16, 9))
函数figure()用于指定图表的宽度、高度、分辨率和背景色。你需要给形参figsize指定一个元组，向matplotlib指出绘图窗口的尺寸，单位为英寸。

Python假定屏幕分辨率为80像素/英寸，如果上述代码指定的图表尺寸不合适，可根据需要调整其中的数字。
如果你知道自己的系统的分辨率，可使用形参dpi向figure()传递该分辨率，以有效地利用可用的屏幕空间，如下所示：
plt.figure(dpi=128, figsize=(10, 6))
"""
