"""
【Python魔术方法】创建属于自己的序列 2019/10/31 20:50
"""

"""
1.__len__(self)：在使用len(obj)函数的时候会调用这个魔术方法。
2.__getitem__(self,key)：在使用下标操作temp['key']以及切片操作的时候会执行这个魔术方法。
3.__setitem__(self,key,value)：在给这个容器设置key和value的时候会调用这个魔术方法。
4.__delitem__(self,key)：在删除容器中的某个key对应的这个值的时候会调用这个魔术方法。
5.__iter__(self)：在遍历这个容器的时候，会调用容器的这个方法，
    然后返回一个迭代器，再调用这个迭代器的__next__方法。
6.__reversed__(self)：在调用reversed(obj)函数的时候会调用这个方法。
"""


class ZLList(object):
    def __init__(self, values=None):
        if values:
            self.values = values
        else:
            self.values = []

    def __len__(self):
        return len(self.values)

    # TODO: item切片操作时
    """
    slice(0, 2, None)
    print(item.start)  ==> 0
    print(item.stop)   ==> 2
    print(item.step)   ==> None
    """

    def __getitem__(self, item):
        return self.values[item]

    """
    key是切片操作时
    slice(0, 2, None)
    """

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)


zllist = ZLList([1, 2, 3, 4, 5])

# TODO: __len__魔术方法：
print(len(zllist))  # TODO: 5
print('=' * 30)

# TODO: __getitem__魔术方法：
temp = zllist[0:2]
print(temp)  # TODO: [1, 2]
print('=' * 30)

# TODO: __setitem__魔术方法：
zllist[0:2] = ['a', 'b']
print(zllist.values)  # TODO: ['a', 'b', 3, 4, 5]
print('=' * 30)

# TODO: __delitem__魔术方法：
del zllist[0:2]
print(zllist.values)  # TODO: [3, 4, 5]
print('=' * 30)

# TODO: __iter__魔术方法：
for x in zllist.values:
    print(x)

print('=' * 30)

# TODO: __reversed__魔术方法：
print(list(reversed(zllist)))   # [5, 4, 3]
