# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/22 15:49
# input()函数接受来自用户的输入，输入值的类型为str，使用=对输入的值进行存储
day = input('今天是星期几？')
print(day, type(day))

# 从键盘录入两个整数，求两个整数的和
n1 = int(input('第一个整数'))
n2 = int(input('第二个整数'))
print(type(n1), type(n2))
# n1和n2是string类型，+起连接作用而不是相加
n = n1 + n2
print('两个整数的和为：', n)
