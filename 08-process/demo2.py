"""
【Python多任务编程】join阻塞方法 2019/11/01 22:36
"""

# TODO: 1.父进程会等待子进程执行完毕后再退出
"""
如果在父进程中执行完所有代码后，还有子进程在执行，那么父进程会等待子进程执行完所有代码后再退出。
"""

# TODO: 2.Process对象的join方法
"""
使用Process创建了子进程，调用start方法后，父子进程会在各自的进程中不断的执行代码。
有时候如果想等待子进程执行完毕后再执行下面的代码，那么这时候可以调用join方法。

join方法还可以传一个timeout，用来指定等待的最长时间。
"""

from multiprocessing import Process
import time


def zhiliao():
    for x in range(0, 6):
        print('子进程执行：%s' % x)
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=zhiliao)
    p.start()

    print('主进程执行中...')

    # TODO: 主进程阻塞，等待子进程完成才执行下面的代码
    p.join()
    # TODO: 等3秒子进程执行代码后往下面执行
    # p.join(3)

    print('所有程序执行完毕退出...')
