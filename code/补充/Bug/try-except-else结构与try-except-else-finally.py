# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/31 14:38
"""
try...except...else结构
如果try块中没有抛出异常，则执行else块，如果try块中抛出异常，则except块
"""
try:
    n1 = int(input('请输入一个整数：'))
    n2 = int(input('请输入另一个整数：'))
    result = n1 / n2
except BaseException as e:
    print('出错了')
    print(e)
else:
    print('结果为：', result)
finally:
    print('无论是否产生异常，总会被执行的代码')
print('程序结束')