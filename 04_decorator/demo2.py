"""
【Python装饰器】装饰器基本使用 2019/10/08 23:13
"""

user = {
    'is_login': True
}


def case():
    def login_required(func):
        def wrapper(*args, **kwargs):
            if user.get('is_login'):
                func(*args, **kwargs)
            else:
                print('跳转到登录页面!...')
        return wrapper

    @login_required
    def edit_user():
        print('修改用户名成功!...')

    def add_article():
        print('添加文章成功!...')

    class Person(object):
        @login_required
        def greet(self):
            print('登录成功!...')

    p = Person()
    p.greet()

    edit_user()


if __name__ == '__main__':
    case()
