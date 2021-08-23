# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/23 10:44
"""在创建的列表中，元素的排列顺序常常是无法预测的，因为你并非总能控制用户提供数据的顺序。
   这虽然在大多数情况下都是不可避免的，但你经常需要以特定的顺序呈现信息。
   有时候，你希望保留列表元素最初的排列顺序，而有时候又需要调整排列顺序。
   Python提供了很多组织列表的方式，可根据具体情况选用。"""
# 1.使用sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
# 有一个汽车列表，并要让其中的汽车按字母顺序排列。
cars.sort()
# sort()永久性地修改了列表元素的排列顺序。现在，汽车是按字母顺序排列的，再也无法恢复到原来的排列顺序：
print(cars)
# 也可以按与字母顺序相反的顺序排列列表元素，为此，只需向sort()方法传递参数reverse=True即可。
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
# 同样，对列表元素排列顺序的修改是永久性的。
print(cars)
# 2.使用函数sorted()对列表进行临时排序
'''要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数sorted()。
   函数sorted() 让你能够按特定顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。'''
print('----------sorted()函数----------')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('原列表如下：')
print(cars)
print('\n排序列表如下：')
print(sorted(cars))
print('\n原列表如下：')
print(cars)

"""注意: 调用函数sorted()后，列表元素的排列顺序并没有变。如果要按与字母顺序相反的顺序显示列表，也可向函数sorted()传递参数reverse=True 。
   注意：在并非所有的值都是小写时，按字母顺序排列列表要复杂些。
   决定排列顺序时，有多种解读大写字母的方式，要指定准确的排列顺序，可能比我们这里所做的 要复杂。然而，大多数排序方式都基于本节介绍的知识。"""
# 3.倒着打印列表
# 要反转列表元素的排列顺序，可使用方法reverse()。reverse()不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序
# reverse()会永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，为此只需对列表再次调用reverse()即可。
print('\n----------reverse()函数----------')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
# 4.确定列表长度
# 使用函数len()可快速获悉列表的长度。
print('\n----------reverse()函数----------')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(len(cars))

# 练习1.想出至少5个渴望去旅游的地方
'''1.1将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。 '''
print('----------练习1----------')
#  1.2按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。
places = ['xian', 'chongqing', 'hangzhou', 'shenzhen', 'sanya', 'dalian']
print(places)
# 1.3使用sorted() 按字母顺序打印这个列表，同时不要修改它。
print(sorted(places))
#  1.4再次打印该列表，核实排列顺序未变。
print(places)
# 1.5使用sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
print(sorted(places, reverse=True))
# 1.6再次打印该列表，核实排列顺序未变。
print(places)
# 1.7使用reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
places.reverse()
print(places)
# 1.8使用reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
places.reverse()
print(places)
# 1.9使用sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
places.sort()
print(places)
# 1.10使用sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。
places.sort(reverse=True)
print(places)

# 练习2.在上节练习1-4编写的程序之一中，使用len() 打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
print('----------练习2----------')
names = ['爱因斯坦', '富兰克林', '特斯拉']
message1 = '尊敬的'
message2 = '先生，请您本周六晚9点前来赴宴'
print(message1 + names[0] + message2)
print(message1 + names[1] + message2)
print(message1 + names[2] + message2)
print('本次晚宴共邀请' + str(len(names)) + '位名流赴宴')

# 练习3.尝试使用各种函数：
'''想想可存储到列表中的东西，如山岳、河流、国家、城市、语言或你喜欢的任何东西。
   编写一个程序，在其中创建一个包含这些元素的列表，然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。'''
print('----------练习4----------')
countries = ['china', 'france', 'america', 'england', 'russia']
print('I come from ' + countries[0].upper() + '!')
# 添加元素
countries.append('germmy')
print(countries)
countries.insert(3, 'India')
print(countries)
# 删除元素
countries.pop()
print(countries)
del countries[3]
print(countries)
# 排序
print(sorted(countries))
print(countries)
countries.sort()
print(countries)
# 逆序
countries.reverse()
print(countries)
length = len(countries)
print('联合国常任理事国共有' + str(length) + '个。')

