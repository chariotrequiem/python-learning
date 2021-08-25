# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/25 16:51
"""
使用类几乎可以模拟任何东西。下面来编写一个表示小狗的简单类Dog ——它表示的不是特定的小狗，而是任何小狗。
对于大多数宠物狗，我们都知道些什么呢？它们都有名字和年龄；我们还知道，大多数小狗还会蹲下和打滚。
由于大多数小狗都具备上述两项信息（名字和年龄）和两种行为（蹲下和打滚），我们的Dog类将包含它们。
这个类让Python知道如何创建表示小狗的对象。编写这个类后，我们将使用它来创建表示特定小狗的实例。
"""
# 1.1创建Dog类
# 根据Dog类创建的每个实例都将存储名字和年龄。我们赋予了每条小狗蹲下（sit()）和打滚（roll_over()）的能力：
# 根据约定，在Python中，首字母大写的名称指的是类。这个类定义中的括号是空的，因为我们要从空白创建这个类。


class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        """此处定义的两个变量都有前缀self。以self为前缀的变量都可供类中的所有方法使用，
           我们还可以通过类的任何实例来访问这些变量。self.name = name获取存储在形参name中的值，并将其存储到变量name中，
           然后该变量被关联到当前创建的实例。self.age = age的作用与此类似。像这样可通过实例访问的变量称为属性。"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")

# 1.1.1方法__init__()
"""
类中的函数称为方法；你前面学到的有关函数的一切都适用于方法，就目前而言，唯一重要的差别是调用方法的方式。
方法__init__()是一个特殊的方法，每当你根据Dog类创建新实例时，Python都会自动运行它。在这个方法的名称中，
开头和末尾各有两个下划线，这是一种约定，旨在避免Python默认方法与普通方法发生名称冲突。 

我们将方法__init__()定义成了包含三个形参：self 、name 和age。
在这个方法的定义中，形参self 必不可少，还必须位于其他形参的前面。为何必须在方法定义中包含形参self 呢？
因为Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self。每个与类相关联的方法调用都自动传递实参self，
它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。我们创建Dog实例时，Python将调用Dog类的方法__init__()。
我们将通过实参向Dog()传递名字和年龄；self会自动传递，因此我们不需要传递它。
每当我们根据Dog类创建实例时，都只需给最后两个形参（name 和age）提供值。
"""

# 1.2根据类创建实例
# 命名约定：我们通常可以认为首字母大写的名称（如Dog）指的是类，而小写的名称（如my_dog）指的是根据类创建的实例。
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 1.2.1访问属性
# 要访问实例的属性，可使用句点表示法。
print(my_dog.name.title())

# 1.2.2调用方法
# 根据Dog类创建实例后，就可以使用句点表示法来调用Dog类中定义的任何方法。下面来让小狗蹲下和打滚：
my_dog.sit()
my_dog.roll_over()

# 1.2.3创建多个实例
# 可按需求根据类创建任意数量的实例。下面再创建一个名为your_dog的实例：
your_dog = Dog('lucy', 3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()