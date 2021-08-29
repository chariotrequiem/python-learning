# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/29 14:17
"""
要在文本文件中存储数据，最简单的方式是将数据作为一系列以逗号分隔的值（CSV）写入文件。
这样的文件称为CSV文件。例如，下面是一行CSV格式的天气数据：
2014-1-5,61,44,26,18,7,-1,56,30,9,30.34,30.27,30.15,,,,10,4,,0.00,0,,195
这是阿拉斯加锡特卡2014年1月5日的天气数据，其中包含当天的最高气温和最低气温，还有众多其他数据。
CSV文件对人来说阅读起来比较麻烦，但程序可轻松地提取并处理其中的值，这有助于加快数据分析过程。
我们将首先处理少量锡特卡的CSV格式的天气数据，这些数据可在本书的配套资源（https://www.nostarch.com/pythoncrashcourse/）中找到。
请将文件sitka_weather_07-2014.csv复制到存储本章程序的文件夹中（下载本书的配套资源后，你就有了这个项目所需的所有文件）。
注意这个项目使用的天气数据是从http://www.wunderground.com/history/下载而来的。
"""
# 1.1分析CSV文件
# csv模块包含在python标准库中，可用于分析CSV文件中的数据行，让我们能够快速提取感性趣的值。下面先来查看这个文件的第一行，其中包含一系列有关数据的描述：
"""
import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
导入模块csv后，我们将要使用的文件的名称存储在filename中。接下来，我们打开这个文件，并将结果文件对象存储在f中。
然后，我们调用csv.reader()，并将前面存储的文件对象作为实参传递给它，从而创建一个与该文件相关联的阅读器（reader ）对象。
我们将这个阅读器对象存储在reader中。 

模块csv包含函数next()，调用它并将阅读器对象传递给它时，它将返回文件中的下一行。
在前面的代码中，我们只调用了next()一次，因此得到的是文件的第一行，其中包含文件头。
我们将返回的数据存储在header_row中。正如你看到的，header_row包含与天气相关的文件头，指出了每行都包含哪些数据：

reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中。
文件头AKDT表示阿拉斯加时间（Alaska Daylight Time），其位置表明每行的第一个值都是日期或时间。
文件头Max TemperatureF指出每行的第二个值都是当天的最高华氏温度。可通过阅读其他的文件头来确定文件包含的信息类型。 

注意: 文件头的格式并非总是一致的，空格和单位可能出现在奇怪的地方。这在原始数据文件中很常见，但不会带来任何问题。
"""

# 1.2打印文件骰及其位置
# 为了让文件头数据更容易理解，将列表中的每个文件头及其位置都打印出来
"""
import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
我们对列表调用了enumerate()来获取每个元素的索引及其值。
"""

# 1.3提取并读取数据
"""
知道需要哪些列中的数据后，我们来读取一些数据。首先读取每天的最高气温：

创建了一个名为highs的空列表，再遍历文件中余下的各行。
阅读器对象从其停留的地方继续往下读取CSV文件，每次都自动返回当前所处位置的下一行。
由于我们已经读取了文件头行，这个循环将从第二行开始——从这行开始包含的是实际数据。
每次执行该循环时，我们都将第2列的数据附加到highs末尾。
import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        highs.append(row[1])

    print(highs)
    
我们提取了每天的最高气温，并将它们作为字符串整洁地存储在一个列表中。 
下面使用int() 将这些字符串转换为数字，让matplotlib能够读取它们：
 for row in reader:
        high = int(row[1])
        highs.append(high)
"""

# 1.4绘制气温图表
"""
为了可视化这些气温数据，我们首先使用matplotlib创建一个显示每日最高气温的简单图形，如下所示：
import csv
from matplotlib import pyplot as plt


filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(highs, c='red')

# 设置图形的格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
"""
# 1.5模块datetime()
"""
下面在图表中添加日期，使其更有用。在天气数据文件中，第一个日期在第二行
读取该数据时，获得的是一个字符串，因为我们需要想办法将字符串'2014-7-1' 转换为一个表示相应日期的对象。
为创建一个表示2014年7月1日的对象，可使用模块datetime中的方法strptime()。我们在终端会话中看看strptime()的工作原理：
from datetime import datetime
first_date = datetime.strptime('2014-7-1', '%Y-%m-%d') 
print(first_date) 

2014-07-01 00:00:00
我们首先导入了模块datetime中的datetime类，然后调用方法strptime()，并将包含所需日期的字符串作为第一个实参。
第二个实参告诉Python如何设置日期的格式。在这个示例中，'%Y-'让Python将字符串中第一个连字符前面的部分视为四位的年份；
'%m-'让Python将第二个连字符前面的部分视为表示月份的数字；而'%d'让Python将字符串的最后一部分视为月份中的一天（1~31）
方法strptime()可接受各种实参，并根据它们来决定如何解读日期。下面列出了其中一些这样的实参：
实参             含义
%A           星期的名称，如Monday 
%B           月份名，如January 
%m           用数字表示的月份（01~12） 
%d           用数字表示月份中的一天（01~31）
%Y           四位的年份，如2015 
%y           两位的年份，如15 
%H           24小时制的小时数（00~23） 
%I           12小时制的小时数（01~12） 
%p           am或pm 
%M           分钟数（00~59） 
%S           秒数（00~61）
"""

