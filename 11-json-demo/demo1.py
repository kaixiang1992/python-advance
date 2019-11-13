"""
【json文件处理】dump成json字符串以及编码问题 2019/11/13 23:05
"""

import json

books = [
    {
        'title': '钢铁是怎么炼成的',
        'price': 39.8
    },
    {
        'title': '西游记',
        'price': 28
    },
    {
        'title': '三国演义',
        'price': 41
    }
]

json_str = json.dumps(books, ensure_ascii=False)
print(json_str)
print('=' * 40)

# TODO: 将JSON直接dump到文件中

with open('books.json', 'w', encoding='utf8') as fp:
    json.dump(books, fp, ensure_ascii=False)
