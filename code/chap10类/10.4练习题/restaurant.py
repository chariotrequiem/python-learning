# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 10:02
class Restaurant:
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