# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 21:22

"""
编写函数或类时，还可为其编写测试。
通过测试，可确定代码面对各种输入都能够按要求的那样工作。测试让你信心满满，深信即便有更多的人使用你的程序，它也能正确地工作。
在程序中添加新代码时，你也可以对其进行测试，确认它们不会破坏程序既有的行为。
程序员都会犯错，因此每个程序员都必须经常测试其代码，在用户发现问题前找出它们。

在本章中，你将学习如何使用Python模块unittest中的工具来测试代码。你将学习编写测试用例，
核实一系列输入都将得到预期的输出。你将看到测试通过了是什么样子，测试未通过又是什么样子，
还将知道测试未通过如何有助于改进代码。你将学习如何测试函数和类，并将知道该为项目编写多少个测试。
from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')

现在假设我们要修改get_formatted_name()，使其还能够处理中间名。
这样做时，我们要确保不破坏这个函数处理只有名和姓的姓名的方式。
为此，我们可以在每次修改get_formatted_name()后都进行测试：
运行程序names.py，并输入像Janis Joplin这样的姓名，但这太烦琐了。
所幸Python提供了一种自动测试函数输出的高效方式。
倘若我们对get_formatted_name()进行自动测试，就能始终信心满满，
确信给这个函数提供我们测试过的姓名时，它都能正确地工作。
"""

# 1.1单元测试和测试用例
"""
Python标准库中的模块unittest提供了代码测试工具。
单元测试用于核实函数的某个方面没有问题；测试用例是一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求。
良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情形的测试。
全覆盖式测试用例包含一整套单元测试，涵盖了各种可能的函数使用方式。
对于大型项目，要实现全覆盖可能很难。通常，最初只要针对代码的重要行为编写测试即可，等项目被广泛使用时再考虑全覆盖。
"""

# 1.2可通过的测试
"""
创建测试用例的语法需要一段时间才能习惯，但测试用例创建后，再添加针对函数的单元测试就很简单了。
要为函数编写测试用例，可先导入模块unittest以及要测试的函数，
再创建一个继承unittest.TestCase的类，并编写一系列方法对函数行为的不同方面进行测试。 

下面是一个只包含一个方法的测试用例，它检查函数get_formatted_name()在给定名和姓时能否正确地工作：
import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    #测试name_function.py
    def test_first_last_name(self):
        #能够正确地处理像Janis Joplin这样的姓名吗？
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()
"""

# 1.3不能通过的测试
"""
测试未通过时结果是什么样的呢？我们来修改get_formatted_name()，使其能够处理中间名，
但这样做时，故意让这个函数无法正确地处理像Janis Joplin这样只有名和姓的姓名。
"""

# 1.4测试未通过时怎么办
"""
测试未通过时怎么办呢？如果你检查的条件没错，测试通过了意味着函数的行为是对的，而测试未通过意味着你编写的新代码有错。
因此，测试未通过时，不要修改测试，而应修复导致测试不能通过的代码：
检查刚对函数所做的修改，找出导致函数行为不符合预期的修改。 

在这个示例中，get_formatted_name()以前只需要两个实参——名和姓，但现在它要求提供名、中间名和姓。
新增的中间名参数是必不可少的，这导致get_formatted_name()的行为不符合预期。
就这里而言，最佳的选择是让中间名变为可选的。这样做后，使用类似于Janis Joplin的姓名进行测试时，测试就会通过了，
同时这个函数还能接受中间名。下面来修改get_formatted_name()，将中间名设置为可选的，然后再次运行这个测试用例。
如果通过了，我们接着确认这个函数能够妥善地处理中间名。 

要将中间名设置为可选的，可在函数定义中将形参middle移到形参列表末尾，并将其默认值指定为一个空字符串。
我们还要添加一个if测试，以便根据是否提供了中间名相应地创建姓名：
"""

# 11.5添加新测试
# 确定get_formatted_name()又能正确地处理简单的姓名后，我们再编写一个测试，用于测试包含中间名的姓名。
# 为此，我们在NamesTestCase类中再添加一个方法：


