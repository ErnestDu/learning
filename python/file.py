# -*- coding:	utf-8 -*-
import os
cirpath = os.path.abspath(os.path.curdir)
print "current directory is " + cirpath
for dirpath, dirnames,filenames in os.walk(cirpath):
	print filenames
