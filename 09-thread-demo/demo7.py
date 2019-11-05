"""
【多线程】实战-下载表情包之同步爬虫完成 2019/11/05 22:59
"""
import requests
from lxml import etree
import re
import os
from urllib import request


# TODO: 同步爬虫

def parse_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/77.0.3865.75 Safari/537.36 '
    }
    res = requests.get(url, headers=headers)
    # TODO: 解析html
    html = etree.HTML(res.text)
    # TODO: 获取class = "page-content text-center"的div下，img的class不等于gif的img标签
    images = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
    # TODO: 遍历img标签
    for image in images:
        # TODO: 获取图片地址
        img_url = image.get('data-original')
        # TODO: 获取图片alt当做图片名称
        alt = image.get('alt')
        try:
            alt = re.sub(r"[\?？\.，,。！!]", "", alt)
            # TODO: 获取图片扩展名
            img_ext = os.path.splitext(img_url)[1]
            # TODO: 重新设置图片名称
            img_filename = alt + img_ext
            # TODO: 下载存储图片
            request.urlretrieve(img_url, './images/%s' % img_filename)
        except Exception as error:
            print(error)
            print(alt)
            continue


def main():
    for x in range(1, 100):
        url = 'https://www.doutula.com/photo/list/?page=%d' % x
        parse_page(url)


if __name__ == '__main__':
    main()
