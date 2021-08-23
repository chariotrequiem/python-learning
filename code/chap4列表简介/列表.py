# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/23 9:16
# 列表由一系列按特定顺序排列的元素组成。
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# 访问列表元素
# 列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置或索引告诉Python即可。要访问列表元素，可指出列表的名称，再指出元素的索引，并将其放在方括号内。
print(bicycles[0])
print(bicycles[0].title())
# 在Python中，第一个列表元素的索引为0，而不是1。
print(bicycles[1])
# Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1 ，可让Python返回最后一个列表元素：
print(bicycles[-1])
'''这种语法很有用，因为你经常需要在不知道列表长度的情况下访问最后的元素。
这种约定也适用于其他负数索引，例如，索引-2 返回倒数第 二个列表元素，索引-3 返回倒数第三个列表元素，以此类推。'''
print(bicycles[-3])
message = 'My first bicycle was a ' + bicycles[0].title() + '.'
print(message)

# 练习1.姓名：将一些朋友的姓名存储在一个列表中，并将其命名为names 。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
names = ['jack', 'jones', 'richard', 'mary', 'henry']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
# 练习2.继续使用上面的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
message = 'Good morning, '
print(message + names[0].title() + '!')
print(message + names[1].title() + '!')
print(message + names[2].title() + '!')
print(message + names[3].title() + '!')
print(message + names[4].title() + '!')
# 练习3.想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，如“I would like to own a Honda motorcycle”。
ways = ['bike', 'car', 'motor', 'helicopter']
message = 'I would like to own a '
print(message + ways[0] + '!')
print(message + ways[1] + '!')
print(message + ways[2] + '!')
print(message + ways[3] + '!')