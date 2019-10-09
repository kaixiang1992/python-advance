"""
【Python装饰器】给装饰器传递参数 2019/10/09 22:59
"""

user = {
    'is_login': True
}


def login_required(site='front'):
    def outer_wrapper(func):
        def inner_wrapper(*args, **kwargs):
            if user.get('is_login'):
                func(*args, **kwargs)
            else:
                if site == 'front':
                    print('跳转到前台登录页面...')
                else:
                    print('跳转到后台登录页面...')

        return inner_wrapper

    return outer_wrapper


@login_required('backend')
def edit_user(username):
    print('新用户名为：%s，修改用户名成功!...' % username)


# TODO:执行顺序分解
# 1. login_required('front')执行返回outer_wrapper
# 2. outer_wrapper('edit_user')执行返回inner_wrapper
# 3. inner_wrapper('zhiliao')执行内部程序代码

edit_user('zhiliao')
