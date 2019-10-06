"""
TODO:113.【迭代器】迭代器和for循环底层原理 2019/10/06 16:21
"""

# TODO: 判断一个对象是否可迭代
# TODO:可以使用instance()判断一个对象是否是Iterable的对象
# TODO:更加专业的判断一个对象是否是可迭代的对象是：这个对象有一个__iter__方法，并且这个方法会返回一个迭代器对象，这种对象就叫做可迭代对象

from collections import Iterable, Iterator

# TODO: 列表是一个可迭代对象
arr = [1, 2, 3]
print(isinstance(arr, Iterable))  # True

# TODO: 字符串是一个可迭代对象
text = 'abc'
print(isinstance(text, Iterable))  # True

# TODO: 元祖是一个可迭代对象
tuple_list = ('a', 'b', 'c')
print(isinstance(tuple_list, Iterable))  # True

# TODO: 整形不是一个可迭代对象
int_number = 123
print(isinstance(int_number, Iterable))  # False


# TODO: 判断一个对象是否是可迭代对象
class MyRange(object):
    def __iter__(self):
        pass


ret = MyRange()
print(isinstance(ret, Iterable))  # True


# TODO:迭代器
# TODO: 在python3中，实现了__next__和__iter__方法，并且这个方法返回了值的对象，叫做迭代器对象。
# TODO: 如果迭代器没有返回值，那么应该在next或者是__next__方法中抛出一个StopIteration异常

class MyRange2(object):
    def __iter__(self):
        pass

    def __next__(self):
        pass


ret2 = MyRange2()
print(isinstance(ret2, Iterator))
print('=' * 30)


# TODO:自定义迭代器

# class CustomizeIterator(object):
#     """
#     TODO: 迭代器
#     """
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < self.end:
#             temp = self.start
#             self.start += 1
#             return temp
#         else:
#             raise StopIteration()


# class CustomizeRange(object):
#     """
#     TODO: 可迭代对象
#     """
#
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         # TODO:返回一个迭代器对象
#         return CustomizeIterator(self.start, self.end)


# TODO: 初始化一个可迭代对象
# for x in CustomizeRange(1, 10):
#     print(x)
#
# print('=' * 30)
# TODO: 使用iter()方法获取可迭代对象的迭代器
# TODO: 有时候我们拥有一个可迭代的对象，我们想要获取这个迭代器，那么可以通过iter(xx)方法或者这个可迭代对象的迭代器

# TODO:使用iter()函数将可迭代的对象转化为迭代器
# range_itrator = iter(CustomizeRange(1, 10))
#
# while True:
#     try:
#         # TODO:不能遍历迭代器，只能通过next来迭代
#         print(range_itrator.__next__())
#     except StopIteration:
#         break

print('实现一个可迭代对象+迭代器对象...')


# TODO: 实现一个可迭代对象+迭代器对象

class SimulationRange(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.index = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            temp = self.start
            self.start += 1
            return temp
        else:
            self.start = self.index
            raise StopIteration()


sim_range = SimulationRange(1, 10)

for x in sim_range:
    print(x)

print('*'*20)

for x in sim_range:
    print(x)

print('='*20)
