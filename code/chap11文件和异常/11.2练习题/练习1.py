# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 15:41
# 访客访 ：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt中。
name = input("Please enter your name: ")

file_name = 'guest.txt'
with open(file_name, 'w') as object_file:
    object_file.write(name)
