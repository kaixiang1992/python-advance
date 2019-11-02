"""
【Python多任务编程】Process进程间通信 2019/11/02 17:30
"""

# TODO: Process进程间通信
"""
使用Process做子进程
使用Queue来做消息队列
"""
from multiprocessing import Process, Queue
import os
import time


# TODO: 写
def write(q):
    values = ['m1', 'm2', 'm3']
    for x in values:
        q.put(x)
        print('write子进程%s put value is %s' % (os.getpid(), x))
        time.sleep(1)


# TODO: 读
def read(q):
    while True:
        try:
            # TODO: 读取消息队列中值，非阻塞模式，读取不到立马抛出异常退出循环
            value = q.get(block=False)
            print('read子进程%s put value is %s' % (os.getpid(), value))
            time.sleep(1)
        except Exception as error:
            break


if __name__ == '__main__':
    q = Queue(3)
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    # TODO: 先put到消息队列
    pw.start()
    # TODO: 在从消息队列中get
    pr.start()

    pw.join()

    print('所有程序执行完毕...')
