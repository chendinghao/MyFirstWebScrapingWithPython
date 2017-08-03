# coding = utf-8

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

# 下面的用正则表达式生成的链接爬虫
def link_crawler(seed_url,link_regex):
    crawl_queue=[seed_url]
    seen=set(crawl_queue)
    while crawl_queue:
        url=crawl_queue.pop()
        html=download(url)
        for link in get_links(html):
            if re.match(link_regex,link):
                link=urlparse.urljoin(seed_url,link)
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

def get_links(html):
    """
    <a href="http://www.w3school.com.cn">W3School</a>
    """
    """
    具体的关于正则表达式内容，请留意我的博客
    """
    webpage_regex=re.compile('<a[^>]+href=["\'](.*?)["\']')
    
    # 正则表达式 re findall 方法能够以列表的形式返回能匹配的子串。
    return webpage_regex.findall(html)

link_crawler('http://example.webscraping.com','/(index|view)')
