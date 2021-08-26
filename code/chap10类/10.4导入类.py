# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 8:57
import car
# 4.1导入单个类
"""
from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
"""

# 4.2在一个模块中存储多个类
"""
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
"""

# 4.3从一个模块中导入多个类
"""
从一个模块中导入多个类时，用逗号分隔了各个类。
from car import Car, ElectricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
"""

# 4.4导入整个模块
my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# 4.5导入模块中的所有类
# 要导入模块中的所有类，可使用以下的语法
# from module_name import *

# 4.6在一个模块中导入另一个模块
"""
有时候，需要将类分散到多个模块中，以免模块太大，或在同一个模块中存储不相关的类。
将类存储在多个模块中时，你可能会发现一个模块中的类依赖于另一个模块中的类。
在这种情况下，可在前一个模块中导入必要的类。
"""