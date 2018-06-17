import urllib2
from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb
my_email = db.blemail


def GetTheEmail(url):
    header = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    request = urllib2.Request(url, None, header)
    try:
        response = urllib2.urlopen(request, timeout=20)
    except:
        pass
    else:
        page = response.read()
        file = open('email.txt', 'w')
        file.write(page)
        file.close()


if __name__ == '__main__':
    url = "https://raw.githubusercontent.com/WSTNPHX/scripts-n-tools/master/malware-email-addresses.txt"
    GetTheEmail(url)
    f = open('email.txt', 'r')
    print f.read()
    my_email.insert({"blacklistemail":f})