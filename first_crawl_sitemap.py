# -*- coding: UTF-8 -*- 

import urllib2          # 利用不同协议获取url的能力 
import re               # 正则表达式
import urlparse         # urlparse 主要把 url 拆分成六部分，并以元组的方式返回

# 下载网页
# user_agent 使用自定义的代理名称，num_retries 当下载错误时可以重新下载
def download(url,user_agent='wswp',num_retries=2):
    print 'Downloading:',url    
    headers={'User-agent':user_agent}
    request=urllib2.Request(url,headers=headers)    
    """
    urllib2利用一个Request对象来映射提出的ＨＴＴＰ请求，在他最简单的形式中你将用你要请求的地址创建一个Request对象，通过调用urlopen并
    传入Ｒequest对象，将返回一个相关请求的response对象。
    """
    try:
        html=urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download Error:', e.reason
        html=None
        if num_retries>0:
            # 在是5xx错误的时候重新下载
            if hasattr(e, 'code') and 500 <=e.code<600:
                return download(url,user_agent,num_retries-1)
    return html

# 利用sitemap
def crawl_sitemap(url):
    sitemap = download(url)
    # <loc> 是 js 中的
    links = re.findall('<loc>(.*?)</loc>',sitemap)
    for link in links:
        html = download(link)

if __name__ == '__main__':
    crawl_sitemap('http://example.webscrapping.com/sitemap.xml')
