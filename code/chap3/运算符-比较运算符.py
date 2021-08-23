# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/22 19:23
# 比较运算符 对变量或表达式的结果进行大小、真假等比较,结果为bool类型
a, b = 10, 20
print('a大于b吗？', a > b)  # False
print('a小于b吗？', a < b)  # True
print('a小于等于b吗？', a <= b)  # True
print('a大于等于b吗？', a >= b)  # False
print('a等于b吗？', a == b)  # False
print('a不等于b吗？', a != b)

''' 一个 = 称为赋值运算符， == 称为比较运算符
    一个变量由三部分组成：标识，类型，值
    == 比较的是值
    比较对象的标识使用 is'''
a = 10
b = 10
print(a == b)  # True 说明a与b的value相等
print(a is b)  # True 说明a与b的id标识相等

lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print(lst1 == lst2)  # True
print(lst1 is lst2)  # False
print(id(lst1))
print(id(lst2))
print(a is not b)  # False  a的id与b的id其实是相同的
print(lst1 is not lst2)  # True a的id与b的id其实是不相同的
