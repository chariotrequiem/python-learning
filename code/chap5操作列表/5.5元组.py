# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/24 9:32
"""列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，然而，有时候你需要创建一系列不可修改的元素，
   元组可以满足这种需求。Python将不能修改的值称为不可变的，而不可变的列表被称为元组。"""
# 1.定义元组
# 元组看起来犹如列表，但使用圆括号而不是方括号来标识。定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样。
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# 尝试修改元组中的元素是被禁止的。由于试图修改元组的操作是被禁止的，因此Python指出不能给元组的元素赋值。
# dimensions[0] = 250

# 2.遍历元组中的所有值
# 像列表一样，也可以使用for 循环来遍历元组中的所有值；
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# 3.修改元组变量
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述元组，可重新定义整个元组
dimensions = (200, 50)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)
print(" \nModified dimensions: ")
dimensions = (400, 100)
for dimension in dimensions:
    print(dimension)

# 练习1.有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在一个元组中。
print('----------练习1.----------')
foods = ('饺子', '牛肉面', '炒饭', '盖浇饭', '抄手')
# 使用一个for 循环将该餐馆提供的五种食品都打印出来。
for food in foods:
    print(food)
# 尝试修改其中的一个元素，核实Python确实会拒绝你这样做。
# foods[0] = '猪脚饭'
# 餐馆调整了菜单，替换了它提供的其中两种食品。请编写一个这样的代码块：给元组变量赋值，并使用一个for循环将新元组的每个元素都打印出来
foods = ('饺子', '牛肉面', '猪脚饭', '炒饭', '抄手')
for food in foods:
    print(food)
