import urllib2
import simplejson
from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb
ip_info = db.info

def search_ip(ip):
    url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s'%ip
    print(url)
    f = urllib2.urlopen(url).read()
    s = simplejson.loads(f)
    country = s['data']['country']
    country_id = s['data']['country_id']
    city = s['data']['city']
    ip_info.insert({'ip':ip, 'country':country, 'city':city, 'country_id':country_id})