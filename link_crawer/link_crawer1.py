# coding = utf-8

import re               # 正则表达式
from downloads import download

# 下面的用正则表达式生成的链接爬虫
# 利用正则表达式决定下载哪些页面
def link_crawler(seed_url,link_regex):
    """
    Crawl from the given seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url] # the queue of URL's to download
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        # filter for links matching our regular expression
        for link in get_links(html):
            if re.match(link_regex, link):
                # add this link to the crawl queue
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
