"""
【Python多任务编程】Pool进程间通信 2019/11/02 18:45
"""

# TODO: 使用Queue给Pool进程池做进程间通信
"""
如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()，而不是multiprocessing.Queue()，
否则会报错。
RuntimeError: Queue objects should only be shared between processes through inheritance。
"""

from multiprocessing import Pool, Manager
import os
import time


# TODO: 写
def write(q):
    values = ['m1', 'm2', 'm3']
    for x in values:
        q.put(x)
        print('write子进程%s, put value is %s' % (os.getpid(), x))
        time.sleep(1)


# TODO: 读
def read(q):
    # TODO: 消息队列不为空开始循环
    while not q.empty():
        value = q.get(block=False)
        print('read子进程%s, get value is %s' % (os.getpid(), value))
        time.sleep(1)


if __name__ == '__main__':
    q = Manager().Queue(3)
    pool = Pool(2)
    # TODO: apply同步执行，先把写入执行完毕
    pool.apply(func=write, args=(q,))
    # TODO: apply同步执行，写入执行完毕后再执行读取
    pool.apply(func=read, args=(q,))
    pool.close()
    pool.join()

    print('所有程序执行完毕...')
