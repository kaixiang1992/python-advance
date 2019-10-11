"""
【Python装饰器】装饰器实现Flask的url映射
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello world'


@app.route('/list')
def article_list():
    return '文章列表'


if __name__ == '__main__':
    app.run()
