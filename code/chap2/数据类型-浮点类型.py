# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/22 11:07
# 浮点类型
# 浮点数由整数部分和小数部分组成
a = 3.14159
print(a, type(a))

# 浮点数存储具有不精确性
# 使用浮点数进行计算时，可能会出现小数位数不确定的情况
n1 = 1.1
n2 = 2.2
n3 = 2.1
print(n1+n2)
print(n1+n3)
# 解决办法
from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2'))
