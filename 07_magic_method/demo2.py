"""
【Python魔术方法】比较运算符魔术方法
"""

"""
判断两个对象大小的条件：
1. 首先看age，谁的age大，谁就大
2. 如果age相等，就看height，谁的height大，谁就更大
"""


class Person(object):
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    # ==比较运算符：比较两个对象是否相等
    def __eq__(self, other):
        return True if self.age == other.age and self.height == other.height else False

    # !=比较运算符：比较两个对象是否不相等
    def __ne__(self, other):
        return False if self.age == other.age and self.height == other.height else True

    # <比较运算符：比较两个对象大小
    def __lt__(self, other):
        if self.age == other.age:
            return True if self.height < other.height else False
        return self.age < other.age

    # >比较运算符：比较两个对象大小
    def __gt__(self, other):
        if self.age == other.age:
            return True if self.height > other.height else False
        return self.age > other.age

    # >= 比较运算符：比较self>other或者self==other
    def __ge__(self, other):
        if self.__gt__(other) or self.__eq__(other):
            return True
        else:
            return False

    # <= 比较运算符：比较self < other或者self == other
    def __le__(self, other):
        if self.__lt__(other) or self.__eq__(other):
            return True
        else:
            return False


# TODO: __eq__ : == 比较运算符
# p1 = Person('p1', 18, 180)
# p2 = Person('p2', 18, 180)
#
# if p1 == p2:
#     print(True)
# else:
#     print(False)

# TODO: __ne__: != 比较运算符
# p1 = Person('p1', 18, 180)
# p2 = Person('p2', 18, 170)
#
# if p1 != p2:
#     print(True)
# else:
#     print(False)

# TODO: __lt__: < 比较运算符
# p1 = Person('p1', 18, 170)
# p2 = Person('p2', 18, 180)
#
# if p1 < p2:
#     print(True)
# else:
#     print(False)

# TODO: __gt__: > 比较运算符
# p1 = Person('p1', 19, 170)
# p2 = Person('p2', 18, 180)
#
# if p1 > p2:
#     print(True)
# else:
#     print(False)

# TODO: __ge__: >= 比较运算符
"""
首先执行>判断，如果为True，那么就返回True
首先执行>判断，如果返回False，在执行==判断，如果返回True，那么就返回True，否则返回False
"""
# p1 = Person('p1', 19, 180)
# p2 = Person('p2', 19, 180)
#
# if p1 >= p2:
#     print(True)
# else:
#     print(False)

# TODO: __le__: <= 比较运算符
"""
首先执行<判断，如果返回True，那么就返回True
首先执行<判断，如果返回False，那么就执行==判断，如果返回为True，那么久返回True，否则返回False
"""
p1 = Person('p1', 19, 170)
p2 = Person('p2', 19, 180)

if p1 <= p2:
    print(True)
else:
    print(False)
