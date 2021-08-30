# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/30 10:19

# 交集  intersection()方法与&等价，都是交集操作
s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}
print(s1.intersection(s2))
print(s1 & s2)

# 并集操作  union()方法与 | 等价，都是并级操作
print(s1.union(s2))
print(s1 | s2)

# 差集操作  difference()方法与 - 等价， 都是差集操作
print(s1.difference(s2))
print(s1 - s2)
print(s2.difference(s1))
print(s2 - s1)

# 对称差集：两集合除交集外剩下的元素的集合 方法symmetric()与^等价，都是对称差集操作
print(s1.symmetric_difference(s2))
print(s1 ^ s2)