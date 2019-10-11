"""
【Python装饰器】装饰器实现Flask的url映射 2019/10/11 23:04
"""

from functools import wraps

user = {
    'is_login': True
}


# TODO: 未加wraps装饰器将返回命名异常
# NameError: name 'wrapper' is not defined
def login_require(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if user.get('is_login'):
            return func(*args, **kwargs)
        else:
            print('未登录，跳转到登录页面')

    return wrapper

class Flask(object):
    def __init__(self):
        self.url_views_maps = {}

    def route(self, url):
        def outer_wrapper(func):
            self.url_views_maps[url] = func.__name__

            def inner_wrapper(*args, **kwargs):
                func(*args, **kwargs)
            return inner_wrapper

        return outer_wrapper

    def run(self):
        """
        key is /，value is hello
        key is /list，value is article_list
        key is /edit，value is edit_user
        """
        # for key, value in self.url_views_maps.items():
        #     print('key is %s，value is %s' % (key, value))

        while True:
            option = input('请输入地址路径：')
            views = self.url_views_maps.get(option)
            if views:
                exec(views + '()')
            else:
                print('很抱歉，您要访问的页面不存在！...')


app = Flask()


@app.route('/')
# TODO: 相当于执行:
# outer_wrapper(hello)()
def hello():
    print('hello world!...')


@app.route('/list')
# TODO: 相当于执行:
# outer_wrapper(article_list)()
def article_list():
    print('文章列表...')

@app.route('/edit')
@login_require
# TODO: 先执行@login_require，再执行@app.route('/edit')，从内到外执行
# TODO: 相当于执行：
# TODO: 1. login_require(edit_user)经@wraps(func)包装后 => 返回 edit_user
# TODO: 2. app.route('/edit') => 返回 outer_wrapper 传入func后 => outer_wrapper(edit_user)
# TODO: 3. 最终相当于 outer_wrapper(edit_user)()
def edit_user():
    print('修改用户名成功...')


if __name__ == '__main__':
    app.run()
