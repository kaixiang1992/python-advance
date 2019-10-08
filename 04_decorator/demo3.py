"""
【Python装饰器】被装饰的函数带有参数 2019/10/08 23:47
"""

user = {
    'is_login': True
}


# TODO: TypeError: 'NoneType' object is not callable
# TODO: None对象不能被调用，即装饰器没有进行return warpper返回，没有进行return返回
# 相当于return None
def login_required(func):
    def warpper(*args, **kwargs):
        if user.get('is_login'):
            func(*args, **kwargs)
        else:
            print('跳转到登录页面...')

    # return None
    return warpper


@login_required
def edit_user(username):
    print('新用户名：%s，修改成功...' % username)


@login_required
def add_article(title, content):
    print('文章标题：%s' % title)
    print('文章内容：%s' % content)
    print('文章发布成功...')


edit_user('zhiliao')
# TODO: 相当于下句执行代码...
login_required(edit_user)('zhiliao')

# TODO: 执行顺序
# TODO: 1.edit_user ==> login_required(edit_user) ==> 相当于得到warpper函数体
# TODO: 2.edit_user('zhiliao') ==> login_required(edit_user)('zhiliao') ==> 相当于warpper('zhiliao')

add_article('锄禾', '锄禾日当午...')
