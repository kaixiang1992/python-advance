"""
【多线程】Queue线程安全队列讲解 2019/11/05 22:17
"""

# TODO: Queue线程安全队列
"""
在线程中，访问一些全局变量，加锁是一个经常的过程。如果你是想把一些数据存储到某个队列中，
那么Python内置了一个线程安全的模块叫做queue模块。Python中的queue模块中提供了同步的、
线程安全的队列类，包括FIFO（先进先出）队列Queue，LIFO（后入先出）队列LifoQueue。
这些队列都实现了锁原语（可以理解为原子操作，即要么不做，要么都做完），能够在多线程中直接使用。
可以使用队列来实现线程间的同步。
相关函数如下：
1.初始化Queue(num)：创建一个先进先出number数量的队列。
2.qsize()：返回队列的大小。
3.empty()：判断队列是否为空。
4.full()：判断队列是否满了。
5.get()：从队列中取最后一个数据。
6.put()：将一个数据放到队列中。
"""

from queue import Queue
import time
import threading

"""
q = Queue(4)
# TODO: 将一个数据放到队列中
q.put(1)
q.put(2)
q.put(3)
q.put(4)

# TODO: 返回队列的大小
print(q.qsize())  # TODO: 4
# TODO: 判断队列是否为空
print(q.empty())    # TODO: False
# TODO: 判断队列是否满了
print(q.full())    # TODO: True
# TODO: 从队列中取最后一个数据
print(q.get())  # TODO: 1

print('=' * 40)
"""


# TODO: 将数据放到队列中
def set_value(q):
    index = 0
    while True:
        q.put(index)
        index += 1
        time.sleep(3)


# TODO: 从队列中获取最后一个暑假
def get_value(q):
    while True:
        print('q.qsize(): %d, q.get(): %s' % (q.qsize(), q.get()))


def main():
    q = Queue(4)
    t1 = threading.Thread(target=set_value, args=(q,))
    t2 = threading.Thread(target=get_value, args=(q,))

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
