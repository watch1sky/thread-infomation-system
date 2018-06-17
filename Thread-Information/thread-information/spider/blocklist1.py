import urllib2
import Filter
import os

def GetThePage(url):
    header = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    request = urllib2.Request(url, None, header)
    try:
        response = urllib2.urlopen(request, timeout=20)
    except Exception,e:
        print e
    else:
        page = response.read()
        file = open("download.html", 'wb+')
        file.write(page)
        file.close()

    if 'IP' in url:
        Filter.get_ip('download.html')
    else:
        Filter.get_url('download.html')

if __name__ == '__main__':
    host = [{'url':'https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt'},
            {'url':'https://ransomwaretracker.abuse.ch/downloads/RW_URLBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/RW_IPBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/CW_C2_URLBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/CW_C2_DOMBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/CW_PS_DOMBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/CW_PS_IPBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/TC_C2_URLBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/TC_C2_DOMBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/TC_PS_DOMBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/TC_PS_IPBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/LY_C2_DOMBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/LY_C2_IPBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/LY_PS_DOMBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/LY_PS_IPBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/LY_DS_URLBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/TL_C2_DOMBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/TL_C2_IPBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/TL_PS_DOMBL.txt'},
            {'url': 'https://ransomwaretracker.abuse.ch/downloads/TL_PS_IPBL.txt'},
            ]
    for h in host:
        GetThePage(h['url'])

    os.remove('download.html')