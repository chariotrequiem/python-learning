# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 10:15
"""
Python标准库是一组模块，安装的Python都包含它。
你现在对类的工作原理已有大致的了解，可以开始使用其他程序员编写好的模块了。
可使用标准库中的任何函数和类，为此只需在程序开头包含一条简单的import语句。
下面来看模块collections中的一个类——OrderedDict。
字典让你能够将信息关联起来，但它们不记录你添加键—值对的顺序。
要创建字典并记录其中的键—值对的添加顺序，可使用模块collections中的OrderedDict类。
OrderedDict实例的行为几乎与字典相同，区别只在于记录了键—值对的添加顺序。

这是一个很不错的类，它兼具列表和字典的主要优点（在将信息关联起来的同时保留原来的顺序）。
等你开始对关心的现实情形建模时，可能会发现有序字典正好能够满足需求。
"""
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")