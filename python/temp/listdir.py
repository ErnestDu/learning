# -*- coding: utf-8 -*-
import os
#print os.listdir("/")
for root, dirs, files in os.walk(os.path.curdir):
#	print root, dirs, files
	open('log', 'a').write("%s %s %s" %(root, dirs, files))
	
