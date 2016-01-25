#!/usr/bin/env python

'''
	Diego Martins de Siqueira
	A perfect Imgur Downloader


	Urls Example:
	-http://i.imgur.com/BoENDec.jpg
	-https://imgur.com/a/5xK6z
	-https://imgur.com/gallery/5xK6z
	-https://imgur.com/WDn2pnD
	-https://fallinloveyoulose.imgur.com/*
	-https://m.imgur.com/account/fallinloveyoulose/*
	-https://imgur.com/user/lukeisskywalking/*
'''

import sys
import argparse
import re
import urlparse
import json
import urllib
from libs.mdownload.mdownload import mdownload

class imgur:

	profile_link = 'https://{subdomain}.imgur.com/ajax/images?sort=0&order=1&album=0&page={page}&perPage=60'

	def __init__(self, workers, folderPath):
		self._urlList		= []
		self._workers 		= workers
		self._folderPath 	= folderPath
		self.dlList			= []

	def addUrl(self, url, folder = ''):

		if type(url) is list:
			self._urlList += url
		else:
			self._urlList.append(url)

		self._prepareUrlList(folder)

	def _findProfileInUrl(self, url, search, delimiter, index):

		parts = url.split(delimiter)

		if search not in parts:
			return False

		profile = parts[parts.index(search)+index]

		if len(profile)<4:
			return False

		return self._prepareProfile(profile)


	def _prepareUrlList(self, folder):
		album  	= re.compile('(\/)(gallery\/|a\/)(\w{5}?)')
		single 	= re.compile('(\/[a-zA-Z\d]+)(\/)?')
		direct 	= re.compile('(\/[a-zA-Z\d]+)(\.\w{3,4})')

		for url in self._urlList:

			parse 		= urlparse.urlparse(url)

			#Junk urls
			if (not parse.netloc.find('imgur.com')) and (not parse.netloc == 'imgur.com') :
				continue

			#https://fallinloveyoulose.imgur.com/*
			profile = self._findProfileInUrl(parse.netloc, 'imgur', '.', -1)
			if (profile):
				continue
			#https://imgur.com/user/lukeisskywalking/*
			profile = self._findProfileInUrl(url, 'user', '/', 1)
			if (profile):
				continue
			#https://imgur.com/account/fallinloveyoulose/*
			profile = self._findProfileInUrl(url, 'account', '/', 1)
			if (profile):
				continue
			#https://imgur.com/a/5xK6z https://imgur.com/gallery/5xK6z
			if album.search(parse.path):
				self._prepareAlbum(parse.path, folder)
				continue
			#http://i.imgur.com/BoENDec.jpg
			if direct.search(parse.path):
				self._prepareDirect(parse.path, folder)
				continue
			#https://imgur.com/WDn2pnD
			if single.search(parse.path):
				self._prepareSingle(parse.path, folder)
				continue

		self._urlList 	= []

	def _getProfile(self, subdomain, page):
		url = self.profile_link.replace('{subdomain}',subdomain)
		url = url.replace('{page}',str(page))

		content = urllib.urlopen(url)

		result = json.load(content)

		if type(result) is not dict:
			return False

		if result['status'] != 200:
			return False

		return result

	def _appendUrl(self, url, folder):
		link = {
			'url'	:	url, 
			'folder':	folder
			}
		self.dlList.append(link)

	def _prepareProfile(self, subdomain):

		total	= 0
		page 	= 0
		count 	= 1

		while total < count:
		
			page 	+=  1
			total 	+=	60

			result 	= self._getProfile(subdomain, page)

			if result == False:
				return False

			count	= result['data']['count']
			images	= result['data']['images']

			for image in images:
				path = '/'+image['hash']+image['ext']
				self._prepareDirect(path,subdomain)

		return True

	def _prepareAlbum(self, path, folder):
		if not path.endswith('/'):
			path += '/'
		path += 'zip'
		path = path.replace("/gallery/", "/a/")
		url = 'https://imgur.com'+path
		self._appendUrl(url,folder)
		return url

	def _prepareDirect(self, path, folder):
		url = 'https://i.imgur.com'+path
		self._appendUrl(url,folder)
		return url

	def _prepareSingle(self, path, folder):
		if path.endswith('/'):
			path = path[:-1]
		url = 'https://i.imgur.com'+path+'.jpg'
		self._appendUrl(url,folder)
		return url


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