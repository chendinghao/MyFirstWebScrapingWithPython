# -*- coding = UTF-8 -*-
# author: Howard
# num_retries 重试次数       user_agent 用户代理    proxy 也是代理
import urllib2  # 利用不同协议获取url的能力,和
import urlparse # urlparse 主要把 url 拆分成六部分，并以元组的方式返回

def download1(url):
    """simple downloader"""
    return urllib2.urlopen(url).read()

def download2(url):
    """ Download function that catches error"""
    print "downloading:",url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
    return html

def download3(url,num_retries=2):
    """ Download function that catches error and also retries 5xx error """
    print "downloading:",url
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries >0:
             if hasattr(e,'code') and 500<= e.code <600:
                 html = download3(url, num_retries-1)
    return html

def download4(url,user_agent='wawp',num_retries=2):
    """Download function that includes user agent support"""
    print "downloading:",url
    headers = {'User-agent' = user_agent}
    request = urllib2.Request(url, headers = headers)
    try:
        html = urllib2.urlopen(url).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries >0:
             if hasattr(e,'code') and 500<= e.code <600:
                 html = download4(url, user_agent,num_retries-1)
    return html

def download5(url, user_agent='wswp', proxy=None, num_retries=2):
    """Download function with support for proxies"""
    print 'Downloading:', url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    """
    urllib2利用一个Request对象来映射提出的ＨＴＴＰ请求，在他最简单的形式中你将用你要请求的地址创建一个Request对象，通过调用urlopen并
    传入Ｒequest对象，将返回一个相关请求的response对象。
    """
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5XX HTTP errors
                html = download5(url, user_agent, proxy, num_retries-1)
    return html

# download 用于下载网页
download = download5

if __name__ == '__main__':
    print download('http://example.webscraping.com')
