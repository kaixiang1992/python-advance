"""
【Python生成器】send方法的用法 2019/10/07 14:24
"""


def my_gen(start):
    while start < 10:
        # TODO: 如果通过next函数执行yield
        # TODO: 那么yield xxx永远返回None
        temp = yield start
        print('temp is %s' % (temp,))
        start += 1


ret = my_gen(1)
# print(ret.send(None))
print(next(ret))
# 1
print(next(ret))
# 2
print(ret.send('hello world!'))
# temp is hello world!
# 3
