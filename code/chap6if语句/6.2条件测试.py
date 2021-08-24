# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/24 10:05
"""每条if语句的核心都是一个值为True或False的表达式，这种表达式被称为条件测试。
   Python根据条件测试的值为True还是False来决定是否执行if语句中的代码。
   如果条件测试的值为True，Python就执行紧跟在if语句后面的代码；如果为False，Python就忽略这些代码。"""

# 1.检查是否相等时不考虑大小写
"""在Python中检查是否相等时区分大小写，例如，两个大小写不同的值会被视为不相等
   如果大小写很重要，这种行为有其优点。但如果大小写无关紧要，而只想检查变量的值，可将变量的值转换为小写，再进行比较"""

# 2.检查是否不相等
# 要判断两个值是否不等，可结合使用惊叹号和等号（!= ），其中的惊叹号表示不 ，在很多编程语言中都如此。
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies")

# 3.比较数字
answer = 17
if answer != 41:
    print("That is not the correct answer. Please try again!")
# 条件语句中可包含各种数学比较，如小于、小于等于、大于、大于等于

# 4.检查多个条件
# 4.1使用and检查多个条件
"""要检查是否两个条件都为True，可使用关键字and将两个条件测试合而为一，如果每个测试都通过了，整个表达式就为True；
   如果至少有一个测试没有通过，整个表达式就为False。"""
age_0 = 18
age_1 = 20
if age_0 > 15 and age_1 > 15:
    print('age > 15')
# 4.2使用or检查多个条件
"""关键字or也能够让你检查多个条件，但只要至少有一个条件满足，就能通过整个测试。
    仅当两个测试都没有通过时，使用or的表达式才为False。"""

# 5.检查特定值是否包含在列表中
"""有时候，执行操作前必须检查列表是否包含特定的值。
   要判断特定的值是否已包含在列表中，可使用关键字in 。"""
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print('mushrooms在披萨配料表中')

# 6.检查特定值是否不包含在列表中
# 还有些时候，确定特定的值未包含在列表中很重要；在这种情况下，可使用关键字not in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

# 7.布尔表达式
# 布尔表达式，不过是条件测试的别名。与条件表达式一样，布尔表达式的结果要么为True，要么为False

# 练习1.编写一系列条件测试；将每个测试以及你对其结果的预测和实际结果都打印出来。你编写的代码应类似于下面这样：
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 练习2.1 检查两个字符串相等和不等。
str1 = 'abcdefg'
str2 = 'abcdefgh'
print("Is str1 == str2 ? I predict False")
print(str1 == str2)
# 练习2.2 使用函数lower() 的测试。
str1 = "abcdefg"
str2 = 'Abcdefg'
print("Is str1 == str2 ? I predict True")
print(str1 == str2.lower())
# 练习2.3 检查两个数字相等、不等、大于、小于、大于等于和小于等于
num1 = 10
num2 = 20
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
# 练习2.4 测试特定的值是否包含在列表中
nums = [1, 2, 3, 4, 5]
print("Is 4 in nums? I predict True")
print(4 in nums)
# 练习2.5 测试特定的值是否未包含在列表中
nums = [1, 2, 3, 4, 5]
print("Is 6 not in nums? I predict True")
print(6 not in nums)