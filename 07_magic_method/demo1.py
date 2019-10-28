"""
【Python魔术方法】常规魔术方法
"""

"""
__str__魔术方法：
在打印某个对象的时候，通常显示的是这个对象所属类的名字以及内存地址，这种样子是不适合人类来阅读的。
因此如果你想在打印某个对象的时候能更加友好一点，那么你可以自己重写这个方法，并且你自己定义好字符串再返回：
在没有重写__str__函数的时候，打印出来的对象是
类名+地址
例：<__main__.Person object at 0x02A708F0>

__repr__魔术方法：
这个魔术方法是用来表述一个对象的，用于给机器看的。这样说可能不好理解，这里以两个小案例说明这个魔术方法的一个用法：
未使用__repr__魔术方法：
例：[<__main__.Person object at 0x036D0A70>, <__main__.Person object at 0x036D00B0>]

在pycharm中，如果将一个对象创建完成后，放到一个列表中，然后再打印这个列表，
那么会打印这个列表中所有的对象，这时候会调用__repr__魔术方法
例：[Person(zhiliao), Person(ketang)]
"""


class Person(object):
    def __init__(self, name):
        self.name = name

    """
    Person<zhiliao>
    Person<ketang>
    """

    def __str__(self):
        return "Person<%s>" % self.name

    """
    [Person(zhiliao), Person(ketang)]
    """

    def __repr__(self):
        return "Person(%s)" % self.name


p1 = Person('zhiliao')
p2 = Person('ketang')
rst = p1
a = [p1, p2]

print(p1)
print(p2)
print(str(rst))
print(a)
