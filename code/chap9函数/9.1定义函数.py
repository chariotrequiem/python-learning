# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/25 9:56
# 下面是一个打印问候语的简单函数，名为greet_user()
"""关键字def告诉Python你要定义一个函数。这是函数定义，向Python指出了函数名，还可能在括号内指出函数为完成其任务需要什么样的信息"""
# 1.1像函数传递信息
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")
greet_user('jeese')
greet_user('sarah')

# 1.2实参和形参
"""在函数greet_user()的定义中，变量username是一个形参——函数完成其工作所需的一项信息。
   在代码greet_user('jesse')中，值'jesse'是一个实参。实参是调用函数时传递给函数的信息。"""

# 练习1.编写一个名为display_message()的函数，它打印一个句子，指出你在本章学的是什么。调用这个函数，确认显示的消息正确无误。
def display_message():
    print("本章学习的是函数")
display_message()

# 练习2.喜欢的图书
"""编写一个名为favorite_book()的函数，其中包含一个名为title的形参。
   这个函数打印一条消息，如One of my favorite books is Alice in Wonderland 。
   调用这个函数，并将一本图书的名称作为实参传递给它。"""
def favorite_book(title):
    print("One of my favorite books is " + title)
favorite_book('Alice in Wonderland')