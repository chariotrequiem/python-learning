# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/24 13:54
# 4.1检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now!')
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

# 4.2确定列表不是空的
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
else:
    print('Are you sure you want a plain pizza?')

# 4.3使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

# 练习1.创建一个至少包含5个用户名的列表，且其中一个用户名为'admin'
# 想象你要编写代码，在每位用户登录网站后都打印一条问候消息。遍历用户名列表，并向每位用户打印一条问候消息。
print("----------练习1.----------")
names = ['eric', 'jack', 'admin', 'mary', 'jane']
for name in names:
    if name == 'eric':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + name.title() + ", thank you for logging in again")

# 练习2.在为完成练习1编写的程序中，添加一条if语句，检查用户名列表是否为空。如果为空，就打印消息“We need to find some users!”。
print("----------练习2.----------")
names = ['eric', 'jack', 'admin', 'mary', 'jane']
if names:
    for name in names:
        if name == 'eric':
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello " + name.title() + ", thank you for logging in again")
else:
    print("We need to find some users!")
# 删除列表中的所有用户名，确定将打印正确的消息。
print('----------练习2.2----------')
names = ['eric', 'jack', 'admin', 'mary', 'jane']
names.clear()
if names:
    print(names)
else:
    print("We need to find some users!")

# 练习3.按下面的说明编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
print("----------练习3----------")
# 创建一个至少包含5个用户名的列表，并将其命名为current_users。
current_users = ['eric', 'jack', 'admin', 'mary', 'jane']
# 再创建一个包含5个用户名的列表，将其命名为new_users，并确保其中有一两个用户名也包含在列表current_users中。
new_users = ['Eric', 'lucian', 'lucy', 'john', 'jane']
# 遍历列表new_users ，对于其中的每个用户名，都检查它是否已被使用。如果是这样，就打印一条消息，指出需要输入别的用户名；
# 否则，打印一条消息，指出这个用户名未被使用。
for new_user in new_users:
    if new_user.lower() in current_users:
        print("该用户名已被使用，请选择其他昵称！")
    else:
        print("该用户名" + new_user + "未被使用")

# 练习4.序数表示位置，如1st和2nd。大多数序数都以th结尾，只有1、2和3例外。在一个列表中存储数字1~9。
print("----------练习4----------")
values = [value for value in range(1, 10)]
for value in values:
    if value == 1:
        print(str(value) + "st")
    elif value == 2:
        print(str(value) + "nd")
    elif value == 3:
        print(str(value) + "rd")
    else:
        print(str(value) + "th")