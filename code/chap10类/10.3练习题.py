# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/25 21:33
# 练习1.冰淇凌小店
"""
冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand的类，让它继承你为完成练习10.2.1而编写的Restaurant类。
添加一个名为flavors的属性，用于存储一个由各种口味的冰淇淋组成的列表。
编写一个显示这些冰淇淋的方法。创建一个IceCreamStand实例，并调用这个方法。
"""


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("\nThe name of the restaurant is " + self.restaurant_name + ".")
        print("The type of it is " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The restaurant is opening now!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, add_number):
        self.number_served += add_number


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['巧克力味', '草莓味', '橙子味']

    def describe_IceCream(self):
        print("我们店里有以下这些口味的冰淇淋：")
        for flavor in self.flavors:
            print("-" + flavor)


my_IceCreamStand = IceCreamStand('开心冰淇淋', '酸奶炒冰淇淋')
my_IceCreamStand.describe_IceCream()

# 练习2.管理员
"""
管理员是一种特殊的用户。编写一个名为Admin的类，让它继承你为完成练习10.2.2而编写的User类。
添加一个名为privileges的属性，用于存储一个由字符串（如"can add post" 、"can delete post" 、"can ban user" 等）组成的列表。
编写一个名为show_privileges()的方法，它显示管理员的权限。创建一个Admin实例，并调用这个方法。
"""

'''
class User():
    def __init__(self, first_name, last_name, age):
        """初始化属性first_name和last_name,age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        name = self.first_name + " " + self.last_name
        print("The information of the user is as following: ")
        print("Name: " + name.title())
        print("Age: " + str(self.age))

    def greet_user(self):
        name = self.first_name + " " + self.last_name
        print("\nWelcome to log in, honored " + name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("\nThe privileges of adminer as following: ")
        for privilege in self.privileges:
            print("-" + privilege)


admin = Admin('jack', 'jones', 25)
admin.show_privileges()
'''

# 练习3.权限
"""
编写一个名为Privileges的类，它只有一个属性——privileges ，其中存储了练习2所说的字符串列表。将方法show_privileges()移到这个类中。
在Admin 类中，将一个Privileges实例用作其属性。创建一个Admin实例，并使用方法show_privileges()来显示其权限。
"""


class User():
    def __init__(self, first_name, last_name, age):
        """初始化属性first_name和last_name,age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        name = self.first_name + " " + self.last_name
        print("The information of the user is as following: ")
        print("Name: " + name.title())
        print("Age: " + str(self.age))

    def greet_user(self):
        name = self.first_name + " " + self.last_name
        print("\nWelcome to log in, honored " + name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("\nThe privileges of adminer as following: ")
        for privilege in self.privileges:
            print("-" + privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privilege = Privileges()


admin = Admin('jack', 'jones', 25)
admin.privilege.show_privileges()


# 练习4.电瓶升级
"""
在本节最后一个electric_car.py版本中，给Battery类添加一个名为upgrade_battery()的方法。
这个方法检查电瓶容量，如果它不是85，就将它设置为85。创建一辆电瓶容量为默认值的电动汽车，调用方法get_range()，
然后对电瓶进行升级，并再次调用get_range()。你会看到这辆汽车的续航里程增加了。
"""


class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """
        初始化父类的属性,再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


print("\n")
my_tesla = ElectricCar('tesla', 'model s', 2016)
print("在调用方法get_range()之前：")
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
print("在调用方法get_range()之后：")
my_tesla.battery.get_range()
