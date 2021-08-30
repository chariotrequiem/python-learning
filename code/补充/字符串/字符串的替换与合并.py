# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/30 15:33

# 字符串替换
# replace()方法，第一个参数指定被替换的子串，第二个参数指定替换子串的字符串
# 该方法返回替换后得到的字符串，替换前的字符串不发生变化，调用该方法时可以通过第三个参数指定最大替换次数
s = 'hello,Python'
print(s.replace('Python', 'Java'))
sl = 'hello,Python,Python,Python'
print(sl.replace('Python', 'Java', 2))

# 字符串的合并
# join()方法，将列表或元组中的字符串合并成一个字符串
lst = ['hello', 'java', 'python']
print('|'.join(lst))  # 使用'|'连接
print(' '.join(lst))

t = ('hello', 'Java', 'Python')
print(' '.join(t))

print('*'.join('Python'))  # P*y*t*h*o*n
