"""
【正则表达式】单字符匹配规则 2019/11/09 15:13
"""
import re

# TODO: 1.匹配某个字符串
"""
不能匹配以回车、制表符、换行符为开头的转义符

text = '\ra'
ret = re.match('a', text)
# TODO: AttributeError: 'NoneType' object has no attribute 'group'
print(ret.group())
"""

# text = 'hello'
# ret = re.match('he', text)
# # TODO: he
# # TODO: AttributeError: 'NoneType' object has no attribute 'group'
# print(ret.group())


# TODO: 2.点.匹配任意的字符
"""
不能匹配以回车、制表符、换行符为开头的转义符

text = '\na'
ret = re.match('.', text)
# TODO: AttributeError: 'NoneType' object has no attribute 'group'
print(ret.group())
"""

# text = '\na'
# ret = re.match('.', text)
# # TODO: a
# print(ret.group())

# TODO: 3.\d匹配任意的数字
"""
\d：匹配0-9的数字不能匹配负数

text = '-1'
ret = re.match('\d', text)
# TODO: AttributeError: 'NoneType' object has no attribute 'group'
print(ret.group())
"""

# text = '-1'
# ret = re.match('\d', text)
# # TODO: 1
# print(ret.group())


# TODO: 4.\D匹配任意的非数字
"""
如果匹配的是一个数字，那么匹配就不成功

text = '5'
ret = re.match('\D', text)
# TODO: AttributeError: 'NoneType' object has no attribute 'group'
print(ret.group())
"""

# text = 'a'
# ret = re.match('\D', text)
# # TODO: a
# print(ret.group())


# TODO: 5. \s匹配的是空白字符(\n,\t,\r和空格)

# text = '\n'
# ret = re.match('\s', text)
# # TODO: 空白
# print(ret.group())


# TODO: 6.\w匹配的是a-z和A-Z以及数字和下划线
"""
TODO: 如果匹配一个其他的字符，那么就匹配不到

text = '——'
ret = re.match('\w', text)
# TODO: AttributeError: 'NoneType' object has no attribute 'group'
print(ret.group())
"""

# text = '——'
# ret = re.match('\w', text)
# print(ret.group())


# TODO: 7.\W匹配的是非a-z和A-Z以及数字和下划线
"""
\W匹配的是和\w相反的
"""

# text = '++'
# ret = re.match('\W', text)
# print(ret.group())

# TODO: 8.[]组合的方式，只要满足中括号中的某一项都算匹配成功

# text = '0371-8888888'
# # TODO: 匹配\d数字 或 -
# ret = re.match('[\d\-]', text)
# print(ret.group())


# TODO: 8.1 以组合的方式实现\d匹配

# text = '9'
# ret = re.match('[0-9]', text)
# print(ret.group())


# TODO: 8.2 以组合的方式实现\D匹配
# text = 'a'
# ret = re.match('[^0-9]', text)
# print(ret.group())


# TODO: 8.3 以组合的方式实现\w匹配
# text = '_'
# ret = re.match('[\da-zA-Z\_]', text)
# print(ret.group())

# TODO: 8.4 以组合的方式实现\W匹配

# text = '--'
# ret = re.match('[^\da-zA-Z\_]', text)
# print(ret.group())


############TODO: 160.【正则表达式】匹配多个字符 2019/11/09 16:32 ###################

# TODO: 9. *: 可以匹配0或者多个字符
"""
TODO: 可有可无，多了不限

匹配不成功，不会抛出异常返回空字符串
"""

# text = 'a1234'
# ret = re.match('\d*', text)
# print(ret.group())


# TODO: 10. +: 可以匹配1个或者多个字符。
"""
最少1个,多了不限

因为匹配的是\w，那么就要求是英文字符，后面跟了一个加号，
意味着最少要有一个满足\w的字符才能够匹配到。
如果text是一个空白字符或者是一个不满足\w的字符，那么就会报错

匹配不成功，会抛出异常
text = '--abc'
ret = re.match('\w+', text)
# TODO: AttributeError: 'NoneType' object has no attribute 'group'
print(ret.group())
"""

# text = '_1abcA'
# ret = re.match('\w+', text)
# # TODO: _1abcA
# print(ret.group())

# TODO: 11. ?: 匹配的字符可以出现一次或者不出现(0或者1)
"""
可有可无，最多一次

匹配不到不会抛出异常
"""

# text = 'A123'
# ret = re.match('\d?', text)
# # TODO: 1
# print(ret.group())


