# Use the file name romeo.txt as the file name
fname = raw_input("Enter file name: ")
things = list()
fh = open(fname)
lst = list()
words = list()

for line in fh:
    lst = line.split()
    words = words + lst

words.sort() #Ordenando as variaveis que estao dentro de "words"

for word in words:
    if not word in things:
        things.append(word)
        

print things
