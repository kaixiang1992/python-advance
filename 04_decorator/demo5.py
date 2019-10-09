"""
【Python装饰器】wraps装饰器 2019/10/09 23:42
"""

from functools import wraps


def greet(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('func 开始执行...')
        func(*args, **kwargs)
        print('func 执行完毕...')

    return wrapper


@greet
def add(x, y):
    print('%d + %d = %d' % (x, y, x + y))


add(1, 2)
# print(add.__name__)  # TODO: 未加wraps装饰器前,wrapper
print(add.__name__)  # TODO: 加wraps装饰器后,add
