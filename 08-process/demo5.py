"""
【Python多任务编程】进程池补充 2019/11/02 14:18
"""

# TODO: 进程池补充
"""
apply_async: 相当于并联模式
apply：相当于串联模式，不常用
"""

from multiprocessing import Pool
import os
import time


def worker(num):
    for x in range(5):
        print('子进程: %s，子进程id: %s' % (num, os.getpid()))
        time.sleep(1)


if __name__ == '__main__':
    print('主进程执行中...')
    pool = Pool(3)
    for x in range(10):
        pool.apply(worker, args=(x,))

    pool.close()
    pool.join()
    print('所有进程均执行完毕...')
