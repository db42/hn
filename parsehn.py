#!/usr/bin/env python
import httplib2
import urllib2
import re
#from BeautifulSoup import BeautifulSoup, SoupStrainer
import BeautifulSoup
import hn

#http = httplib2.Http(proxy_info = httplib2.ProxyInfo(socks.PROXY_TYPE_HTTP, '10.10.78.62', 3128))
#status, response = http.request('http://www.reddit.com/r/programming')

#response=open('index.html.3','r').read()
def parse_r():
	list_r=[]
	f=urllib2.urlopen('http://www.reddit.com/r/programming/')
	response=f.read()
	soup = BeautifulSoup.BeautifulSoup(response)
	for a in soup.findAll('a'):
		temp=a.get('href','null')
		if re.search("title",a.get('class',"none")):
			list_r.append(temp)
	f.close()
	return list_r
def parse_hn():
	list_hn=[]
	f=urllib2.urlopen('http://news.ycombinator.com/')
	response=f.read()
	soup= BeautifulSoup.BeautifulSoup(response)
	for a in soup.findAll('a'):
		link= a.get('href','null')
		if "http://" in link and ("ycombinator" not in link):
			list_hn.append(link)
	return list_hn

def main():
	list_hn = parse_hn()
	list_r  = parse_r()
	count = hn.compare(list_hn,list_r)
	print "total similar links:" +str(count)

if __name__ == '__main__':
	main()
    


