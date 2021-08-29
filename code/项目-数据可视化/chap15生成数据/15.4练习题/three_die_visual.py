# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/28 15:44
from new_die import Die
import pygal

# 创建一个D6
die_1 = Die()
die_2 = Die()
die_3 = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = [x for x in range(3, 19)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('three_visual.svg')