#further url formatting

f = open("urls_stripped.txt")
f2 = open("urls_stripped2.txt","w")
for line in f:
	if "http" in line:
		print line,
		f2.write(line.strip() + "\n")

