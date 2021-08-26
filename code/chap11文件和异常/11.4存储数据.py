# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 20:01
import json
"""
很多程序都要求用户输入某种信息，如让用户存储游戏首选项或提供要可视化的数据。
不管专注的是什么，程序都把用户提供的信息存储在列表和字典等数据结构中。
用户关闭程序时，你几乎总是要保存他们提供的信息；一种简单的方式是使用模块json来存储数据。

模块json让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。
你还可以使用json在Python程序之间分享数据。
更重要的是，JSON数据格式并非Python专用的，这让你能够将以JSON格式存储的数据与使用其他编程语言的人分享。
这是一种轻便格式，很有用，也易于学习。

注意:JSON（JavaScript Object Notation）格式最初是为JavaScript开发的，但随后成了一种常见格式，被包括Python在内的众多语言采用。
"""
# 4.1使用json.dump()和json.load()
"""
我们来编写一个存储一组数字的简短程序，再编写一个将这些数字读取到内存中的程序。
第一个程序将使用json.dump()来存储这组数字，而第二个程序将使用json.load()。 

函数json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象。
下面演示了如何使用json.dump() 来存储数字列表：

我们先导入模块json，再创建一个数字列表。指定要将该数字列表存储到其中的文件的名称。
通常使用文件扩展名.json来指出文件存储的数据为JSON格式。
接下来，我们以写入模式打开这个文件，让json能够将数据写入其中。使用函数json.dump()将数字列表存储到文件numbers.json中。

import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'D:/CODE/Python学习/python-learning/chap11文件和异常/text_files/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
with open(filename) as f_obj:
    number = json.load(f_obj)
print(number)
"""


# 4.2保存和读取用户生成的数据
"""
对于用户生成的数据，使用json保存它们大有裨益，因为如果不以某种方式进行存储，等程序停止运行时用户的信息将丢失。
下面来看一个这样的例子：用户首次运行程序时被提示输入自己的名字，这样再次运行程序时就记住他了。 
我们先来存储用户的名字：

username = input("What's your name? ")
filename = 'D:/CODE/Python学习/python-learning/chap11文件和异常/text_files/username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
"""

"""
现在再编写一个程序，向其名字被存储的用户发出问候:
这个程序运行时，我们将尝试从文件username.json中获取用户名，
因此我们首先编写一个尝试恢复用户名的try代码块。
如果这个文件不存在，我们就在except代码块中提示用户输入用户名，并将其存储在username.json中，以便程序再次运行时能够获取它：

# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它

filename = 'D:/CODE/Python学习/python-learning/chap11文件和异常/text_files/username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What's your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username.title() + "!")
else:
    print("Welcome back, " + username.title() + "!")
"""

# 4.3重构
"""
经常会遇到这样的情况：代码能够正确地运行，但可做进一步的改进——将代码划分为一系列完成具体工作的函数。
这样的过程被称为重构。重构让代码更清晰、更易于理解、更容易扩展。
"""


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
        print("Welcome back, " + username.title() + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username.title() + "!")


greet_user()
