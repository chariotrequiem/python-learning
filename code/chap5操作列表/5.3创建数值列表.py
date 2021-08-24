# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/23 22:37

# 1.使用函数range()
# python函数range()能够轻松地生成一系列的数字
# 函数range()让Python从你指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出不包含第二个值（这里为5）。
for value in range(1, 5):
    print(value)
# 要打印数字1-5，需要使用range(1,6)
for value in range(1, 6):
    print(value)

# 2.使用range()创建数字列表
# 要创建数字列表，可使用函数list()将range()的结果直接转换为列表。如果将range()作为list()的参数，输出将为一个数字列表。
numbers = list(range(1, 6))
print(numbers)
# 使用range()函数时，还可以指定步长
even_numbers = list(range(2, 11, 2))
print(even_numbers)
# 使用函数range()几乎能够创建任何需要的数字集，例如，如何创建一个列表，其中包含前10个整数(即1~10)的平方
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)
# 也可以如下
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# 3.对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(digits))
print(max(digits))
print(sum(digits))
print(len(digits))

# 4.列表解析
# 列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素。
"""要使用这种语法，首先指定一个描述性的列表名，如squares;
   然后，指定一个左方括号，并定义一个表达式，用于生成你要存储到列表中的值。
   在这个示例中，表达式 为value**2 ，它计算平方值。接下来，编写一个for 循环，用于给表达式提供值，再加上右方括号。
   在这个示例中，for 循环为for value in range(1,11) ，它将值 1~10提供给表达式value**2。请注意，这里的for语句末尾没有冒号。"""
squares = [value**2 for value in range(1, 11)]
print(squares)

# 练习1.使用一个for循环打印数字1~20（含）。
print('----------练习1----------')
for value in range(1, 21):
    print(value)
# 练习2.创建一个列表，其中包含数字1~1 000 000，再使用一个for循环将这些数字打印出来（如果输出的时间太长，按Ctrl+ C停止输出，或关闭输出窗口）。
print('----------练习2----------')
for value in range(1, 1000001):
    print(value)
# 练习3.创建一个列表，其中包含数字1~1 000 000，再使用min()和max()核实该列表确实是从1开始，到1 000 000结束的。
# 另外，对这个列表 调用函数sum()，看看Python将一百万个数字相加需要多长时间。
print('----------练习3----------')
values = [value for value in range(1, 1000001)]
print(min(values))
print(max(values))
print(sum(values))
# 练习4.通过给函数range()指定第三个参数来创建一个列表，其中包含1~20的奇数;再使用一个for 循环将这些数字都打印出来。
print('----------练习4----------')
values = [value for value in range(1, 21, 2)]
for value in values:
    print(value)
# 练习5.创建一个列表，其中包含3~30内能被3整除的数字；再使用一个for 循环将这个列表中的数字都打印出来。
print('----------练习5----------')
values = [value for value in range(3, 31, 3)]
for value in values:
    print(value)
# 练习6.将同一个数字乘三次称为立方。例如，在Python中，2的立方用2**3 表示。
# 请创建一个列表，其中包含前10个整数（即1~10）的立方，再使用一个for 循 环将这些立方数都打印出来。
print('----------练习6----------')
values = [value**3 for value in range(1, 11)]
for value in values:
    print(value)
# 练习7.使用列表解析生成一个列表，其中包含前10个整数的立方。
print('----------练习7----------')
numbers = [number**3 for number in range(1, 11)]
print(numbers)