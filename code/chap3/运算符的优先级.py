# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/22 20:27
# 1.算术运算最优先
# ** 优先于 (*,/,//,%) 优先于 (+,-)
# 2.位运算其次
# (<<,>>) 优先于 & 优先于 |
# 3.比较运算符优先级再次 >,<,>=,<=,==,!=
# 4.布尔运算符再次  and or
# 5.赋值运算符最次 =
message = 'hello world'
print(message)
message = 'hello python world'
print(message)
name = 'ada lovelace'
print(name.title())
print(name.upper())
print(name.lower())
firstname = 'ada'
lastname = 'lovelace'
full_name = firstname + ' ' + lastname
print(full_name)
print('hello, ' + full_name.title() + '!')
print('\tpython')
print('language\nC\nC++\n')
print('Language\n\tPython\n\tC\n\tJavaScript')
language = ' Python '
print(language + 'abcd')
language = language.rstrip()
language = language.lstrip()
print(language + 'abcd')
print(2+3*4)
a = (2+3)*4
print(a)
b = 0.2+0.1
print(b)
age = 23
message = "Happy " + str(age) + "rd Birthday"
print(message)


