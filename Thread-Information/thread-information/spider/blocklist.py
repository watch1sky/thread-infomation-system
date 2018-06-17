import urllib2
import re
from bs4 import BeautifulSoup
import threading
import Queue
import Filter
import lxml
import os

ret = list()
DownList = Queue.Queue()
queueLocker = threading.Lock()

def GetThePage(url):
    header = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    request = urllib2.Request(url, None, header)
    try:
        response = urllib2.urlopen(request, timeout=20)
    except:
        pass
    else:
        page = response.read()
        file = open("blocklist.html", 'wb+')
        file.write(page)
        file.close()

def GetTheUrl(url):
    header = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    request = urllib2.Request(url, None, header)
    try:
        response = urllib2.urlopen(request, timeout=20)
    except:
        pass
    else:
        page = response.read()
        file = open('blocklist.html', 'w')
        file.write(page)
        file.close()
        if 'ip' in url:
            Filter.get_ip('blocklist.html')
        elif 'domain' in url or 'host' in url or 'URL' in url:
            Filter.get_url('blocklist.html')
        else:
            pass


def DisposePage(pagename):
    pattern = re.compile('blocklist')
    soup = BeautifulSoup(open(pagename), 'lxml')
    for link in soup.find_all('a'):
        url = link.get('href')
        goal = pattern.search(url)
        if goal:
            url = 'https://zeustracker.abuse.ch/'+url
            doc = {'downurl': url}
            DownList.put(doc)
        else:
            pass


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
                try:
                    GetTheUrl(DownDoc['downurl'])
                except:
                    print 'timeout'
                    break
            else:
                break


if __name__ == '__main__':

    GetThePage('https://zeustracker.abuse.ch/blocklist.php')
    DisposePage('blocklist.html')
    for i in xrange(1, 10):
        t = DownFile()
        try:
            t.start()
        except:
            pass

    os.remove('blocklist.html')