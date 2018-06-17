# encoding = utf8

import download

list = [{'url':'https://www.badips.com/get/list/any/2?age=7d','flag':1},#ip
        {'url':'http://danger.rulez.sk/projects/bruteforceblocker/blist.php','flag':1},#ip2
        {'url':'http://cinsscore.com/list/ci-badguys.txt','flag':1},#ip
        {'url':'http://cybersweat.shop/iprep/iprep_ramnode.txt','flag':1},#ip
        {'url':'http://blocklist.greensnow.co/greensnow.txt','flag':1},#ip
        {'url':'https://www.malwaredomainlist.com/hostslist/hosts.txt','flag':0},#doamin
        {'url':'https://myip.ms/files/blacklist/htaccess/latest_blacklist.txt','flag':1},#ip
        {'url':'https://openphish.com/feed.txt','flag':0},#url
        {'url':'https://ransomwaretracker.abuse.ch/downloads/RW_DOMBL.txt','flag':0},#domain
        {'url':'https://ransomwaretracker.abuse.ch/downloads/RW_IPBL.txt','flag':1},#ip
        {'url':'https://ransomwaretracker.abuse.ch/downloads/RW_URLBL.txt','flag':0},#url
        {'url':'https://report.cs.rutgers.edu/DROP/attackers','flag':1},#ip
        {'url':'http://sblam.com/blacklist.txt','flag':1},#ip
        {'url':'http://www.urlvir.com/export-hosts/','flag':0,},#domain
        {'url':'http://vxvault.net/URL_List.php','flag':0},#url
        {'url':'https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist','flag':0},#domain
        {'url':'https://zeustracker.abuse.ch/blocklist.php?download=badips','flag':1},#ip
        {'url':'https://zeustracker.abuse.ch/blocklist.php?download=compromised','flag':1},#ip2
        {'url':'https://reputation.alienvault.com/reputation.generic','flag':1},#ip2
        {'url':'http://www.ciarmy.com/list/ci-badguys.txt','flag':1},#ip
        {'url':'http://www.nothink.org/blacklist/blacklist_malware_dns.txt','flag':1},#ip
        {'url':'http://www.nothink.org/blacklist/blacklist_malware_http.txt','flag':0},#domain
        {'url':'http://www.nothink.org/blacklist/blacklist_malware_irc.txt','flag':1},#ip
        {'url':'http://www.nothink.org/blacklist/blacklist_ssh_all.txt','flag':1},#ip
        {'url':'http://www.joewein.net/dl/bl/dom-bl.txt','flag':0},#domain
        {'url':'http://www.botvrij.eu/data/misp.text_ip-dst.ADMIN.txt', 'flag':1},
        {'url':'http://osint.bambenekconsulting.com/feeds/c2-ipmasterlist.txt', 'flag':1},
        {'url':'http://rules.emergingthreats.net/fwrules/emerging-Block-IPs.txt', 'flag':1},
        {'url':'http://rules.emergingthreats.net/blockrules/compromised-ips.txt', 'flag':1},
        {'url':'http://rules.emergingthreats.net/blockrules/emerging-botcc.excluded', 'flag':1},
        {'url':'http://mirror1.malwaredomains.com/files/domains.txt', 'flag':0},
        {'url':'https://talos-intelligence-site.s3.amazonaws.com/production/document_files/files/000/030/623/original/ip_filter.blf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIXACIED2SPMSC7GA%2F20180403%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20180403T121736Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=8b91028e9dbd4ca121a4970d0ebec01b1e3677f35f3a3781674cb3b9ee7c7dd3', 'flag':1},
        {'url':'https://sslbl.abuse.ch/blacklist/dyre_sslipblacklist_aggressive.csv', 'flag':1},
        {'url':'https://sslbl.abuse.ch/blacklist/dyre_sslipblacklist_aggressive.rules', 'flag':1},
        {'url':'https://www.dan.me.uk/tornodes', 'flag':1},
        {'url':'https://urlhaus.abuse.ch/downloads/csv/', 'flag':0},
        {'url':'https://ransomwaretracker.abuse.ch/feeds/csv/', 'flag':0},
        {'url':'https://hosts-file.net/psh.txt', 'flag':0},
        {'url':'https://hosts-file.net/fsa.txt', 'flag':0},
        {'url':'https://hosts-file.net/exp.txt', 'flag':0},
        {'url':'https://hosts-file.net/emd.txt', 'flag':0},
        {'url':'http://mirror1.malwaredomains.com/files/dynamic_dns.txt', 'flag':0}
        ]
for list1 in list:
    download.download(list1['url'], list1['flag'])