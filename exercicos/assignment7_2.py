# Use the file name mbox-short.txt as the file name
count = 0
soma = 0
fname = raw_input("Enter file name: ")

if len(fname) == 0:
	fname = "mbox-short.txt"
	
fh = open(fname)

for line in fh:
	if line.startswith("X-DSPAM-Confidence:"):
		line = line.rstrip() # Apagando as linhas em branco
		fin = line.find(" ")
		num = line[fin+1:]
		numf = float(num)
		soma = soma + numf
		count = count + 1

aver = soma / count
print "Average spam confidence:", aver