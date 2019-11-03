"""
【多线程】使用Thread类创建多线程 2019/11/03 23:25
"""

# TODO: 1.查看线程数
"""
使用threading.enumerate()函数便可以看到当前线程的数量。
"""

# TODO: 2.查看当前线程名字
"""
使用threading.current_thread()可以看到当前线程的信息。
"""

# TODO: 3.继承自threading.Thread类
"""
为了让线程代码更好的封装。可以使用threading模块下的Thread类，继承自这个类，
然后实现run方法，线程就会自动运行run方法中的代码。
"""

import threading
import time


class codingThrad(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在写代码%s，当前线程信息: %s' % (x, threading.current_thread()))
            print('当前线程总数： %s' % threading.enumerate())
            time.sleep(1)


class drawingThread(threading.Thread):
    def run(self):
        for x in range(3):
            print('正在画画%s，当前线程信息：%s' % (x, threading.current_thread()))
            print('当前线程总数： %s' % threading.enumerate())
            time.sleep(1)


def main():
    t1 = codingThrad()
    t2 = drawingThread()

    print('当前线程总数： %s' % threading.enumerate())

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
