# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 18:03
# 加法运算
"""
创建两个文件cats.txt和dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。将这些代码放在一个try-except代码块中，
以便在文件不存在时捕获FileNotFound错误，并打印一条友好的消息。
将其中一个文件移到另一个地方，并确认except代码块中的代码将正确地执行。
"""


def read_animals(filename):
    try:
        with open(filename) as f_obj:
            animals = f_obj.readlines()
    except FileNotFoundError:
        pass
    else:
        for animal in animals:
            print(animal)


file_names = ['cats.txt', 'dogs.txt']
for file_name in file_names:
    read_animals(file_name)