# 1.6在图标中添加日期
"""
知道如何处理CSV文件中的日期后，就可对气温图形进行改进了，即提取日期和最高气温，并将它们传递给plot() ，如下所示：
import csv
from datetime import datetime
from matplotlib import pyplot as plt

# 从文件中获取日期和最高气温
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red')

# 设置图形的格式
plt.title("Daily high temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
我们创建了两个空列表，用于存储从文件中提取的日期和最高气温。然后，将包含日期信息的数据（row[0] ）转换为datetime对象，
并将其附加到列表dates末尾。将日期和最高气温值传递给plot()。调用了fig.autofmt_xdate()来绘制斜的日期标签，以免它们彼此重叠。
"""

# 1.7涵盖更长的时间
"""
设置好图表后，我们来添加更多的数据，以成一幅更复杂的锡特卡天气图。
将文件sitka_weather_2014.csv复制到存储本章程序的文件夹中，该文件包含Weather Underground提供 的整年的锡特卡天气数据。 
现在可以创建覆盖整年的天气图了：
--snip--
# 从文件中获取日期和最高气温
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    --snip--
    # 设置图形的格式
    plt.title("Daily high temperatures - 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    --snip--
"""

# 1.8再绘制一个数据系列
"""
我们可以在其中再添加最低气温数据，使其更有用。为此，需要从数据文件中提取最低气温，并将它们添加到图表中，如下所示：

"""

# 1.9给图标区域着色
"""
添加两个数据系列后，我们就可以了解每天的气温范围了。
下面来给这个图表做最后的修饰，通过着色来呈现每天的气温范围。
为此，我们将使用方法fill_between()，它接受一个x值系列和两个y值系列，并填充两个y值系列之间的空间：
--snip-- 
# 根据数据绘制图形 
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5) 
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1) 
--snip--
实参alpha指定颜色的透明度。Alpha值为0表示完全透明，1（默认设置）表示完全不透明。
通过将alpha设置为0.5，可让红色和蓝色折线的颜色看起来更浅。 
我们向fill_between()传递了一个x值系列：列表dates ，还传递了两个y值系列：highs和lows。
实参facecolor指定了填充区域的颜色，我们还将alpha设置成了较小的值0.1，让填充区域将两个数据系列连接起来的同时不分散观察者的注意力。
"""

# 1.10错误检查
"""
我们应该能够使用有关任何地方的天气数据来运行highs_lows.py中的代码，但有些气象站会偶尔出现故障，未能收集部分或全部其应该收集的数据。
缺失数据可能会引发异常，如果不妥善地处理，还可能导致程序崩溃。 

例如，我们来看看生成加利福尼亚死亡谷的气温图时出现的情况。
将文件death_valley_2014.csv复制到本章程序所在的文件夹，再修改highs_lows.py，使其生成死亡谷的气温图：
其中没有记录2014年2月16日的数据，表示最高温度的字符串为空。
为解决这种问题，我们在从CSV文件中读取值时执行错误检查代码，对分析数据集时可能出现的异常进行处理，如下所示：
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates, high, and low temperatures from file.
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
对于每一行，我们都尝试从中提取日期、最高气温和最低气温。
只要缺失其中一项数据，Python就会引发ValueError异常，而我们可这样处理：打印一条错误消息，指出缺失数据的日期。
打印错误消息后，循环将接着处理下一行。如果获取特定日期的所有数据时没有发生错误，将运行else代码块，并将数据附加到相应列表的末尾。
鉴于我们绘图时使用的是有关另一个地方的信息，我们修改了标题，在图表中指出了这个地方。
"""