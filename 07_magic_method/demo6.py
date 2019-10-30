"""
【Python魔术方法】属性访问控制魔术方法 2019/10/31 00:09
"""

# TODO: 控制属性的访问和设置
"""
1.__getattr__魔术方法：
在访问一个对象的某个属性的时候，如果这个属性不存在，那么就会执行__getattr__方法，
将属性的名字传进去。如果这个属性存在，那么就不会调用__getattr__方法

2.__setattr__魔术方法：
只要给一个对象的属性设置值，那么就会调用这个方法。但是要注意的是，
不要在这个方法中调用self.xxx=xxx的形式，因为会产生递归调用。
如果想要给对象的属性设置值，那么应该使用self.__dict__[key]=value这个魔术属性
递归调用异常如下：
RecursionError: maximum recursion depth exceeded while calling a Python object

3.__getattribute__魔术方法:
这个魔术方法是，只要你访问了一个对象的属性，不管这个属性存不存在都会去执行这个方法，
所以在写这个方法的时候要小心循环调用。
这个方法只能在新式类中使用，不能在旧时类中使用。

访问不存在的属性时，先执行__getattr__后，如无属性不存在异常时，再执行__getattribute__

产生循环调用如下示例：
return self.__dict__[item]
RecursionError: maximum recursion depth exceeded while calling a Python object
"""

import logging


class Person(object):
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.is_adult = False

    def __getattr__(self, item):
        print(2)
        if item == 'pname':
            logging.warning('请尽快迁移至name属性, pname属性将在下个版本废弃...')
            return self.name
        else:
            raise AttributeError('属性不存在...')

    def __setattr__(self, key, value):
        if key == 'age':
            self.__dict__['age'] = value
            if value >= 18:
                self.__dict__['is_adult'] = True
            else:
                self.__dict__['is_adult'] = False
        else:
            self.__dict__[key] = value

    def __getattribute__(self, item):
        print(1)
        print(item)
        return super(Person, self).__getattribute__(item)


p1 = Person('zhiliao')
p1.age = 16
print(p1.name)
