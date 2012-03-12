#!/usr/bin/python
# Filename: Spider1.py
# Spider1.py -u url -d deep
import os
import sys
import urllib
import sqlite3
import re
from BeautifulSoup import BeautifulSoup
i = 0
while i < len(sys.argv):	## get parameters
	if sys.argv[i] == "-u":	
		url = sys.argv[i + 1]
	elif sys.argv[i] == "-d":
		deep_max = sys.argv[i + 1]
	i += 1

deep_max = int(deep_max)
deep = 1
def get_data(link):
	page_data = urllib.urlopen(link).read()
	return page_data

def record_data(filename, url, page_data):
	open(filename, 'a').write(url)
	open(filename, 'a').write(page_data)
	return 0

#conn = sqlite3.connect("db")
#c = conn.cursor()
#c.execute('create table site (url text, data text, deep real)')
#c.execute('insert into site values ("%s", "%s", "%d")' %(url, data, deep))
#conn.commit()
#c.close()
count = 0
soup = BeautifulSoup(get_data(url))
filename = str(deep)
print "deep " ,deep, "count" ,count
record_data(filename, url, get_data(url))
deep += 1
count += 1
links = soup('a', href = re.compile('http'))

#for link in links:
#	print link
#print len(links)
#for link in links:
#	print link['href']
#	record_data(str(i), get_data(link['href']))
#	i += 1
if deep <= deep_max:
	count = 0
	for link in links:
		url = link['href']
		print url
		filename = str(deep)
		print "deep " ,deep, "count" ,count
		record_data(filename, url, get_data(url))
		soup = BeautifulSoup(get_data(url))
		links = links + soup('a', href = re.compile('http'))
		count += 1
	links = soup('a', href = re.compile('http'))
	deep += 1
