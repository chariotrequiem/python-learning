# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/23 22:18
# Python根据缩进来判断代码行与前一个代码行的关系。
# 当你始编写必须正确缩进的代码时，需要注意一些常见的缩进错误。

# 1.忘记缩进
# 对于位于for语句后面且属于循环组成部分的代码行，一定要缩进。

# 2.忘记缩进额外的代码行
# 有时候，循环能够运行而不会报告错误，但结果可能会出乎意料。试图在循环中执行多项任务，却忘记缩进其中的一些代码行时，就会出现这种情况。

# 3.不必要的缩进
# 如果不小心缩进了无需缩进的代码行，Python将指出这一点

# 4.循环后不必要的缩进
# 如果你不小心缩进了应在循环结束后执行的代码，这些代码将针对每个列表元素重复执行。

# 5.遗漏了冒号
# for语句末尾的冒号告诉Python，下一行是循环的第一行。如果你不小心遗漏了冒号,将导致语法错误。

# 练习1.想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用for 循环将每种比萨的名称都打印出来。
print('----------练习1----------')
pizzas = ['奥尔良披萨', '水果披萨', '香肠披萨']
for pizza in pizzas:
    print(pizza)
# 修改这个for 循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种比萨，都显示一行输出，如“I like pepperoni pizza”。
    print('I like ' + pizza)
# 在程序末尾添加一行代码，它不在for循环中，指出你有多喜欢比萨。输出应包含针对每种比萨的消息，还有一个总结性句子，如“I really love pizza!”。
print('I really like pizza!')

# 练习2.动物：想出至少三种有共同特征的动物，将这些动物的名称存储在一个列表中，再使用for循环将每种动物的名称都打印出来。
print('----------练习2----------')
animals = ['cat', 'dog', 'turtle']
for animal in animals:
    print(animal)
# 修改这个程序，使其针对每种动物都打印一个句子，如“A dog would make a great pet”。
    print('A ' + animal + ' would make a great pet!')
# 在程序末尾添加一行代码，指出这些动物的共同之处，如打印诸如“Any of these animals would make a great pet!”这样的句子。
print('Any of these animals would make a great pet!')