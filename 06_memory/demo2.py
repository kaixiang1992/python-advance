"""
【Python内存管理】标记清除和分代回收
"""

import sys


class Person(object):
    def __init__(self, name):
        self.name = name
        self.prev = None
        self.next = None

    def __del__(self):
        print('%s被释放了...' % (self.name,))


p1 = Person('p1')
p2 = Person('p2')
p3 = Person('p3')
p4 = Person('p4')

p1.next = p2
p2.prev = p1

temp1 = p3
temp2 = p4

print(sys.getrefcount(p1))
print(sys.getrefcount(p2))
print(sys.getrefcount(p3))
print(sys.getrefcount(p4))