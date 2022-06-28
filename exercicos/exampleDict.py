name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name, "r")
text = handle.read()
words = text.split()

counts = dict()
for word in words:
	counts[word] = counts.get(word,0) + 1

print counts