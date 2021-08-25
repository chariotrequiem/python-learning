# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/25 10:12
"""鉴于函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。
   向函数传递实参的方式很多，可使用位置实参，这要求实参的顺序与形参的顺序相同；
   也可使用关键关实参，其中每个实参都由变量名和值组成；还可使用列表和字典。下面来依次介绍这些方式。"""
# 2.1位置实参
# 调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，最简单的关联方式是基于实参的顺序。这种关联方式被称为位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\n我有一只" + animal_type + "。")
    print("我的" + animal_type + "的名字是" + pet_name + "。")
describe_pet('猫', '球球')
# 2.1.1调用函数多次
describe_pet('狗', '欢欢')
# 2.1.2位置实参的顺序很重要，请确认函数调用中实参的顺序与函数定义中形参的顺序一致。

# 2.2关键字实参
"""关键字实参是传递给函数的名称——值对。直接在实参中将名称和值关联起来，因此向函数传递实参时不会混淆
   关键字实参让你无需考虑函数调用中的实参顺序，还清楚地指出了函数调用中各个值的用途。"""
# 注意：使用关键字实参时，务必准确地指定函数定义中的形参名。
describe_pet(animal_type='乌龟', pet_name='小惠')

# 2.3默认值
"""编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python将使用指定的实参值；
   否则，将使用形参的默认值。因此，给形参指定默认值后，可在函数调用中省略相应的实参。
   使用默认值可简化函数调用，还可清楚地指出函数的典型用法。"""
# 注意：使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。这让Python依然能够正确地解读位置实参。
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')

# 2.4等效的函数调用
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# 一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')
# 一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# 2.5避免实参错误
# 提供的实参多于或少于函数完成其工作所需的信息时，将出现实参不匹配错误。

# 练习1.编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。这个函数应打印一个句子，概要地说明T恤的尺码和字样。
def make_shirt(shirt_size, shirt_words):
    print("\nT恤的尺码为" + str(shirt_size) + ", 上面印有" + shirt_words + "的字样")
make_shirt(25, '中秋快乐')
make_shirt(shirt_size=36, shirt_words='水逆退散')

# 练习2.大号T恤
"""修改函数make_shirt()，使其在默认情况下制作一件印有字样“I love Python”的大号T恤。
   调用这个函数来制作如下T恤：一件印有默认字样的大号T恤、一件印有默认字样的中号T恤和一件印有其他字样的T恤（尺码无关紧要）"""
def make_shirt2(shirt_size='large', shirt_words='I love Python'):
    print("\nT恤的尺码为" + shirt_size + ", 上面印有" + shirt_words + "的字样")
make_shirt2()
make_shirt2(shirt_size='medium')
make_shirt2(shirt_words='Hello python')

# 练习3.城市
"""编写一个名为describe_city()的函数，它接受一座城市的名字以及该城市所属的国家。
   这个函数应打印一个简单的句子，如Reykjavik is in Iceland。给用于存储国家的形参指定默认值。
   为三座不同的城市调用这个函数，且其中至少有一座城市不属于默认国家。"""
def describe_city(city, country='China'):
    print(city + ' is in ' + country)
describe_city('Hong Kong')
describe_city('BeiJing')
describe_city('Paris', 'France')
