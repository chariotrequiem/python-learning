# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 15:09

"""
在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的Python知识，
其中每一行都以“In Python you can”打头。将这个文件命名为learning_python.txt，
并将其存储到为完成本章练习而编写的程序所在的目录中。编写一个程序，它读取这个文件，
并将你所写的内容打印三次：第一次打印时读取整个文件；
第二次打印时遍历文件对象；第三次打印时将各行存储在一个列表中，再在with代码块外打印它们。
"""
file_name = 'learning_python.txt'
with open(file_name) as object_file:
    contents = object_file.read()
    print(contents)

file_name = 'learning_python.txt'
with open(file_name) as object_file:
    for line in object_file:
        print(line)

file_name = 'learning_python.txt'
with open(file_name) as object_file:
    lines = object_file.readlines()

print(lines)
for line in lines:
    print(line)

