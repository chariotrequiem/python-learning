# 当前版本 ： python3.8.2
# 开发时间 ： 2021/9/1 10:43
"""
python是动态语言，在创建对象之后，可以动态地绑定属性和方法
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '在吃饭')


# 一个Student类可以创建N多个Student类的实例对象，每个实体对象的属性值不同
stu1 = Student('张三', 20)
stu2 = Student('李四', 16)
print(id(stu1))
print(id(stu2))
print('-------------------为stu2绑定动态性别属性--------------')
stu2.gender = '女'
print(stu1.name, stu1.age)
print(stu2.name, stu2.age, stu2.gender)

print('---------------------------------')
stu1.eat()
stu2.eat()


def show():
    print('定义在类之外的，称函数')


stu1.show = show
stu1.show()