# -*- coding: UTF-8 -*- 
import re               # 正则表达式
from downloads import download

# 利用sitemap
def crawl_sitemap(url):
    sitemap = download(url)
    # <loc> 是 js 中的标签
    links = re.findall('<loc>(.*?)</loc>',sitemap)
    for link in links:
        html = download(link)

if __name__ == '__main__':
    crawl_sitemap('http://example.webscrapping.com/sitemap.xml')
