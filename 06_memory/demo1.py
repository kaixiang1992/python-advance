"""
【Python内存管理】引用计数和循环引用(1) 2019/10/24 22:38
"""
import sys

# print('引用计数...')


# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __del__(self):
#         print('%s被释放了...' % (self.name,))
#
#
# while True:
#     p1 = Person('p1')
#     p2 = Person('p2')
#     temp1 = p1
#     del p1
#     del p2
#     text = input('测试输入：')

# print('='*30)


"""
引用计数这一技术虽然可以在一定程度上解决内存管理的问题。但是还是有不能解决的问题，即循环引用。
比如现在有两个对象分别为a和b，a指向了b，b又指向了a，那么他们两的引用计数永远都不会为0。
也即永远得不到回收。
"""
print('循环引用...')


class Person(object):
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None

    def __del__(self):
        print('%s被释放了...' % (self.name,))


while True:
    p1 = Person('p1')
    p2 = Person('p2')
    p1.next = p2
    p2.prev = p1
    print(sys.getrefcount(p1))
    print(sys.getrefcount(p2))
    del p1
    del p2
    text = input('测试输入:')
