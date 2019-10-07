"""
【Python生成器】生成器小案例 2019/10/07 14:51
"""

# from collections import Iterable,Iterator

#TODO: 生成器中的return语句会触发StopIterator异常:

# def my_gen(start):
#     while start < 10:
#         yield start
#         start += 1
#         return 'hello world!'

# ret = my_gen(1)
# print(next(ret))
# try:
#     next(ret)
# except Exception as error:
#     print('error msg：')
#     print(error)

# TODO: 斐波那契数列
# TODO: 第一轮
# 0 1 1 2 3 5 8 13 21 34
# a b
#   c
# TODO: 第二轮
# 0 1 1 2 3 5 8 13 21 34
#   a b
#     c

#TODO: 普通while循环实现
def basis_my_gen(count):
    index = 1
    a,b = 0,1
    while index <= count:
        print(b, end=" ")
        # TODO: 临时变量c保存变量b的值
        c = b
        b = a + b
        a = c
        index += 1

basis_my_gen(10)
print("")
print('='*30)

#TODO: 生成器版本实现斐波那契数列

def fib(count):
    index = 1
    a,b = 0,1
    while index <= count:
        yield b
        c = b
        b = a + b
        a = c
        index += 1

ret = fib(10)
for x in ret:
    print(x, end=" ")

print("")
print('='*30)
print('多任务切换示例：')

def qq_music(duration):
    time = 0
    while time <= duration:
        print('QQ音乐播放第%d分钟...'%(time, ))
        yield None
        time += 1

def youku_movie(duration):
    time = 0
    while time <= duration:
        print('优酷电影播放第%d分钟...'%(time, ))
        yield None
        time += 1

def main():
    music = qq_music(15)
    movie = youku_movie(60)
    # TODO: 音乐、电影是否播放结束
    music_isend = False
    movie_isend = False
    while True:
        try:
            next(music)
        except Exception:
            music_isend = True
        
        try:
            next(movie)
        except Exception:
            movie_isend = True
        
        if music_isend and movie_isend:
            print('多任务切换执行完毕....')
            break

if __name__ == '__main__':
    main()