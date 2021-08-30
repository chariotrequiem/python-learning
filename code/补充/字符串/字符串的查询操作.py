# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/30 14:38
# index()方法  查找子串substr第一次出现的位置，如果查找的子串不存在时，则抛出ValueError
s = 'hello,hello'
print(s.index('lo'))  # 3
# rindex()方法  查找子串substr最后一次出现的位置，如果查找的子串不存在时，则抛出ValueError
print(s.rindex('lo'))  # 9
# find()  查找子串substr第一次出现的位置，如果查找的子串不存在时，则返回-1
print(s.find('lo'))  # 3
# rfind()  查找子串substr最后一次出现的位置，如果查找的子串不存在时，则返回-1
print(s.rfind('lo'))  # 9

# print(s.index('k'))  # ValueError: substring not found
print(s.find('k'))

"""建议使用find()与rfind()进行查询，查找字串不存在时，不会报错，而是返回-1"""