"""
【Python多任务编程】进程池详解 2019/11/02 14:00
"""

# TODO: 进程池
"""
multiprocessing模块中有一个类Pool，这个类相当于一个池，专门用来存储进程。
Pool的__init__可以传递一个参数，这个参数指定这个进程池中同一时刻最多只能拥有多少个进程。


并且，在使用进程池，父进程不会等待子进程池中的子进程执行完毕后退出，而是当父进程中的代码执行完毕以后会立即退出。
使用 pool.join(),

"""

from multiprocessing import Pool
import os
import time


def worker(num):
    for x in range(5):
        print('子进程：%s，子进程id: %s' % (num, os.getpid()))
        time.sleep(1)


if __name__ == '__main__':
    print('主程序运行中...')
    # TODO: 这个池子中同一时刻最多只能有3个进度
    pool = Pool(3)
    for x in range(10):
        pool.apply_async(worker, args=(x, ))

    # TODO: 关闭进程池，不能再添加新的进程了
    pool.close()
    # 主进程把子进程添加到进程池中后，不会等待进程池中其他的子进程都执行完毕后在退出，
    # 而是当主进程的代码执行完毕后会立刻退出，因此这个地方没有join，
    # 那么子进程将得不到执行
    pool.join()

    print('所有程序执行完毕...')