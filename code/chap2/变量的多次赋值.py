# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/22 10:44
# 当多次赋值后变量名会指向新的空间
name = '玛丽亚'
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)

name = '楚留香'
print(name)
print('标识', id(name))
print('类型', type(name))
print('值', name)
