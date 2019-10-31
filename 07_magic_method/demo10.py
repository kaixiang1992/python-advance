"""
【Python魔术方法】pickle魔术方法 2019/10/31 23:49
"""

"""
有时候一个对象，想要保存在硬盘中。这时候我们就需要使用到对象持久化的技术了。
在Python中，如果要将一个对象存储到硬盘中，需要使用pickle模块，
其中dump方法可以将一个对象存到硬盘中，
load方法可以从硬盘中加载一个对象。

Python许多内置的数据结构是可以直接序列化的，比如：字典、列表、元组、字符串等
"""

import pickle


def dump_data_pickle():
    data = {
        'foo': [1, 2, 3],
        'bar': ('hello', 'world'),
        'baz': True
    }
    with open('data.pkl', 'wb') as fp:
        pickle.dump(data, fp)


def dump_load_pickle():
    with open('data.pkl', 'rb') as fp:
        data = pickle.load(fp)
        print(data)


dump_load_pickle()
print('=' * 40)

"""
自定义可持续化对象：
自己定义的类的对象，默认情况下是不能持续化的。如果想要让自定义的对象可持续化，那么应该实现两个魔术方法：
第一个是__getstate__，这个魔术方法在把对象存储到硬盘中的时候会调用的，会将这个方法的返回值存储进去，
    返回值应该是可以持续化的数据类型，比如字典、列表、字符串等；
第二个是__setstate__，这个魔术方法是从硬盘中加载对象的时候，
    会调用，会将你之前存储进去的值，通过参数的形式传递进来。
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # TODO: 把对象存储到硬盘
    def __getstate__(self):
        # TODO: 返回可持续化数据类型
        return {'name': self.name, 'age': self.age}

    # TODO: 读取硬盘加载对象
    def __setstate__(self, state):
        self.name = state.get('name')
        self.age = state.get('age')

    def __str__(self):
        return 'Person(name: %s, age: %d)' % (self.name, self.age)


def dump_obj():
    p1 = Person('zhiliao', 18)
    with open('test.pkl', 'wb') as fp:
        pickle.dump(p1, fp)


def load_obj():
    with open('test.pkl', 'rb') as fp:
        p1 = pickle.load(fp)
        print(p1)


load_obj()
