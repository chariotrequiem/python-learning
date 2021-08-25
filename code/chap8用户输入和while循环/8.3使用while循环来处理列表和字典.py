# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/24 22:58
"""要在遍历列表的同时对其进行修改，可使用while循环。
   通过将while循环同列表和字典结合起来使用，可收集、存储并组织大量输入，供以后查看和显示。"""
# 3.1在列表之间移动元素
"""假设有一个列表，其中包含新注册但还未验证的网站用户；验证这些用户后，如何将他们移到另一个已验证用户列表中呢？
   一种办法是使用一个while 循环，在验证用户的同时 将其从未验证用户列表中提取出来，再将其加入到另一个已验证用户列表中。
   代码可能类似于下面这样："""
# 首先，创建一个待验证用户列表和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# 验证每个用户，直到没有未验证用户为止，将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# 显示所有已验证用户
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 3.2删除包含特定值的所有列表元素
"""在前面，我们使用函数remove()来删除列表中的特定值，这之所以可行，是因为要删除的值在列表中只出现了一次。
   如果要删除列表中所有包含特定值的元素，该怎么办呢？"""
# 假设你有一个宠物列表，其中包含多个值为'cat'的元素。要删除所有这些元素，可不断运行一个while循环，直到列表中不再包含值'cat'
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 3.3使用用户输入来填充字典
"""可使用while循环提示用户输入任意数量的信息。下面来创建一个调查程序，其中的循环每次执行时都提示输入被调查者的名字和回答。
   我们将收集的数据存储在一个字典中，以便将回答同被调查者关联起来："""
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb someday?")

    # 将答案储存在字典中
    responses[name] = response
    # 看看是否还有人要参与
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
# 调查结束，显示结果
print("\n--------Poll Results--------")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

# 练习1.熟食店
"""创建一个名为sandwich_orders的列表，在其中包含各种三明治的名字；再创建一个名为finished_sandwiches的空列表。
   遍历列表sandwich_orders ，对于其中的每种三明治，都打印一条消息，如I made your tuna sandwich，
   并将其移到列表finished_sandwiches 。所有三明治都制作好后，打印一条消息，将这些三明治列出来。"""
print("----------练习1----------")
sandwich_orders = ['酸黄瓜三明治', '香肠三明治', '芝士三明治']
finished_sandwiches = []
while sandwich_orders:
    print("I made your tuna sandwich")
    sandwich_order = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_order)
print("所有三明治制作完成！")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)

# 练习2.五香烟熏牛肉(pastrami)卖完了
"""使用为完成练习1而创建的列表sandwich_orders，并确保'pastrami'在其中至少出现了三次。
   在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；
   再使用一个while循环将列表sandwich_orders中的'pastrami'都删除。确认最终的列表finished_sandwiches中不包含'pastrami'"""
print("----------练习2----------")
sandwich_orders = ['酸黄瓜三明治', '香肠三明治', '芝士三明治',
                   '五香烟熏牛肉三明治', '五香烟熏牛肉三明治', '五香烟熏牛肉三明治']
finished_sandwiches = []
print("熟食店的五香烟熏牛肉卖完了")
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    if sandwich_order == '五香烟熏牛肉三明治':
        continue
    else:
        finished_sandwiches.append(sandwich_order)
        print("I made your tuna sandwich")
print("所有三明治制作完成！")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)

# 练习3.梦想的度假胜地
"""编写一个程序，调查用户梦想的度假胜地。使用类似于“If you could visit one place in the world, where would you go?”
   的提示，并编写一个打印调查结果的代码块。"""
print("----------练习3----------")
places = {}
active = True
while active:
    name = input("\nWhat's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    places[name] = place
    # 看看是否还有人要参与
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        active = False
# 调查结束，显示结果
print("\n------------Places-------------")
for name, place in places.items():
    print(name + "想要去" + place)


