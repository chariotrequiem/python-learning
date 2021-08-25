# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/25 20:30
# 练习1.就餐人数
"""
在为完成练习10.1.1而编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。
根据这个类创建一个名为restaurant的实例;打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
添加一个名为set_number_served()的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
添加一个名为increment_number_served()的方法，它让你能够将就餐人数递增。
调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
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


restaurant = Restaurant('halcon', 'French')
print("There are " + str(restaurant.number_served) + " people in the restaurant.")
restaurant.number_served = 5
print("There are " + str(restaurant.number_served) + " people in the restaurant.")
restaurant.set_number_served(50)
print("There are " + str(restaurant.number_served) + " people in the restaurant.")
restaurant.increment_number_served(10)
print("There are " + str(restaurant.number_served) + " people in the restaurant.")

# 练习2.尝试登录次数
"""
在为完成练习10.1.3而编写的User类中，添加一个名为login_attempts的属性。
编写一个名为increment_login_attempts()的方法，它将属性login_attempts的值加1。
再编写一个名为reset_login_attempts()的方法，它将属性login_attempts的值重置为0。 
根据User类创建一个实例，再调用方法increment_login_attempts()多次。打印属性login_attempts的值，确认它被正确地递增；
然后，调用方法reset_login_attempts()，并再次打印属性login_attempts的值，确认它被重置为0。
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


user = User('jack', 'jones', 18)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

