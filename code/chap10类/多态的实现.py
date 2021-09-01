# 当前版本 ： python3.8.2
# 开发时间 ： 2021/9/1 15:03
"""
静态语言(如Java)和动态语言(如python)关于多态的区别：
    -静态语言实现多态的三个必要条件
        -继承
        -方法重写
        -父类引用指向子类对象

    动态语言的多态崇尚"鸭子类型"当看到一直鸟走起来像鸭子、游泳起来像鸭子、收起来也像鸭子，那么这只鸟就可以被称为是鸭子
    在鸭子类型中，不需要关心对象是什么类型，到底是不是鸭子，只关心对象的行为
"""


class Animal:
    def eat(self):
        print('动物会吃')


class Dog(Animal):
    def eat(self):
        print('狗吃骨头...')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼....')


class Person:
    def eat(self):
        print('人吃五谷杂粮...')


def fun(obj):
    obj.eat()


# 开始调用函数
fun(Cat())
fun(Dog())
fun(Person())


