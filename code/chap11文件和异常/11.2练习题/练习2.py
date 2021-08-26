# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 15:44
"""
访客名单：编写一个while循环，提示用户输入其名字。
用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt中。
确保这个文件中的每条记录都独占一行。
"""
file_name = 'guest_book.txt'
while True:
    print("欢迎使用天河云登陆系统！\n")
    print("请输入你的姓名，退出请按'q'")
    name = input('姓名：')
    if name == 'q':
        break
    else:
        print("欢迎登陆，尊敬的" + name + "会员！")
        with open(file_name, 'a') as object_file:
            object_file.write(name + '\n')
