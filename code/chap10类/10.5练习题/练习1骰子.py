# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 10:24
"""
模块random包含以各种方式生成随机数的函数，其中的randint()返回一个位于指定范围内的整数，例如，下面的代码返回一个1~6内的整数：
from random import randint
x = randint(1, 6)

请创建一个Die类，它包含一个名为sides的属性，该属性的默认值为6。
编写一个名为roll_die()的方法，它打印位于1和骰子面数之间的随机数。创建一个6面的骰子，再掷10次。
创建一个10面的骰子和一个20面的骰子，并将它们都掷10次。
"""
from random import randint


class Die:
    def __init__(self, sides=6):
        """初始化投资的面数"""
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print("骰出的点数为：" + str(x))


die_0 = Die()
x = 0
while True:
    die_0.roll_die()
    x += 1
    if x == 10:
        break

print("----------10面骰子----------")
die_1 = Die(10)
y = 0
while True:
    die_1.roll_die()
    y += 1
    if y == 10:
        break

print("----------20面骰子----------")
die_2 = Die(20)
i = 0
while True:
    die_2.roll_die()
    i += 1
    if i == 10:
        break

