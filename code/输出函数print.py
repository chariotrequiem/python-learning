# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/21 20:40

# print函数输出的内容可以是数字
print(520)
print(98.4)
# print函数输出的内容还可以是字符串
print('hello world')
print("hello python")
# print函数输出的内容还可以是含有运算符的表达式
print(3+1)
# print函数可以将内容输出目的地1.显示器 2.文件
# 将数据输出到文件中
# 注意点：1.所指定的盘符存在2.使用file=变量名
fp = open('D:/text.txt', 'a+')  # ‘a+’，如果不存在就创建，如果存在就进行追加
print('hello world', file=fp)
fp.close()
# print函数的输出形式1.换行 2.不换行
# 不进行换行输出(输出内容在一行当中)
print('hello', 'world', 'python')