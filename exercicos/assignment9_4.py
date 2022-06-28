name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

text = open(name)

numero = 0
counts = dict()
words = list()
count = "Counting"
for line in text:
	if not line.startswith("From "): continue
	lines = line.split()
	email = lines[1:2]
	words = words + email
	import os
	os.system("cls")
	print count
	count = count + "."


for word in words:	
	counts[word] = counts.get(word,0) + 1
	import os
	os.system("cls")
	print count
	count = count + "."
	

bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print bigword, bigcount