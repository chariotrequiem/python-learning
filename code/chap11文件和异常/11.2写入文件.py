# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 15:29
"""
保存数据的最简单的方式之一是将其写入到文件中。通过将输出写入文件，即便关闭包含程序输出的终端窗口，这些输出也依然存在：
你可以在程序结束运行后查看这些输出，可与别人分享输出文件，还可编写程序来将这些输出读取到内存中并进行处理。
"""
# 2.1写入空文件
"""
要将文本写入文件，你在调用open()时需要提供另一个实参，告诉Python你要写入打开的文件。
为明白其中的工作原理，我们来将一条简单的消息存储到文件中，而不是将其打印到屏幕上
在这个示例中，调用open()时提供了两个实参。
第一个实参也是要打开的文件的名称；第二个实参（'w' ）告诉Python，我们要以写入模式打开这个文件。
打开文件时，可指定读取模式（'r' ）、写入模式（'w' ）、附加模式（'a' ）或让你能够读取和写入文件的模式（'r+' ）。
如果你省略了模式实参，Python将以默认的只读模式打开文件。 
如果你要写入的文件不存在，函数open()将自动创建它。
然而，以写入（'w' ）模式打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件。

file_name = 'programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write("I love programming")
"""
# 注意：Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。

# 2.2写入多行
# 函数write()不会在你写入的文本末尾添加换行符，因此如果你写入多行时没有指定换行符，文件看起来可能不是你希望的那样：
# 要让每个字符串都单独占一行，需要在write() 语句中包含换行符：
"""
file_name = 'programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
"""

# 2.3附加到文件
"""
如果你要给文件添加内容，而不是覆盖原有的内容，可以附加模式打开文件。
你以附加模式打开文件时，Python不会在返回文件对象前清空文件，而你写入到文件的行都将添加到文件末尾。
如果指定的文件不存在，Python将为你创建一个空文件。
"""
file_name = 'programming.txt'
with open(file_name, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")




