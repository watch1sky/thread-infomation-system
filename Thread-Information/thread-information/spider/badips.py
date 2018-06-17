import urllib2
import re
import Filter
import time
from pymongo import MongoClient
import os

conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb
ip_info = db.info

URL = "https://www.badips.com/info/"
header = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
i = 17819
url = URL + str(i)

while True:
    request = urllib2.Request(url, None, header)
    time.sleep(1)
    try:
        response = urllib2.urlopen(request, timeout=30)
    except:
        time.sleep(2)
        response = urllib2.urlopen(request, timeout=30)
    else:
        page = response.read()
        result = re.search(
            "((1[0-9][0-9]\.)|(2[0-4][0-9]\.)|(25[0-5]\.)|([1-9][0-9]\.)|([0-9]\.)){3}((1[0-9][0-9])|(2[0-4][0-9])|(25[0-5])|([1-9][0-9])|([0-9]))",
            page)
        if (result == None):
            break
        file = open("badips.html", 'wb+')
        file.write(page)
        file.close()
        Filter.get_ip("badips.html")
    i += 1
    url = URL + str(i)

os.remove('badips.html')