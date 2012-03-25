#!/usr/bin/python
import os
import sys
import urllib
import re
from BeautifulSoup import BeautifulSoup
i = 0
testself = 0	# disable testself by default
logfile = None
loglevel = None
## get option parameters
while i < len(sys.argv):
	if sys.argv[i] == '-u':
		url = sys.argv[i + 1]
	elif sys.argv[i] == '-d':
		deep_max = sys.argv[i + 1]
	elif sys.argv[i] == '-f':
		logfile = sys.argv[i + 1]
	elif sys.argv[i] == '-l':
		loglevel = sys.argv[i + 1]
	elif sys.argv[i] == '--testself':
		testself = 1
	i += 1
## print option 
deep = 1
deep_max = int(deep_max)
count = 1
def get_data(link):
	page_data = urllib.urlopen(link).read()
	return page_data

def record_data(filename, page_data):
	open(filename, 'a').write(page_data)
	return 0

def get_link(filename):
	soup = BeautifulSoup(open(filename, 'r'))
	links = soup('a', href = re.compile('http'))
	return links['href']

def write_log(logfile, deep, url):
	

print deep, count , url
record_data('1', get_data(url))
deep += 1

while deep < deep_max:
	count = 1
	soup = BeautifulSoup(open(str(deep - 1), 'r'))
	links = soup('a', href = re.compile('http'))
#	links = get_link(str(deep - 1))
	for link in links:
		print deep, count, link['href']
		record_data(str(deep), get_data(link['href']))
		count += 1
	deep += 1
