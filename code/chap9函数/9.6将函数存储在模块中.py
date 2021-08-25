# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/25 16:21
"""
函数的优点之一是使用它们可将代码块与主程序分离。通过给函数指定描述性名称，可让主程序容易理解得多。
还可以更进一步，将函数存储在被称为模块的独立文件中，再将模块导入到主程序中。import语句允许在当前运行的程序文件中使用模块中的代码。

通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。这还能让你在众多不同的程序中重用函数。
将函数存储在独立文件中后，可与其他程序员共享这些文件而不是整个程序。知道如何导入函数还能让你使用其他程序员编写的函数库。
导入模块的方法有多种，下面对每种都作简要的介绍。
"""
# 6.1导入整个模块
# 要让函数是可导入的，得先创建模块。模块是扩展名为.py的文件，包含要导入到程序中的代码。
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""
这就是一种导入方法：只需编写一条import 语句并在其中指定模块名，就可在程序中使用该模块中的所有函数。
"""

# 6.2导入特定函数
"""
还可以导入模块中的特定函数，这种导入方法的语法如下：
from module_name import function_name
通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：
from module_name import function_0, function_1, function_2
对于前面的示例，如果只想导入要使用的函数，代码将类似于下面这样：
"""
from pizza import  make_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 6.3使用as给函数指定别名
"""
如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名别 ——函数的另一个名称，
类似于外号。要给函数指定这种特殊外号，需要在导入它时这样做。
指定别名的通用语法如下： 
from module_name import function_name as fn
下面给函数make_pizza() 指定了别名mp()
from pizza import make_pizza as mp
"""

# 6.4使用as给模块指定别名
"""
还可以给模块指定别名。通过给模块指定简短的别名（如给模块pizza指定别名p ），让你能够更轻松地调用模块中的函数。
给模块指定别名的通用语法如下： 
import module_name as mn

相比于pizza.make_pizza() ，p.make_pizza()更为简洁：
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
上述import语句给模块pizza指定了别名p，但该模块中所有函数的名称都没变。
调用函数make_pizza()时，可编写代码p.make_pizza()而不是pizza.make_pizza()，
这样不仅能使代码更简洁，还可以让你不再关注模块名，而专注于描述性的函数名。
这些函数名明确地指出了函数的功能，对理解代码而言，它们比模块名更重要。
"""

# 6.5导入模块中的所有函数
"""
使用星号（* ）运算符可让Python导入模块中的所有函数：
import语句中的星号让Python将模块pizza中的每个函数都复制到这个程序文件中。
由于导入了每个函数，可通过名称来调用每个函数，而无需使用句点表示法。
然而，使用并非自己编写的大型模块时，最好不要采用这种导入方法;
如果模块中有函数的名称与你的项目中使用的名称相同，可能导致意想不到的结果：
Python可能遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数。 

最佳的做法是，要么只导入你需要使用的函数，要么导入整个模块并使用句点表示法。
这能让代码更清晰，更容易阅读和理解。这里之所以介绍这种导入方法，只是想让你在阅读别人编写的代码时，
如果遇到类似于下面的import 语句，能够理解它们：
from module_name import *
"""


