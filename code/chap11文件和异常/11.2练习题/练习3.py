# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 15:54
"""
关于编程的调查：编写一个while循环，询问用户为何喜欢编程。
每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
"""
file_name = 'reasons.txt'
while True:
    print("\n你为什么喜欢编程呢？")
    print("(退出请按'q')")
    reason = input("请输入你的原因：")
    if reason != 'q':
        with open(file_name, 'a') as object_file:
            object_file.write(reason + "\n")
    else:
        break
