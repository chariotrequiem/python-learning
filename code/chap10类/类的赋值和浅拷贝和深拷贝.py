# 当前版本 ： python3.8.2
# 开发时间 ： 2021/9/1 16:02
"""
变量的赋值操作：
    -只是形成了两个变量，实际上还是指向同一个对象
浅拷贝：
    -Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此，源对象和拷贝对象会引用同一个子对象
深拷贝：
    -使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，源对象和拷贝对象的所有子对象也不相同
"""


class Cpu:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# (1.)变量的赋值
cpu1 = Cpu()
cpu2 = cpu1
print(cpu1)
print(cpu2)

# (2.)类由浅拷贝
print('---------------------------------')
disk = Disk()  # 创建一个硬盘类的对象
computer = Computer(cpu1, disk)  # 创建一个计算机类的对象

# 浅拷贝
import copy
computer2 = copy.copy(computer)
# 运行后明显可以看出computer1和computer2是不同的对象，但包含的子对象cpu和disk内存地址却是相同的
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)

print('-------------------------------------------')
# 深拷贝
computer3 = copy.deepcopy(computer)
# 运行后明显可以看出computer1和computer2是不同的对象，包含的子对象cpu和disk内存地址也是不相同的
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)
