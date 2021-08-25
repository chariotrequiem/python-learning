# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/24 22:07
# for循环用于针对集合中的每个元素都一个代码块，而while循环不断地运行，直到指定的条件不满足为止。
# 2.1使用while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 2.2让用户选择何时退出
# 可使用while循环让程序在用户愿意时不断地运行，我们也可以在其中定义一个退出值，只要用户输入的不是这个值，程序就接着运行
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
# 创建了一个变量——message,用于存储用户输入的值。
# 将变量message 的初始值设置为空字符串"",让Python首次执行while代码行时有可供检查的东西。
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# 2.3使用标志
# 在复杂的程序中，很多不同的事件都会导致程序停止运行，如果在一条while语句中检查所有这些条件，将既复杂又困难。
# 在要求很多条件都满足才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态。
# 这个变量被称为标志，充当了程序的交通信号灯。你可让程序在标志为True 时继续运行，并在任何事件导致标志的值为False时让程序停止运行。
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# 2.4使用break退出循环
"""要立即退出while循环不再运行循环中余下的代码，也不管条件测试的结果如何，可使用break 语句。
   break语句用于控制程序流程，可使用它来控制哪些代码行将执行， 哪些代码行不执行，从而让程序按要求执行你要执行的代码。"""
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
# 注意：在任何Python循环中都可使用break语句。例如，可使用break 语句来退出遍历列表或字典的for循环

# 2.5在循环中使用continue
# 要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue语句，它不像break语句那样不再执行余下的代码并退出整个循环。
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# 2.6避免无限循环
# 每个while循环都必须有停止运行的途径，这样才不会没完没了地执行下去。
# 如果程序陷入无限循环，可按Ctrl+ C，也可关闭显示程序输出的终端窗口。

# 练习1.编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit'时结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料。
print("------------练习1----------")
prompt = "请选择你需要的配料: "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print("我们将会在披萨中添加" + message)
# 练习2.有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3~12岁的观众为10美元；超过12岁的观众为15美元。请编写一个循环，在其中询问用户的年龄，并指出其票价。
print("------------练习2----------")
prompt = "请输入你的年龄 "
age = ""
while age != 'quit':
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("免票！")
        elif age < 12:
            print("12美元每位！")
        else:
            print("15美元每位！")
# 练习3.重做练习2，使用变量active来控制循环结束的时机。
print("------------练习3----------")
prompt = "请输入你的年龄: "
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("免票！")
        elif age < 12:
            print("12美元每位！")
        else:
            print("15美元每位！")


