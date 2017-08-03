# -*- coding = UTF-8 -*-
# author: Howard

import urllib2
import urlparse

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