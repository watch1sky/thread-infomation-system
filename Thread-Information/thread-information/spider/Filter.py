# -- coding: utf-8 --
import re

from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb
my_ip = db.blip
my_url = db.blurl

def get_ip(filename):
    with open(filename, 'r') as fileline:
        fip = open('ip.txt','a')
        for fl in fileline:
            result = re.search("((1[0-9][0-9]\.)|(2[0-4][0-9]\.)|(25[0-5]\.)|([1-9][0-9]\.)|([0-9]\.)){3}((1[0-9][0-9])|(2[0-4][0-9])|(25[0-5])|([1-9][0-9])|([0-9]))",fl)# 模式匹配ip地址
            if result and 'a' not in fl:
                fip.write(fl[result.span()[0]:result.span()[1]]+'\n')
                my_ip.insert({"blacklistip": fl})
            else:
                pass
        fip.close()

def get_url(filename):
    with open(filename, 'r') as fileline:
        furl = open('url.txt','a')
        for fl in fileline:
            result = re.search(r'\b((?:[a-z][\w-]+:(?:\/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}\/?)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\)){0,}(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s\!()\[\]{};:\'\"\.\,<>?«»“”‘’]){0,})', fl)
            if result:
                if '#' in fl:
                    pass
                else:
                    furl.write(fl[result.span()[0]:result.span()[1]]+'\n')
                    my_url.insert({"blacklistdomain":fl[result.span()[0]:result.span()[1]]}, {"domaininfo":fl})
            else:
                pass
        furl.close()