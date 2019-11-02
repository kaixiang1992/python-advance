"""
【Python多任务编程】multiprocessing多进程编程 2019/11/01 22:04
"""

# TODO: multiprocessing模块

# TODO: 获取进程号
import os

"""
通过os模块的一个函数getpid()可以获取到当前进程的进程号。
通过getppid()可以获取到这个进程的父进程的进程号。
"""

from multiprocessing import Process
import os


def zhiliao():
    print('子进程执行...')
    print('子进程id: %s' % os.getpid())
    print('主进程id: %s' % os.getppid())
    print('hello world!...')
    print('子进程执行完毕...')


if __name__ == '__main__':
    # TODO: 开启一个子进程
    p = Process(target=zhiliao)
    p.start()

    # TODO: 执行主进程
    print('主进程代码执行...')
    print('主进程id：%s' % os.getpid())
