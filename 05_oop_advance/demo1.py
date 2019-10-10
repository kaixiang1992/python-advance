"""
【Python面向对象进阶】动态添加属性和方法 2019/10/10 21:30
"""

import types

# TODO:动态添加属性
# 1.使用对象名.属性名添加
# 2.使用setattr函数添加

print('动态添加属性...')


class setattrObj(object):
    country = 'china'

    def __init__(self, username):
        self.username = username


setattr_obj = setattrObj('zhiliao')
setattr_obj.age = 18
print(setattr_obj.age)
if hasattr(setattr_obj, 'country'):
    print(True)
else:
    print(False)

setattr(setattr_obj, 'city', '长沙')
print(setattr_obj.city)

print('==========动态添加方法==========')

print('动态添加实例方法...')


# TODO:动态添加实例方法
# 使用types.MethodType方法
# type.MethodType(param1, param2)
# param1:这个函数本身，TODO:例：run
# param2:调用run这个函数的时候，传给run方法的第一个参数。即实例化对象 TODO:例:addmethod_obj
# TODO: 例: types.MethodType(run, addmethod_obj)


class addMethodobj(object):
    def __init__(self, name):
        self.name = name


def run(self):
    print('%s 在奔跑...' % self.name)


addmethod_obj = addMethodobj('中国')
addmethod_obj.run = types.MethodType(run, addmethod_obj)
# addmethod_obj.run = run(addmethod_obj)

addmethod_obj.run()

print('=' * 30)

# TODO:动态添加类方法
# 添加类方法，是把这个方法添加给类。因此添加类方法的时候不是给对象添加，而是给类添加。
# 1.添加类方法的时候不需要使用types.MethodType，直接将这个函数赋值给类就可以了，
# 但是需要使用classmethod装饰器将这个方法设置为一个类方法

print('添加类方法...')


class addclsMethod(object):
    country = 'china'

    def __init__(self, name):
        self.name = name


@classmethod
def greet(cls):
    print('%s 在奔跑...' % cls.country)


addclsMethod.greet = greet
addclsMethod.greet()
print('=' * 30)

# TODO:动态添加静态方法
# 添加静态方法，是把这个方法添加给类。因此也是直接给类添加的，并且使用staticmethod这个装饰器
# 静态方法不需要传递任何参数

print('动态添加静态方法...')


@staticmethod
def staticrun():
    print('添加静态方法成功...')


addclsMethod.staticrun = staticrun
addclsMethod.staticrun()
print('=' * 30)


# TODO: 动态删除属性和方法
# 1.del 对象.属性名
# 2.delattr(对象,"属性名")

class delattrObj(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


delattr_obj = delattrObj('zhiliao', 18)
setattr(delattr_obj, 'country', 'china')
print(delattr_obj.name)
# delattr(delattr_obj, 'name')
# print('del value after ', delattr_obj.name)


print('==========__slots__魔术变量==========')


# TODO:有时候我们想要指定某个类的对象，只要使用我指定的这些属性，
# 不能随便添加其他的属性，那么这时候就可以使用__slots__魔术变量。
# 这个魔术变量是一个列表或者一个元祖，里面存放属性的名字，以后
# 在对象外面，就只能添加这个魔术变量中指定的属性，不能添加其
# 他属性

class Person(object):
    # __slots__ = ['name', 'age']
    __slots__ = ('name', 'age')

    def __init__(self, name):
        self.name = name


p1 = Person('zhiliao')
# p1.height = 180
setattr(p1, 'height', 180)
print(p1.height)
