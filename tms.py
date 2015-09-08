#!/usr/bin/env python

import urllib2

def getSource(url):
	# thanks: http://stackoverflow.com/questions/30580639/cant-get-python-to-download-webpage-source-code-browser-version-not-supported
	req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"})
	source = urllib2.urlopen(req).read() # get html source
	return source

def main():
	'''
	Driver function
	'''
	print getSource('http://www.google.com')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt: # thanks: http://stackoverflow.com/a/21144662/2929868
		print 'Exiting by user request.'
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
