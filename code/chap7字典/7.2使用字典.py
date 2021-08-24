# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/24 14:43
"""在Python中，字典是一系列键----值对。每个键都与一个值相关联，你可以使用键来访问与之相关联的值。
   与键相关联的值可以是数字、字符串、列表乃至字典。事实上，可将任何Python对象用作字典中的值。
   在Python中，字典用放在花括号{}中的一系列键—值对表示
   键—值对是两个相关联的值。指定键时，Python将返回与之相关联的值。
   键和值之间用冒号分隔，而键—值对之间用逗号分隔。在字典中，你想存储多少个键—值对都可以。"""
# 2.1访问字典中的值
# 要获取与键相关联的值，可依次指定字典名和放在方括号内的键
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# 2.2添加键--值对
# 字典是一种动态结构，可随时在其中添加键—值对。要添加键—值对，可依次指定字典名、用方括号括起的键和相关联的值。
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_positions'] = 0
alien_0['y_positions'] = 25
# 注意，键—值对的排列顺序与添加顺序不同。Python不关心键—值对的添加顺序，而只关心键和值之间的关联关系。
print(alien_0)

# 2.3创建一个空字典
# 有时候，在空字典中添加键—值对是为了方便，而有时候必须这样做。为此，可先使用一对空的花括号定义一个字典，再分行添加各个键—值对。
alien_1 = {}
pass  # 添加pass防止创建空字典报错
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

# 2.4修改字典中的字
# 要修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关联的新值。
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# 向右移动外星人
# 根据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人速度一定很快
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))

alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人速度一定很快
    x_increment = 3
# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']))

# 2.5删除键---值对
# 对于字典中不再需要的信息，可使用del语句将相应的键—值对彻底删除。使用del语句时，必须指定字典名和要删除的键。
# 注意：删除的键—值对永远消失了
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# 2.6由类似对象组成的字典
# 字典可以存储一个对象（游戏中的一个外星人）的多种信息，但也可以使用字典来存储众多对象的同一种信息
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
    }
print("Srash's favorite language is " + favorite_languages['sarah'].title() + ".")

# 练习1.使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。
# 该字典应包含键first_name、last_name、age和city。将存储在该字典中的每项信息都打印出来。
print("----------练习1----------")
people = {
    'fist_name': 'lee',
    'last_name': 'bruce',
    'age': '28',
    'city': 'hong kong'
    }
print("His first name is " + people['fist_name'].title() + ".")
print("His last name is " + people['last_name'].title() + ".")
print("He is " + str(people['age']) + " years old.")
print("He lives in " + people['city'].title() + ".")

# 练习2.使用一个字典来存储一些人喜欢的数字。请想出5个人的名字，并将这些名字用作字典中的键；
# 想出每个人喜欢的一个数字，并将这些数字作为值存 储在字典中。打印每个人的名字和喜欢的数字。
print("------------练习2----------")
dic = {'jack': 25, 'eric': 20, 'john': 15, 'mary': 18, 'lucian': 99}
print("Jack's favorite number is " + str(dic['jack']) + ".")
print("Eric's favorite number is " + str(dic['eric']) + ".")
print("John's favorite number is " + str(dic['john']) + ".")
print("Mary's favorite number is " + str(dic['mary']) + ".")
print("Lucian's favorite number is " + str(dic['lucian']) + ".")