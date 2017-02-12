import urllib

readfile = file('website.txt','r')
textfile = file('web_crawl.txt','wt')
textfile.write('website'+'\t'+ 'e-commerce')
for item in readfile:
	url = "http://" + item
	try:
		sock = urllib.urlopen(url)
		htmlSource = sock.read()
		if "rel=\"canonical\"" in htmlSource:
			textfile.write('\n' + url.rstrip()+'\t'+'true')
		else:
			textfile.write('\n' + url.rstrip()+'\t'+'false')
	except IOError:
		textfile.write('\n' + url.rstrip()+'\t'+'Not Responding')

textfile.close()
sock.close()		
		
		

