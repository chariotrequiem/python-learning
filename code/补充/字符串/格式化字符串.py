# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/30 16:15
"""
格式化字符串:
  -- % 做占位符：
  %s->字符串  %i或%d->整数  %f->浮点数
  -- {} 做占位符
"""
# 1. %
name = '张三'
age = 20
print('我叫%s，今年%d岁' % (name, age))
# 2. {}
print('我叫{0}，今年{1}岁'.format(name, age))
# 3. f-string
print(f'我叫{name}, 今年{age}岁')

