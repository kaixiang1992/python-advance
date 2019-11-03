"""
【多线程】多线程概念和threading模块介绍 2019/11/03 09:55
"""
import threading
import time


# TODO：多线程

# TODO: 传统模式
# def coding():
#     for x in range(3):
#         print('正在写代码%s' % x)
#         time.sleep(1)
#
#
# def drawing():
#     for x in range(3):
#         print('正在画画%s' % x)
#         time.sleep(1)
#
#
# def main():
#     coding()
#     drawing()
#
#
# if __name__ == '__main__':
#     main()


# TODO: 多线程模式
def coding():
    for x in range(3):
        print('正在写代码%s' % x)
        time.sleep(1)


def drawing():
    for x in range(3):
        print('正在画画%s' % x)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=drawing)

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
    print('所有程序均执行完毕...')
