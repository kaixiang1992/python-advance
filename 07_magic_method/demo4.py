"""
【Python魔术方法】二元运算符魔术方法 2019/10/30 22:10
"""

"""
普通算术操作符：
1.__add__(self,other)魔术方法：在两个对象相加的时候执行的方法。
2.__sub__(self,other)魔术方法：在两个对象相减的时候执行的方法。
3.__mul__(self,other)魔术方法：在两个对象相乘的时候执行的方法。
4.__floordiv__(self,other)魔术方法：在两个对象使用//运算的时候执行的方法。
5.__truediv__(self,other)魔术方法：在两个对象之间使用真除的时候执行的方法。
    在Python3中使用/运算的时候会执行这个方法。
6.__mod__(self,other)魔术方法：在使用%取模运算的时候执行的方法。
"""



class Coornidate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # TODO: + 运算
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Coornidate(x, y)

    # TODO: - 运算
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Coornidate(x, y)

    # TODO: * 运算
    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Coornidate(x, y)

    # TODO: // 整除运算
    def __floordiv__(self, other):
        x = self.x // other.x
        y = self.y // other.y
        return Coornidate(x, y)

    # TODO: / 真除运算
    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        return Coornidate(x, y)

    # TODO: % 运算
    def __mod__(self, other):
        x = self.x % other.x
        y = self.y % other.y
        return Coornidate(x, y)

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)


c1 = Coornidate(1, 2)
c2 = Coornidate(2, 3)
# c3 = c1 + c2
# c3 = c1 - c2
# c3 = c1 * c2
# c3 = c2 // c1
# c3 = c1 / c2
c3 = c1 % c2
print(c3)

