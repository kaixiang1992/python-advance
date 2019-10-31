"""
【Python魔术方法】with语句魔术方法 2019/10/31 22:42
"""

"""
会话控制器:
它通过控制两个魔术方法：__enter__(self)以及__exit__(self,exception_type,exception_value,traceback)
来定义一个代码块被执行或者终止后会话管理器应该做什么。
他可以被用来处理异常，清除工作或者做一些代码块执行完毕之后的日常工作。
如果代码执行成功，没有任何异常，那么exception_type、exception_value以及traceback将会是None。
否则的话你可以选择处理这个异常或者是直接交给用户处理。
如果你想处理这个异常的话，那么必须在__exit__在所有结束之后返回True
"""


class FileOpener(object):
    def __init__(self, filename, mode, encoding):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.fp = open(self.filename, self.mode, encoding=self.encoding)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()
        print(exc_type) # TODO: <class 'ZeroDivisionError'>
        print(exc_val)  # TODO: division by zero
        print(exc_tb)   # TODO: <traceback object at 0x00933D50>
        return True


with FileOpener('abc.txt', 'w', 'utf-8') as fp:
    fp.write('hello world!...')
    a = 0
    b = 1
    c = b / a
    print(c)
