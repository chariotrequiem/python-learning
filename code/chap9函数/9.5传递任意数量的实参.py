# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/25 15:37
"""
有时候，你预先不知道函数需要接受多少个实参，好在Python允许函数从调用语句中收集任意数量的实参。
例如，来看一个制作比萨的函数，它需要接受很多配料，但你无法预先确定顾客要多少种配料。下面的函数只有一个形参*toppings ，
但不管调用语句提供了多少实参，这个形参都将它们统统收入囊中：

形参名*toppings中的星号让Python创建一个名为toppings 的空元组，并将收到的所有值都封装到这个元组中。
函数体内的print 语句通过生成输出来证明Python能够处理使用一个值调用函数的情形，也能处理使用三个值来调用函数的情形。
它以类似的方式处理不同的调用，注意，Python将实参封装到一个元组中，即便函数只收到一个值也如此：
"""
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 现在，可以将这条print语句替换为一个循环，对配料列表进行遍历，并对顾客点的比萨进行描述
def make_pizza(*toppings):
    """概述要制作的比萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 5.1结合使用 位置实参和任意数量实参
"""
如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。
Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
"""
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 5.2使用任意数量的关键字实参
"""
有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。
在这种情况下，可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接受多少。
一个这样的示例是创建用户简介：你知道你将收到有关用户的信息，但不确定会是什么样的信息。
在下面的示例中，函数build_profile()接受名和姓，同时还接受任意数量的关键字实参：
形参**user_info 中的两个星号让Python创建一个名为user_info 的 空字典，并将收到的所有名称—值对都封装到这个字典中。
"""
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
"""
我们调用build_profile() ，向它传递名（'albert' ）、姓（'einstein' ）和两个键—值对（location='princeton' 
和field='physics' ），并将返回 的profile 存储在变量user_profile 中，再打印这个变量：
"""
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

# 练习1.三明治
"""编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个函数只有一个形参（它收集函数调用中提供的所有食材），
   并打印一条消息，对顾客点的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。"""
print("----------练习1----------")
def my_make_pizza(*toppings):
    print("\nThe sandwich contains as following: ")
    for topping in toppings:
        print("\t-" + topping)
my_make_pizza('green pepper', 'tomato', 'cheese')
my_make_pizza('green pepper', 'tomato')
my_make_pizza('green pepper')

# 练习2.汽车
"""
编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
这样调用这个函数：提供必不可少的信息，以及两个名称—值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用："""
def make_car(maker, kind, **extra_info):
    car_info = {}
    car_info['manufacturer'] = maker
    car_info['model'] = kind
    for key, value in extra_info.items():
        car_info[key] = value
    return car_info
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

