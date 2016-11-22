2016年11月19日
使用《Web scraping with pathon》
这是我学完python基础后入门爬虫看着书“写”的第一个爬虫 
感觉爬虫的思路很奇妙，挺有趣的！

import re   #这里是正则表达式
import urllib2  #
import urlparse #创建绝对路径
1st web scraping 是我根据第一章的前部分的基础爬虫“抄的”吧
1、使用python文档查阅信息http://python.usyiyi.cn/translate/python_278/library/urllib2.html
2、urllib2是用来获取url的信息的
   这里使用了 request=urllib2.Request(url,headers=headers)  其中，headers这个参数必须赋予字典型的值
   html=urllib2.urlopen(request).read()是读取url
3、if num_retries>0 是用于遇到下载错误时的重新下载
4、link_crawer是链接爬虫

从5开始是第一章介绍的高级功能
5、解析robots.txt文件，以避免下载禁止爬去的url
6、使用代理
7、下载限速
8、避免爬虫陷阱
