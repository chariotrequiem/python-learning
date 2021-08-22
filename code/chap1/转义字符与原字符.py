# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/21 20:59
# 转义字符
# 转义字符就是反斜杠+想要实现的转义功能首字母
# 当字符串中包含反斜杠、单引号和双引号等有特殊用途的字符时，必须使用反斜杠对这些字符进行转义
# 换行：\n  回车：\r  水平制表符：\t  退格：\b
print('hello\nworld')
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')
print('hello\bworld')
print('http:\\\\www.baidu.com')
print('老师说:\'大家好\'')
# 原字符 不希望字符串中的转义字符起作用，就使用原字符，就是在字符串后面加上r，或R
print(r'hello\nworld')
# 注意：最后一个字符不能是反斜杠（两个可以）
# print(r'hello\nworld\')
