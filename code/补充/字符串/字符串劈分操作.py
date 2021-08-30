# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/30 15:14
"""
   split()方法 :
   -从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
   -可以通过参数sep指定劈分字符串的劈分符
   -通过参数maxsplit指定劈分字符串的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部份

   rsplit()方法：
   -从字符串的右边开始劈分，默认的劈分字符是空格字符串，返回的值都是一个列表
   -可以通过参数sep指定劈分字符串的劈分符
   -通过参数maxsplit指定劈分字符串的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部份
"""

s = 'hello world python'
lst = s.split()
print(lst)
sl = 'hello|world|python'
print(sl.split(sep='|'))
print(sl.split(sep='|', maxsplit=1))
"""rsplit()从右侧开始劈分"""
print(s.rsplit())
print(sl.rsplit('|'))
print(sl.split(sep='|', maxsplit=1))