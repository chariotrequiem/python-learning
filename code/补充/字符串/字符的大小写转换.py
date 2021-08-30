# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/30 14:46
s = 'hello, world!'
# upper() 把字符串中的所有字符都转成大写字母
a = s.upper()  # 转成大写后，会产生一个新的字符串对象
print(a, id(a))
print(s, id(s))
# lower() 把字符串中所有字符都转成小写字母
b = s.lower()
print(b, id(b))
print(s, id(s))
# swapcase() 把字符串中所有大写字母转成小写字母，把所有小写字母都转成大写字母
print(s.swapcase())
# capitalize() 把第一个字符转换成大写，把其余字符转换成小写
print(s.capitalize())
# title() 把每个单词的第一个字符转换成大写，把每个单词的剩余字符转换成小写
print(s.title())