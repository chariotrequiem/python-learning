# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/24 15:33

# Python支持对字典遍历。字典可用于以各种方式存储信息，因此有多种遍历字典的方式：可遍历字典的所有键—值对、键或值。
# 3.1遍历所有的键--值对
user_0 ={
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
# 要编写用于遍历字典的for循环，可声明两个变量，用于存储键—值对中的键和值。
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
    }
for name, language in favorite_languages.items():
    print("\nname: " + name)
    print("language: " + language)

# 3.2遍历字典中的所有键
# 在不需要使用字典中的值时，方法keys()很有用
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
    }
for name in favorite_languages.keys():
    print(name.title())
"""遍历字典时，会默认遍历所有的键，因此，如果将上述代码中的for name in favorite_languages.keys():
   替换为for name in favorite_languages: ，输出将不变。"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
    }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")
# 还可以用keys()来确定是否在字典中
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
    }
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# 3.3按顺序遍历字典中的所有键
"""字典总是明确地记录键和值之间的关联关系，但获取字典的元素时，获取顺序是不可预测的。
   这不是问题，因为通常你想要的只是获取与键相关联的正确的值。
   要以特定的顺序返回元素，一种办法是在for循环中对返回的键进行排序。
   为此，可使用函数sorted()来获得按特定顺序排列的键列表的副本："""
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
    }
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# 3.4遍历字典中的所有值
"""如果你感兴趣的主要是字典包含的值，可使用方法values() ，它返回一个值列表，而不包含任何键。"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
    }
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())

"""这种做法提取字典中所有的值，而没有考虑是否重复。涉及的值很少时，这也许不是问题，
   但如果被调查者很多，最终的列表可能包含大量的重复项。为剔除重复项，可使用集合（set）。"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
    }
print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())

# 练习1.创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能是'nile': 'egypt' 。
print("--------练习1----------")
rivers = {
    'nile': 'eygpt',
    'yangtze river': 'china',
    'yellow river': 'china'
}
# 使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
# 使用循环将该字典中每条河流的名字都打印出来。
for river in rivers.keys():
    print(river.title())
    # 使用循环将该字典包含的每个国家的名字都打印出来。方法1
    print(rivers[river].title())
#  使用循环将该字典包含的每个国家的名字都打印出来。方法2
for country in rivers.values():
    print(country.title())