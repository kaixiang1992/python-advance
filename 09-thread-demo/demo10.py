"""
【多线程】作业-多线程下载百思不得姐段子爬虫作业 2019/11/06 23:08
"""

import threading
from queue import Queue
import requests
from lxml import etree
import csv


# TODO: 生产者
class Producer(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
    }
    domain = 'http://www.budejie.com'

    def __init__(self, page_queue, joke_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.joke_queue = joke_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                # break
                return
            # TODO: 获取最后一条URL地址
            url = self.page_queue.get()
            # TODO: 获取GET响应消息
            res = requests.get(url, headers=self.headers)
            # TODO: 获取HTML内容
            html = etree.HTML(res.text)
            # TODO: 获取段子a 标签
            a_tag = html.xpath('//div[@class="j-r-list"]//div[@class="j-r-list-c-desc"]//a')
            # TODO: 循环本页所有的a标签
            for a in a_tag:
                # TODO: 获取a标签链接
                href = self.domain + a.get('href')
                # TODO: 获取a内文本
                text = a.xpath('.//text()')
                # TODO: 拼接text 列表去掉左右空格
                jokes = '\n'.join(text).strip()
                # TODO: 段子消息队列添加数据
                self.joke_queue.put((href, jokes))


# TODO: 消费者
class Consumer(threading.Thread):
    def __init__(self, page_queue, joke_queue, gLock, writer, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.joke_queue = joke_queue
        self.gLock = gLock
        self.writer = writer

    def run(self):
        while True:
            # TODO: 页面URL消息队列 + 段子消息队列 都为空退出循环
            if self.page_queue.empty() and self.joke_queue.empty():
                # break
                return
            # TODO: 获取最后一条数据 href+jokes
            href, jokes = self.joke_queue.get()
            # TODO: 加锁
            self.gLock.acquire()
            # TODO: 写入csv数据
            self.writer.writerow((jokes, href))
            # TODO: 释放锁
            self.gLock.release()
            print('%s 写入成功...' % href)


def main():
    # TODO: 页面URL消息队列
    page_queue = Queue(10)
    # TODO: 段子消息队列
    joke_queue = Queue(50)
    # TODO: 全局锁
    gLock = threading.Lock()
    # TODO: csv文件
    fp = open('bsbdj.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(fp)
    # TODO: 写入csv title
    writer.writerow(('content', 'link'))

    # TODO: 存取10页URL
    for x in range(1, 11):
        url = 'http://www.budejie.com/text/%d' % x
        page_queue.put(url)

    # TODO: 5个生产者
    for x in range(5):
        t = Producer(page_queue, joke_queue)
        t.start()

    # TODO: 5个消费者
    for x in range(5):
        t = Consumer(page_queue, joke_queue, gLock, writer)
        t.start()


if __name__ == '__main__':
    main()
