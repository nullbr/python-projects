# Use words.txt as the file name
fname = raw_input("Enter file name: ")

if len(fh) == 0:
	fname = "words.txt"
	
fh = open(fname)

for line in fh:
	fh = line.rstrip().upper()  # Apagando as linhas em branco e deixando as letras maiusculas
	print fh