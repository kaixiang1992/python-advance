"""
【多线程】Lock版生产者和消费者模式 2019/11/04 21:00
"""

"""
生产者和消费者模式是多线程开发中经常见到的一种模式。生产者的线程专门用来生产一些数据，然后存放到一个中间的变量中。
消费者再从这个中间的变量中取出数据进行消费。
但是因为要使用中间变量，中间变量经常是一些全局变量，因此需要使用锁来保证数据完整性。
以下是使用threading.Lock锁实现的“生产者与消费者模式”的一个例子
"""

# TODO: Lock版生产者和消费者模式

import threading
import random
import time

gMoney = 1000  # TODO: 预存款
gLock = threading.Lock()  # TODO: 全局锁
gTotalTimes = 10  # TODO: 生产总次数
gTimes = 0  # TODO: 当前生产次数


# TODO: 生产者
class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            # TODO: 超过生产总次数不予生产，并释放锁
            if gTimes > gTotalTimes:
                gLock.release()
                break
            gMoney += money
            gTimes += 1
            print('生产者：%s，生产了%s元，当前余额：%d' % (threading.current_thread(), money, gMoney))
            gLock.release()
            time.sleep(0.5)


# TODO: 消费者
class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            gLock.acquire()
            # TODO: 余额正常
            if gMoney >= money:
                gMoney -= money
                print('消费者：%s，消费了%s元，当前余额：%d' % (threading.current_thread(), money, gMoney))
            else:
                # TODO: 超过生产总次数不予消费，并释放锁
                if gTimes > gTotalTimes:
                    gLock.release()
                    break
                # TODO: 余额不足不予消费，并释放锁
                print('消费者：%s，消费了%s元，当前余额：%d，余额不足' % (threading.current_thread(), money, gMoney))
                gLock.release()
                break
            gLock.release()
            time.sleep(0.5)


def main():
    # TODO: 5个生产者
    for x in range(5):
        t = Producer(name='生产者%s线程' % x)
        t.start()

    # TODO: 3个消费者
    for x in range(3):
        t = Consumer(name='消费者%s线程' % x)
        t.start()


if __name__ == '__main__':
    main()
