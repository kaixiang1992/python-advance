"""
【多线程】实战-下载表情包之异步爬虫完成 2019/11/06 00:06
"""

import threading
import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue
import time


class Producer(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

    # TODO: 重写__init__方法
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        # TODO: 调用父类init方法
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    # TODO: run方法
    def run(self):
        while True:
            # TODO: 页面url消息队列空退出循环
            if self.page_queue.empty():
                print(2)
                break
            # TODO: 获取最后一条url地址
            url = self.page_queue.get()
            # TODO: 解析URL HTML内容+添加img地址消息队列数据
            self.page_parse(url)

    # TODO: 解析URL HTML内容+添加img地址消息队列数据
    def page_parse(self, url):
        res = requests.get(url, headers=self.headers)
        # TODO: 解析html
        html = etree.HTML(res.text)
        # # TODO: 获取class = "page-content text-center"的div下，img的class不等于gif的img标签
        images = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
        # TODO: 遍历img标签
        # print(id(self.img_queue))
        for image in images:
            # TODO: 获取图片地址
            img_url = image.get('data-original')
            # TODO: 获取图片alt当做图片名称
            alt = image.get('alt')
            try:
                # TODO: alt非法字符处理
                alt = re.sub(r"[\?？\.，,。！!*]", "", alt)
                # TODO: 获取图片扩展名
                img_ext = os.path.splitext(img_url)[1]
                # TODO: 重新设置图片名称
                img_filename = alt + img_ext
                # TODO: img地址+名称存入消息队列
                self.img_queue.put((img_url, img_filename))
            except Exception as error:
                print(error)
                continue


class Consumer(threading.Thread):
    # TODO: 重写__init__方法
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        # TODO: 调用父类init方法
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    # TODO: run方法
    def run(self):
        while True:
            # TODO: 页面url消息队列 + img地址消息队列 都为空 退出循环
            if self.img_queue.empty() and self.page_queue.empty():
                print(1)
                break
            # TODO: 从消息队列获取最后一条数据
            img_url, img_filename = self.img_queue.get()
            # TODO: 下载存储图片
            request.urlretrieve(img_url, './images/%s' % img_filename)
            print('%s 下载完成..' % img_filename)


def main():
    # TODO: 页面url消息队列
    page_queue = Queue(100)
    # TODO: img地址消息队列
    img_queue = Queue(500)
    for x in range(1, 101):
        url = 'https://www.doutula.com/photo/list/?page=%d' % x
        # TODO: 将页面url地址存入队列
        page_queue.put(url)

    print(page_queue.qsize())
    # TODO: 5个生产者
    for x in range(5):
        t = Producer(page_queue, img_queue)
        t.start()

    # TODO: 5个消费者
    for x in range(5):
        t = Consumer(page_queue, img_queue)
        t.start()


if __name__ == '__main__':
    main()
