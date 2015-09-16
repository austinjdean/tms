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

# https://duapp2.drexel.edu/webtms_du/app?component=quarterTermDetailsNext&page=Home&service=direct&sp=ZH4sIAAAAAAAAADWLOw7CMBAFlyA%2BNaInF8DGSKGhBFGlQeQCS7yKguzg2BtIxYm4GnfAKOKV82beH5gEDyvSndCeejKi9iyedGUbhEZGUZC3MGyUwDiHGZZc1JYYlvkNHyhDa%2BQPBEbr9jnMOSaHu47GYjAMNpW8sK%2Bb6v8fKZQtvCDpnWOYbjcqU1kMTmhMeu7QRylV2Vrtvq1QxdGkAAAA
# https://duapp2.drexel.edu/webtms_du/app?component=quarterTermDetailsNext&page=Home&service=direct&sp=ZH4sIAAAAAAAAAFvzloG1uIhBPjWlVC%2BlKLUiNUcvs6hErzw1qSS3WC8lsSRRLyS1KJcBAhiZGJh9GNgTk0tCMnNTSxhEfLISyxL1iwtz9EECxSWJuQXWPgwcJUAtzvkpQBVCEBU5iXnp%2BsElRZl56TB5l9Ti5EKGOgamioKCEgY2IwNDUyNToJHhmXlAaYXA0sQiEG1oqmtoBgCbhSKKpgAAAA%3D%3D
# https://duapp2.drexel.edu/webtms_du/app?component=quarterTermDetailsNext&page=Home&service=direct&sp=ZH4sIAAAAAAAAAFvzloG1uIhBPjWlVC%2BlKLUiNUcvs6hErzw1qSS3WC8lsSRRLyS1KJcBAhiZGJh9GNgTk0tCMnNTSxhEfLISyxL1iwtz9EECxSWJuQXWPgwcJUAtzvkpQBVCEBU5iXnp%2BsElRZl56TB5l9Ti5EKGOgamioKCEgY2IwNDU2NToJHBBSBVCoGliUVAZQqGprqGZgAfTc62pgAAAA%3D%3D
# https://duapp2.drexel.edu/webtms_du/app?component=quarterTermDetailsNext&page=Home&service=direct&sp=ZH4sIAAAAAAAAADWMPQ6CQBCFR4w%2FtbGXC7iAERtLLWkMXGBkJ2QNizA7KJUn8mrewTXEV37ve%2B%2F9gZlj2JDulWYaqFaGRT3pKtYpjYKqILYwZhLANIMFllIYSwLr7IYPjFxXRz%2FgBG17zGApfnK6a2%2BsRqPGpopyYdNU%2F%2F5MruzgBcHQtgLzXZyk%2B9Rf5r21xOGlR%2FZamKTb5PAFy%2Bn%2BwKYAAAA%3D

