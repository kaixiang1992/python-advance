"""
【正则表达式】实战-古诗文网爬虫实战 2019/11/12 23:03
"""

import requests
import re
import json

"""
re.DOTALL: 让.匹配所有任意字符串包括\n换行
"""

POETRY_LIST = []


# TODO: 解析URL
def page_parse(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
    }
    res = requests.get(url, headers=headers).text
    # TODO: 标题
    """
    class=cont的div下的第一个b标签为标题 非贪婪模式只匹配一次
    """
    titles = re.findall(r'<div\s+class="cont">.*?<b>(.*?)</b>', res, re.DOTALL)
    # TODO: 朝代
    """
    class=source的p下的第一个a标签为朝代 非贪婪模式只匹配一次
    """
    dynasties = re.findall(r'<p\s+class="source">.*?<a.*?>(.*?)</a>', res, re.DOTALL)
    # TODO: 作者
    """
    class=source的p下的第二个a标签为作者 非贪婪模式只匹配一次
    """
    authors = re.findall(r'<p\s+class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', res, re.DOTALL)
    # TODO: 内容
    """
    class="contson"的div下的内容
    """
    textlist = []
    contents = re.findall(r'<div\s+class="contson".*?>(.*?)</div>', res, re.DOTALL)
    for content in contents:
        """
        循环剔除剩余<p>、<br>标签
        """
        text = re.sub(r'<.*?>', '', content).strip()
        # TODO: 去除空格或换行符等
        text = re.sub('\s', '', text)
        textlist.append(text)

    pantries_zip = zip(titles, dynasties, authors, textlist)
    global POETRY_LIST
    for poetry in pantries_zip:
        title, dynasty, author, text = poetry
        POETRY_LIST.append({
            'title': title,
            'dynasty': dynasty,
            'author': author,
            'text': text
        })


# TODO: 主进程函数
def main():
    for x in range(1, 11):
        url = 'https://so.gushiwen.org/shiwen/default_0AA{}.aspx'.format(x)
        page_parse(url)
    print('下载古诗文完毕...')
    with open('./pantries.json', 'w', encoding='utf8') as fp:
        json.dump(POETRY_LIST, fp, ensure_ascii=False)


if __name__ == '__main__':
    main()
