# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 20:53
# 喜欢的数字
"""
编写一个程序，提示用户输入他喜欢的数字，并使用json.dump()将这个数字存储到文件中。
再编写一个程序，从文件中读取这个值，并打印消息“I know your favorite number! It's _____.”。
"""
import json


def stored_number():
    number = input("请输入喜欢的数字： ")
    filename = 'number.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
    return number


def print_number():
    filename = 'number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        print("I know your favorite number! It's " + str(number))


stored_number()
print_number()




