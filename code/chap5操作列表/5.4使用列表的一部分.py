# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/24 9:01
# 处理列表的部分元素——Python称之为切片
# 1.切片
"""要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数range()一样，Python在到达你指定的第二个索引前面的元素后停止。
   要输出列表中的前三个元素，需 要指定索引0~3，这将输出分别为0 、1 和2 的元素。"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# 也可以生成列表的任何子集，例如，如果要提取列表的第2~4个元素，可将起始索引指定为1 ，并将终止索引指定为4；
print(players[1:4])
# 如果没有指定第一个索引，Python将自动从列表开头开始;
print(players[:4])
# 要让切片终止于列表末尾，也可使用类似的语法。例如，如果要提取从第3个元素到列表末尾的所有元素，可将起始索引指定为2 ，并省略终止索引;
print(players[2:])
# 无论列表多长，这种语法都能够让你输出从特定位置到列表末尾的所有元素。本书前面说过，负数索引返回离列表末尾相应距离的元素，因此你可以输出列表末尾的任何切片。
# 例如，如果你要输出名单上的最后三名队员，可使用切片players[-3:];即使列表长度发生变化，也依然如此
print(players[-3:])

# 2.遍历切片
# 如果要遍历列表的部分元素，可在for循环中使用切片。
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# 3.复制列表
"""要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:] ）。
   这让Python创建一个始于第一个元素，终止于最后一个元素的切片，即复制整个列表。"""
# 注意：倘若我们只是简单地将my_foods赋给friend_foods，就不能得到两个列表。
My_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = My_foods[:]
My_foods.append('cannoli')
friend_foods.append('ice cream')
print('My favorite foods are: ')
print(My_foods)
print("\nMy friend's favorite foods are: ")
print(friend_foods)

# 练习1.选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
print('----------练习1.----------')
# 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
print("The first three items in the list are：")
print(My_foods[:3])
# 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
print("Three items from the middle of the list are：")
print(My_foods[1:4])
# 打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。
print("The last three items in the list are：")
print(My_foods[-3:])

# 练习2.在你为完成练习5-2而编写的程序中，创建比萨列表的副本，并将其存储到变量friend_pizzas 中，再完成如下任务。
print("----------练习2.----------")
my_pizzas = ['奥尔良披萨', '水果披萨', '香肠披萨']
friends_pizzas = my_pizzas[:]
# 在原来的比萨列表中添加一种比萨。
my_pizzas.append('榴莲披萨')
# 在列表friend_pizzas 中添加另一种比萨。
friends_pizzas.append('芝士披萨')
"""核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一个for循环来打印第一个列表；
   打印消息“My friend's favorite pizzas are:”，再使用一 个for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。"""
print("My favorite pizzas are: ")
for pizza in my_pizzas:
    print(pizza)
print("My friend's favorite pizzas are: ")
for pizza in friends_pizzas:
    print(pizza)
