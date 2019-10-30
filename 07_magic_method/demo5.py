"""
【Python魔术方法】增量赋值魔术方法 2019/10/30 22:36
"""

# TODO: 增量赋值魔术方法
"""
1.__iadd__(self,other)魔术方法：在给对象做+=运算的时候会执行的方法
2.__isub__(self,other)魔术方法：在给对象做-=运算的时候会执行的方法。
3.__imul__(self,other)魔术方法：在给对象做*=运算的时候会执行的方法。
4.__idiv__(self,other)魔术方法：在给对象做/=运算的时候会执行的方法。 -- Python2
5.__itruediv__(self,other)魔术方法：在给对象做真/=运算的时候会执行的方法。 --Python3
"""


class Coornidate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # TODO: += 运算
    def __iadd__(self, other):
        self.x += other
        self.y += other
        return self

    # TODO: -= 运算
    def __isub__(self, other):
        self.x -= other
        self.y -= other
        return self

    # TODO: *= 运算
    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    # TODO: /= 运算
    def __itruediv__(self, other):
        self.x /= other
        self.y /= other
        return self

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)


c1 = Coornidate(1, 2)
# c1 += 1
# c1 -= 1
# c1 *= 2
c1 /= 2
print(c1)
