# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/24 9:53
"""假设你有一个汽车列表，并想将其中每辆汽车的名称打印出来。对于大多数汽车，都应以首字母大写的方式打印其名称，
   但对于汽车名'bmw' ，应以全大写的方式打印。下面的代码遍历一个列表，并以首字母大写的方式打印其中的汽车名，
   但对于汽车名'bmw' ，以全大写的方式打印："""
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

