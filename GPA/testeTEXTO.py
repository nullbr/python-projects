g1 = 1
g2 = 2
g3 = 3
g4 = 4
g5 = 5
g6 = 6
g7 = 7
g8 = 8
c1 = "1"
c2 = "2"
c3 = "3"
c4 = "4"
c5 = "5"
c6 = '6'
c7 = '7'
c8 = '8'

idioma = 1

arq = open("GPA Calculator.txt", "w")
	
if idioma == 1:
	scores = "Your score of the 1st year in the scale is 0 - 10:"
	print "\n", scores
	arq.write(scores)
elif idioma == 2:
	notas = "As notas do seu 1ro ano na escala de 0 - 10:"
	print "\n", notas
	arq.write(notas)
elif idioma == 3:
	calificaciones = "Tus calificaciones en tu 1ro en la escala de 0 - 10 son:"
	print "\n", calificaciones
	arq.write(calificaciones)
	
arq.write("\n")
	
print "\n ", c1, "=", g1
print "\n ", c2, "=", g2
print "\n ", c3, "=", g3
print "\n ", c4, "=", g4
print "\n ", c5, "=", g5
print "\n ", c6, "=", g6
print "\n ", c7, "=", g7
print "\n ", c8, "=", g8
	

grade2 = str(g2)
grade3 = str(g3)
grade4 = str(g4)
grade5 = str(g5)
grade6 = str(g6)
grade7 = str(g7)
grade8 = str(g8)

space = ' '
equal = ' = '
writeg1 = (space + c1 + equal + str(g1))
print writeg1
arq.write(writeg1)
arq.close()