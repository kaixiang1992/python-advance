"""
【Python面向对象进阶】元类 2019/10/14 20:58
"""

# TODO: 返回的是类，而非实例化对象
print('返回的是类，而非实例化对象...')


def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass

        return Foo
    else:
        class Bar(object):
            pass

        return Bar


my_class = choose_class('foo')
print(my_class)
print('=' * 20)

# TODO: 使用type创建类：
# TODO:type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
# TODO:类名: Person，继承object，属性name,age

print('使用type创建类...')
Person = type('Person', (object,), {'name': 'zhiliao', 'age': 18})
print(Person)
p = Person()
print(p)
print(p.name)
print(p.age)
print('=' * 20)

"""
【Python面向对象进阶】自定义元类 2019/10/23 23:10
"""

# TODO: 到底什么是元类


print('到底什么是元类...')

age = 35
print(age.__class__.__class__)

name = 'zhiliao'
print(name.__class__.__class__)


def abc():
    pass


print(abc.__class__.__class__)


class MyObj(object):
    pass


my_obj = MyObj()
print(my_obj.__class__.__class__)
print('=' * 20)

# TODO: 自定义元类


print('自定义元类，用函数的形式...')


# 1.用函数的形式

# TODO: 元类会自动将你通常传给`type`的参数作为自己的参数传入

def upper_attr_metaclass(class_name, parent_tuple, class_attr):
    # print(class_name)
    # print(parent_tuple)
    # print(class_attr)
    """返回一个类对象，将属性都转化为大写形式"""

    """选择不已__开头且__结尾的属性"""
    new_class_attr = [(k, v) for k, v in class_attr.items() if not k.startswith('__') and not k.endswith('__')]
    """将它们转为大写形式"""
    upper_class_attr = dict([(k.upper(), v) for k, v in new_class_attr])
    print(upper_class_attr)
    return type(class_name, parent_tuple, upper_class_attr)


"""
Python 2.x版本写法如下：
https://docs.python.org/zh-cn/3.7/library/2to3.html?highlight=__metaclass__
"""
# class mymetaClass(object):
#     __metaclass__ = upper_attr_metaclass
#     country = 'china'

"""
Python 3.7.x版本语法如下：
"""


class mymetaClass(metaclass=upper_attr_metaclass):
    country = 'china'


# TODO: AttributeError: type object 'mymetaClass' has no attribute 'country'
# print(mymetaClass.country)
print(mymetaClass.COUNTRY)  # TODO: china
print('=' * 20)

"""
【Python面向对象进阶】自定义元类--用类的形式 2019/10/24 20:30
"""

print('自定义元类，用类的形式...')


# TODO: 自定义元类，用类的形式继承自type
class UpperAttrClass(type):
    def __new__(cls, class_name, parent_tuple, class_attr):
        new_class_attr = [(k, v) for k, v in class_attr.items() if not k.startswith('__') and not k.endswith('__')]
        upper_class_attr = dict([(k.upper(), v) for k, v in new_class_attr])
        print(upper_class_attr)
        return super().__new__(cls, class_name, parent_tuple, upper_class_attr)


class attrClass(object, metaclass=UpperAttrClass):
    country = 'china'

print(attrClass.COUNTRY)