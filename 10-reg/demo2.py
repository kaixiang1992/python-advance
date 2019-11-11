"""
【正则表达式】转义字符和原生字符串 2019/11/10 18:20
"""
import re

# TODO: 1.转义字符
"""
在正则表达式中，有些字符是有特殊意义的字符。因此如果想要匹配这些字符，
那么就必须使用反斜杠进行转义。比如$代表的是以...结尾，如果想要匹配$，那么就必须使用\$
"""

# text = 'apple price is $299'
# ret = re.search('\$\d+', text)
# print(ret.group())


# TODO: 2.原生字符串
"""
在正则表达式中，\是专门用来做转义的。在Python中\也是用来做转义的。
因此如果想要在普通的字符串中匹配出\，那么要给出四个\。
"""

# text = '\\n'
# ret = re.match('\\\\n', text)
# # TODO: \n
# print(ret.group())


# TODO: 使用原生字符串

text = r'\n'
ret = re.match(r'\\n', text)
# TODO: \n
print(ret.group())
