# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/22 19:42
# 布尔运算符指的是对两个布尔值之间的运算，包括and, or, not, in, not in
print('————————and 并且————————')
a, b = 1, 2
print(a == 1 and b == 2)  # True
print(a == 1 and b < 2)  # False
print(a != 1 and b == 2)  # False
print(a != 1 and b != 2)  # False
print('————————or 或者————————')
print(a == 1 or b == 2)  # True
print(a == 1 or b < 2)  # True
print(a != 1 or b == 2)  # True
print(a != 1 or b != 2)  # False
print('————————not 非————————')
f = True
f2 = False
print(not f)  # False
print(not f2)  # True
print('---------------in与not in——————')
s = 'hello'
print('h' in s)  # True
print('m' in s)  # False
print('h' not in s)  # False
print('m' not in s)  # True

