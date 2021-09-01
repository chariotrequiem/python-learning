# 当前版本 ： python3.8.2
# 开发时间 ： 2021/9/1 14:47
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def info(self):
        print('姓名：{0}，年龄：{1}'.format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    def info(self):
        super().info()
        print('学号：{0}'.format(self.score))


class Teacher(Person):
    def __init__(self, name, age, times):
        super().__init__(name, age)
        self.times = times

    def info(self):
        super().info()
        print('教龄：{0}'.format(self.times))


stu = Student('张三', 20, 100)
teac = Teacher('李四', 35, 15)
stu.info()
teac.info()