# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 21:04
import json


def my_demo():
    filename = 'number.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        number = input("请输入喜欢的数字： ")
        filename = 'number.json'
        with open(filename, 'w') as f_obj:
            json.dump(number, f_obj)
    else:
        print("I know your favorite number! It's " + str(number))


my_demo()