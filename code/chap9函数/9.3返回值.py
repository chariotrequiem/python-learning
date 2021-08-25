# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/25 10:59
"""函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值。
   函数返回的值被称为返回值。在函数中，可使用return语句将值返回到调用函数的代码行。"""
# 3.1返回简单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# 3.2让实参变成可选的
# 有时候，需要让实参变成可选的，这样使用函数的人就只需在必要时才提供额外的信息。可使用默认值来让实参变成可选的。
def get_formatted_name2(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name2('jimi', 'hendrix')
print(musician)
musician = get_formatted_name2('john', 'hooker', 'lee')
print(musician)

# 3.3返回字典
# 函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。例如，下面的函数接受姓名的组成部分，并返回一个表示人的字典：
def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    """在函数定义中，我们新增了一个可选形参age ，并将其默认值设置为空字符串。
    如果函数调用中包含这个形参的值，这个值将存储到字典中。在任何情况下，
    这个函数都会存储人的姓名，但可对其进行修改，使其也存储有关人的其他信息。"""
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age = 27)
print(musician)

# 3.4结合使用函数和while循环
def get_formatted_name3(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
# 这是一个无限循环!
while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' at any time to quit!)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name3(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

# 练习1.专辑
"""编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。
   这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。
   使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。"""
def make_album(m_name, m_album, number = ''):
    albums = {'name':m_name, 'album':m_album}
    if number:
        albums['number'] = number
    return albums
a = make_album('周杰伦', '七里香', 25)
b = make_album('许嵩', '玫瑰花的葬礼')
c = make_album('杨千shan', '处处吻')
print(a)
print(b)
print(c)

# 练习2.用户的专辑：
"""在为完成上个练习编写的程序中，编写一个while循环，让用户输入一个专辑的歌手和名称。
   获取这些信息后，使用它们来调用函数make_album()，并将创建的字典打印出来。在这个while 循环中，务必要提供退出途径。"""
def make_album(m_name, m_album, number = ''):
    albums = {'name':m_name, 'album':m_album}
    if number:
        albums['number'] = number
    return albums
while True:
    m_name = input("\nEnter a singer's name")
    if m_name == 'q':
        break
    m_album = input("Enter the name")
    if m_album == 'q':
        break
    album = make_album(m_name, m_album)
    print(album)