# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/30 15:42
"""
字符串的比较操作：
运算符：>, >=, <, <=, ==, !=
比较规则：
首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，依次比较下去
知道两个字符串中的字符不相等时，其比较结果就是两个字符串的比较结果，两个字符串中的所有后续将不再被比较

比较原理：
两个字符进行比较时，比较的是其ordinal value(原始值)，调用内置函数ord可以得到指定字符的ordinal value。
与内置函数ord对应的是内置函数chr，调用内置函数chr时指定ordinal value可以得到其对应的字符
"""

print('apple' > 'app')
print('apple' > 'banana')
print(ord('a'), ord('b'))
print(ord('杨'))

print(chr(97), chr(98))
print(chr(26472))

"""== 与 is 的区别
   == 比较的是 value
   is 比较的是id是否相等
"""
a = b = 'python'
c = 'python'
print(a == b)
print(b == c)

print(a is b)
print(a is c)
print(id(a))  # 2025191897968
print(id(b))  # 2025191897968
print(id(c))  # 2025191897968