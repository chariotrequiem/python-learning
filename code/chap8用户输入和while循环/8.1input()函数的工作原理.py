# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/24 21:23
# 函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python将其存储在一个变量中，以方便你使用。
# 函数input()接受一个参数,即要向用户显示的提示或说明，让用户知道该如何做。
message = input('Tell me something, and I will repeat it back to you: ')
print(message)

# 1.1编写清晰的程序
# 每当你使用函数input()时，都应指定清晰而易于明白的提示，准确地指出你希望用户提供什么样的信息——指出用户该输入任何信息的提示都行
# 通过在提示末尾（这里是冒号后面）包含一个空格，可将提示与用户输入分开，让用户清楚地知道其输入始于何处，如下所示：
name = input("please enter your name: ")
print("Hello, " + name + "!")
"""有时候，提示可能超过一行，例如，你可能需要指出获取特定输入的原因。
   在这种情况下，可将提示存储在一个变量中，再将该变量传递给函数input()。
   这样，即便提示超过一行，input()语句也非常清晰。"""
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

# 1.2使用int()来获取数值输入
# 使用函数input()时，Python将用户输入解读为字符串。
"""age = input("How old are you? ")
   # 用户如果输入数字21，但我们请求Python提供变量age的值时，它返回的是'21' ——用户输入的数值的字符串表示。
   # 如果我们只想打印输入，这一点问题都没有；但如果你试图将输入作为数字使用，就会引发错误：
   # 试图将输入用于数值比较时，Python会引发错误，因为它无法将字符串和整数进行比较；不能将存储在age中的字符串'21'与数值18进行比较
   if age >= 18:      
        print("you are an adult!")"""
# 为解决这个问题，可使用函数int()，它让Python将输入视为数值。函数int()将数字的字符串表示转换为数值表示
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You have already became an adult!")

# e.g.判断一个人是否满足坐过山车的身高要求
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# 1.3求模运算符
"""处理数值信息时，求模运算符（%）是一个很有用的工具，它将两个数相除并返回余数
   求模运算符不会指出一个数是另一个数的多少倍，而只指出余数是多少。
   如果一个数可被另一个数整除，余数就为0，因此求模运算符将返回0。可利用这一点来判断一个数是奇数还是偶数："""
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even")
else:
    print("\nThe number " + str(number) + " is odd.")

# 练习1.编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，如“Let me see if I can find you a Subaru”。
print("----------练习1----------")
message = input("What kind of cars do you want to rent? ")
print("Are you sure you want to rent " + message + "? Let me see if I can find you a Subaru")

# 练习2.编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。
print("----------练习2----------")
num = input("店内有多少人在用餐? ")
num = int(num)
if num > 8:
    print("没有空桌了！")
else:
    print("还有空桌。")

# 练习3.让用户输入一个数字，并指出这个数字是否是10的整数倍。
print("----------练习3----------")
number = input("Enter a number: ")
number = int(number)
if number % 10 == 0:
    print("\n" + str(number) + "是10的倍数。")
else:
    print("\n" + str(number) + "不是10的倍数。")