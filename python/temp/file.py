#!/usr/bin/env python
# coding=utf8
import os
import sys
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error
def FilePath():
	curpath = os.path.abspath(os.path.curdir)
	log = curpath + 'log'
	workpath = curpath
	for dirpath, dirnames, filenames in os.walk(workpath):
		for i in filenames:
			if os.path.splitext(i)[1] == '.mp3':
				filepath = os.path.join(dirpath, i)
				audio = MP3(filepath, ID3 = ID3)				
				album = audio['TALB'][0]
				artist = audio['TPE1'][0]
				frames = audio.tags.getall("APIC")
				for frame in frames:
					ext = ".img"
					if frame.mime == "image/jpeg" or frame.mime == "image/jpg":
						ext = ".jpg"
					elif frame.mime == "image/png":  
				 		ext = ".png"  
				u_album = unicode(album)
				print u_album
				u_artist = unicode(artist)
				print u_artist
FilePath()		
