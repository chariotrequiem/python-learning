# 当前版本 ： python3.8.2
# 开发时间 ： 2021/9/1 15:18
"""
    特殊方法和特殊属性;
        特殊属性：
        __dict__  ： 获得类对象或实例对象所绑定的所有属性和方法的字典

        特殊方法：
        __len__():   通过重写__len__()方法，让内置函数len()的参数可以是自定义类型
        __add__():   通过重写__add__()方法，可使用自定义对象具有"+"功能
        __new__():   用于创建对象
        __init__():  对创建的对象进行初始化

"""


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu1 = Student('张三')
stu2 = Student('李四')
s = stu1 + stu2  # 实现了两个对象的加法运算(因为在Student类中，编写__add__()特殊的方法)
print(s)
s = stu1.__add__(stu2)
print(s)
print('-------------------------------------')
lst = [11, 22, 33, 44]
print(len(lst))  # len是内容函数len
print(lst.__len__())
print(len(stu1))
