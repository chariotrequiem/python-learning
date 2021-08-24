# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/23 21:58
# 你经常需要遍历列表的所有元素，对每个元素执行相同的操作。
# 需要对列表中的每个元素都执行相同的操作时，可使用Python中的for循环。

# 用for循环来打印魔术师名单中的所有名字
magicians = ['alice', 'david', 'carolina']
# 这行代码让Python从列表magicians中取出一个名字，并将其存储在变量magician 中。
for magician in magicians:
    print(magician)

# 1.在for循环中执行更多操作
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')

"""在for循环中，想包含多少行代码都可以。
   在代码行for magician in magicians 后面，每个缩进的代码行都是循环的一部分，且将针对列表中的每个值都执行一次。
   因此，可对列表中的每个值执行任意次数的操作。"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    print("I can't wait to see you next trick, " + magician.title() + ".\n")

# 2.在for循环结束后执行一些操作
print('----------2.在for循环结束后执行一些操作----------')
"""for循环结束后再怎么做呢？通常，你需要提供总结性输出或接着执行程序必须完成的其他任务。 
   在for循环后面，没有缩进的代码都只执行一次，而不会重复执行。"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    print("I can't wait to see you next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great show!")
