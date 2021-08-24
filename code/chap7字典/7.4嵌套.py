# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/24 16:17
"""有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。
   你可以在列表中嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。"""
# 4.1字典列表
# 首先创建了三个字典，其中每个字典都表示一个外星人。
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
# 将这些字典都放到一个名为aliens的列表中
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 使用range()生成外星人
# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien in range(30):  # range()返回一系列数字，其唯一的用途是告诉Python我们要重复这个循环多少次。
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)
# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("......")
# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))

"""这些外星人都具有相同的特征，但在Python看来，每个外星人都是独立的，这让我们能够独立地修改每个外星人。 
   在什么情况下需要处理成群结队的外星人呢？想象一下，可能随着游戏的进行，有些外星人会变色且移动速度会加快。
   必要时，我们可以使用for循环和if语句来修改某些外星人的颜色。例如，要将前三个外星人修改为黄色的、速度为中等且值10个点，可以这样做："""
aliens = []
# 创建30个绿色的外星人
for alien in range(30):  # range()返回一系列数字，其唯一的用途是告诉Python我们要重复这个循环多少次。
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# 显示前五个外星人
for alien in aliens[0:5]:
    print(alien)
print("......")

"""可以进一步扩展这个循环，在其中添加一个elif 代码块，将黄色外星人改为移动速度快且值15个点的红色外星人，如下所示"""
print("----------------------------")
aliens = []
for alien in range(30):  # range()返回一系列数字，其唯一的用途是告诉Python我们要重复这个循环多少次。
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[0:10]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens:
    print(alien)
print("......")

# 4.2在字典中存储列表
"""有时候，需要将列表存储在字典中，而不是将字典存储在列表中。
   例如，你如何描述顾客点的比萨呢？如果使用列表，只能存储要添加的比萨配料；但如果使用字典，就不仅可在其中包含配料列表，
   还可包含其他有关比萨的描述。在下面的示例中，存储了比萨的两方面信息：外皮类型和配料列表。
   其中的配料列表是一个与键'toppings'相关联的值。要访问该列表，我们使用字典名和键'toppings'，
   就像访问字典中的其他值一样。这将返回一个配料列表，而不是单个值"""
# 存储所点pizza的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
# 概述所点的pizza
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

"""每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。"""
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(name + "'s favorite language is:")
    else:
        print(name + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

# 4.3在字典中存储字典
"""可在字典中嵌套字典，但这样做时，代码可能很快复杂起来。例如，如果有多个网站用户，每个都有独特的用户名，
   可在字典中将用户名作为键，然后将每位用户的信息存储在一个字典中，并将该字典作为与用户名相关联的值。
   在下面的程序中，对于每位用户，我们都存储了其三项信息：名、姓和居住地；
   为访问这些信息，我们遍历所有的用户名，并访问与每个用户名相关联的信息字典"""
print("--------4.3--------")
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
"""请注意，表示每位用户的字典的结构都相同，虽然Python并没有这样的要求，但这使得嵌套的字典处理起来更容易。
   倘若表示每位用户的字典都包含不同的键，for循环内部的代码将更复杂。"""

# 练习1.创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在每个字典中，包含宠物的类型及其主人的名字。
# 将这些字典存储在一个名为pets的列表中，再遍历该列表，并将宠物的所有信息都打印出来。
pet_0 = {'kind': 'cat', 'master': 'jack'}
pet_1 = {'kind': 'dog', 'master': 'eric'}
pet_2 = {'kind': 'turtle', 'master': 'jane'}
pets = [pet_0, pet_1, pet_2]
print(pets)
for pet in pets:
    print(pet['master'].title() + " have a cute " + pet['kind'])

# 练习2.创建一个名为favorite_places的字典。在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的1~3个地方。
# 为让这个练习更有趣些，可让一些朋友指出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
favorite_places = {
    'eric': ['france', 'england', 'china'],
    'jane': ['hong kong'],
    'john': ['russia', 'poland']
}
for name, places in favorite_places.items():
    if len(places) == 1:
        print(name.title() + "'s favorite place is:")
    else:
        print(name.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())

# 练习3.创建一个名为cities的字典，其中将三个城市名用作键；对于每座城市，都创建一个字典，
# 并在其中包含该城市所属的国家、人口约数以及一个有关该 城市的事实。在表示每座城市的字典中，
# 应包含country 、population 和fact等键。将每座城市的名字以及有关它们的信息都打印出来。
cities = {
    'lodon': {
        'country': 'england',
        'population': 150000000,
        'fact': 'Lodon is famous for its fog'
    },
    'beijing': {
        'country': 'china',
        'population': 10000000,
        'fact': 'BeiJing has a long history'
    },
    'paris': {
        'country': 'france',
        'population': 6000000,
        'fact': 'Paris is a romantic city'
    }
}
for city, city_info in cities.items():
    print("\nCity: " + city.title())
    Country = city_info['country']
    Population = city_info['population']
    fact = city_info['fact']
    print(city.title() + "ia a city of " + Country.title() + ", it has " + str(Population) + " people.\nIn fact, " + fact)

