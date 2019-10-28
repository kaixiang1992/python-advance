"""
【Python内存管理】gc模块 2019/10/28 22:13
"""
import sys
import gc

# TODO: 查看一个对象的引用计数
"""
打印出来的引用计数，总是会比真实的引用计数多1，原因是因为你将这个对象传给了getrefcount函数，
这个过程会给这个对象的引用计数加1。
"""
print('查看一个对象的引用计数...')
a = 'hello world'
print(sys.getrefcount(a))
print('=' * 30)

# TODO: gc.get_threshold(): 获取gc模块执行垃圾回收的阈值。
# TODO: gc.set_threshold(): 设置垃圾回收的阈值
# TODO: gc.get_count(): 获取当前自动执行垃圾回收的计数器。返回一个元祖。
#  第0个是零代的垃圾对象的数量
#  第1个是零代链表遍历的次数
#  第2个是1代链表遍历的次数
# TODO: gc.set_debug(flags):设置gc的debug日志，一般设置为gc.DEBUG_LEAK可以看到内存泄露的对象
# TODO: gc.collect(generation):执行垃圾回收。会将那些循环引用的对象给回收了。
#  这个函数可以传递参数：
#  0:只回收第0代的垃圾对象
#  1:代表回收第0代和第1代的对象
#  2:代表回收第0、1、2代的对象
#  不传参数，使用2作为默认参数

print('gc模块常用函数...')


# print(gc.get_threshold())  # TODO: (700, 10, 10)
# gc.set_threshold(500, 20, 20)
# print(gc.get_threshold())  # TODO: (500, 20, 20)


class Person(object):
    def __init__(self, name):
        self.name = name
        self.pointer = None

    def __del__(self):
        print('%s 被释放了...' % self.name)


gc.set_debug(gc.DEBUG_LEAK)

while True:
    print(gc.get_count())
    p1 = Person('p1')
    p2 = Person('p2')

    # TODO: 产生循环引用
    p1.pointer = p2
    p2.pointer = p1

    del p1
    del p2

    text = input('测试输入:')
    gc.collect(2)
