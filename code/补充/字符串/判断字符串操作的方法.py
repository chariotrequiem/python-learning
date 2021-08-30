# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/30 15:23
s = 'hellopython'
# isidentifier()方法  判断指定的字符串是不是合法的标识符(字母数字下划线)
print('1.', s.isidentifier())
# isspace()方法       判断指定的字符串是否全部由空白字符组成(回车、换行、水平制表符)
print('2.', s.isspace())
# isalpha()方法       判断指定的字符串是否全部由字母组成
print('3.', s.isalpha())
# isdecimal()方法     判断指定字符串是否全部由十进制的数字组成
print('4.', s.isdecimal())
# isnumeric()方法     判断指定的字符串是否全部由数字组成
print('5.', s.isnumeric())
# isalnum()方法       判断指定字符串是否全部由字母和数字组成
print('6.', s.isalnum())
