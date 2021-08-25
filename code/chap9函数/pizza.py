# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/25 16:25
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
