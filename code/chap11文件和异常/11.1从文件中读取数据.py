# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 10:44
"""
要使用文本文件中的信息，首先需要将信息读取到内存中。为此，你可以一次性读取文件的全部内容，也可以以每次一行的方式逐步读取。
"""
# 1.1读取整个文件
"""
在这个程序中，第1行代码做了大量的工作。
我们先来看看函数open()。要以任何方式使用文件——哪怕仅仅是打印其内容，都得先打开打文件，这样才能访问它。
函数open()接受一个参数：要打开的文件的名称。Python在当前执行的文件所在的目录中查找指定的文件。
在这个示例中，当前运行的是file_reader.py，因此Python在file_reader.py所在的目录中查找pi_digits.txt。
函数open()返回一个表示文件的对象。在这里，open('pi_digits.txt')返回一个表示文件pi_digits.txt的对象；
Python将这个对象存储在我们将在后面使用的变量中。 

关键字with在不再需要访问文件后将其关闭。在这个程序中，注意到我们调用了open()，但没有调用close()；
你也可以调用open()和close()来打开和关闭文件，但这样做时，如果程序存在bug，导致close()语句未执行，文件将不会关闭。
这看似微不足道，但未妥善地关闭文件可能会导致数据丢失或受损。如果在程序中过早地调用close()，
你会发现需要使用文件时它已关闭（无法访问），这会导致更多的错误。
并非在任何情况下都能轻松确定关闭文件的恰当时机，但通过使用前面所示的结构，可让Python去确定：
你只管打开文件，并在需要时使用它，Python自会在合适的时候自动将其关闭。 

有了表示pi_digits.txt的文件对象后，我们使用方法read()（前述程序的第2行）读取这个文件的全部内容，
并将其作为一个长长的字符串存储在变量contents中。这样通过打印contents的值，就可将这个文本文件的全部内容显示出来：
"""
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
"""
相比于原始文件，该输出唯一不同的地方是末尾多了一个空行。
为何会多出这个空行呢？因为read()到达文件末尾时返回一个空字符串，而将这个空字符串显示出来时就是一个空行。要删除多出来的空行，可在print 语句中使用rstrip() ：
"""

# 1.2文件路径
"""
当你将类似pi_digits.txt这样的简单文件名传递给函数open()时，Python将在当前执行的文件（即.py程序文件）所在的目录中查找文件。 

根据你组织文件的方式，有时可能要打开不在程序文件所属目录中的文件。
例如，你可能将程序文件存储在了文件夹python_work中，而在文件夹python_work中，有一个名为 text_files的文件夹，
用于存储程序文件操作的文本文件。虽然文件夹text_files包含在文件夹python_work中，
但仅向open()传递位于该文件夹中的文件的名称也不可行，因为Python只在文件夹python_work中查找，
而不会在其子文件夹text_files中查找。要让Python打开不与程序文件位于同一个目录中的文件，需要提供文件路径，
它让Python到系统的特定位置去查找。 

由于文件夹text_files位于文件夹python_work中，因此可使用相对文件路径来打开该文件夹中的文件。
相对文件路径让Python到指定的位置去查找，而该位置是相对于当前运行的程序所在目录的。
在Windows系统中，在文件路径中使用反斜杠'\'而不是斜杠'/',你可以这样编写代码：
"""
with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

file_path = 'D:\\CODE\\Python学习\\python-learning\\chap11文件和异常\\text_files\\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

# 1.3逐行打印
"""
读取文件时，常常需要检查其中的每一行：你可能要在文件中查找特定的信息，或者要以某种方式修改文件中的文本。
例如，你可能要遍历一个包含天气数据的文件，并使用天气描述中包含字样sunny的行。
在新闻报道中，你可能会查找包含标签<headline>的行，并按特定的格式设置它。
"""
filename = 'pi_digits.txt'
with open(filename, 'r') as file_object:
    for line in file_object:
        print(line.rstrip())

# 1.4创建一个包含文件各行内容的列表
"""
使用关键字with时，open()返回的文件对象只在with 代码块内可用。
如果要在with代码块外访问文件的内容，可在with代码块内将文件的各行存储在一个列表中，
并在with代码块外使用该列表：你可以立即处理文件的各个部分，也可推迟到程序后面再处理。
"""
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# 1.5使用文件的内容
"""
将文件读取到内存中后，就可以以任何方式使用这些数据了。
下面以简单的方式使用圆周率的值。首先，我们将创建一个字符串，它包含文件中存储的所有数字，且没有任何空格：
"""
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    """在变量pi_string存储的字符串中，包含原来位于每行左边的空格，为删除这些空格，可使用strip()而不是rstrip()"""
    pi_string += line.rstrip().strip()

print(pi_string)
print(len(pi_string))


# 注意：读取文本文件时，Python将其中的所有文本都解读为字符串。
# 如果你读取的是数字，并要将其作为数值使用，就必须使用函数int()将其转换为整数，或使用函数float()将其转换为浮点数。


# 1.6包含一百万位的大型文件
"""
前面我们分析的都是一个只有三行的文本文件，但这些代码示例也可处理大得多的文件。
如果我们有一个文本文件，其中包含精确到小数点后1 000 000位而不是30位的圆周率值，
也可创建一个包含所有这些数字的字符串。为此，我们无需对前面的程序做任何修改，只需将这个文件传递给它即可。
在这里，我们只打印到小数点后50位，以免终端为显示全部1 000 000位而不断地翻滚：

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    # 在变量pi_string存储的字符串中，包含原来位于每行左边的空格，为删除这些空格，可使用strip()而不是rstrip()
    pi_string += line.rstrip().strip()

print(pi_string)
print(len(pi_string))
"""
# 1.7圆周率中包含你的生日吗
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    pi_string = file_object.read()
print(len(pi_string))
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


