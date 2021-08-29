# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/28 15:46
from new_die import Die
import pygal

# 创建一个D6
die_1 = Die()
die_2 = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# 分析结果

max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling three D6 50000 times."
hist.x_labels = list(range(1, 37))
hist.x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6*D6', frequencies)
hist.render_to_file('times_visual.svg')
