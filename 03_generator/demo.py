"""
TODO:【Python生成器】生成器的基本使用 2019/10/06 21:45
"""

from collections import Iterable, Iterator


# TODO:解决打印1-1亿的问题

# TODO:普通列表生成式
# num_list = [x for x in range(1, 100000000)]
# for x in num_list:
#     print(x)

# TODO: 生成式
# num_list = (x for x in range(1, 100000000))
# print(type(num_list))  # <class 'generator'>
# for x in num_list:
#     print(x)


# TODO: next函数
# next函数可以迭代生成器的返回值

# def my_gen():
#     yield 1
#     yield 2
#     yield 3
#
#
# ret = my_gen()
# print(next(ret))
# print(next(ret))
# print(next(ret))
# print(next(ret))  # StopIteration

def my_range(start, end):
    index = start
    while index < end:
        yield index
        index += 1


ret = my_range(1, 100000000)
# TODO: 生成器其实是迭代器也是可迭代对象
print(isinstance(ret, Iterable))  # True
print(isinstance(ret, Iterator))  # True

for x in ret:
    print(x)