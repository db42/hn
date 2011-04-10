#!/usr/bin/env python
import httplib2
import urllib2
import re
#from BeautifulSoup import BeautifulSoup, SoupStrainer
import BeautifulSoup
import hn


request = urllib2.Request('http://news.ycombinator.com/submitlink?u=http%3A%2F%2Fnews.ycombinator.com%2Fsubmit&t=Hacker%20News%20|%20Submit')
response = urllib2.urlopen(request)
print response.read()
soup = BeautifulSoup.BeautifulSoup(response.read())
#a=soup.find('title')
titleTag = soup.html.head.title
print titleTag.string

