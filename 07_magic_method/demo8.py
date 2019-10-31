"""
【Python魔术方法】可调用的对象魔术方法 2019/10/31 22:15
"""

"""
在Python中，一个特殊的魔术方法可以让类的实例的行为表现的像函数一样，
你可以调用他们，将一个函数当做一个参数传到另外一个函数
"""


class Coornidate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%s, %s)' % (self.x, self.y)


c1 = Coornidate(1, 2)
print(c1)  # TODO: (1, 2)
c1(2, 3)
print(c1)  # TODO: (2, 3)
print('=' * 30)


def index():
    return 'index page...'


class IndexView(object):
    def __call__(self, *args, **kwargs):
        return 'view index page....'


def visit_website(view):
    print(view())


visit_website(index)
visit_website(IndexView())
