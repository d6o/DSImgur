#!/usr/bin/env python

'''
	Diego Martins de Siqueira
	A perfect Imgur Downloader


	Urls Example:
	-http://i.imgur.com/BoENDec.jpg
	-https://imgur.com/a/5xK6z
	-https://imgur.com/gallery/5xK6z
	-https://imgur.com/WDn2pnD
'''

import sys
import argparse
from libs.mdownload.mdownload import mdownload
import re
import urlparse

class imgur:

	domains = ['imgur.com', 'i.imgur.com']

	def __init__(self, workers, folderPath):
		self._urlList		= []
		self._workers 		= workers
		self._folderPath 	= folderPath
		self.dlList			= []

	def addUrl(self, url):

		if type(url) is list:
			self._urlList += url
		else:
			self._urlList.append(url)

		self._prepareUrlList()

	def _prepareUrlList(self):
		album  	= re.compile('(\/)(gallery\/|a\/)(\w{5}?)')
		single 	= re.compile('(\/[a-zA-Z\d]+)(\/)?')
		direct 	= re.compile('(\/[a-zA-Z\d]+)(\.\w{3,4})')

		for url in self._urlList:

			parse = urlparse.urlparse(url)

			if not parse.netloc in self.domains:
				continue

			if album.search(parse.path):
				self.dlList.append(self._prepareAlbum(parse.path))
				continue
			if direct.search(parse.path):
				self.dlList.append(self._prepareDirect(parse.path))
				continue
			if single.search(parse.path):
				self.dlList.append(self._prepareSingle(parse.path))
				continue

		self._urlList 	= []

	def _prepareAlbum(self, path):
		if not path.endswith('/'):
			path += '/'
		path += 'zip'
		path = path.replace("/gallery/", "/a/")
		return 'https://imgur.com'+path

	def _prepareDirect(self, path):
		return 'https://i.imgur.com'+path

	def _prepareSingle(self, path):
		if path.endswith('/'):
			path = path[:-1]
		return 'https://i.imgur.com'+path+'.jpg'

	def download(self):
		if len(self.dlList) <= 0:
			return False

		mdownload(self.dlList, self._workers, self._folderPath)

		self.dlList = []

		return True


def main(argv):
	parser = argparse.ArgumentParser(
		description = "A perfect Imgur Downloader.")
	parser.add_argument("--threads", type=int, default=5, 
		help="Number of parallel downloads. The default is 5.")
	parser.add_argument("--output", type=str, default="downloads", 
		help="Output folder")
	parser.add_argument('urls', type=str, nargs='+',
		help='URLs to be downloaded')

	args = parser.parse_args()

	try:
		i = imgur(args.threads, args.output)
		i.addUrl(args.urls)
		i.download()

		print 'All images have been downloaded.'
	except KeyboardInterrupt:
		print 'Interrupt received, stopping downloads'

	sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])