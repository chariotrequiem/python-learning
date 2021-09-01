# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/25 19:58
"""
类属性：类中方法外的变量称为类属性，被该类的所有对象所共享
类方法：使用@ classmethod修饰的方法，使用类名直接访问的方法
静态方法：使用@staticmethod修饰的方法，使用类名直接访问的方法
print(Student.native_place)  # 访问类属性
Student.cm()  # 调用类方法
Student.sm()  # 调用静态方法
"""
# 2.1Car类
# 下面编写一个表示汽车的类，他储存了有关汽车的信息，还有一个汇总这些信息的方法
"""
class Car():
    #一次模拟汽车的简单尝试
    def __init__(self, make, model, year):
        #初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        #返回整洁的描述性信息
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
"""

# 2.2给属性指定默认值
"""
类中的每个属性都必须有初始值，哪怕这个值是0或空字符串。在有些情况下，如设置默认值时，
在方法__init__()内指定这种初始值是可行的；如果你对某个属性这样做了，就无需包含为它提供初始值的形参。
"""
class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性
           现在，当Python调用方法__init__()来创建新实例时，将像前一个示例一样以属性的方式存储制造商、型号和生产年份。
           接下来，Python将创建一个名为odometer_reading的属性，并将其初始值设置为0"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles



# 2.3修改属性的值
# 有三种不同的方式修改属性的值: 直接通过实例进行修改;通过方法进行设置;通过方法进行递增(增加特定的值)。下面依次介绍这些方法。

# 2.3.1直接修改属性的值  要修改属性的值，最简单的方式是通过实例直接访问它。
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 2.3.2 通过方法修改属性的值
# 如果有替你更新属性的方法，将大有裨益。这样就无需直接访问属性，而可将值传递给一个方法，由它在内部进行更新。
"""
class Car(): 
--snip--
    def update_odometer(self, mileage): 
    # 将里程表读数设置为指定的值
    self.odometer_reading = mileage
"""

my_new_car.update_odometer(55)
my_new_car.read_odometer()

# 2.3.3通过方法对属性值进行递增
"""
有时候需要将属性值递增特定的量，而不是将其设置为全新的值。假设我们购买了一辆二手车，且从购买到登记期间增加了100英里的里程，
下面的方法让我们能够传递这个增量，并相应地增加里程表读数：
    def increment_odometer(self, miles):
        #将里程表读数增加指定的量
        self.odometer_reading += miles 
"""
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()




