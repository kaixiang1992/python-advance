"""
【csv文件处理】读取csv文件的两种方式 2019/11/13 23:57
"""
import csv
import time

# TODO: 1.读取CSV文件以列表形式
"""
csv.reader读取返回的是一个迭代器，返回的数据结构是一个列表
通过下标访问列表中的参数，默认会读取csv文件的第一行标题
跳过标题行：next(reader)
"""


def read_csv_demo1():
    with open('./stock.csv', 'r') as fp:
        # TODO: 返回的是一个迭代器
        reader = csv.reader(fp)
        # TODO: 跳过标题行
        next(reader)
        for x in reader:
            value = {
                'name': x[3],
                'volumn': x[-1]
            }
            print(value)


# TODO: 2.读取csv文件以字典形式
"""
csv.DictReader(fp)读取返回的是一个字典列表。
通过标题名获取value,默认剔除标题行数据。
"""


def read_csv_demo2():
    with open('./stock.csv', 'r') as fp:
        reader = csv.DictReader(fp)
        for index, x in enumerate(reader):
            value = {
                'name': x['secShortName'],
                'volumn': x['turnoverVol']
            }
            print(value)


if __name__ == '__main__':
    start_time = time.perf_counter()
    read_csv_demo2()
    end_time = time.perf_counter()
    print('read time {} seconds'.format(end_time - start_time))
