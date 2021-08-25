# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/25 19:32
# 练习1.餐馆
"""
创建一个名为Restaurant的类，其方法__init__()设置两个属性：restaurant_name和cuisine_type。
创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，
而后者打印一条消息，指出餐馆正在营业。
根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。
"""
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("\nThe name of the restaurant is " + self.restaurant_name + ".")
        print("The type of it is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant is opening now!")


restaurant = Restaurant('halcon', 'French')
print("Name is " + restaurant.cuisine_type + ".")
print("Type is " + restaurant.cuisine_type + ".")
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 练习2.三家餐馆
# 根据你为完成练习1.而编写的类创建三个实例，并对每个实例调用方法describe_restaurant()。
restaurant_1 = Restaurant('MacDolond', 'America')
restaurant_2 = Restaurant('Haidilao', 'Chinese')
restaurant_3 = Restaurant('shitang', 'Hell')
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

# 练习3.用户
"""
创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会存储的其他几个属性。
在类User中定义一个名为describe_user()的方法，它打印用户信息摘要；
再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
创建多个表示不同用户的实例，并对每个实例都调用上述两个方法。
"""


class User():
    def __init__(self, first_name, last_name, age):
        """初始化属性first_name和last_name,age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        name = self.first_name + " " + self.last_name
        print("The information of the user is as following: ")
        print("Name: " + name.title())
        print("Age: " + str(self.age))

    def greet_user(self):
        name = self.first_name + " " + self.last_name
        print("\nWelcome to log in, honored " + name.title() + "!")


user_0 = User('willim', 'adams', 25)
user_0.greet_user()
user_0.describe_user()

user_1 = User('jack', 'jones', 18)
user_1.greet_user()
user_1.describe_user()

user_2 = User('lucy', 'dan', 22)
user_2.greet_user()
user_2.describe_user()


