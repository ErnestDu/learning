#!/usr/bin/env python
# Filename: dns_resolve.py
## resolve server*.example.com all at once 
import dns.resolver
a = 'server'
b = '.example.com'
for x in range(1, 100):
	y = str(x)
	host = a + y + b
	ip = dns.resolver.query(host,"A")
	for i in ip:
		print i,host
