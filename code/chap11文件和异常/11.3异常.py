# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 16:00
"""
Python使用被称为异常的特殊对象来管理程序执行期间发生的错误。
每当发生让Python不知所措的错误时，它都会创建一个异常对象。
如果你编写了处理该异常的代码，程序将继续运行；
如果你未对异常进行处理，程序将停止，并显示一个traceback，其中包含有关异常的报告。

异常是使用try-except代码块处理的。try-except代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办。
使用了try-except代码块时，即便出现异常，程序也将继续运行：显示你编写的友好的错误消息，而不是令用户迷惑的traceback。
"""
# 3.1处理ZeroDivisionError异常
# print(5/0)

# 3.2使用try-except代码块
"""
当你认为可能发生了错误时，可编写一个try-except代码块来处理可能引发的异常。
你让Python尝试运行一些代码，并告诉它如果这些代码引发了指定的异常，该怎么办。 
处理ZeroDivisionError异常的try-except代码块类似于下面这样：
"""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# 3.3使用异常避免崩溃
"""
发生错误时，如果程序还有工作没有完成，妥善地处理错误就尤其重要。
这种情况经常会出现在要求用户提供输入的程序中；
如果程序能够妥善地处理无效输入，就能再提示用户提供有效输入，而不至于崩溃。 

下面来创建一个只执行除法运算的简单计算器：

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_name = input("\nFirst number: ")
    if first_name == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_name) / int(second_number)
    print(answer)
"""

# 3.4else代码块
"""
通过将可能引发错误的代码放在try-except代码块中，可提高这个程序抵御错误的能力。
错误是执行除法运算的代码行导致的，因此我们需要将它放到try-except代码块中。
这个示例还包含一个else代码块；依赖于try代码块成功执行的代码都应放到else代码块中：
"""
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_name = input("\nFirst number: ")
    if first_name == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_name) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

"""
我们让Python尝试执行try代码块中的除法运算，这个代码块只包含可能导致错误的代码。
依赖于try 代码块成功执行的代码都放在else代码块中；
在这个示例中，如果除法运算成功，我们就使用else代码块来打印结果。 

except代码块告诉Python，出现ZeroDivisionError异常时该怎么办。
如果try代码块因除零错误而失败，我们就打印一条友好的消息，告诉用户如何避免这种错误。
程序将继续运行，用户根本看不到traceback：
"""

"""
try-except-else代码块的工作原理大致如下：Python尝试执行try代码块中的代码；只有可能引发异常的代码才需要放在try语句中。
有时候，有一些仅在try代码块成功执行时才需要运行的代码；这些代码应放在else代码块中。
except代码块告诉Python，如果它尝试运行try代码块中的代码时引发了指定的异常，该怎么办。 

通过预测可能发生错误的代码，可编写健壮的程序，它们即便面临无效数据或缺少资源，也能继续运行，从而能够抵御无意的用户错误和恶意的攻击。
"""

# 3.5处理FileNotFoundError异常
"""
使用文件时，一种常见的问题是找不到文件：你要查找的文件可能在其他地方、文件名可能不正确或者这个文件根本就不存在。
对于所有这些情形，都可使用try-except代码块以直观的方式进行处理。 

我们来尝试读取一个不存在的文件。下面的程序尝试读取文件alice.txt的内容，但我没有将这个文件存储在alice.py所在的目录中：

filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
"""

# 3.6分析文本
"""
你可以分析包含整本书的文本文件。很多经典文学作品都是以简单文本文件的方式提供的，因为它们不受版权限制。
本节使用的文本来自项目Gutenberg（http://gutenberg.org/ ），这个项目提供了一系列不受版权限制的文学作品，
如果你要在编程项目中使用文学文本，这是一个很不错的资源。 

下面来提取童话Alicein Wonderland的文本，并尝试计算它包含多少个单词。
我们将使用方法split()，它根据一个字符串创建一个单词列表。下面是对只包含童话名"Alice in Wonderland"的字符串调用方法split()的结果：

title = "Alice in Wonderland"
print(title.split())

方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
结果是一个包含字符串中所有单词的列表，虽然有些单词可能包含标点。
为计算Alicein Wonderland包含多少个单词，我们将对整篇小说调用split()，
再计算得到的列表包含多少个元素，从而确定整篇童话大致包含多少个单词：

file_name = 'alice.txt'
try:
    with open(file_name) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + "does nt exist."
    print(msg)
else:
    # 计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + file_name + " has about " + str(num_words) + " words.")
"""

# 3.7使用多个文件
# 下面多分析几本书。这样做之前，我们先将这个程序的大部分代码移到一个名为count_words()的函数中，这样对多本书进行分析时将更容易：
"""
def count_words(filename):
    #计算一个文件大致包含多少个单词
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + "does nt exist."
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


file_names = ['alice.txt', 'moby_dick.txt', 'siddhartha.txt', 'little_women.txt']
for file_name in file_names:
    count_words(file_name)
"""

# 3.8失败时一声不吭
"""
在前一个示例中，我们告诉用户有一个文件找不到。
但并非每次捕获到异常时都需要告诉用户，有时候你希望程序在发生异常时一声不吭，就像什么都没有发生一样继续运行。 
要让程序在失败时一声不吭，可像通常那样编写try代码块，但在except代码块中明确地告诉Python什么都不要做。
Python有一个pass语句，可在代码块中使用它来让Python什么都不要做：

pass语句还充当了占位符，它提醒你在程序的某个地方什么都没有做，并且以后也许要在这里做些什么。
例如，在这个程序中，我们可能决定将找不到的文件的名称写入到文件missing_files.txt中。
用户看不到这个文件，但我们可以读取这个文件，进而处理所有文件找不到的问题。
"""


def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


file_names = ['alice.txt', 'moby_dick.txt', 'siddhartha.txt', 'little_women.txt']
for file_name in file_names:
    count_words(file_name)

# 3.9决定报告哪些错误
"""
在什么情况下该向用户报告错误？在什么情况下又应该在失败时一声不吭呢？
如果用户知道要分析哪些文件，他们可能希望在有文件没有分析时出现一条消息，将其中的原因告诉他们。
如果用户只想看到结果，而并不知道要分析哪些文件，可能就无需在有些文件不存在时告知他们。
向用户显示他不想看到的信息可能会降低程序的可用性。
Python的错误处理结构让你能够细致地控制与用户分享错误信息的程度，要分享多少信息由你决定。 

编写得很好且经过详尽测试的代码不容易出现内部错误，如语法或逻辑错误，
但只要程序依赖于外部因素，如用户输入、存在指定的文件、有网络链接，就有可能出现异常。
凭借经验可判断该在程序的什么地方包含异常处理块，以及出现错误时该向用户提供多少相关的信息。
"""