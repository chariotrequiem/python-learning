# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 19:49
# 常见单词
"""
访问项目Gutenberg（http://gutenberg.org/ ），并找一些你想分析的图书。
下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
你可以使用方法count()来确定特定的单词或短语在字符串中出现了多少次。

请注意，通过使用lower()将字符串转换为小写，可捕捉要查找的单词出现的所有次数，而不管其大小写格式如何。
编写一个程序，它读取你在项目Gutenberg中获取的文件，并计算单词'the'在每个文件中分别出现了多少次
"""


def count_words(file_name):
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        num_words = contents.lower().count('the')
        print("The file " + file_name + " has about " + str(num_words) + " 'the' word.")


filenames = ['alice.txt', 'moby_dick.txt', 'siddhartha.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
