"""
【csv文件处理】写入csv文件的两种方式 2019/11/14 00:27
"""
import csv

# TODO: 1.写入数据到csv文件以元祖形式
"""
newline默认换行写入，设置为不换行写入为：newline=''
创建一个writer对象，主要用到两个方法:
1. writerow，这个是写入一行.
2. 一个是writerows，这个是写入多行.
"""


def writer_csv_demo1():
    headers = ['student_name', 'age', 'height', 'weight']
    values = [
        ('张三', 19, '175cm', '60kg'),
        ('李四', 20, '165cm', '70kg'),
        ('王五', 18, '185cm', '80kg')
    ]
    with open('./classroom1.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        # TODO: 写入表头
        writer.writerow(headers)
        # TODO: 写入表数据
        writer.writerows(values)


# TODO: 2.写入数据到csv文件以字典形式
"""
创建一个DictWriter对象，主要用到三个方法：
1. writeheader() 写入表头无需传递任何参数.
2. writerow，写入一行数据.
3. writerows，写入多行数据.
"""


def writer_csv_demo2():
    headers = ['student_name', 'age', 'height', 'weight']
    values = [
        {'student_name': '张三', 'age': 18, 'height': '175cm', 'weight': '60kg'},
        {'student_name': '李四', 'age': 20, 'height': '165cm', 'weight': '70kg'},
        {'student_name': '王五', 'age': 19, 'height': '185cm', 'weight': '80kg'}
    ]
    with open('./classroom2.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.DictWriter(fp, headers)
        # TODO: 写入表头数据的时候，需要调用writeheader()方法
        writer.writeheader()
        # TODO: 写入数据
        writer.writerows(values)


if __name__ == '__main__':
    writer_csv_demo2()
