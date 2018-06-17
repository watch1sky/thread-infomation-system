# -- coding: utf-8 --

import os
#from pymongo import MongoClient

#conn = MongoClient('127.0.0.1', 27017)
#db = conn.mydb
#db.dropDatabase()

path = os.getcwd()
filelist = ['badips.py','firehol.py', 'urls.py', 'BlackList.py', 'blocklist.py', 'blocklist1.py', 'email.py', 'blocklist-ipsets.py','badips.py', 'phishtank.py','count.py']

for each_py in filelist:
    try:
        command = 'python %s'%each_py
        print command
        os.system(command)
    except:
        print 'error in script :', each_py
        print 'run another script'

os.remove('ip.html')
os.remove('url.html')