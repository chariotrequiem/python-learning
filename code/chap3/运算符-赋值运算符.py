# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/22 16:27
# 1.赋值运算符的执行顺序为从右向左
a = 3 + 4
print(a)
# 2.赋值运算符支持链式赋值
a = b = c = 20
print('a = ', a, 'b = ', b, 'c = ', c)
print(id(a), id(b), id(c))

# 3.支持参数赋值
print('—————————支持参数赋值————————')
a = 20
a += 30  # 相当于a = a + 30
print(a)
a -= 10  # 相当于a = a - 10
print(a)
a *= 2  # 相当于a = a * 2
print(type(a))   # int
print(a)
a /= 3  # 相当于a = a / 2
print(type(a))   # float
print(a)
a //= 2  # 相当于a = a // 2
print(type(a))  # float
print(a)
a %= 3  # 相当于a = a % 2
print(a)

# 4.支持系列解包赋值
print('—————————支持解包赋值————————')
a, b, c = 20, 30, 40
print('a = ', a, 'b = ', b, 'c = ', c)
print(id(a), id(b), id(c))

print('——————交换两个变量的值——————')
a, b = 10, 20
print('交换前：a = ', a, 'b = ', b)
# 交换
a, b = b, a
print('交换后：a = ', a, 'b = ', b)