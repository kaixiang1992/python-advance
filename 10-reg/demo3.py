"""
TODO: 【正则表达式】group分组 2019/11/10 18:43
"""
import re

# TODO: 分组
"""
在正则表达式中，可以对过滤到的字符串进行分组。分组使用圆括号()的方式。
group()：和group(0)是等价的，返回的是整个满足条件的字符串。
groups()：返回的是里面的子组。索引从1开始。
group(1)：返回的是第一个子组，可以传入多个。如：group(1,2,3...)
"""

# text = 'apple price is $99, orange price is $10'
# ret = re.match('.*(\$\d+).*(\$\d+)', text)

# TODO: group() == group(0)，返回满足挣个条件的字符串
# TODO: apple price is $99, orange price is $10
# print(ret.group())

# TODO: $99
# print(ret.group(1))

# TODO: $10
# print(ret.group(2))

# TODO: 抛出异常：IndexError: no such group
# print(ret.group(3))

# TODO: 传入多个
# TODO: ('apple price is $99, orange price is $10', '$99', '$10')
# print(ret.group(0, 1, 2))

# TODO: groups返回里面的分组。索引从1开始
# TODO: ('$99', '$10')
# print(ret.groups())


########### TODO: 【正则表达式】re模块常用函数 2019/11/11 23:42 ##############

# TODO: 1.findall --> 返回列表
"""
找出所有满足条件的，返回的是一个列表
"""
# text = 'apple price is $99,orange price is $10'
# ret = re.findall('\d+', text)
# # TODO: ['99', '10']
# print(ret)


# TODO: 2.sub --> 返回字符串
"""
用来替换字符串。将匹配到的字符串替换为其他字符串。
"""

# text = 'apple price is $299, orange price is $10'
# ret = re.sub('\$\d+', '0', text)
# # TODO: apple price is 0, orange price is 0
# print(ret)


# TODO: sub获取拉勾网的招聘信息 html = """ <dd class="job_bt"> <h3 class="description">职位描述：</h3> <div class="job-detail">
#  <p>岗位职责：</p> <p>1、与算法、数据、产品等部门密切合作；&nbsp;</p> <p>2、开发可靠,高效准确的数据集市,并提供技术支持；</p> <p>3、进行算法平台的需求分析，方案设计；</p>
#  <p>4、研究并实践前沿软件技术。</p> <p><br></p> <p>岗位要求：&nbsp;</p> <p>1、本科（统招）及以上学历，精通Python，三年以上开发经验；&nbsp;</p> <p>2、熟悉<a
#  class="jd-ad" href="https://kaiwu.lagou.com/course/courseInfo.htm?courseId=5&amp;sid=10-MySQL-1573487658396"
#  target="_blank" rel="nofollow" data-ad="10" data-lg-tj-id="1kcw" data-lg-tj-no="idnull"
#  data-lg-tj-cid="101573487658396" data-lg-tj-content="MySQL">MySQL</a>、MongoDB<a class="jd-ad"
#  href="https://kaiwu.lagou.com/course/courseInfo.htm?courseId=1&amp;sid=3-%E6%95%B0%E6%8D%AE%E5%BA%93-1573487658397
#  " target="_blank" rel="nofollow" data-ad="3" data-lg-tj-id="1kcw" data-lg-tj-no="idnull"
#  data-lg-tj-cid="31573487658397" data-lg-tj-content="数据库">数据库</a>、数据建模、数据处理调优；&nbsp;</p>
#  <p>3、熟悉基于Spark、ElasticSearch、HBase&nbsp;等大数据平台的相关开发;</p> <p>4、有一定的数据分析和挖掘能力，能从海量数据提炼核心结果，及时发现和分析其中隐含的变化和问题；</p>
#  <p>5、高度责任心，积极主动，良好的团队协作精神和执行力，较强的分析问题和解决问题能力；&nbsp;</p> <p>6、具有成熟的数据平台搭建经验优先。</p> </div> </dd> """

"""
.+?：转为非贪婪模式，任意字符，最少一个多了不限
"""
# ret = re.sub('<.+?>', '', html)
# print(ret)


# TODO: 3.split --> 返回列表
"""
使用正则表达式来分割字符串
"""

# text = 'hello world ni hao'
# ret = re.split('\s', text)
# # TODO: ['hello', 'world', 'ni', 'hao']
# print(ret)


# TODO: 4.compile
"""
对于一些经常要用到的正则表达式，可以使用compile进行编译，后期再使用的时候可以直接拿过来用，
执行效率会更快。而且compile还可以指定flag=re.VERBOSE，在写正则表达式的时候可以做好注释。
"""

text = 'apple price is $299.50, orange price is $10.10'
r = re.compile(r"""
    \$  #TODO: 匹配$符号
    \d+ #TODO: 整数部分
    \.? #TODO: 最多一位小数点
    \d{1,} #TODO: 小数点后面的数字至少一位多了不限
""", re.VERBOSE)
ret = re.search(r, text)
print(ret.group())
