# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/24 10:36
# 3.1简单的if语句
# 最简单的if语句只有一个测试和一个操作
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# 3.2 if-else语句
age = 17
if age > 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# 3.3if-elif-else结构
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
print('----------另一种写法----------')
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

# 3.4使用多个elif代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".")

# 3.5省略else代码块
# Python并不要求if-elif结构后面必须有else代码块。在有些情况下，else代码块很有用；而在其他一些情况下，使用一条elif语句来处理特定的情形更清晰
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $" + str(price) + ".")

# 3.6测试多个条件
"""if-elif-else结构功能强大，但仅适合用于只有一个条件满足的情况;遇到通过了的测试后，Python就跳过余下的测试。
   这种行为很好，效率很高，让你能够测试一个特定的条件。然而，有时候必须检查你关心的所有条件。
   在这种情况下，应使用一系列不包含elif和else代码块的简单if语句。
   在可能有多个条件为True，且你需要在每个条件为True时都采取相应措施时，适合使用这种方法。"""
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')
print('\nFinished making your pizza!')

# 练习1. 假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color 的变量，并将其设置为'green'、'yellow'或'red'。
print('----------练习1----------')
alien_color = 'green'
# 编写一条if语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了5个点。
if alien_color == 'green':
    print('You get 5 points!')

# 练习2.像上个练习那样设置外星人的颜色，并编写一个if-else结构。
print('----------练习2----------')
# 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。
alien_color = 'red'
if alien_color == 'green':
    print("You got 5 points!")
# 如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。
else:
    print('You got 10 points!')

# 练习3.将练习2中的if-else结构改为if-elif-else结构。
print('----------练习3----------')
alien_color = 'red'
# 如果外星人是绿色的，就打印一条消息，指出玩家获得了5个点。
if alien_color == 'green':
    print('You got 5 points!')
# 如果外星人是黄色的，就打印一条消息，指出玩家获得了10个点。
elif alien_color == 'yellow':
    print('You got 10 points!')
# 如果外星人是红色的，就打印一条消息，指出玩家获得了15个点。
else:
    print('You got 15 points!')

# 练习4.设置变量age 的值，再编写一个if-elif-else 结构，根据age 的值判断处于人生的哪个阶段。
print('----------练习4----------')
age = 25
if age < 2:
    print('他是婴儿')
elif age < 4:
    print('他正在蹒跚学步')
elif age < 13:
    print('他是儿童')
elif age < 20:
    print('他是青少年')
elif age < 65:
    print('他是成年人')
else:
    print('他是老年人')

