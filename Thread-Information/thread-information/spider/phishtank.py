# -- coding: utf-8 --
import urllib2
import Filter
import os

#获取url中的内容并保存到文件中，传入的参数url:要打开的url；query:具体的文件链接；name:保存的文件的文件名
def alienvault(url, name):
    header = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    request = urllib2.Request(url, None, header)
    try:
        response = urllib2.urlopen(request, timeout=20)
    except:
        pass
    else:
        page = response.read()
        file = open("%s.html"%name, 'wb+')
        file.write(page)
        file.close()


#将url等信息传入到函数中并开始函数执行
if __name__ == '__main__':
    #host = {'url':'http://data.phishtank.com/data/online-valid.csv', 'name':'phishtank'}
    url = 'http://data.phishtank.com/data/online-valid.csv'
    name = 'phishtank'
    alienvault(url, name)
    Filter.get_url('%s.html'%name)
    os.remove('%s.html'%name)