# TODO: 12.{m}: 匹配m个字符
"""
text = '!!abcd123'
ret = re.match('\w{4}', text)
# TODO: AttributeError: 'NoneType' object has no attribute 'group'
print(ret.group())
"""

# text = 'abcd123'
# ret = re.match('\w{5}', text)
# print(ret.group())


# TODO: 13.{m,n}: 匹配m-n个字符，在这中间的字符都可以匹配到
"""
字符串不满足条件时，抛出异常

text = '1'
# TODO: 匹配至少3位，最多9位字符串
ret = re.match('\d{3, 9}', text)
# TODO: AttributeError: 'NoneType' object has no attribute 'group'
print(ret.group())
"""

# text = '1'
# ret = re.match('\d{3, 9}', text)
# print(ret.group())

# text = '2345661'
# ret = re.match('\d{1,3}', text)
# # TODO: 234
# print(ret.group())


############ TODO: 161.【正则表达式】常用匹配小案例 2019/11/09 17:28 ##############

# TODO: 14.验证手机号码
"""
手机号码的规则是以1开头，第二位可以是34587，后面那9位就可以随意了。

不满足条件的手机号码，抛出异常
AttributeError: 'NoneType' object has no attribute
"""

# text = '17355667788'
# ret = re.match('1[34587]\d{9}', text)
# # TODO: 17355667788
# print(ret.group())


# TODO: 15. 验证邮箱
"""
验证邮箱：邮箱的规则是邮箱名称是用数字、字母、下划线组成的，然后是@符号，后面就是域名了。

不满足匹配条件，直接抛出异常
AttributeError: 'NoneType' object has no attribute 'group'
"""

# text = 'test_python123@qq.com'
# ret = re.match('\w+\@[a-z0-9]+\.[a-z]+', text)
# # TODO: test_python123@qq.com
# print(ret.group())


# TODO: 16.验证URL
"""
URL的规则是前面是http或者https或者是ftp
然后再加上一个冒号，再加上一个斜杠，
再后面就是可以出现任意非空白字符了。
匹配任意非空白字符： ^\s
"""

# text = 'https://www.baidu.com'
# ret = re.match('(http|https|ftp)\:\/\/[^\s]+', text)
# # TODO: https://www.baidu.com
# print(ret.group())


# TODO: 17.验证身份证
"""
身份证的规则是，总共有18位，前面17位都是数字，
后面一位可以是数字，也可以是小写的x，也可以是大写的X。
"""

# text = '31131119890812323X'
# ret = re.match('\d{17}[0-9xX]', text)
# # TODO: 31131119890812323X
# print(ret.group())

########### TODO: 【正则表达式】开始结束和或语法 2019/11/09 20:12 #################

# TODO: 18.^脱字号: 表示以..开始
"""
^如果在中括号中代表取反操作
"""

# text = 'hello'
# ret = re.match('^h', text)
# # TODO: h
# print(ret.group())


# TODO: 19.$ 表示以...结束

# text = 'test_email@163.comaaeaer'
# ret = re.match('\w+\@[0-9a-z]+\.[a-z]+', text)
# # TODO: test_email@163.comaaeaer
# print(ret.group())

# 匹配163.com的邮箱
# text = 'test_email@163.com'
# ret = re.match('\w+\@163\.com$', text)
# # TODO: test_email@163.com
# print(ret.group())


# TODO: 20. |: 匹配多个表达式或者字符串

# text = 'https'
# ret = re.match('(https|ftp)', text)
# print(ret.group())


# TODO: 21.贪婪模式和非贪婪模式
"""
贪婪模式：正则表达式会匹配尽量多的字符。默认是贪婪模式。
非贪婪模式：正则表达式会匹配尽量少的字符。

非贪婪模式使用：
在* + ?后面使用?即可, 非贪婪模式按照最小条件输出
例： 
+: 最少一个，多了不限。按照最少一个输出。
"""

# text = '0123456'
# ret = re.match('\d+', text)
# # TODO: 默认采用贪婪模式，输出：0123456
# print(ret.group())


# TODO: 切换非贪婪模式

# text = '0123456'
# ret = re.match('\d+?', text)
# # TODO: 改成非贪婪模式，输出0
# print(ret.group())

# TODO: 22.匹配0-100之间的数字
"""
可以匹配项：1, 11, 99, 100
不可以匹配项： 0, 09, 101
一位整数数限制为：1-9
两位整数限制为：10-99
三位整数限制为：100
"""

text = '100'
ret = re.match('[1-9]\d?$|100$', text)
print(ret.group())