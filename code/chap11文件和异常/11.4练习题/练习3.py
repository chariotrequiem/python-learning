# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 21:10
import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'D:/CODE/Python学习/python-learning/chap11文件和异常/text_files/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'D:/CODE/Python学习/python-learning/chap11文件和异常/text_files/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        check = input("Is " + username.title() + " your name? y/n ")
        if check == 'y':
            print("Welcome back, " + username.title() + "!")
        else:
            print("Please enter the right name: ")
            username = get_new_username()
            print("We'll remember you when you come back, " + username.title() + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username.title() + "!")


greet_user()