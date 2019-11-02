"""
【Python多任务编程】使用类的方式创建子进程 2019/11/01 23:00
"""

# TODO: 使用类的方式创建子进程
"""
以类的形式定义子进程的执行代码。那么你可以自定义一个类，让他继承自Process，
然后在这个类中实现run方法，以后这个子进程在执行的时候就会调用这个run方法中的代码。
"""

from multiprocessing import Process
import time
import os

class MyProcess(Process):
    def run(self):
        print('主进程id: %s' % os.getppid())
        for x in range(5):
            print('子进程 %s' % x)
            print('子进程id: %s' % os.getpid())
            time.sleep(1)


if __name__ == '__main__':
    p = MyProcess()
    p.start()

    print('主进程id: %s' % os.getpid())
    p.join()
    print('所有代码执行完毕...')