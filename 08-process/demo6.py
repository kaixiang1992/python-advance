"""
【Python多任务编程】父子进程数据共享问题 2019/11/02 14:50
"""

# TODO: 进程间数据不共享
"""
在一个程序中，如果创建了一个子进程，那么这个子进程会拷贝一份当前进程所有的资源作为子进程的运行环境。
也就是说，子进程中的变量可能跟父进程一样，但其实是另外一个块内存区域了。他们之间的数据是不共享的。

所有资源：变量，函数，class 类等
"""

from multiprocessing import Process

AGE = 1


def greet(names):
    global AGE
    AGE += 1
    names.append('ketang')
    print('=====子进程=====')
    print('AGE的值：%d，id为：%s' % (AGE, id(AGE)))
    print('names：%s' % (names,))
    print('=====子进程结束=====')


if __name__ == '__main__':
    names = ['zhiliao']
    # greet(names)
    p = Process(target=greet, args=(names,))
    p.start()
    p.join()

    print('=====主进程=====')
    print('AGE的值：%d，id为：%s' % (AGE, id(AGE)))
    print('names：%s' % (names,))
    print('=====主进程结束=====')
