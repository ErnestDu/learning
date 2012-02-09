#!/usr/bin/env python
# -*- coding:utf-8 -*- 
import os
import sys
import urllib
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
				open('file.log', 'a').write("%s %s\n" %(u_artist, u_album))
				base_url="http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=b25b959554ed76058ac220b7b2e0a026"
				url=base_url+"&artist="+u_artist+"&album="+u_album
				print url
				xmlfile = u_artist+u_album;
				open(str(u_album)+".xml", 'a').write(urllib.urlopen(url).read())
				out = os.popen("grep mega %s.xml|cut -c 24-$(($(grep mega %s.xml|wc -c)-9))" %(u_album, u_album)).read()
				print out
				open(u_album+".jpg", 'a').write(urllib.urlopen(out).read())
os.popen("rm *.jpg *.xml")
FilePath()		
