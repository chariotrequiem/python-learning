# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 15:18
"""
读取你刚创建的文件learning_python.txt中的每一行，将其中的Python都替换为另一门语言的名称，如C。将修改后的各行都打印到屏幕上。
"""
file_name = 'learning_python.txt'

with open(file_name) as object_file:
    lines = object_file.readlines()

print(lines)

for line in lines:
    print(line.replace('python', 'C'))

