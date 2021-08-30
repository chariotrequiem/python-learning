# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/30 10:11

# 两个集合是否相等，可以使用运算符==或!=进行判断
s = {10, 20, 30, 40}
s2 = {20, 30, 40, 10}
print(s == s2)
print(s != s2)

# 一个集合是否是另一个集合的子集，可以调用issubset进行判断
s3 = {10, 20, 30, 40, 50, 60}
s4 = {30, 40, 50}
print(s4.issubset(s3))

# 一个集合是否是另一个集合的超集，可以调用方法issuperset
print(s3.issuperset(s4))

# 两个集合是否有交集，使用方法isdisjoint
print(s3.isdisjoint(s4))  # False 有交集