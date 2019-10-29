"""
【Python魔术方法】一元运算符魔术方法 2019/10/30 00:13
"""

"""
一元操作符和函数：
1.__pos__(self)魔术方法：在这个对象前面使用正号的时候执行的方法
2.__neg__(self)魔术方法：在这个对象前面使用负号的时候执行的方法
3.__abs__(self)魔术方法：在这个对象上使用abs函数的时候执行的方法
4.__invert__(self)魔术方法：在这个对象前面使用~的时候执行的方法
"""


class Coornidate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # TODO: __pos__(self)魔术方法: 在这个对象前面使用正号的时候执行的方法
    def __pos__(self):
        return self

    # TODO: __neg__(self)魔术方法：在这个对象前面使用负号的时候执行的方法
    def __neg__(self):
        return Coornidate(-self.x, -self.y)

    # TODO: __abs__(self)魔术方法：在这个对象上使用abs函数的时候执行的方法
    def __abs__(self):
        return Coornidate(abs(self.x), abs(self.y))

    # TODO: __invert__(self)魔术方法：在这个对象前面使用~的时候执行的方法
    def __invert__(self):
        return Coornidate(255 - self.x, 255 - self.y)

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)


c1 = Coornidate(-1, -2)
# TODO: (-1, -2)
print(c1)

print('__pos__....')
c2 = +c1
# TODO: (-1, -2)
print(c2)

print('__neg__....')
c3 = -c1
# TODO: (1, 2)
print(c3)

print('__abs__....')
c4 = abs(c1)
# TODO: (1, 2)
print(c4)

print('__invert__....')
c5 = ~c1
# TODO: (256, 257)
print(c5)
