# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/30 9:50

# 集合元素的判断操作   in 或 not in
s = {10, 20, 30, 40, 50}
print(10 in s)
print(100 in s)
print(30 not in s)
print(100 not in s)

# 集合元素的新增操作
# 调用add()方法，一次添加一个元素
s.add(60)
print(s)
# 调用update()方法，一次至少添加一个元素
s.update({100, 200, 300})
print(s)
s.update([90, 91, 92])
print(s)
s.update((1000, 1001, 1002))
print(s)

# 集合元素的删除操作
# 调用remove()方法，一次删除一个指定元素，如果指定的元素不存在抛出KeyError
s.remove(100)
print(s)
# 调用discard()方法，一次删除一个指定元素，如果指定的元素不存在不抛异常
s.discard(500)
print(s)
# 调用pop()方法，一次只删除一个任意元素(不能指定参数，无参)
s.pop()
print(s)
# 调用clear()方法，清空集合
s.clear()
print(s)
