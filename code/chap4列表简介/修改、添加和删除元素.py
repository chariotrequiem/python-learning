# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/23 9:32
# 创建的大多数列表都将是动态的，这意味着列表创建后，将随着程序的运行增删元素。
# 1.修改列表元素
# 修改列表元素的语法与访问列表元素的语法类似。要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# 2.在列表中添加元素
# 2.1在列表末尾添加元素
# 在列表中添加新元素时，最简单的方式是将元素附加到列表末尾。给列表附加元素时，它将添加到列表末尾。
motors = ['honda', 'yamaha', 'suzuki']
print(motors)
motors.append('ducati')
print(motors)
# append()向列表末尾添加元素
names = []
names.append('mary')
names.append('jack')
names.append('henry')
print(names)

# 2.2在列表中插入元素
# 使用方法insert()可在列表的任何位置添加新元素。为此，需要指定新元素的索引和值。
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.insert(0, 'ducati')
print(motorcycles)

# 3.从列表中删除元素
# 3.1使用del语句删除元素，如果知道要删除的元素在列表中的位置，可使用del语句。
# 使用del可删除任何位置处的列表元素，条件是知道其索引。
# 使用del语句将值从列表中删除后，就无法再访问它了。
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# 3.2使用方法pop()删除元素
# 每当使用pop()时，被弹出的元素就不再在列表中了
# 方法pop()可删除列表末尾的元素，并让你能够接着使用它。
# 术语弹出（pop）源自这样的类比：列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# 3.3弹出列表中任何位置处的元素
# 事实上，可以使用pop()来删除列表中任何位置的元素，只需在括号中指定要删除的元素的索引即可。
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print('The first motorcycles I owned was a ' + first_owned.title() + '.')

# 关于del()和pop()的选择：如果你要从列表中删除一个元素，且不再以任何方式使用它，就使用del 语句；如果你要在删除元 素后还能继续使用它，就使用方法pop() 。

# 3.4根据值删除元素
# 有时候不知道要从列表中删除的值所处的位置。如果只知道要删除的元素的值，可使用方法remove()
# 方法remove()只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值。
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)
# 使用remove()从列表中删除元素时，也可以接着使用它的值
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')

'''练习1.如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？
   请创建一个列表，其中包含至少3个你想邀请的人；然后，使用 这个列表打印消息，邀请这些人来与你共进晚餐。'''
print('-------------练习1----------')
names = ['爱因斯坦', '富兰克林', '特斯拉']
message1 = '尊敬的'
message2 = '先生，请您本周六晚9点前来赴宴'
print(message1 + names[0] + message2)
print(message1 + names[1] + message2)
print(message1 + names[2] + message2)
'''练习2.修改嘉宾名单：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。 
   以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。 
   修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。 
   再次打印一系列消息，向名单中的每位嘉宾发出邀请'''
print('-------------练习2----------')
print(message1 + names[0] + '先生本周六晚九点有事，无法前来赴宴')
names[0] = '爱迪生'
print(message1 + names[0] + message2)
print(message1 + names[1] + message2)
print(message1 + names[2] + message2)
'''练习3.添加嘉宾：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。 
   以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print 语句，指出你找到了一个更大的餐桌。 
   使用insert() 将一位新嘉宾添加到名单开头。 使用insert() 将另一位新嘉宾添加到名单中间。 
   使用append() 将最后一位新嘉宾添加到名单末尾。 打印一系列消息，向名单中的每位嘉宾发出邀请。'''
print('-------------练习3----------')
print('我们找到了一张更大的餐桌，可以再邀请三位嘉宾')
names.insert(0, '居里夫人')
names.insert(2, '玻尔')
names.append('奥巴马')
print(message1 + names[0] + message2)
print(message1 + names[1] + message2)
print(message1 + names[2] + message2)
print(message1 + names[3] + message2)
print(message1 + names[4] + message2)
print(message1 + names[5] + message2)
'''练习4.缩减名单：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。 
   以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。 
   使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。 
   对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。 
   使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。'''
print('-------------练习4----------')
message3 = '先生，我们很抱歉，由于某些原因本周六晚无法邀请您共进晚餐'
print('我们很抱歉通知您新购买的餐桌无法及时送达，因此只能邀请两位嘉宾')
popped_names = names.pop()
print(message1 + popped_names + message3)
popped_names = names.pop()
print(message1 + popped_names + message3)
popped_names = names.pop()
print(message1 + popped_names + message3)
popped_names = names.pop()
print(message1 + popped_names + message3)
message4 = '先生/女士，您仍在本周六的晚宴邀请行列'
print(message1 + names[0] + message4)
print(message1 + names[1] + message4)

del names[0]
print(names)
del names[0]
print(names)