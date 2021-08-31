# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/31 10:17
"""
    Bug的常见类型：
    -- 粗心导致的语法错误 SyntaxError
            1.漏了末尾的符号，如if语句，循环语句，else子句等
            2.缩进错误，该缩进的没缩进，不该缩进的瞎缩进
            3.把英文符号写成中文符号，比如说：引号、冒号、括号
            4.字符串拼接的时候，把字符串和数字拼在一起、
            5.没有定义变量。比如while的循环条件的变量
            6.'=='比较运算符和'='赋值运算符的混用
            eg.1
            age = input('请输入你的年龄：')
            if age > 18:  # age是str类型，不能与int型进行比较
                print('你已经是成年人了')

            eg.2
            while i < 10:  # i并没有赋初值
                print（i） # 此处括号为（），应为()
                # 没有跳出循环语句  i+=1

            eg.3
            for i in range(3):
                uname = input('请输入用户名：')
                pwd = input(''请输入密码：)
                if uname = 'admin' and pwd = 'admin': # 判断是否相等应使用'=='而非'='赋值符号
                    print('登陆成功！ ')
                else
                    print('输入有误 ')
            else
                print('对不起，三次均输入错误')

    --知识点不熟练导致的错误;
            eg.1索引越界问题IndexError
            lst = [11, 22, 33, 44]  # 列表的索引从0开始
            print(lst[4])

            eg2.append()方法的使用不熟练
            lst = []
            lst = append('A', 'B', 'C')  # 应为list.append()， 且append()方法一次只能添加一个元素
            print(lst)


    --思路不清导致的问题
            1.使用print()函数
            2.使用"#"暂时注释部分代码

    --被动跳坑
    程序代码逻辑没有错，只是因为用户错误操作或一些"例外情况"而导致的程序崩溃
    try-except
    可以添加多个except结构
    捕获异常的顺序按照先子类后父类的顺序，为了避免遗漏可能出现的异常，可以在最后增加BaseException
        try:
            a = int(input('请输入第一个整数：'))
            b = int(input('请输入第二个整数：'))
            result = a / b
            print('结果为：', result)
        except ZeroDivisionError:
            print('对不起，除数不允许为0')
        except ValueError:
            print('只能输入数字串')
        print('程序结束')
"""

