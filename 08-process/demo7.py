"""
【Python多任务编程】Queue消息队列 2019/11/02 16:16
"""

# TODO: Queue消息队列
"""
进程之间数据都是不共享的，因此想要在两个进程之间使用相同的数据，那么这时候就需要使用进程间的通信
"""

# TODO: Queue
"""
1.Queue(count)：初始化一个消息队列，并指定这个队列中最多拥有多少条消息。
2.put(obj, [block, timeout]):
    推入一条消息到队列中。默认是阻塞的，也就是说如果这个消息队列中已经满了，那么会一直等待，将这个消息添加到消息队列中。
    可选参数：
    block: 
        默认True：阻塞， 
        False：不阻塞，如果消息队列是满的，那么立马抛出异常 --> q.put('m3', block=False)
    timeout: 指定阻塞最长的时间，如果超过这个时间消息队列还是满的，就会抛出异常。
        q.put('m3', timeout=2)
3.put_nowait(obj): 非阻塞的推送一条消息到队列，如果这个队列已经满了，那么会立马抛出异常。
    语法相当于：q.put('m3', block=False)
4.qsize()：获取这个消息队列的消息数量。
5.full()：判断这个消息队列是否满了。
6.empty()：判断这个消息队列是否空了。
7.get([block, timeout]): 获取队列中的一条消息，然后将其从队列中删除。
    可选参数：
    block: 
        默认为True：阻塞
        False: 不阻塞，如果没有值，立马抛出异常 --> q.get(block=False)
    timeout:
        指定如果多久没有获取到值后抛出异常 --> q.get(timeout=2)
"""

from multiprocessing import Queue

# TODO: 初始化3条消息队列
q = Queue(3)

# TODO: put
q.put([1, 2, 3])
q.put('m1')
q.put('m2')
"""
超过2秒队列还是满的，直接抛出异常
"""
# q.put('m3', timeout=2)

# TODO: put_nowait()
# q.put_nowait([1, 2, 3])
# q.put_nowait('m1')
# q.put_nowait('m2')

# TODO: qsize()
"""
读取消息队列消息数量
"""
print(q.qsize())  # TODO: 3

# TODO: full()
"""
消息队列是否满员
"""
print('q full() value is %s' % q.full())  # TODO: True

# TODO: empty()
"""
是否为空
"""
print('q empty() value is %s' % q.empty())  # TODO: False

# TODO: get()
# print('get.........')
# print(q.get())
# print(q.get())
# print(q.get())

# TODO: empty()
"""
是否为空
"""
# print('q empty() value is %s' % q.empty())  # TODO: False
