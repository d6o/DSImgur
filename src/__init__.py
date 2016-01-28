#!/usr/bin/env python

"""
Diego Martins de Siqueira
MIT License
DSImgur - Easily download images, Albums, Galleries and entire Profiles from Imgur. The most powerful Imgur Downloader!! You can use as program or as module!
"""

import sys
import argparse
from DSImgur import DSImgur

def main(argv=sys.argv[0]):
	parser = argparse.ArgumentParser(
		description = "Easily download images, Albums, Galleries and entire Profiles from Imgur. The most powerful Imgur Downloader!! You can use as program or as module!")
	parser.add_argument("--workers", type=int, default=5, 
		help="Number of parallel downloads. The default is 5.")
	parser.add_argument("--output", type=str, default="downloads", 
		help="Output folder")
	parser.add_argument("--http", action="store_true",
		help="Force use HTTP (Insecure). Default is HTTPS")
	parser.add_argument('urls', type=str, nargs='+',
		help='URLs to be downloaded')

	args = parser.parse_args()

	protocol = 'https://'

	if args.http:
		protocol = 'http://'

	try:
		i = DSImgur(args.workers, args.output,protocol)
		i.addUrl(args.urls)
		i.download()

		print 'All images have been downloaded.'
	except KeyboardInterrupt:
		print 'Interrupt received, stopping downloads'

	sys.exit()

if __name__ == "__main__":
   main(sys.argv[1:])