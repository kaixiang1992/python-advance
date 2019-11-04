"""
【多线程】Condition版生产者与消费者模式 2019/11/04 23:50
"""

# TODO: Condition版生产者与消费者模式
"""
threading.Condition可以在没有数据的时候处于阻塞等待状态。一旦有合适的数据了，
还可以使用notify相关的函数来通知其他处于等待状态的线程。
这样就可以不用做一些无用的上锁和解锁的操作。可以提高程序的性能。
"""
"""
1.acquire：上锁。
2.release：解锁。
3.wait：将当前线程处于等待状态，并且会释放锁。
    可以被其他线程使用notify和notify_all函数唤醒。
    被唤醒后会继续等待上锁，上锁后继续执行下面的代码。
4.notify：通知某个正在等待的线程，默认是第1个等待的线程。
5.notify_all：通知所有正在等待的线程。notify和notify_all不会释放锁。并且需要在release之前调用。
"""
import threading
import random
import time

gMoney = 1000  # TODO: 预存款
gCondition = threading.Condition()  # TODO: 全局锁
gTotalTimes = 10  # TODO: 生产总次数
gTimes = 0  # TODO: 当前生产次数


# TODO: 生产者
class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100, 1000)
            # TODO: 上锁
            gCondition.acquire()
            # TODO: 超过最大生产次数
            if gTimes > gTotalTimes:
                # TODO: 释放锁
                gCondition.release()
                break
            gMoney += money
            print('%s生产者，生产了%s元，当前余额：%s元' % (threading.current_thread(), money, gMoney))
            gTimes += 1
            # TODO: 通知所有正在等待线程
            gCondition.notify_all()
            # TODO: 释放锁
            gCondition.release()
            time.sleep(0.5)


# TODO: 消费者
class Consumer(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(100, 1000)
            # TODO: 上锁
            gCondition.acquire()
            # TODO: 余额不足，这里要给个while循环判断，等待条件不满足即余额充足
            while gMoney < money:
                # TODO: 超过最大生产次数
                if gTimes > gTotalTimes:
                    # TODO: 释放锁
                    gCondition.release()
                    return
                print('%s消费者，准备消费%s元，当前余额：%s元，余额不足!' % (threading.current_thread(), money, gMoney))
                """
                将当前线程处于等待状态，并且会释放锁。
                可以被其他线程使用notify和notify_all函数唤醒。
                被唤醒后会继续等待上锁，上锁后继续执行下面的代码。
                """
                gCondition.wait()
            gMoney -= money
            print('%s消费者，消费了%s元，剩余%s元' % (threading.current_thread(), money, gMoney))
            # TODO: 释放锁
            gCondition.release()
            time.sleep(0.5)


def main():
    # TODO: 3个消费者
    for x in range(3):
        t = Consumer()
        t.start()

    # TODO: 5个生产者
    for x in range(5):
        t = Producer()
        t.start()


if __name__ == '__main__':
    main()
