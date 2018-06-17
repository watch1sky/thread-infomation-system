# -- coding: utf-8 --

import urllib2
import os
from  Filter import get_ip,get_url

def download(url, flag):
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    request = urllib2.Request(url, None, headers)
    try:
        response = urllib2.urlopen(request, timeout=30)#请求回应
    except urllib2.HTTPError as e:
        pass
    except urllib2.URLError as e:
        pass
    else:
        page = response.read()
        if flag:
            File = open("ip.html", 'wb+')
            File.write(page)
            get_ip("ip.html")
            File.close()
        else:
            File = open("url.html", 'wb+')
            File.write(page)
            get_url("url.html")
            File.close()