#!/usr/bin/env python
# coding=utf8
import os
import sys
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
def FilePath():
	curpath = os.path.abspath(os.path.curdir)
	log = curpath + 'log'
#	if os.path.exists(sys.argv[1]):
#		workpath = sys.argv[1] 
#	else:
#		workpath = curpath
#	print "working path is " + workpath
	workpath = curpath
	for dirpath, dirnames, filenames in os.walk(workpath):
		for i in filenames:
			if os.path.splitext(i)[1] == '.mp3':
				filepath = os.path.join(dirpath, i)
#				print filepath
#				open('log','a').write(filepath + '\n')
				audio = MP3(filepath, ID3 = ID3)				
#				try:	
#					audio.add_tags()
#				except error:
#					print "audio file has id3 tags"
				album = audio['TALB'][0]
				artist = audio['TPE1'][0]
				frames = audio.tags.getall("APIC")
				for frame in frames:
#					print frame
					ext = ".img"
					if frame.mime == "image/jpeg" or frame.mime == "image/jpg":
						ext = ".jpg"
					elif frame.mime == "image/png":  
				 		ext = ".png"  
#			    elif frame.mime == "image/gif":
#					ext = ".gif"
#				print filepath
#				print album
#				print artist
#				u_path = unicode(filepath)
				u_album = unicode(album)
				print u_album
				u_artist = unicode(artist)
				print u_artist
#				open('log', 'a').write(album)
FilePath()		
