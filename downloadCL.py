#grabs city/area urls from txt file, then appends search string to url and downloads ads to 'cl_ads' folder

import urllib2

#searches for 'comics'
append = "/search/sss?query=comics&sort=rel"

f = open("urls_stripped2.txt")
x = 1
for line in f:
	f2 = open("cl_ads/" + str(x) + ".html", "w")
	print line[:-1] + append
	test = urllib2.urlopen(line[:-1] + append)
	for testline in test:
		#print testline
		f2.write(testline)
	f2.close()
	x += 1
