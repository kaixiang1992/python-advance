"""
【Python装饰器】闭包及其使用 2019/10/07 16:27
"""


# TODO: 什么是闭包
# 如果在一个函数内，定义了另一个函数，并且那个函数使用了外面函数的变量，并且外面那个函数返回了里面这个函数的引用。
# 那么称里面的这个函数为闭包。

def greet(name):
    def sey_hello():
        print('hello, my name is %s' % name)

    return sey_hello


greet('zhiliao')()
print('=' * 30)

# TODO: 用闭包实现一个计算器

print('用闭包实现一个计算器....')


def calculator(option):
    if option == 1:  # TODO: 加法
        def add(x, y):
            return x + y

        return add
    elif option == 2:  # TODO:减法
        def minus(x, y):
            return x - y

        return minus
    elif option == 3:  # TODO: 乘法
        def multiply(x, y):
            return x * y

        return multiply
    else:  # TODO: 除法
        def divide(x, y):
            return x / y

        return divide


add_cal = calculator(1)
total = add_cal(10, 20)
print('加法和为：%d' % total)

minus_cal = calculator(2)
minus = minus_cal(10, 20)
print('减法值为：%d' % minus)

multiply_cal = calculator(3)
multiply = multiply_cal(10, 20)
print('乘法值为:%d' % multiply)

divide_cal = calculator(4)
divide = divide_cal(10, 20)
print('除法值为:%.2f' % divide)
print('=' * 30)

# TODO: global关键字:
print('global关键字....')

NUM = 10


def num_add(count):
    # TODO: 未使用global关键字: UnboundLocalError: local variable 'NUM' referenced before assignment
    global NUM
    NUM += count
    return NUM


print(num_add(10))

print('=' * 30)

# TODO: nonlocal关键字：
# 如果想在闭包中修改外面函数的变量，这时候应该使用nonlocal关键字，来把这个变量标示为外面函数的变量。

print('nonlocal关键字...')


def welcome(name):
    def say_welcome():
        # TODO: 未使用nonlocal关键：UnboundLocalError: local variable 'name' referenced before assignment
        nonlocal name
        name += ' ketang'
        print('欢迎来到%s' % name)

    return say_welcome


welcome('zhiliao')()
