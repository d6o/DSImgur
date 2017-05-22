#!/usr/bin/env python

'''
    Diego Martins de Siqueira
    DSImgur - Easily download images, Albums, Galleries and entire Profiles from Imgur. The most powerful Imgur Downloader!! You can use as program or as module!


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
import urllib.parse
import json

if sys.version_info[0] == 2:
    import urllib
else:
    import urllib.request as urllib
    import urllib.parse as urlparse
    
# https://github.com/DiSiqueira/DSDownload
from DSDownload import DSDownload

class DSImgur:

    profile_link = 'https://{subdomain}.imgur.com/ajax/images?sort=0&order=1&album=0&page={page}&perPage=60'
    albums_link = 'https://{subdomain}.imgur.com/'

    def __init__(self, workers, folderPath, protocol = 'https://'):
        self._urlList        = []
        self._workers         = workers
        self._folderPath     = folderPath
        self.dlList            = []
        self._protocol        = protocol

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
        album      = re.compile('(\/)(gallery\/|a\/)(\w{5}?)')
        single     = re.compile('(\/[a-zA-Z\d]+)(\/)?')
        direct     = re.compile('(\/[a-zA-Z\d]+)(\.\w{3,4})')

        for url in self._urlList:
            parse         = urlparse.urlparse(url)

            #Junk urls
            if parse.netloc.find('imgur.com') < 0 :
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

        self._urlList     = []

    def _getProfileImages(self, subdomain, page):
        url = self.profile_link.replace('{subdomain}',subdomain)
        url = url.replace('{page}',str(page))

        content = urllib.urlopen(url)

        try:
            result = json.load(content)
        except ValueError as e:
            return False

        if type(result) is not dict:
            return False

        if result['status'] != 200:
            return False

        return result

    def _getProfileAlbums(self, subdomain):
        url = self.albums_link.replace('{subdomain}',subdomain)
        content = urllib.urlopen(url)

        data = content.read()
        content.close()

        regex        = r"id=\"album-(.+?)\""
        album_list    = re.findall(regex, data)

        return album_list

    def _appendUrl(self, url, folder):
        link = {
            'url'    :    url,
            'folder':    folder
            }
        self.dlList.append(link)

    def _prepareProfile(self, subdomain):

        total    = 0
        page     = 0
        count     = 1

        while total < count:

            page     +=  1
            total     +=    60

            result     = self._getProfileImages(subdomain, page)

            if result == False:
                return False

            count    = result['data']['count']
            images    = result['data']['images']

            for image in images:
                path = '/'+image['hash']+image['ext']
                self._prepareDirect(path,subdomain)

        album_list     = self._getProfileAlbums(subdomain)

        if result == False:
            return False

        for album in album_list:
            self._prepareAlbum('/a/' + album,subdomain)

        return True

    def _prepareAlbum(self, path, folder):
        if not path.endswith('/'):
            path += '/'

        path += 'zip'
        path = path.replace("/gallery/", "/a/")
        url = self._protocol+'imgur.com'+path
        self._appendUrl(url,folder)
        return url

    def _prepareDirect(self, path, folder):
        url = self._protocol+'i.imgur.com'+path
        self._appendUrl(url,folder)
        return url

    def _prepareSingle(self, path, folder):
        if path.endswith('/'):
            path = path[:-1]
        url = self._protocol+'i.imgur.com'+path+'.jpg'
        self._appendUrl(url,folder)
        return url


    def download(self):
        if len(self.dlList) <= 0:
            return False

        DSDownload(self.dlList, self._workers, self._folderPath)

        self.dlList = []

        return True
