# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/31 14:47
"""
序号   异常类型               描述
1      ZeroDivisionError      除(或取模)零(所有数据类型)
2      IndexError             序列中没有次索引
3      KeyError               映射中没有这个键
4      NameError              未声明/初始化对象(没有属性)
5      SyntaxError            Python语法错误
6      ValueError             传入无效的参数
......
"""
# 程序调试：打断点，debug
i = 1
while i <= 10:
    print(i)
    i += 1
