# -- coding: utf-8 --
import urllib2
import threading
import Queue
import testjson
import os
from download import download

DownList = Queue.Queue()
queueLocker = threading.Lock()

#对传入的文件中的内容进行处理，生成要获取内容的url
#参数：PageName：文件名
def DisposePage(PageName):
    with open(PageName, 'r') as f:
        DownDate = testjson.load(f)
        for DD in DownDate:
            name = DD['ipset']
            downurl = "https://iplists.firehol.org/files/%s.netset"%name
            flag = DD['ips']
            doc = {'name':name, 'downurl':downurl, 'flag':flag}
            DownList.put(doc)

#线程类，对文件下载进行多线程操作
class DownFile(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.queue = DownList

    def run(self):
        while True:
            if not self.queue.empty():
                queueLocker.acquire()
                DownDoc = DownList.get()
                queueLocker.release()
                download(DownDoc['downurl'], DownDoc['flag'])
            else:
                break

if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}  # 请求头
    request = urllib2.Request('http://iplists.firehol.org/all-ipsets.json', None, headers)  # 请求包
    response = urllib2.urlopen(request, timeout=30)
    page = response.read()
    with open('0.html','w') as file:
        file.write(page)
    DisposePage('0.html')
    os.remove('0.html')
    for i in xrange(0, 10):#开始多线程
        t = DownFile()
        try:
            t.start()
        except:
            pass