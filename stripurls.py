#used to strip the city/area urls from craigslist.com

f = open("urls.txt")
f2 = open("urls_stripped.txt","w")
for line in f:
	if "li" in line:
		print line,
		f2.write(line,)

