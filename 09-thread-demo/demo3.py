"""
【多线程】多线程共享全局变量以及锁机制 2019/11/03 23:50
"""

# TODO: 多线程共享全局变量的问题
"""
多线程都是在同一个进程中运行的。因此在进程中的全局变量所有线程都是可共享的。
这就造成了一个问题，因为线程执行的顺序是无序的。有可能会造成数据错误。
"""
# TODO: 锁机制
"""
为了解决以上使用共享全局变量的问题。threading提供了一个Lock类，
这个类可以在某个线程访问某个变量的时候加锁，其他线程此时就不能进来，
直到当前线程处理完后，把锁释放了，其他线程才能进来处理。
加锁： gLock.acquire()
释放锁： gLock.release()
"""
import threading

VALUE = 0
gLock = threading.Lock()


def add_value():
    global VALUE
    gLock.acquire()
    for x in range(100000):
        VALUE += 1
    gLock.release()
    print(VALUE)


def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()


if __name__ == '__main__':
    main()
