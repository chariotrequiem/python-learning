# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/25 14:52

# 向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象(如字典)。将列表传递给函数后，函数就能直接访问其内容。
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 4.1在函数中修改列表
# 将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的，使得能够高效地处理大量的数据。
"""来看一家为用户提交的设计制作3D打印模型的公司。需要打印的设计存储在一个列表中，打印后移到另一个列表中。
   下面是在不使用函数的情况下模拟这个过程的代码："""
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # 模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)
# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

"""为重新组织这些代码，我们可编写两个函数，每个都做一件具体的工作。
   大部分代码都与原来相同，只是效率更高。第一个函数将负责处理打印设计的工作，而第二个将概述打印了哪些设计："""
def print_models(unprinted_designs, completed_models):
    """
        模拟打印每个设计，直到没有未打印的设计为止
        打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
# 主程序
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 4.2禁止函数修改列表
"""有时候，需要禁止函数修改列表。例如，假设像前一个示例那样，你有一个未打印的设计列表，并编写了一个将这些设计移到打印好
   的模型列表中的函数。你可能会做出这样的决定：即便打印所有设计后，也要保留原来的未打印的设计列表，以供备案。但由于你将
   所有的设计都移出了unprinted_designs ，这个列表变成了空的，原来的列表没有了。为解决这个问题，可向函数传递列表的副本而
   不是原件；这样函数所做的任何修改都只影响副本，而丝毫不影响原件。"""
"""要将列表的副本传递给函数，可以像下面这样做：
   function_name(list_name[:])  # 切片表示法[:]创建列表的副本。"""
"""虽然向函数传递列表的副本可保留原始列表的内容，但除非有充分的理由需要传递副本，否则还是应该将原始列表传递给函数，
   因为让函数使用现成列表可避免花时间和内存创 建副本，从而提高效率，在处理大型列表时尤其如此。"""

# 练习1.魔术师
"""创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians()的函数，这个函数打印列表中每个魔术师的名字。"""
print("----------练习1----------")
"""def show_magicians(magician_names):
    for magician_name in magician_names:
        print(magician_name)

names = ['刘谦', '大卫科波菲尔', '胡迪尼']
show_magicians(names)"""

# 练习2.了不起的魔术师
"""在你为完成练习1而编写的程序中，编写一个名为make_great()的函数，对魔术师列表进行修改，
   在每个魔术师的名字中都加入字样“the Great”。调用函数show_magicians()，确认魔术师列表确实变了。"""
print("----------练习2----------")
"""
def show_magicians(magician_names):
    for magician_name in magician_names:
        print(magician_name)
def make_great(magician_names, new_magician_names):
    for magician_name in magician_names:
        new_magician_name = 'the Great ' + magician_name
        new_magician_names.append(new_magician_name)

names = ['刘谦', '大卫科波菲尔', '胡迪尼']
new_names = []
make_great(names, new_names)
show_magicians(new_names)
"""

# 练习3.不变的魔术师
"""修改你为完成练习2而编写的程序，在调用函数make_great()时，向它传递魔术师列表的副本。由于不想修改原始列表，
   请返回修改后的列表，并将其存储到另一个列表中。分别使用这两个列表来调用show_magicians()，
   确认一个列表包含的是原来的魔术师名字，而另一个列表包含的是添加了字样“the Great”的魔术师名字"""
print("----------练习3----------")
def show_magicians(magician_names):
    for magician_name in magician_names:
        print(magician_name)
def make_great(magician_names, new_magician_names):
    for magician_name in magician_names:
        new_magician_name = 'the Great ' + magician_name
        new_magician_names.append(new_magician_name)

names = ['刘谦', '大卫科波菲尔', '胡迪尼']
new_names = []
make_great(names[:], new_names)
show_magicians(names)
show_magicians(new_names)