#比较好地理解了正则表达式
#coding=utf-8
#正则表达式来抓取数据
import re
import urllib2

# 这里使用代理去访问网站

def download(url,user_agent='wswp',porxy=None,num_retries=2):
    print 'Downloading:',url
    headers={'User-agent':user_agent}
    request=urllib2.Request(url,headers=headers)
    opener=urllib2.build_opener()   #构造opener
    if porxy:
        proxy_params={urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html=opener.open(request).read()
    except urllib2.URLError as e:
        print 'Download Error:', e.reason
        html=None
        if num_retries>0:
            if hasattr(e, 'code') and 500 <=e.code<600:
                return download(url,user_agent,num_retries-1)
    return html

url='http://example.webscraping.com/view/United-KIndom-239'
html=download(url)
print(re.findall('<td class="w2p_fw">(.*?)</td>',html))


