# -- coding: utf-8 --
import gzip
import httplib
import os
import StringIO
import Filter

#获取url中的内容并保存到文件中，传入的参数url:要打开的url；query:具体的文件链接；name:保存的文件的文件名
def alienvault(url, query, name):

    hhandle = httplib.HTTPConnection(url, timeout=20)
    hhandle.putrequest('GET', query)
    hhandle.putheader('Connection', 'keep-alive')
    hhandle.putheader('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    hhandle.putheader('Accept-Encoding', 'gzip, deflate, sdch')
    hhandle.putheader('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
    hhandle.putheader('Accept-Language', 'en-GB,en-US;q=0.8,en;q=0.6')
    hhandle.endheaders()

    response = hhandle.getresponse()
    if response.status == 200:
        if response.getheader('Content-Encoding') == 'gzip':
            content = StringIO.StringIO(response.read())
            server_response = gzip.GzipFile(fileobj=content).read()
            with open('%s.html'%name, 'w') as f:
                f.write(server_response)
        else:
            server_response = response.read()
            with open('%s.html'%name, 'w') as f:
                f.write(server_response)
#将url等信息传入到函数中并开始函数执行
if __name__ == '__main__':
    alienvault_host = [{'url':'reputation.alienvault.com', 'query':'/reputation.data', 'name':'alienvault'},
                       {'url':'torstatus.blutmagie.de', 'query':'/ip_list_exit.php/Tor_ip_list_EXIT.csv', 'name':'tor_exit_nodes'},
                       {'url':'lists.blocklist.de', 'query':'/lists/all.txt', 'name':'de_blocklist'},
                       {'url':'rules.emergingthreats.net', 'query':'/blockrules/compromised-ips.txt', 'name':'emerging_threats'}]
    i=1
    for ah in alienvault_host:
        alienvault(ah['url'], ah['query'], ah['name'])
        Filter.get_ip('%s.html'%ah['name'])
        os.remove('%s.html'%ah['name'])