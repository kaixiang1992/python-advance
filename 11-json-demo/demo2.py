"""
【json文件处理】load成Python对象 2019/11/13 23:37
"""
import json

# TODO: 1.将一个json字符串load成python对象

json_str = '[{"title": "钢铁是怎么炼成的", "price": 39.8}, {"title": "西游记", "price": 28}, {"title": "三国演义", "price": 41}]'
books_list = json.loads(json_str, encoding='utf8')
print(books_list)
print('=' * 40)

# TODO: 2.直接从文件中读取json

with open('./books.json', 'r', encoding='utf8') as fp:
    books = json.load(fp)
    for book in books:
        print(book)
