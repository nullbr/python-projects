

g9 = 0
g10 = 0
g11 = 0
g12 = 0
g13 = 0 
g14 = 0
g15 = 0
g16 = 0
g17 = 0
g18 = 0

g9y2 = 0
g10y2 = 0
g11y2 = 0
g12y2 = 0
g13y2 = 0 
g14y2 = 0
g15y2 = 0
g16y2 = 0
g17y2 = 0
g18y2 = 0

g1y3 = 0
g2y3 = 0
g3y3 = 0
g4y3 = 0 
g5y3 = 0
g6y3 = 0
g7y3 = 0
g8y3 = 0
g9y3 = 0
g10y3 = 0
g11y3 = 0
g12y3 = 0
g13y3 = 0
g14y3 = 0
g15y3 = 0
g16y3 = 0
g17y3 = 0
g18y3 = 0

g1y4 = 0
g2y4 = 0 
g3y4 = 0
g4y4 = 0
g5y4 = 0
g6y4 = 0
g7y4 = 0
g8y4 = 0
g9y4 = 0
g10y4 = 0
g11y4 = 0 
g12y4 = 0
g13y4 = 0
g14y4 = 0
g15y4 = 0
g16y4 = 0
g17y4 = 0
g18y4 = 0

g1y5 = 0
g2y5 = 0
g3y5 = 0
g4y5 = 0
g5y5 = 0
g6y5 = 0
g7y5 = 0
g8y5 = 0
g9y5 = 0
g10y5 = 0
g11y5 = 0
g12y5 = 0
g13y5 = 0
g14y5 = 0
g15y5 = 0
g16y5 = 0
g17y5 = 0
g18y5 = 0

gp9 = 0
gp10 = 0
gp11 = 0
gp12 = 0
gp13 = 0
gp14 = 0
gp15 = 0
gp16 = 0
gp17 = 0
gp18 = 0

gp9y2 = 0
gp10y2 = 0 
gp11y2 = 0
gp12y2 = 0 
gp13y2 = 0
gp14y2 = 0
gp15y2 = 0
gp16y2 = 0
gp17y2 = 0
gp18y2 = 0

gp1y3 = 0 
gp2y3 = 0
gp3y3 = 0
gp4y3 = 0
gp5y3 = 0
gp6y3 = 0
gp7y3 = 0
gp8y3 = 0
gp9y3 = 0
gp10y3 = 0
gp11y3 = 0
gp12y3 = 0
gp13y3 = 0
gp14y3 = 0
gp15y3 = 0
gp16y3 = 0
gp17y3 = 0
gp18y3 = 0

gp1y4 = 0
gp2y4 = 0
gp3y4 = 0
gp4y4 = 0
gp5y4 = 0
gp6y4 = 0
gp7y4 = 0
gp8y4 = 0
gp9y4 = 0
gp10y4 = 0
gp11y4 = 0
gp12y4 = 0
gp13y4 = 0
gp14y4 = 0
gp15y4 = 0
gp16y4 = 0
gp17y4 = 0
gp18y4 = 0

gp1y5 = 0
gp2y5 = 0
gp3y5 = 0
gp4y5 = 0
gp5y5 = 0
gp6y5 = 0
gp7y5 = 0
gp8y5 = 0
gp9y5 = 0
gp10y5 = 0
gp11y5 = 0
gp12y5 = 0
gp13y5 = 0
gp14y5 = 0
gp15y5 = 0
gp16y5 = 0
gp17y5 = 0
gp18y5 = 0

y = 1
test = 0
year = 0
repeat = 0
yp = 0
suffix = 1
suffixC = 1

cyf3 = 0
cyf4 = 0
cyf5 = 0

cla1 = 0
cla2 = 0
cla3 = 0
cla4 = 0
cla5 = 0

gpay3 = 0
gpay4 = 0
gpay5 = 0

i = 1
while i == 1:
	print "\n 1 - To use it in English"
	print " 2 - Para usar em Portugues-BR" 
	print " 3 - Para utilizar en Espanol"
	try:
		idio = raw_input("\n Enter here: ")
		idioma = int(idio)
		if idioma == 1:
			print "\n You select English"
			print " If you want to continue press 1, or if you want to select an another lenguage press 2"
			con = raw_input(" Enter here: ")
			conti = int(con)
			if conti == 2:
				i = 1
			else:
				i = 0
				import os
				os.system("cls")
				print "\n Welcome to the GPA calculator! \n"
			
		elif idioma == 2:
			print "\n Voce escolheu Portugues-BR"
			print " Se voce deseja continuar aperte 1, ou se quiser escolher um outro idioma aperte 2"
			con = raw_input(" Insira aqui: ")
			conti = int(con)
			if conti == 2:
				i = 1
			else:
				i = 0
				import os
				os.system("cls")
				print "\n Bem vindo ao GPA calculator! \n"
				
		elif idioma == 3:
			print "\n Elegiste Espanol"
			print " Si deseas seguir aplaste en 1, o si deseas elegir un otro idioma aplase en 2"
			con = raw_input(" Ingresa aqui: ")
			conti = int(con)
			if conti == 2:
				i = 1
			else:
				i = 0
				import os
				os.system("cls")
				print "\n Bienvenido al GPA calculator! \n"
		else:
			print "Please, enter 1, 2 or 3"
			i == 1
	except:
		print "Please, enter 1, 2 or 3"
		i == 1

while test == 0 or repeat < year:
	u = 1
	yp = yp + 1
	if year >= 2 and year <= 5:
		b = 0
	else:
		b = 1
	while b == 1:
		try:
			if idioma == 1:
				print "\n How many years do you have in the High-School? "
				years = raw_input(" Enter here: ")
				years = int(years)
				year = years
				if years == 2:
					print "\n ", years, "years "
					b = 0
				elif years == 3:
					print "\n ", years, "years "
					b = 0
				elif years == 4:
					print "\n ", years, "years "
					b = 0
				elif years == 5:
					print "\n ", years, "years "
					b = 0
				else:
					print " Please enter a number between 2 and 5"
					b = 1
			elif idioma == 2:
				print "\n Quantos anos voce tem no ensino medio? "
				years = raw_input(" Insira aqui: ")
				years = int(years)
				year = years
				if years == 2:
					print "\n ", years, "anos "
					b = 0
				elif years == 3:
					print "\n ", years, "anos"
					b = 0
				elif years == 4:
					print "\n ", years, "anos "
					b = 0
				elif years == 5:
					print "\n ", years, "anos "
					b = 0
				else:
					print " Por favor insira um numero entre 2 e 5 "
					b = 1
			elif idioma == 3:	
				print "\n Cuantos anos tienes en bachillerato? "
				years = raw_input(" Ingresa aqui: ")
				years = int(years)
				year = years
				if years == 2:
					print "\n ", years, "anos "
					b = 0
				elif years == 3:
					print "\n ", years, "anos"
					b = 0
				elif years == 4:
					print "\n ", years, "anos"
					b = 0
				elif years == 5:
					print "\n ", years, "anos "
					b = 0
				else:
					print " Por favor ingresa un numero entre 2 y 5"
					b = 1
	
		except:
			if idioma == 1:
				print " Please enter a number between 2 and 5"
				b = 1
			elif idioma == 2:
				print " Por favor insira um numero entre 2 e 5"
				b = 1
			elif idioma == 3:
				print " Por favor ingresa un numero entre 2 y 5"
				b = 1
	
	t = 1
	
	import os
	os.system("cls")
	
	while t == 1:
		try:
			if suffix == 1:
				if idioma == 1:
					suff = "st"
				elif idioma == 2 or idioma == 3:
					suff = "ro"
					
			elif suffix == 2:
				if idioma == 1:
					suff = "nd"
				elif idioma == 2 or idioma == 3:
					suff = "do"
					
			elif suffix == 3:
				if idioma == 1:
					suff = "rd"
				elif idioma == 2 or idioma == 3:
					suff = "ro"
					
			elif suffix == 4:
				suff = "th"
				if idioma == 1:
					suff = "th"
				elif idioma == 2 or idioma == 3:
					suff = "to"
				
			elif suffix == 5:
				if idioma == 1:
					suff = "th"
				elif idioma == 2 or idioma == 3:
					suff = "to"
					
			ys = str(yp)
			
			if yp == 1:
				cyf = 1
			elif yp == 2:
				cyf2 = 2
			elif yp == 3:
				cyf3 = 3
			elif yp == 4:
				cyf4 = 4
			elif yp == 5:
				cyf5 = 5
			
			if idioma == 1:
				print "\n How many classes do you have in your "+ ys + suff +" year? min 8 and max 18"
				qt = raw_input(" Enter here: ")
			elif idioma == 2:	
				print "\n Quantas materias voce tem em seu "+ ys + suff +" ano? min 8 and max 18"
				qt = raw_input(" Insira aqui: ")
			elif idioma == 3:	
				print "\n Cuantas clases tienes en tu "+ ys + suff +" ano? min 8 and max 18"
				qt = raw_input(" Ingresa aqui: ")
				
			cla = int(qt)
			x = cla
			if yp == 1:
				cla1 = x
			elif yp == 2:
				cla2 = x
			elif yp == 3:
				cla3 = x
			elif yp == 4:
				cla4 = x
			elif yp == 5:
				cla5 = x
			yp = int(ys)
			if cla >= 8 and cla <= 18:
				t = 0
			
			else:
				if idioma == 1:
					print "\n Please, enter a number between 8 and 18 \n"
				elif idioma == 2:
					print "\n Por favor insira um numero entre 8 e 18 \n"
				elif idioma == 3:
					print "\n Por favor ingresa u numero entre 8 y 18 \n"
				
				t = 1
		
		except:
			if idioma == 1:
				print "\n Please, enter a number between 8 and 18 \n"
			elif idioma == 2:
				print "\n Por favor insira um numero entre 8 e 18 \n"
			elif idioma == 3:
				print "\n Por favor ingresa u numero entre 8 y 18 \n"
					
			t = 1
		
	if cla >= 8 and cla <= 18:
		if idioma == 1:
			print "\n How you want to put your score?"
			print "\n Press 1 to use: A, B, C, D, F"
			print " Press 2 to use: 0 - 10"
			print " Press 3 to use: 0 - 100 \n"
		elif idioma == 2:
			print "\n Como voce quer colocar a sua nota?"
			print "\n Insira 1 para: A, B, C, D, F"
			print " Insira 2 para: 0 - 10"
			print " Insira 3 para: 0 - 100 \n"
		elif idioma == 3:
			print "\n Como como quieres poner tus calificaciones?"
			print "\n Ingresa 1 para: A, B, C, D, F"
			print " Ingresa 2 para: 0 - 10"
			print " Ingresa 3 para: 0 - 100 \n"
		
		while u == 1:
			try:
				if idioma == 1:
					opt = raw_input(" Enter here: ")
					opt = int(opt)
					if opt == 1:
						print "\n You select A, B, C, D, F"
						u = 0
					elif opt == 2:
						print "\n You select 0 - 10"
						u = 0
					elif opt == 3:
						print "\n You select 0 - 100"
						u = 0
					else:
						print "\n Please enter a number between 1 and 3 \n"
						u = 1
				elif idioma == 2:
					opt = raw_input(" Insira aqui: ")
					opt = int(opt)
					if opt == 1:
						print "\n Voce escoleu A, B, C, D, F"
						u = 0
					elif opt == 2:
						print "\n Voce escoleu 0 - 10"
						u = 0
					elif opt == 3:
						print "\n Voce escoleu 0 - 100"
						u = 0
					else:
						print "\n Por favor insira um numero entre 1 e 3 \n"
						u = 1
				elif idioma == 3:
					opt = raw_input(" Insira aqui: ")
					opt = int(opt)
					if opt == 1:
						print "\n Has elegido A, B, C, D, F"
						u = 0
					elif opt == 2:
						print "\n Has elegido 0 - 10"
						u = 0
					elif opt == 3:
						print "\n Has elegido 0 - 100"
						u = 0
					else:
						print "\n Por favor ingresa un numero entre 1 y 3 \n"
						u = 1
						
			except:
				print "\n Por favor ingresa un numero entre 1 y 3 \n"
				u = 1
		
		notas = opt
		while x > 0:
			if suffixC == 1:
				suffC = "st"
			elif suffixC == 2:
				suffC = "nd"
			elif suffixC == 3:
				suffC = "rd"
			elif suffixC >= 4:
				suffC = "th"
			suffixC = suffixC + 1
			
			
			if opt == 1:	
				num = str(y)
				if idioma == 1:
					print "\n What is the name of your "+ num + suffC +" class?"
					c = raw_input(" Enter here: ")
				elif idioma == 2:
					print "\n Como se chama a sua "+ num + suffC +" materia?"
					c = raw_input(" Isira aqui: ")
				elif idioma == 3:
					print "\n Como llama tu "+ num + suffC +" clase?"
					c = raw_input(" Ingresa aqui: ")
				y = int(num)
				i = 1
				while i == 1:
					if idioma == 1:
						print " What is your grade in this class?"
						g = raw_input(" Enter here: ")
					elif idioma == 2:
						print " Qual eh a sua nota nessa materia?"
						g = raw_input(" Insira aqui: ")
					elif idioma == 3:
						print " Cual es tu calificacion en esta clase?"
						g = raw_input(" Ingresa aqui: ")
					
					if g == "A" or g == "a":
						g = 10.0
						i = 0
					elif g == "A-" or g == "a-":
						g = 9.2
						i = 0
					elif g == "B+" or g == "b+":
						g = 8.9
						i = 0
					elif g == "B" or g == "b":
						g = 8.6
						i = 0
					elif g == "B-" or g == "b-":
						g = 8.2
						i = 0
					elif g == "C+" or g == "c+":
						g = 7.9
						i = 0
					elif g == "C" or g == "c":
						g = 7.6
						i = 0
					elif g == "C-" or g == "c-":
						g = 7.2
						i = 0
					elif g == "D+" or g == "d+":
						g = 6.9
						i = 0
					elif g == "D" or g == "d":
						g = 6.6
						i = 0
					elif g == "D-" or g == "d-":
						g = 6.2
						i = 0
					elif g == "F" or g == "f":
						g = 5.9
						i = 0
					else:
						print "\n Please enter a valid score \n"
						i = 1
			
			elif opt == 2:
				num = str(y)
				if idioma == 1:
					print "\n What is the name of your "+ num + suffC +" class?"
					c = raw_input(" Enter here: ")
				elif idioma == 2:
					print "\n Como se chama a sua "+ num + suffC +" materia?"
					c = raw_input(" Isira aqui: ")
				elif idioma == 3:
					print "\n Como llama tu "+ num + suffC +" clase?"
					c = raw_input(" Ingresa aqui: ")
				y = int(num)
				i = 1
				while i == 1:
					try:
						if idioma == 1:
							print " What is your grade in this class?"
							gra = raw_input(" Enter here: ")
						elif idioma == 2:
							print " Qual eh a sua nota nessa materia?"
							gra = raw_input(" Insira aqui: ")
						elif idioma == 3:
							print " Cual es tu calificacion en esta clase?"
							gra = raw_input(" Ingresa aqui: ")
						g = float(gra)
						if g >= 0 and g <= 10:
							i = 0
						else:
							if idioma == 1:
								print "\n Please enter a number between 0 and 10 \n"
							elif idioma == 2:
								print "\n Por favor insira um numero entre 0 e 10 \n"
							elif idioma == 3:
								print "\n Por favor ingrese un numero entre 0 y 10 \n"
							i = 1
					except:
						if idioma == 1:
							print "\n Please enter a number between 0 and 10 \n"
						elif idioma == 2:
							print "\n Por favor insira um numero entre 0 e 10 \n"
						elif idioma == 3:
							print "\n Por favor ingrese un numero entre 0 y 10 \n"
						i = 1
							
			elif opt == 3:	
				num = str(y)
				if idioma == 1:
					print "\n What is the name of your "+ num + suffC +" class?"
					c = raw_input(" Enter here: ")
				elif idioma == 2:
					print "\n Como se chama a sua "+ num + suffC +" materia?"
					c = raw_input(" Isira aqui: ")
				elif idioma == 3:
					print "\n Como llama tu "+ num + suffC +" clase?"
					c = raw_input(" Ingresa aqui: ")
				y = int(num)
				i = 1
				while i == 1:
					try:
						if idioma == 1:
							print " What is your grade in this class?"
							gra = raw_input(" Enter here: ")
						elif idioma == 2:
							print " Qual eh a sua nota nessa materia?"
							gra = raw_input(" Insira aqui: ")
						elif idioma == 3:
							print " Cual es tu calificacion en esta clase?"
							gra = raw_input(" Ingresa aqui: ")
						g = float(gra)
						if g >= 93 and g <= 100:
							g = 10.0
							i = 0
						elif g >= 90 and g <= 92:
							g = 9.2
							i = 0
						elif g >= 87 and g <= 89:
							g = 8.9
							i = 0
						elif g >= 83 and g <= 86:
							g = 8.6
							i = 0
						elif g >= 80 and g <= 82:
							g = 8.2
							i = 0
						elif g >= 77 and g <= 79:
							g = 7.9
							i = 0
						elif g >= 73 and g <= 76:
							g = 7.6
							i = 0
						elif g >= 70 and g <= 72:
							g = 7.2
							i = 0
						elif g >= 67 and g <= 69:
							g = 6.9
							i = 0
						elif g >= 63 and g <= 66:
							g = 6.6
							i = 0
						elif g >= 60 and g <= 62:
							g = 6.2
							i = 0
						elif g >= 0 and g <= 59:
							g = 5.9
							i = 0
						else:
							if idioma == 1:
								print "\n Please enter a number between 0 and 10 \n"
							elif idioma == 2:
								print "\n Por favor insira um numero entre 0 e 10 \n"
							elif idioma == 3:
								print "\n Por favor ingrese un numero entre 0 y 10 \n"
							i = 1
					
					except:
						if idioma == 1:
							print "\n Please enter a number between 0 and 10 \n"
						elif idioma == 2:
							print "\n Por favor insira um numero entre 0 e 10 \n"
						elif idioma == 3:
							print "\n Por favor ingrese un numero entre 0 y 10 \n"
						i = 1	
			if cla == 8:
				if y == 1:
					if yp == 1:
						c1 = c
						g1 = g
					elif yp == 2:
						c1y2 = c
						g1y2 = g
					elif yp == 3:
						c1y3 = c
						g1y3 = g
					elif yp == 4:
						c1y4 = c
						g1y4 = g
					elif yp == 5:
						c1y5 = c
						g1y5 = g
						
				elif y == 2:
					if yp == 1:
						c2 = c
						g2 = g
					elif yp == 2:
						c2y2 = c
						g2y2 = g
					elif yp == 3:
						c2y3 = c
						g2y3 = g
					elif yp == 4:
						c2y4 = c
						g2y4 = g
					elif yp == 5:
						c2y5 = c
						g2y5 = g
						
				elif y == 3:
					if yp == 1:
						c3 = c
						g3 = g
					elif yp == 2:
						c3y2 = c
						g3y2 = g
					elif yp == 3:
						c3y3 = c
						g3y3 = g
					elif yp == 4:
						c3y4 = c
						g3y4 = g
					elif yp == 5:
						c3y5 = c
						g3y5 = g
					
				elif y == 4:
					if yp == 1:
						c4 = c
						g4 = g
					elif yp == 2:
						c4y2 = c
						g4y2 = g
					elif yp == 3:
						c4y3 = c
						g4y3 = g
					elif yp == 4:
						c4y4 = c
						g4y4 = g
					elif yp == 5:
						c4y5 = c
						g4y5 = g
					
				elif y == 5:
					if yp == 1:
						c5 = c
						g5 = g
					elif yp == 2:
						c5y2 = c
						g5y2 = g
					elif yp == 3:
						c5y3 = c
						g5y3 = g
					elif yp == 4:
						c5y4 = c
						g5y4 = g
					elif yp == 5:
						c5y5 = c
						g5y5 = g
					
				elif y == 6:
					if yp == 1:
						c6 = c
						g6 = g
					elif yp == 2:
						c6y2 = c
						g6y2 = g
					elif yp == 3:
						c6y3 = c
						g6y3 = g
					elif yp == 4:
						c6y4 = c
						g6y4 = g
					elif yp == 5:
						c6y5 = c
						g6y5 = g
						
				elif y == 7:
					if yp == 1:
						c7 = c
						g7 = g
					elif yp == 2:
						c7y2 = c
						g7y2 = g
					elif yp == 3:
						c7y3 = c
						g7y3 = g
					elif yp == 4:
						c7y4 = c
						g7y4 = g
					elif yp == 5:
						c7y5 = c
						g7y5 = g
					
				elif y == 8:
					if yp == 1:
						c8 = c
						g8 = g
					elif yp == 2:
						c8y2 = c
						g8y2 = g
					elif yp == 3:
						c8y3 = c
						g8y3 = g
					elif yp == 4:
						c8y4 = c
						g8y4 = g
					elif yp == 5:
						c8y5 = c
						g8y5 = g			
			
		
			elif cla == 9:
				if y == 1:
					if yp == 1:
						c1 = c
						g1 = g
					elif yp == 2:
						c1y2 = c
						g1y2 = g
					elif yp == 3:
						c1y3 = c
						g1y3 = g
					elif yp == 4:
						c1y4 = c
						g1y4 = g
					elif yp == 5:
						c1y5 = c
						g1y5 = g
						
				elif y == 2:
					if yp == 1:
						c2 = c
						g2 = g
					elif yp == 2:
						c2y2 = c
						g2y2 = g
					elif yp == 3:
						c2y3 = c
						g2y3 = g
					elif yp == 4:
						c2y4 = c
						g2y4 = g
					elif yp == 5:
						c2y5 = c
						g2y5 = g
						
				elif y == 3:
					if yp == 1:
						c3 = c
						g3 = g
					elif yp == 2:
						c3y2 = c
						g3y2 = g
					elif yp == 3:
						c3y3 = c
						g3y3 = g
					elif yp == 4:
						c3y4 = c
						g3y4 = g
					elif yp == 5:
						c3y5 = c
						g3y5 = g
					
				elif y == 4:
					if yp == 1:
						c4 = c
						g4 = g
					elif yp == 2:
						c4y2 = c
						g4y2 = g
					elif yp == 3:
						c4y3 = c
						g4y3 = g
					elif yp == 4:
						c4y4 = c
						g4y4 = g
					elif yp == 5:
						c4y5 = c
						g4y5 = g
					
				elif y == 5:
					if yp == 1:
						c5 = c
						g5 = g
					elif yp == 2:
						c5y2 = c
						g5y2 = g
					elif yp == 3:
						c5y3 = c
						g5y3 = g
					elif yp == 4:
						c5y4 = c
						g5y4 = g
					elif yp == 5:
						c5y5 = c
						g5y5 = g
					
				elif y == 6:
					if yp == 1:
						c6 = c
						g6 = g
					elif yp == 2:
						c6y2 = c
						g6y2 = g
					elif yp == 3:
						c6y3 = c
						g6y3 = g
					elif yp == 4:
						c6y4 = c
						g6y4 = g
					elif yp == 5:
						c6y5 = c
						g6y5 = g
						
				elif y == 7:
					if yp == 1:
						c7 = c
						g7 = g
					elif yp == 2:
						c7y2 = c
						g7y2 = g
					elif yp == 3:
						c7y3 = c
						g7y3 = g
					elif yp == 4:
						c7y4 = c
						g7y4 = g
					elif yp == 5:
						c7y5 = c
						g7y5 = g
					
				elif y == 8:
					if yp == 1:
						c8 = c
						g8 = g
					elif yp == 2:
						c8y2 = c
						g8y2 = g
					elif yp == 3:
						c8y3 = c
						g8y3 = g
					elif yp == 4:
						c8y4 = c
						g8y4 = g
					elif yp == 5:
						c8y5 = c
						g8y5 = g
					
				elif y == 9:
					if yp == 1:
						c9 = c
						g9 = g
					elif yp == 2:
						c9y2 = c
						g9y2 = g
					elif yp == 3:
						c9y3 = c
						g9y3 = g
					elif yp == 4:
						c9y4 = c
						g9y4 = g
					elif yp == 5:
						c9y5 = c
						g9y5 = g
		
			elif cla == 10:
				if y == 1:
					if yp == 1:
						c1 = c
						g1 = g
					elif yp == 2:
						c1y2 = c
						g1y2 = g
					elif yp == 3:
						c1y3 = c
						g1y3 = g
					elif yp == 4:
						c1y4 = c
						g1y4 = g
					elif yp == 5:
						c1y5 = c
						g1y5 = g
						
				elif y == 2:
					if yp == 1:
						c2 = c
						g2 = g
					elif yp == 2:
						c2y2 = c
						g2y2 = g
					elif yp == 3:
						c2y3 = c
						g2y3 = g
					elif yp == 4:
						c2y4 = c
						g2y4 = g
					elif yp == 5:
						c2y5 = c
						g2y5 = g
						
				elif y == 3:
					if yp == 1:
						c3 = c
						g3 = g
					elif yp == 2:
						c3y2 = c
						g3y2 = g
					elif yp == 3:
						c3y3 = c
						g3y3 = g
					elif yp == 4:
						c3y4 = c
						g3y4 = g
					elif yp == 5:
						c3y5 = c
						g3y5 = g
					
				elif y == 4:
					if yp == 1:
						c4 = c
						g4 = g
					elif yp == 2:
						c4y2 = c
						g4y2 = g
					elif yp == 3:
						c4y3 = c
						g4y3 = g
					elif yp == 4:
						c4y4 = c
						g4y4 = g
					elif yp == 5:
						c4y5 = c
						g4y5 = g
					
				elif y == 5:
					if yp == 1:
						c5 = c
						g5 = g
					elif yp == 2:
						c5y2 = c
						g5y2 = g
					elif yp == 3:
						c5y3 = c
						g5y3 = g
					elif yp == 4:
						c5y4 = c
						g5y4 = g
					elif yp == 5:
						c5y5 = c
						g5y5 = g
					
				elif y == 6:
					if yp == 1:
						c6 = c
						g6 = g
					elif yp == 2:
						c6y2 = c
						g6y2 = g
					elif yp == 3:
						c6y3 = c
						g6y3 = g
					elif yp == 4:
						c6y4 = c
						g6y4 = g
					elif yp == 5:
						c6y5 = c
						g6y5 = g
						
				elif y == 7:
					if yp == 1:
						c7 = c
						g7 = g
					elif yp == 2:
						c7y2 = c
						g7y2 = g
					elif yp == 3:
						c7y3 = c
						g7y3 = g
					elif yp == 4:
						c7y4 = c
						g7y4 = g
					elif yp == 5:
						c7y5 = c
						g7y5 = g
					
				elif y == 8:
					if yp == 1:
						c8 = c
						g8 = g
					elif yp == 2:
						c8y2 = c
						g8y2 = g
					elif yp == 3:
						c8y3 = c
						g8y3 = g
					elif yp == 4:
						c8y4 = c
						g8y4 = g
					elif yp == 5:
						c8y5 = c
						g8y5 = g
					
				elif y == 9 :
					if yp == 1:
						c9 = c
						g9 = g
					elif yp == 2:
						c9y2 = c
						g9y2 = g
					elif yp == 3:
						c9y3 = c
						g9y3 = g
					elif yp == 4:
						c9y4 = c
						g9y4 = g
					elif yp == 5:
						c9y5 = c
						g9y5 = g
						
				elif y == 10:
					if yp == 1:
						c10 = c
						g10 = g
					elif yp == 2:
						c10y2 = c
						g10y2 = g
					elif yp == 3:
						c10y3 = c
						g10y3 = g
					elif yp == 4:
						c10y4 = c
						g10y4 = g
					elif yp == 5:
						c10y5 = c
						g10y5 = g
	
			elif cla == 11:
				if y == 1:
					if yp == 1:
						c1 = c
						g1 = g
					elif yp == 2:
						c1y2 = c
						g1y2 = g
					elif yp == 3:
						c1y3 = c
						g1y3 = g
					elif yp == 4:
						c1y4 = c
						g1y4 = g
					elif yp == 5:
						c1y5 = c
						g1y5 = g
						
				elif y == 2:
					if yp == 1:
						c2 = c
						g2 = g
					elif yp == 2:
						c2y2 = c
						g2y2 = g
					elif yp == 3:
						c2y3 = c
						g2y3 = g
					elif yp == 4:
						c2y4 = c
						g2y4 = g
					elif yp == 5:
						c2y5 = c
						g2y5 = g
						
				elif y == 3:
					if yp == 1:
						c3 = c
						g3 = g
					elif yp == 2:
						c3y2 = c
						g3y2 = g
					elif yp == 3:
						c3y3 = c
						g3y3 = g
					elif yp == 4:
						c3y4 = c
						g3y4 = g
					elif yp == 5:
						c3y5 = c
						g3y5 = g
					
				elif y == 4:
					if yp == 1:
						c4 = c
						g4 = g
					elif yp == 2:
						c4y2 = c
						g4y2 = g
					elif yp == 3:
						c4y3 = c
						g4y3 = g
					elif yp == 4:
						c4y4 = c
						g4y4 = g
					elif yp == 5:
						c4y5 = c
						g4y5 = g
					
				elif y == 5:
					if yp == 1:
						c5 = c
						g5 = g
					elif yp == 2:
						c5y2 = c
						g5y2 = g
					elif yp == 3:
						c5y3 = c
						g5y3 = g
					elif yp == 4:
						c5y4 = c
						g5y4 = g
					elif yp == 5:
						c5y5 = c
						g5y5 = g
					
				elif y == 6:
					if yp == 1:
						c6 = c
						g6 = g
					elif yp == 2:
						c6y2 = c
						g6y2 = g
					elif yp == 3:
						c6y3 = c
						g6y3 = g
					elif yp == 4:
						c6y4 = c
						g6y4 = g
					elif yp == 5:
						c6y5 = c
						g6y5 = g
						
				elif y == 7:
					if yp == 1:
						c7 = c
						g7 = g
					elif yp == 2:
						c7y2 = c
						g7y2 = g
					elif yp == 3:
						c7y3 = c
						g7y3 = g
					elif yp == 4:
						c7y4 = c
						g7y4 = g
					elif yp == 5:
						c7y5 = c
						g7y5 = g
					
				elif y == 8:
					if yp == 1:
						c8 = c
						g8 = g
					elif yp == 2:
						c8y2 = c
						g8y2 = g
					elif yp == 3:
						c8y3 = c
						g8y3 = g
					elif yp == 4:
						c8y4 = c
						g8y4 = g
					elif yp == 5:
						c8y5 = c
						g8y5 = g
					
				elif y == 9 :
					if yp == 1:
						c9 = c
						g9 = g
					elif yp == 2:
						c9y2 = c
						g9y2 = g
					elif yp == 3:
						c9y3 = c
						g9y3 = g
					elif yp == 4:
						c9y4 = c
						g9y4 = g
					elif yp == 5:
						c9y5 = c
						g9y5 = g
						
				elif y == 10:
					if yp == 1:
						c10 = c
						g10 = g
					elif yp == 2:
						c10y2 = c
						g10y2 = g
					elif yp == 3:
						c10y3 = c
						g10y3 = g
					elif yp == 4:
						c10y4 = c
						g10y4 = g
					elif yp == 5:
						c10y5 = c
						g10y5 = g
				
				elif y == 11:
					if yp == 1:
						c11 = c
						g11 = g
					elif yp == 2:
						c11y2 = c
						g11y2 = g
					elif yp == 3:
						c11y3 = c
						g11y3 = g
					elif yp == 4:
						c11y4 = c
						g11y4 = g
					elif yp == 5:
						c11y5 = c
						g11y5 = g
		
			elif cla == 12:
				if y == 1:
					if yp == 1:
						c1 = c
						g1 = g
					elif yp == 2:
						c1y2 = c
						g1y2 = g
					elif yp == 3:
						c1y3 = c
						g1y3 = g
					elif yp == 4:
						c1y4 = c
						g1y4 = g
					elif yp == 5:
						c1y5 = c
						g1y5 = g
						
				elif y == 2:
					if yp == 1:
						c2 = c
						g2 = g
					elif yp == 2:
						c2y2 = c
						g2y2 = g
					elif yp == 3:
						c2y3 = c
						g2y3 = g
					elif yp == 4:
						c2y4 = c
						g2y4 = g
					elif yp == 5:
						c2y5 = c
						g2y5 = g
						
				elif y == 3:
					if yp == 1:
						c3 = c
						g3 = g
					elif yp == 2:
						c3y2 = c
						g3y2 = g
					elif yp == 3:
						c3y3 = c
						g3y3 = g
					elif yp == 4:
						c3y4 = c
						g3y4 = g
					elif yp == 5:
						c3y5 = c
						g3y5 = g
					
				elif y == 4:
					if yp == 1:
						c4 = c
						g4 = g
					elif yp == 2:
						c4y2 = c
						g4y2 = g
					elif yp == 3:
						c4y3 = c
						g4y3 = g
					elif yp == 4:
						c4y4 = c
						g4y4 = g
					elif yp == 5:
						c4y5 = c
						g4y5 = g
					
				elif y == 5:
					if yp == 1:
						c5 = c
						g5 = g
					elif yp == 2:
						c5y2 = c
						g5y2 = g
					elif yp == 3:
						c5y3 = c
						g5y3 = g
					elif yp == 4:
						c5y4 = c
						g5y4 = g
					elif yp == 5:
						c5y5 = c
						g5y5 = g
					
				elif y == 6:
					if yp == 1:
						c6 = c
						g6 = g
					elif yp == 2:
						c6y2 = c
						g6y2 = g
					elif yp == 3:
						c6y3 = c
						g6y3 = g
					elif yp == 4:
						c6y4 = c
						g6y4 = g
					elif yp == 5:
						c6y5 = c
						g6y5 = g
						
				elif y == 7:
					if yp == 1:
						c7 = c
						g7 = g
					elif yp == 2:
						c7y2 = c
						g7y2 = g
					elif yp == 3:
						c7y3 = c
						g7y3 = g
					elif yp == 4:
						c7y4 = c
						g7y4 = g
					elif yp == 5:
						c7y5 = c
						g7y5 = g
					
				elif y == 8:
					if yp == 1:
						c8 = c
						g8 = g
					elif yp == 2:
						c8y2 = c
						g8y2 = g
					elif yp == 3:
						c8y3 = c
						g8y3 = g
					elif yp == 4:
						c8y4 = c
						g8y4 = g
					elif yp == 5:
						c8y5 = c
						g8y5 = g
					
				elif y == 9 :
					if yp == 1:
						c9 = c
						g9 = g
					elif yp == 2:
						c9y2 = c
						g9y2 = g
					elif yp == 3:
						c9y3 = c
						g9y3 = g
					elif yp == 4:
						c9y4 = c
						g9y4 = g
					elif yp == 5:
						c9y5 = c
						g9y5 = g
						
				elif y == 10:
					if yp == 1:
						c10 = c
						g10 = g
					elif yp == 2:
						c10y2 = c
						g10y2 = g
					elif yp == 3:
						c10y3 = c
						g10y3 = g
					elif yp == 4:
						c10y4 = c
						g10y4 = g
					elif yp == 5:
						c10y5 = c
						g10y5 = g
				
				elif y == 11:
					if yp == 1:
						c11 = c
						g11 = g
					elif yp == 2:
						c11y2 = c
						g11y2 = g
					elif yp == 3:
						c11y3 = c
						g11y3 = g
					elif yp == 4:
						c11y4 = c
						g11y4 = g
					elif yp == 5:
						c11y5 = c
						g11y5 = g
						
				elif y == 12:
					if yp == 1:
						c12 = c
						g12 = g
					elif yp == 2:
						c12y2 = c
						g12y2 = g
					elif yp == 3:
						c12y3 = c
						g12y3 = g
					elif yp == 4:
						c12y4 = c
						g12y4 = g
					elif yp == 5:
						c12y5 = c
						g12y5 = g
	
		
			elif cla == 13:
				if y == 1:
					if yp == 1:
						c1 = c
						g1 = g
					elif yp == 2:
						c1y2 = c
						g1y2 = g
					elif yp == 3:
						c1y3 = c
						g1y3 = g
					elif yp == 4:
						c1y4 = c
						g1y4 = g
					elif yp == 5:
						c1y5 = c
						g1y5 = g
						
				elif y == 2:
					if yp == 1:
						c2 = c
						g2 = g
					elif yp == 2:
						c2y2 = c
						g2y2 = g
					elif yp == 3:
						c2y3 = c
						g2y3 = g
					elif yp == 4:
						c2y4 = c
						g2y4 = g
					elif yp == 5:
						c2y5 = c
						g2y5 = g
						
				elif y == 3:
					if yp == 1:
						c3 = c
						g3 = g
					elif yp == 2:
						c3y2 = c
						g3y2 = g
					elif yp == 3:
						c3y3 = c
						g3y3 = g
					elif yp == 4:
						c3y4 = c
						g3y4 = g
					elif yp == 5:
						c3y5 = c
						g3y5 = g
					
				elif y == 4:
					if yp == 1:
						c4 = c
						g4 = g
					elif yp == 2:
						c4y2 = c
						g4y2 = g
					elif yp == 3:
						c4y3 = c
						g4y3 = g
					elif yp == 4:
						c4y4 = c
						g4y4 = g
					elif yp == 5:
						c4y5 = c
						g4y5 = g
					
				elif y == 5:
					if yp == 1:
						c5 = c
						g5 = g
					elif yp == 2:
						c5y2 = c
						g5y2 = g
					elif yp == 3:
						c5y3 = c
						g5y3 = g
					elif yp == 4:
						c5y4 = c
						g5y4 = g
					elif yp == 5:
						c5y5 = c
						g5y5 = g
					
				elif y == 6:
					if yp == 1:
						c6 = c
						g6 = g
					elif yp == 2:
						c6y2 = c
						g6y2 = g
					elif yp == 3:
						c6y3 = c
						g6y3 = g
					elif yp == 4:
						c6y4 = c
						g6y4 = g
					elif yp == 5:
						c6y5 = c
						g6y5 = g
						
				elif y == 7:
					if yp == 1:
						c7 = c
						g7 = g
					elif yp == 2:
						c7y2 = c
						g7y2 = g
					elif yp == 3:
						c7y3 = c
						g7y3 = g
					elif yp == 4:
						c7y4 = c
						g7y4 = g
					elif yp == 5:
						c7y5 = c
						g7y5 = g
					
				elif y == 8:
					if yp == 1:
						c8 = c
						g8 = g
					elif yp == 2:
						c8y2 = c
						g8y2 = g
					elif yp == 3:
						c8y3 = c
						g8y3 = g
					elif yp == 4:
						c8y4 = c
						g8y4 = g
					elif yp == 5:
						c8y5 = c
						g8y5 = g
					
				elif y == 9 :
					if yp == 1:
						c9 = c
						g9 = g
					elif yp == 2:
						c9y2 = c
						g9y2 = g
					elif yp == 3:
						c9y3 = c
						g9y3 = g
					elif yp == 4:
						c9y4 = c
						g9y4 = g
					elif yp == 5:
						c9y5 = c
						g9y5 = g
						
				elif y == 10:
					if yp == 1:
						c10 = c
						g10 = g
					elif yp == 2:
						c10y2 = c
						g10y2 = g
					elif yp == 3:
						c10y3 = c
						g10y3 = g
					elif yp == 4:
						c10y4 = c
						g10y4 = g
					elif yp == 5:
						c10y5 = c
						g10y5 = g
				
				elif y == 11:
					if yp == 1:
						c11 = c
						g11 = g
					elif yp == 2:
						c11y2 = c
						g11y2 = g
					elif yp == 3:
						c11y3 = c
						g11y3 = g
					elif yp == 4:
						c11y4 = c
						g11y4 = g
					elif yp == 5:
						c11y5 = c
						g11y5 = g
						
				elif y == 12:
					if yp == 1:
						c12 = c
						g12 = g
					elif yp == 2:
						c12y2 = c
						g12y2 = g
					elif yp == 3:
						c12y3 = c
						g12y3 = g
					elif yp == 4:
						c12y4 = c
						g12y4 = g
					elif yp == 5:
						c12y5 = c
						g12y5 = g
						
				elif y == 13:
					if yp == 1:
						c13 = c
						g13 = g
					elif yp == 2:
						c13y2 = c
						g13y2 = g
					elif yp == 3:
						c13y3 = c
						g13y3 = g
					elif yp == 4:
						c13y4 = c
						g13y4 = g
					elif yp == 5:
						c13y5 = c
						g13y5 = g
	
		
			elif cla == 14:
				if y == 1:
					if yp == 1:
						c1 = c
						g1 = g
					elif yp == 2:
						c1y2 = c
						g1y2 = g
					elif yp == 3:
						c1y3 = c
						g1y3 = g
					elif yp == 4:
						c1y4 = c
						g1y4 = g
					elif yp == 5:
						c1y5 = c
						g1y5 = g
						
				elif y == 2:
					if yp == 1:
						c2 = c
						g2 = g
					elif yp == 2:
						c2y2 = c
						g2y2 = g
					elif yp == 3:
						c2y3 = c
						g2y3 = g
					elif yp == 4:
						c2y4 = c
						g2y4 = g
					elif yp == 5:
						c2y5 = c
						g2y5 = g
						
				elif y == 3:
					if yp == 1:
						c3 = c
						g3 = g
					elif yp == 2:
						c3y2 = c
						g3y2 = g
					elif yp == 3:
						c3y3 = c
						g3y3 = g
					elif yp == 4:
						c3y4 = c
						g3y4 = g
					elif yp == 5:
						c3y5 = c
						g3y5 = g
					
				elif y == 4:
					if yp == 1:
						c4 = c
						g4 = g
					elif yp == 2:
						c4y2 = c
						g4y2 = g
					elif yp == 3:
						c4y3 = c
						g4y3 = g
					elif yp == 4:
						c4y4 = c
						g4y4 = g
					elif yp == 5:
						c4y5 = c
						g4y5 = g
					
				elif y == 5:
					if yp == 1:
						c5 = c
						g5 = g
					elif yp == 2:
						c5y2 = c
						g5y2 = g
					elif yp == 3:
						c5y3 = c
						g5y3 = g
					elif yp == 4:
						c5y4 = c
						g5y4 = g
					elif yp == 5:
						c5y5 = c
						g5y5 = g
					
				elif y == 6:
					if yp == 1:
						c6 = c
						g6 = g
					elif yp == 2:
						c6y2 = c
						g6y2 = g
					elif yp == 3:
						c6y3 = c
						g6y3 = g
					elif yp == 4:
						c6y4 = c
						g6y4 = g
					elif yp == 5:
						c6y5 = c
						g6y5 = g
						
				elif y == 7:
					if yp == 1:
						c7 = c
						g7 = g
					elif yp == 2:
						c7y2 = c
						g7y2 = g
					elif yp == 3:
						c7y3 = c
						g7y3 = g
					elif yp == 4:
						c7y4 = c
						g7y4 = g
					elif yp == 5:
						c7y5 = c
						g7y5 = g
					
				elif y == 8:
					if yp == 1:
						c8 = c
						g8 = g
					elif yp == 2:
						c8y2 = c
						g8y2 = g
					elif yp == 3:
						c8y3 = c
						g8y3 = g
					elif yp == 4:
						c8y4 = c
						g8y4 = g
					elif yp == 5:
						c8y5 = c
						g8y5 = g
					
				elif y == 9 :
					if yp == 1:
						c9 = c
						g9 = g
					elif yp == 2:
						c9y2 = c
						g9y2 = g
					elif yp == 3:
						c9y3 = c
						g9y3 = g
					elif yp == 4:
						c9y4 = c
						g9y4 = g
					elif yp == 5:
						c9y5 = c
						g9y5 = g
						
				elif y == 10:
					if yp == 1:
						c10 = c
						g10 = g
					elif yp == 2:
						c10y2 = c
						g10y2 = g
					elif yp == 3:
						c10y3 = c
						g10y3 = g
					elif yp == 4:
						c10y4 = c
						g10y4 = g
					elif yp == 5:
						c10y5 = c
						g10y5 = g
				
				elif y == 11:
					if yp == 1:
						c11 = c
						g11 = g
					elif yp == 2:
						c11y2 = c
						g11y2 = g
					elif yp == 3:
						c11y3 = c
						g11y3 = g
					elif yp == 4:
						c11y4 = c
						g11y4 = g
					elif yp == 5:
						c11y5 = c
						g11y5 = g
						
				elif y == 12:
					if yp == 1:
						c12 = c
						g12 = g
					elif yp == 2:
						c12y2 = c
						g12y2 = g
					elif yp == 3:
						c12y3 = c
						g12y3 = g
					elif yp == 4:
						c12y4 = c
						g12y4 = g
					elif yp == 5:
						c12y5 = c
						g12y5 = g
						
				elif y == 13:
					if yp == 1:
						c13 = c
						g13 = g
					elif yp == 2:
						c13y2 = c
						g13y2 = g
					elif yp == 3:
						c13y3 = c
						g13y3 = g
					elif yp == 4:
						c13y4 = c
						g13y4 = g
					elif yp == 5:
						c13y5 = c
						g13y5 = g
						
				elif y == 14:
					if yp == 1:
						c14 = c
						g14 = g
					elif yp == 2:
						c14y2 = c
						g14y2 = g
					elif yp == 3:
						c14y3 = c
						g14y3 = g
					elif yp == 4:
						c14y4 = c
						g14y4 = g
					elif yp == 5:
						c14y5 = c
						g14y5 = g
	
			
			elif cla == 15:
				if y == 1:
					if yp == 1:
						c1 = c
						g1 = g
					elif yp == 2:
						c1y2 = c
						g1y2 = g
					elif yp == 3:
						c1y3 = c
						g1y3 = g
					elif yp == 4:
						c1y4 = c
						g1y4 = g
					elif yp == 5:
						c1y5 = c
						g1y5 = g
						
				elif y == 2:
					if yp == 1:
						c2 = c
						g2 = g
					elif yp == 2:
						c2y2 = c
						g2y2 = g
					elif yp == 3:
						c2y3 = c
						g2y3 = g
					elif yp == 4:
						c2y4 = c
						g2y4 = g
					elif yp == 5:
						c2y5 = c
						g2y5 = g
						
				elif y == 3:
					if yp == 1:
						c3 = c
						g3 = g
					elif yp == 2:
						c3y2 = c
						g3y2 = g
					elif yp == 3:
						c3y3 = c
						g3y3 = g
					elif yp == 4:
						c3y4 = c
						g3y4 = g
					elif yp == 5:
						c3y5 = c
						g3y5 = g
					
				elif y == 4:
					if yp == 1:
						c4 = c
						g4 = g
					elif yp == 2:
						c4y2 = c
						g4y2 = g
					elif yp == 3:
						c4y3 = c
						g4y3 = g
					elif yp == 4:
						c4y4 = c
						g4y4 = g
					elif yp == 5:
						c4y5 = c
						g4y5 = g
					
				elif y == 5:
					if yp == 1:
						c5 = c
						g5 = g
					elif yp == 2:
						c5y2 = c
						g5y2 = g
					elif yp == 3:
						c5y3 = c
						g5y3 = g
					elif yp == 4:
						c5y4 = c
						g5y4 = g
					elif yp == 5:
						c5y5 = c
						g5y5 = g
					
				elif y == 6:
					if yp == 1:
						c6 = c
						g6 = g
					elif yp == 2:
						c6y2 = c
						g6y2 = g
					elif yp == 3:
						c6y3 = c
						g6y3 = g
					elif yp == 4:
						c6y4 = c
						g6y4 = g
					elif yp == 5:
						c6y5 = c
						g6y5 = g
						
				elif y == 7:
					if yp == 1:
						c7 = c
						g7 = g
					elif yp == 2:
						c7y2 = c
						g7y2 = g
					elif yp == 3:
						c7y3 = c
						g7y3 = g
					elif yp == 4:
						c7y4 = c
						g7y4 = g
					elif yp == 5:
						c7y5 = c
						g7y5 = g
					
				elif y == 8:
					if yp == 1:
						c8 = c
						g8 = g
					elif yp == 2:
						c8y2 = c
						g8y2 = g
					elif yp == 3:
						c8y3 = c
						g8y3 = g
					elif yp == 4:
						c8y4 = c
						g8y4 = g
					elif yp == 5:
						c8y5 = c
						g8y5 = g
					
				elif y == 9 :
					if yp == 1:
						c9 = c
						g9 = g
					elif yp == 2:
						c9y2 = c
						g9y2 = g
					elif yp == 3:
						c9y3 = c
						g9y3 = g
					elif yp == 4:
						c9y4 = c
						g9y4 = g
					elif yp == 5:
						c9y5 = c
						g9y5 = g
						
				elif y == 10:
					if yp == 1:
						c10 = c
						g10 = g
					elif yp == 2:
						c10y2 = c
						g10y2 = g
					elif yp == 3:
						c10y3 = c
						g10y3 = g
					elif yp == 4:
						c10y4 = c
						g10y4 = g
					elif yp == 5:
						c10y5 = c
						g10y5 = g
				
				elif y == 11:
					if yp == 1:
						c11 = c
						g11 = g
					elif yp == 2:
						c11y2 = c
						g11y2 = g
					elif yp == 3:
						c11y3 = c
						g11y3 = g
					elif yp == 4:
						c11y4 = c
						g11y4 = g
					elif yp == 5:
						c11y5 = c
						g11y5 = g
						
				elif y == 12:
					if yp == 1:
						c12 = c
						g12 = g
					elif yp == 2:
						c12y2 = c
						g12y2 = g
					elif yp == 3:
						c12y3 = c
						g12y3 = g
					elif yp == 4:
						c12y4 = c
						g12y4 = g
					elif yp == 5:
						c12y5 = c
						g12y5 = g
						
				elif y == 13:
					if yp == 1:
						c13 = c
						g13 = g
					elif yp == 2:
						c13y2 = c
						g13y2 = g
					elif yp == 3:
						c13y3 = c
						g13y3 = g
					elif yp == 4:
						c13y4 = c
						g13y4 = g
					elif yp == 5:
						c13y5 = c
						g13y5 = g
						
				elif y == 14:
					if yp == 1:
						c14 = c
						g14 = g
					elif yp == 2:
						c14y2 = c
						g14y2 = g
					elif yp == 3:
						c14y3 = c
						g14y3 = g
					elif yp == 4:
						c14y4 = c
						g14y4 = g
					elif yp == 5:
						c14y5 = c
						g14y5 = g
						
				elif y == 15:
					if yp == 1:
						c15 = c
						g15 = g
					elif yp == 2:
						c15y2 = c
						g15y2 = g
					elif yp == 3:
						c15y3 = c
						g15y3 = g
					elif yp == 4:
						c15y4 = c
						g15y4 = g
					elif yp == 5:
						c15y5 = c
						g15y5 = g
		
			elif cla == 16:
				if y == 1:
					if yp == 1:
						c1 = c
						g1 = g
					elif yp == 2:
						c1y2 = c
						g1y2 = g
					elif yp == 3:
						c1y3 = c
						g1y3 = g
					elif yp == 4:
						c1y4 = c
						g1y4 = g
					elif yp == 5:
						c1y5 = c
						g1y5 = g
						
				elif y == 2:
					if yp == 1:
						c2 = c
						g2 = g
					elif yp == 2:
						c2y2 = c
						g2y2 = g
					elif yp == 3:
						c2y3 = c
						g2y3 = g
					elif yp == 4:
						c2y4 = c
						g2y4 = g
					elif yp == 5:
						c2y5 = c
						g2y5 = g
						
				elif y == 3:
					if yp == 1:
						c3 = c
						g3 = g
					elif yp == 2:
						c3y2 = c
						g3y2 = g
					elif yp == 3:
						c3y3 = c
						g3y3 = g
					elif yp == 4:
						c3y4 = c
						g3y4 = g
					elif yp == 5:
						c3y5 = c
						g3y5 = g
					
				elif y == 4:
					if yp == 1:
						c4 = c
						g4 = g
					elif yp == 2:
						c4y2 = c
						g4y2 = g
					elif yp == 3:
						c4y3 = c
						g4y3 = g
					elif yp == 4:
						c4y4 = c
						g4y4 = g
					elif yp == 5:
						c4y5 = c
						g4y5 = g
					
				elif y == 5:
					if yp == 1:
						c5 = c
						g5 = g
					elif yp == 2:
						c5y2 = c
						g5y2 = g
					elif yp == 3:
						c5y3 = c
						g5y3 = g
					elif yp == 4:
						c5y4 = c
						g5y4 = g
					elif yp == 5:
						c5y5 = c
						g5y5 = g
					
				elif y == 6:
					if yp == 1:
						c6 = c
						g6 = g
					elif yp == 2:
						c6y2 = c
						g6y2 = g
					elif yp == 3:
						c6y3 = c
						g6y3 = g
					elif yp == 4:
						c6y4 = c
						g6y4 = g
					elif yp == 5:
						c6y5 = c
						g6y5 = g
						
				elif y == 7:
					if yp == 1:
						c7 = c
						g7 = g
					elif yp == 2:
						c7y2 = c
						g7y2 = g
					elif yp == 3:
						c7y3 = c
						g7y3 = g
					elif yp == 4:
						c7y4 = c
						g7y4 = g
					elif yp == 5:
						c7y5 = c
						g7y5 = g
					
				elif y == 8:
					if yp == 1:
						c8 = c
						g8 = g
					elif yp == 2:
						c8y2 = c
						g8y2 = g
					elif yp == 3:
						c8y3 = c
						g8y3 = g
					elif yp == 4:
						c8y4 = c
						g8y4 = g
					elif yp == 5:
						c8y5 = c
						g8y5 = g
					
				elif y == 9 :
					if yp == 1:
						c9 = c
						g9 = g
					elif yp == 2:
						c9y2 = c
						g9y2 = g
					elif yp == 3:
						c9y3 = c
						g9y3 = g
					elif yp == 4:
						c9y4 = c
						g9y4 = g
					elif yp == 5:
						c9y5 = c
						g9y5 = g
						
				elif y == 10:
					if yp == 1:
						c10 = c
						g10 = g
					elif yp == 2:
						c10y2 = c
						g10y2 = g
					elif yp == 3:
						c10y3 = c
						g10y3 = g
					elif yp == 4:
						c10y4 = c
						g10y4 = g
					elif yp == 5:
						c10y5 = c
						g10y5 = g
				
				elif y == 11:
					if yp == 1:
						c11 = c
						g11 = g
					elif yp == 2:
						c11y2 = c
						g11y2 = g
					elif yp == 3:
						c11y3 = c
						g11y3 = g
					elif yp == 4:
						c11y4 = c
						g11y4 = g
					elif yp == 5:
						c11y5 = c
						g11y5 = g
						
				elif y == 12:
					if yp == 1:
						c12 = c
						g12 = g
					elif yp == 2:
						c12y2 = c
						g12y2 = g
					elif yp == 3:
						c12y3 = c
						g12y3 = g
					elif yp == 4:
						c12y4 = c
						g12y4 = g
					elif yp == 5:
						c12y5 = c
						g12y5 = g
						
				elif y == 13:
					if yp == 1:
						c13 = c
						g13 = g
					elif yp == 2:
						c13y2 = c
						g13y2 = g
					elif yp == 3:
						c13y3 = c
						g13y3 = g
					elif yp == 4:
						c13y4 = c
						g13y4 = g
					elif yp == 5:
						c13y5 = c
						g13y5 = g
						
				elif y == 14:
					if yp == 1:
						c14 = c
						g14 = g
					elif yp == 2:
						c14y2 = c
						g14y2 = g
					elif yp == 3:
						c14y3 = c
						g14y3 = g
					elif yp == 4:
						c14y4 = c
						g14y4 = g
					elif yp == 5:
						c14y5 = c
						g14y5 = g
						
				elif y == 15:
					if yp == 1:
						c15 = c
						g15 = g
					elif yp == 2:
						c15y2 = c
						g15y2 = g
					elif yp == 3:
						c15y3 = c
						g15y3 = g
					elif yp == 4:
						c15y4 = c
						g15y4 = g
					elif yp == 5:
						c15y5 = c
						g15y5 = g
						
				elif y == 16:
					if yp == 1:
						c16 = c
						g16 = g
					elif yp == 2:
						c16y2 = c
						g16y2 = g
					elif yp == 3:
						c16y3 = c
						g16y3 = g
					elif yp == 4:
						c16y4 = c
						g16y4 = g
					elif yp == 5:
						c16y5 = c
						g16y5 = g
	
		
			elif cla == 17:
				if y == 1:
					if yp == 1:
						c1 = c
						g1 = g
					elif yp == 2:
						c1y2 = c
						g1y2 = g
					elif yp == 3:
						c1y3 = c
						g1y3 = g
					elif yp == 4:
						c1y4 = c
						g1y4 = g
					elif yp == 5:
						c1y5 = c
						g1y5 = g
						
				elif y == 2:
					if yp == 1:
						c2 = c
						g2 = g
					elif yp == 2:
						c2y2 = c
						g2y2 = g
					elif yp == 3:
						c2y3 = c
						g2y3 = g
					elif yp == 4:
						c2y4 = c
						g2y4 = g
					elif yp == 5:
						c2y5 = c
						g2y5 = g
						
				elif y == 3:
					if yp == 1:
						c3 = c
						g3 = g
					elif yp == 2:
						c3y2 = c
						g3y2 = g
					elif yp == 3:
						c3y3 = c
						g3y3 = g
					elif yp == 4:
						c3y4 = c
						g3y4 = g
					elif yp == 5:
						c3y5 = c
						g3y5 = g
					
				elif y == 4:
					if yp == 1:
						c4 = c
						g4 = g
					elif yp == 2:
						c4y2 = c
						g4y2 = g
					elif yp == 3:
						c4y3 = c
						g4y3 = g
					elif yp == 4:
						c4y4 = c
						g4y4 = g
					elif yp == 5:
						c4y5 = c
						g4y5 = g
					
				elif y == 5:
					if yp == 1:
						c5 = c
						g5 = g
					elif yp == 2:
						c5y2 = c
						g5y2 = g
					elif yp == 3:
						c5y3 = c
						g5y3 = g
					elif yp == 4:
						c5y4 = c
						g5y4 = g
					elif yp == 5:
						c5y5 = c
						g5y5 = g
					
				elif y == 6:
					if yp == 1:
						c6 = c
						g6 = g
					elif yp == 2:
						c6y2 = c
						g6y2 = g
					elif yp == 3:
						c6y3 = c
						g6y3 = g
					elif yp == 4:
						c6y4 = c
						g6y4 = g
					elif yp == 5:
						c6y5 = c
						g6y5 = g
						
				elif y == 7:
					if yp == 1:
						c7 = c
						g7 = g
					elif yp == 2:
						c7y2 = c
						g7y2 = g
					elif yp == 3:
						c7y3 = c
						g7y3 = g
					elif yp == 4:
						c7y4 = c
						g7y4 = g
					elif yp == 5:
						c7y5 = c
						g7y5 = g
					
				elif y == 8:
					if yp == 1:
						c8 = c
						g8 = g
					elif yp == 2:
						c8y2 = c
						g8y2 = g
					elif yp == 3:
						c8y3 = c
						g8y3 = g
					elif yp == 4:
						c8y4 = c
						g8y4 = g
					elif yp == 5:
						c8y5 = c
						g8y5 = g
					
				elif y == 9 :
					if yp == 1:
						c9 = c
						g9 = g
					elif yp == 2:
						c9y2 = c
						g9y2 = g
					elif yp == 3:
						c9y3 = c
						g9y3 = g
					elif yp == 4:
						c9y4 = c
						g9y4 = g
					elif yp == 5:
						c9y5 = c
						g9y5 = g
						
				elif y == 10:
					if yp == 1:
						c10 = c
						g10 = g
					elif yp == 2:
						c10y2 = c
						g10y2 = g
					elif yp == 3:
						c10y3 = c
						g10y3 = g
					elif yp == 4:
						c10y4 = c
						g10y4 = g
					elif yp == 5:
						c10y5 = c
						g10y5 = g
				
				elif y == 11:
					if yp == 1:
						c11 = c
						g11 = g
					elif yp == 2:
						c11y2 = c
						g11y2 = g
					elif yp == 3:
						c11y3 = c
						g11y3 = g
					elif yp == 4:
						c11y4 = c
						g11y4 = g
					elif yp == 5:
						c11y5 = c
						g11y5 = g
						
				elif y == 12:
					if yp == 1:
						c12 = c
						g12 = g
					elif yp == 2:
						c12y2 = c
						g12y2 = g
					elif yp == 3:
						c12y3 = c
						g12y3 = g
					elif yp == 4:
						c12y4 = c
						g12y4 = g
					elif yp == 5:
						c12y5 = c
						g12y5 = g
						
				elif y == 13:
					if yp == 1:
						c13 = c
						g13 = g
					elif yp == 2:
						c13y2 = c
						g13y2 = g
					elif yp == 3:
						c13y3 = c
						g13y3 = g
					elif yp == 4:
						c13y4 = c
						g13y4 = g
					elif yp == 5:
						c13y5 = c
						g13y5 = g
						
				elif y == 14:
					if yp == 1:
						c14 = c
						g14 = g
					elif yp == 2:
						c14y2 = c
						g14y2 = g
					elif yp == 3:
						c14y3 = c
						g14y3 = g
					elif yp == 4:
						c14y4 = c
						g14y4 = g
					elif yp == 5:
						c14y5 = c
						g14y5 = g
						
				elif y == 15:
					if yp == 1:
						c15 = c
						g15 = g
					elif yp == 2:
						c15y2 = c
						g15y2 = g
					elif yp == 3:
						c15y3 = c
						g15y3 = g
					elif yp == 4:
						c15y4 = c
						g15y4 = g
					elif yp == 5:
						c15y5 = c
						g15y5 = g
						
				elif y == 16:
					if yp == 1:
						c16 = c
						g16 = g
					elif yp == 2:
						c16y2 = c
						g16y2 = g
					elif yp == 3:
						c16y3 = c
						g16y3 = g
					elif yp == 4:
						c16y4 = c
						g16y4 = g
					elif yp == 5:
						c16y5 = c
						g16y5 = g
						
				elif y == 17:
					if yp == 1:
						c17 = c
						g17 = g
					elif yp == 2:
						c17y2 = c
						g17y2 = g
					elif yp == 3:
						c17y3 = c
						g17y3 = g
					elif yp == 4:
						c17y4 = c
						g17y4 = g
					elif yp == 5:
						c17y5 = c
						g17y5 = g
	
		
			elif cla == 18:
				if y == 1:
					if yp == 1:
						c1 = c
						g1 = g
					elif yp == 2:
						c1y2 = c
						g1y2 = g
					elif yp == 3:
						c1y3 = c
						g1y3 = g
					elif yp == 4:
						c1y4 = c
						g1y4 = g
					elif yp == 5:
						c1y5 = c
						g1y5 = g
						
				elif y == 2:
					if yp == 1:
						c2 = c
						g2 = g
					elif yp == 2:
						c2y2 = c
						g2y2 = g
					elif yp == 3:
						c2y3 = c
						g2y3 = g
					elif yp == 4:
						c2y4 = c
						g2y4 = g
					elif yp == 5:
						c2y5 = c
						g2y5 = g
						
				elif y == 3:
					if yp == 1:
						c3 = c
						g3 = g
					elif yp == 2:
						c3y2 = c
						g3y2 = g
					elif yp == 3:
						c3y3 = c
						g3y3 = g
					elif yp == 4:
						c3y4 = c
						g3y4 = g
					elif yp == 5:
						c3y5 = c
						g3y5 = g
					
				elif y == 4:
					if yp == 1:
						c4 = c
						g4 = g
					elif yp == 2:
						c4y2 = c
						g4y2 = g
					elif yp == 3:
						c4y3 = c
						g4y3 = g
					elif yp == 4:
						c4y4 = c
						g4y4 = g
					elif yp == 5:
						c4y5 = c
						g4y5 = g
					
				elif y == 5:
					if yp == 1:
						c5 = c
						g5 = g
					elif yp == 2:
						c5y2 = c
						g5y2 = g
					elif yp == 3:
						c5y3 = c
						g5y3 = g
					elif yp == 4:
						c5y4 = c
						g5y4 = g
					elif yp == 5:
						c5y5 = c
						g5y5 = g
					
				elif y == 6:
					if yp == 1:
						c6 = c
						g6 = g
					elif yp == 2:
						c6y2 = c
						g6y2 = g
					elif yp == 3:
						c6y3 = c
						g6y3 = g
					elif yp == 4:
						c6y4 = c
						g6y4 = g
					elif yp == 5:
						c6y5 = c
						g6y5 = g
						
				elif y == 7:
					if yp == 1:
						c7 = c
						g7 = g
					elif yp == 2:
						c7y2 = c
						g7y2 = g
					elif yp == 3:
						c7y3 = c
						g7y3 = g
					elif yp == 4:
						c7y4 = c
						g7y4 = g
					elif yp == 5:
						c7y5 = c
						g7y5 = g
					
				elif y == 8:
					if yp == 1:
						c8 = c
						g8 = g
					elif yp == 2:
						c8y2 = c
						g8y2 = g
					elif yp == 3:
						c8y3 = c
						g8y3 = g
					elif yp == 4:
						c8y4 = c
						g8y4 = g
					elif yp == 5:
						c8y5 = c
						g8y5 = g
					
				elif y == 9 :
					if yp == 1:
						c9 = c
						g9 = g
					elif yp == 2:
						c9y2 = c
						g9y2 = g
					elif yp == 3:
						c9y3 = c
						g9y3 = g
					elif yp == 4:
						c9y4 = c
						g9y4 = g
					elif yp == 5:
						c9y5 = c
						g9y5 = g
						
				elif y == 10:
					if yp == 1:
						c10 = c
						g10 = g
					elif yp == 2:
						c10y2 = c
						g10y2 = g
					elif yp == 3:
						c10y3 = c
						g10y3 = g
					elif yp == 4:
						c10y4 = c
						g10y4 = g
					elif yp == 5:
						c10y5 = c
						g10y5 = g
				
				elif y == 11:
					if yp == 1:
						c11 = c
						g11 = g
					elif yp == 2:
						c11y2 = c
						g11y2 = g
					elif yp == 3:
						c11y3 = c
						g11y3 = g
					elif yp == 4:
						c11y4 = c
						g11y4 = g
					elif yp == 5:
						c11y5 = c
						g11y5 = g
						
				elif y == 12:
					if yp == 1:
						c12 = c
						g12 = g
					elif yp == 2:
						c12y2 = c
						g12y2 = g
					elif yp == 3:
						c12y3 = c
						g12y3 = g
					elif yp == 4:
						c12y4 = c
						g12y4 = g
					elif yp == 5:
						c12y5 = c
						g12y5 = g
						
				elif y == 13:
					if yp == 1:
						c13 = c
						g13 = g
					elif yp == 2:
						c13y2 = c
						g13y2 = g
					elif yp == 3:
						c13y3 = c
						g13y3 = g
					elif yp == 4:
						c13y4 = c
						g13y4 = gs
					elif yp == 5:
						c13y5 = c
						g13y5 = g
						
				elif y == 14:
					if yp == 1:
						c14 = c
						g14 = g
					elif yp == 2:
						c14y2 = c
						g14y2 = g
					elif yp == 3:
						c14y3 = c
						g14y3 = g
					elif yp == 4:
						c14y4 = c
						g14y4 = g
					elif yp == 5:
						c14y5 = c
						g14y5 = g
						
				elif y == 15:
					if yp == 1:
						c15 = c
						g15 = g
					elif yp == 2:
						c15y2 = c
						g15y2 = g
					elif yp == 3:
						c15y3 = c
						g15y3 = g
					elif yp == 4:
						c15y4 = c
						g15y4 = g
					elif yp == 5:
						c15y5 = c
						g15y5 = g
						
				elif y == 16:
					if yp == 1:
						c16 = c
						g16 = g
					elif yp == 2:
						c16y2 = c
						g16y2 = g
					elif yp == 3:
						c16y3 = c
						g16y3 = g
					elif yp == 4:
						c16y4 = c
						g16y4 = g
					elif yp == 5:
						c16y5 = c
						g16y5 = g
						
				elif y == 17:
					if yp == 1:
						c17 = c
						g5 = g
					elif yp == 2:
						c17y2 = c
						g17y2 = g
					elif yp == 3:
						c17y3 = c
						g17y3 = g
					elif yp == 4:
						c17y4 = c
						g17y4 = g
					elif yp == 5:
						c17y5 = c
						g17y5 = g
			
				elif y == 18:
					if yp == 1:
						c18 = c
						g18 = g
					elif yp == 2:
						c18y2 = c
						g18y2 = g
					elif yp == 3:
						c18y3 = c
						g18y3 = g
					elif yp == 4:
						c18y4 = c
						g18y4 = g
					elif yp == 5:
						c18y5 = c
						g18y5 = g
			
			y = y + 1
		
			x = x - 1
			
		y = 1
		test = 1
		opt = 0
		
	else:
		print " Please, enter a number between 8 and 20"
		test = 0
	
	repeat = repeat + 1
	suffix = suffix + 1


x = cla1	
y = 1
while x > 0:
	if cyf == 1:
		if y == 1:
			if g1 >= 9.3 and g1 <= 10:
				gp1 = 4.0
			elif g1 >=  9 and g1 <= 9.2:
				gp1 = 3.7
			elif g1 >=  8.7 and g1 <= 8.9:
				gp1 = 3.3
			elif g1 >=  8.3 and g1 <= 8.6:
				gp1 = 3.0
			elif g1 >=  8 and g1 <= 8.2:
				gp1 = 2.7
			elif g1 >=  7.7 and g1 <= 7.9:
				gp1 = 2.3
			elif g1 >=  7.3 and g1 <= 7.6:
				gp1 = 2.0
			elif g1 >=  7 and g1 <= 7.2:
				gp1 = 1.7
			elif g1 >=  6.7 and g1 <= 6.9:
				gp1 = 1.3
			elif g1 >=  6.3 and g1 <= 6.6:
				gp1 = 1.0
			elif g1 >=  6 and g1 <= 6.2:
				gp1 = .7
			elif g1 < 6:
				gp1 = 0
			
		elif y == 2:
			if g2 >= 9.3 and g2 <= 10:
				gp2 = 4.0
			elif g2 >=  9 and g2 <= 9.2:
				gp2 = 3.7
			elif g2 >=  8.7 and g2 <= 8.9:
				gp2 = 3.3
			elif g2 >=  8.3 and g2 <= 8.6:
				gp2 = 3.0
			elif g2 >=  8 and g2 <= 8.2:
				gp2 = 2.7
			elif g2 >=  7.7 and g2 <= 7.9:
				gp2 = 2.3
			elif g2 >=  7.3 and g2 <= 7.6:
				gp2 = 2.0
			elif g2 >=  7 and g2 <= 7.2:
				gp2 = 1.7
			elif g2 >=  6.7 and g2 <= 6.9:
				gp2 = 1.3
			elif g2 >=  6.3 and g2 <= 6.6:
				gp2 = 1.0
			elif g2 >=  6 and g2 <= 6.2:
				gp2 = .7
			elif g2 < 6:
				gp2 = 0
	
		elif y == 3:
			if g3 >= 9.3     and g3 <= 10:
				gp3 = 4.0
			elif g3 >=  9   and g3 <= 9.2:
				gp3 = 3.7
			elif g3 >=  8.7 and g3 <= 8.9:
				gp3 = 3.3
			elif g3 >=  8.3 and g3 <= 8.6:
				gp3 = 3.0
			elif g3 >=  8   and g3 <= 8.2:
				gp3 = 2.7
			elif g3 >=  7.7 and g3 <= 7.9:
				gp3 = 2.3
			elif g3 >=  7.3 and g3 <= 7.6:
				gp3 = 2.0
			elif g3 >=  7   and g3 <= 7.2:
				gp3 = 1.7
			elif g3 >=  6.7 and g3 <= 6.9:
				gp3 = 1.3
			elif g3 >=  6.3 and g3 <= 6.6:
				gp3 = 1.0
			elif g3 >=  6   and g3 <= 6.2:
				gp3 = .7
			elif g3 < 6:
				gp3 = 0
	
		elif y == 4:
			if g4 >= 9.3     and g4 <= 10:
				gp4 = 4.0
			elif g4 >=  9   and g4 <= 9.2:
				gp4 = 3.7
			elif g4 >=  8.7 and g4 <= 8.9:
				gp4 = 3.3
			elif g4 >=  8.3 and g4 <= 8.6:
				gp4 = 3.0
			elif g4 >=  8   and g4 <= 8.2:
				gp4 = 2.7
			elif g4 >=  7.7 and g4 <= 7.9:
				gp4 = 2.3
			elif g4 >=  7.3 and g4 <= 7.6:
				gp4 = 2.0
			elif g4 >=  7   and g4 <= 7.2:
				gp4 = 1.7
			elif g4 >=  6.7 and g4 <= 6.9:
				gp4 = 1.3
			elif g4 >=  6.3 and g4 <= 6.6:
				gp4 = 1.0
			elif g4 >=  6   and g4 <= 6.2:
				gp4 = .7
			elif g4 < 6:
				gp4 = 0
	
		elif y == 5:
			if   g5 >= 9.3  and g5 <= 10:
				gp5 = 4.0
			elif g5 >=  9   and g5 <= 9.2:
				gp5 = 3.7
			elif g5 >=  8.7 and g5 <= 8.9:
				gp5 = 3.3
			elif g5 >=  8.3 and g5 <= 8.6:
				gp5 = 3.0
			elif g5 >=  8   and g5 <= 8.2:
				gp5 = 2.7
			elif g5 >=  7.7 and g5 <= 7.9:
				gp5 = 2.3
			elif g5 >=  7.3 and g5 <= 7.6:
				gp5 = 2.0
			elif g5 >=  7   and g5 <= 7.2:
				gp5 = 1.7
			elif g5 >=  6.7 and g5 <= 6.9:
				gp5 = 1.3
			elif g5 >=  6.3 and g5 <= 6.6:
				gp5 = 1.0
			elif g5 >=  6   and g5 <= 6.2:
				gp5 = .7
			elif g5 < 6:
				gp5 = 0
	
		elif y == 6:
			if g6 >= 9.3  and g6 <= 10:
				gp6 = 4.0
			elif g6 >=  9   and g6 <= 9.2:
				gp6 = 3.7
			elif g6 >=  8.7 and g6 <= 8.9:
				gp6 = 3.3
			elif g6 >=  8.3 and g6 <= 8.6:
				gp6 = 3.0
			elif g6 >=  8   and g6 <= 8.2:
				gp6 = 2.7
			elif g6 >=  7.7 and g6 <= 7.9:
				gp6 = 2.3
			elif g6 >=  7.3 and g6 <= 7.6:
				gp6 = 2.0
			elif g6 >=  7   and g6 <= 7.2:
				gp6 = 1.7
			elif g6 >=  6.7 and g6 <= 6.9:
				gp6 = 1.3
			elif g6 >=  6.3 and g6 <= 6.6:
				gp6 = 1.0
			elif g6 >=  6   and g6 <= 6.2:
				gp6 = .7
			elif g6 < 6:
				gp6 = 0
		
		elif y == 7:
			if g7 >= 9.3  and g7 <= 10:
				gp7 = 4.0
			elif g7 >=  9   and g7 <= 9.2:
				gp7 = 3.7
			elif g7 >=  8.7 and g7 <= 8.9:
				gp7 = 3.3
			elif g7 >=  8.3 and g7 <= 8.6:
				gp7 = 3.0
			elif g7 >=  8   and g7 <= 8.2:
				gp7 = 2.7
			elif g7 >=  7.7 and g7 <= 7.9:
				gp7 = 2.3
			elif g7 >=  7.3 and g7 <= 7.6:
				gp7 = 2.0
			elif g7 >=  7   and g7 <= 7.2:
				gp7 = 1.7
			elif g7 >=  6.7 and g7 <= 6.9:
				gp7 = 1.3
			elif g7 >=  6.3 and g7 <= 6.6:
				gp7 = 1.0
			elif g7 >=  6   and g7 <= 6.2:
				gp7 = .7
			elif g7 < 6:
				gp7 = 0
			
		elif y == 8:
			if g8 >= 9.3  and g8 <= 10:
				gp8 = 4.0
			elif g8 >=  9   and g8 <= 9.2:
				gp8 = 3.7
			elif g8 >=  8.7 and g8 <= 8.9:
				gp8 = 3.3
			elif g8 >=  8.3 and g8 <= 8.6:
				gp8 = 3.0
			elif g8 >=  8   and g8 <= 8.2:
				gp8 = 2.7
			elif g8 >=  7.7 and g8 <= 7.9:
				gp8 = 2.3
			elif g8 >=  7.3 and g8 <= 7.6:
				gp8 = 2.0
			elif g8 >=  7   and g8 <= 7.2:
				gp8 = 1.7
			elif g8 >=  6.7 and g8 <= 6.9:
				gp8 = 1.3
			elif g8 >=  6.3 and g8 <= 6.6:
				gp8 = 1.0
			elif g8 >=  6   and g8 <= 6.2:
				gp8 = .7
			elif g8 < 6:
				gp8 = 0
	
		elif y == 9:
			if g9 >= 9.3  and g9 <= 10:
				gp9 = 4.0
			elif g9 >=  9   and g9 <= 9.2:
				gp9 = 3.7
			elif g9 >=  8.7 and g9 <= 8.9:
				gp9 = 3.3
			elif g9 >=  8.3 and g9 <= 8.6:
				gp9 = 3.0
			elif g9 >=  8   and g9 <= 8.2:
				gp9 = 2.7
			elif g9 >=  7.7 and g9 <= 7.9:
				gp9 = 2.3
			elif g9 >=  7.3 and g9 <= 7.6:
				gp9 = 2.0
			elif g9 >=  7   and g9 <= 7.2:
				gp9 = 1.7
			elif g9 >=  6.7 and g9 <= 6.9:
				gp9 = 1.3
			elif g9 >=  6.3 and g9 <= 6.6:
				gp9 = 1.0
			elif g9 >=  6   and g9 <= 6.2:
				gp9 = .7
			elif g9 < 6:
				gp9 = 0
	
		elif y == 10:
			if g10 >= 9.3  and g10 <= 10:
				gp10 = 4.0
			elif g10 >=  9   and g10 <= 9.2:
				gp10 = 3.7
			elif g10 >=  8.7 and g10 <= 8.9:
				gp10 = 3.3
			elif g10 >=  8.3 and g10 <= 8.6:
				gp10 = 3.0
			elif g10 >=  8   and g10 <= 8.2:
				gp10 = 2.7
			elif g10 >=  7.7 and g10 <= 7.9:
				gp10 = 2.3
			elif g10 >=  7.3 and g10 <= 7.6:
				gp10 = 2.0
			elif g10 >=  7   and g10 <= 7.2:
				gp510 = 1.7
			elif g10 >=  6.7 and g10 <= 6.9:
				gp10 = 1.3
			elif g10 >=  6.3 and g10 <= 6.6:
				gp10 = 1.0
			elif g10 >=  6   and g10 <= 6.2:
				gp10 = .7
			elif g10 < 6:
				gp10 = 0
	
		elif y == 11:
			if g11 >= 9.3  and g11 <= 10:
				gp11 = 4.0
			elif g11 >=  9   and g11 <= 9.2:
				gp11 = 3.7
			elif g11 >=  8.7 and g11 <= 8.9:
				gp11 = 3.3
			elif g11 >=  8.3 and g11 <= 8.6:
				gp11 = 3.0
			elif g11 >=  8   and g11 <= 8.2:
				gp11 = 2.7
			elif g11 >=  7.7 and g11 <= 7.9:
				gp11 = 2.3
			elif g11 >=  7.3 and g11 <= 7.6:
				gp11 = 2.0
			elif g11 >=  7   and g11 <= 7.2:
				gp11 = 1.7
			elif g11 >=  6.7 and g11 <= 6.9:
				gp11 = 1.3
			elif g11 >=  6.3 and g11 <= 6.6:
				gp11 = 1.0
			elif g11 >=  6   and g11 <= 6.2:
				gp11 = .7
			elif g11 < 6:
				gp11 = 0
	
		elif y == 12:
			if   g12 >= 9.3  and g12 <= 10:
				gp12 = 4.0
			elif g12 >=  9   and g12 <= 9.2:
				gp12 = 3.7
			elif g12 >=  8.7 and g12 <= 8.9:
				gp12 = 3.3
			elif g12 >=  8.3 and g12 <= 8.6:
				gp12 = 3.0
			elif g12 >=  8   and g12 <= 8.2:
				gp12 = 2.7
			elif g12 >=  7.7 and g12 <= 7.9:
				gp12 = 2.3
			elif g12 >=  7.3 and g12 <= 7.6:
				gp12 = 2.0
			elif g12 >=  7   and g12 <= 7.2:
				gp12 = 1.7
			elif g12 >=  6.7 and g12 <= 6.9:
				gp12 = 1.3
			elif g12 >=  6.3 and g12 <= 6.6:
				gp12 = 1.0
			elif g12 >=  6   and g12 <= 6.2:
				gp12 = .7
			elif g12 < 6:
				gp12 = 0
	
		elif y == 13:
			if   g13 >= 9.3  and g13 <= 10:
				gp5 = 4.0
			elif g5 >=  9   and g13 <= 9.2:
				gp5 = 3.7
			elif g5 >=  8.7 and g13 <= 8.9:
				gp5 = 3.3
			elif g5 >=  8.3 and g13 <= 8.6:
				gp5 = 3.0
			elif g5 >=  8   and g13 <= 8.2:
				gp5 = 2.7
			elif g5 >=  7.7 and g13 <= 7.9:
				gp5 = 2.3
			elif g5 >=  7.3 and g13 <= 7.6:
				gp5 = 2.0
			elif g5 >=  7   and g13 <= 7.2:
				gp5 = 1.7
			elif g5 >=  6.7 and g13 <= 6.9:
				gp5 = 1.3
			elif g5 >=  6.3 and g13 <= 6.6:
				gp5 = 1.0
			elif g5 >=  6   and g13 <= 6.2:
				gp5 = .7
			elif g5 < 6:
				gp5 = 0
	
		elif y == 14:
			if   g5 >= 9.3  and g5 <= 10:
				gp5 = 4.0
			elif g5 >=  9   and g5 <= 9.2:
				gp5 = 3.7
			elif g5 >=  8.7 and g5 <= 8.9:
				gp5 = 3.3
			elif g5 >=  8.3 and g5 <= 8.6:
				gp5 = 3.0
			elif g5 >=  8   and g5 <= 8.2:
				gp5 = 2.7
			elif g5 >=  7.7 and g5 <= 7.9:
				gp5 = 2.3
			elif g5 >=  7.3 and g5 <= 7.6:
				gp5 = 2.0
			elif g5 >=  7   and g5 <= 7.2:
				gp5 = 1.7
			elif g5 >=  6.7 and g5 <= 6.9:
				gp5 = 1.3
			elif g5 >=  6.3 and g5 <= 6.6:
				gp5 = 1.0
			elif g5 >=  6   and g5 <= 6.2:
				gp5 = .7
			elif g5 < 6:
				gp5 = 0
	
		elif y == 15:
			if   g5 >= 9.3  and g5 <= 10:
				gp5 = 4.0
			elif g5 >=  9   and g5 <= 9.2:
				gp5 = 3.7
			elif g5 >=  8.7 and g5 <= 8.9:
				gp5 = 3.3
			elif g5 >=  8.3 and g5 <= 8.6:
				gp5 = 3.0
			elif g5 >=  8   and g5 <= 8.2:
				gp5 = 2.7
			elif g5 >=  7.7 and g5 <= 7.9:
				gp5 = 2.3
			elif g5 >=  7.3 and g5 <= 7.6:
				gp5 = 2.0
			elif g5 >=  7   and g5 <= 7.2:
				gp5 = 1.7
			elif g5 >=  6.7 and g5 <= 6.9:
				gp5 = 1.3
			elif g5 >=  6.3 and g5 <= 6.6:
				gp5 = 1.0
			elif g5 >=  6   and g5 <= 6.2:
				gp5 = .7
			elif g5 < 6:
				gp5 = 0
	
		elif y == 16:
			if   g5 >= 9.3  and g5 <= 10:
				gp5 = 4.0
			elif g5 >=  9   and g5 <= 9.2:
				gp5 = 3.7
			elif g5 >=  8.7 and g5 <= 8.9:
				gp5 = 3.3
			elif g5 >=  8.3 and g5 <= 8.6:
				gp5 = 3.0
			elif g5 >=  8   and g5 <= 8.2:
				gp5 = 2.7
			elif g5 >=  7.7 and g5 <= 7.9:
				gp5 = 2.3
			elif g5 >=  7.3 and g5 <= 7.6:
				gp5 = 2.0
			elif g5 >=  7   and g5 <= 7.2:
				gp5 = 1.7
			elif g5 >=  6.7 and g5 <= 6.9:
				gp5 = 1.3
			elif g5 >=  6.3 and g5 <= 6.6:
				gp5 = 1.0
			elif g5 >=  6   and g5 <= 6.2:
				gp5 = .7
			elif g5 < 6:
				gp5 = 0
	
		elif y == 17:
			if   g5 >= 9.3  and g5 <= 10:
				gp5 = 4.0
			elif g5 >=  9   and g5 <= 9.2:
				gp5 = 3.7
			elif g5 >=  8.7 and g5 <= 8.9:
				gp5 = 3.3
			elif g5 >=  8.3 and g5 <= 8.6:
				gp5 = 3.0
			elif g5 >=  8   and g5 <= 8.2:
				gp5 = 2.7
			elif g5 >=  7.7 and g5 <= 7.9:
				gp5 = 2.3
			elif g5 >=  7.3 and g5 <= 7.6:
				gp5 = 2.0
			elif g5 >=  7   and g5 <= 7.2:
				gp5 = 1.7
			elif g5 >=  6.7 and g5 <= 6.9:
				gp5 = 1.3
			elif g5 >=  6.3 and g5 <= 6.6:
				gp5 = 1.0
			elif g5 >=  6   and g5 <= 6.2:
				gp5 = .7
			elif g5 < 6:
				gp5 = 0
	
		elif y == 18:
			if   g5 >= 9.3  and g5 <= 10:
				gp5 = 4.0
			elif g5 >=  9   and g5 <= 9.2:
				gp5 = 3.7
			elif g5 >=  8.7 and g5 <= 8.9:
				gp5 = 3.3
			elif g5 >=  8.3 and g5 <= 8.6:
				gp5 = 3.0
			elif g5 >=  8   and g5 <= 8.2:
				gp5 = 2.7
			elif g5 >=  7.7 and g5 <= 7.9:
				gp5 = 2.3
			elif g5 >=  7.3 and g5 <= 7.6:
				gp5 = 2.0
			elif g5 >=  7   and g5 <= 7.2:
				gp5 = 1.7
			elif g5 >=  6.7 and g5 <= 6.9:
				gp5 = 1.3
			elif g5 >=  6.3 and g5 <= 6.6:
				gp5 = 1.0
			elif g5 >=  6   and g5 <= 6.2:
				gp5 = .7
			elif g5 < 6:
				gp5 = 0
	
			
	y = y + 1
	x = x - 1
	
x = cla2
y = 1
while x > 0:
	if cyf2 == 2:
		if y == 1:
			if g1y2 >= 9.3 and g1y2 <= 10:
				gp1y2 = 4.0
			elif g1y2 >=  9 and g1y2 <= 9.2:
				gp1y2 = 3.7
			elif g1y2 >=  8.7 and g1y2 <= 8.9:
				gp1y2 = 3.3
			elif g1y2 >=  8.3 and g1y2 <= 8.6:
				gp1y2 = 3.0
			elif g1y2 >=  8 and g1y2 <= 8.2:
				gp1y2 = 2.7
			elif g1y2 >=  7.7 and g1y2 <= 7.9:
				gp1y2 = 2.3
			elif g1y2 >=  7.3 and g1y2 <= 7.6:
				gp1y2 = 2.0
			elif g1y2 >=  7 and g1y2 <= 7.2:
				gp1y2 = 1.7
			elif g1y2 >=  6.7 and g1y2 <= 6.9:
				gp1y2 = 1.3
			elif g1y2 >=  6.3 and g1y2 <= 6.6:
				gp1y2 = 1.0
			elif g1y2 >=  6 and g1y2 <= 6.2:
				gp1y2 = .7
			elif g1y2 < 6:
				gp1y2 = 0
				
		elif y == 2:
			if g2y2 >= 9.3 and g2y2 <= 10:
				gp2y2 = 4.0
			elif g2y2 >=  9 and g2y2 <= 9.2:
				gp2y2 = 3.7
			elif g2y2 >=  8.7 and g2y2 <= 8.9:
				gp2y2 = 3.3
			elif g2y2 >=  8.3 and g2y2 <= 8.6:
				gp2y2 = 3.0
			elif g2y2 >=  8 and g2y2 <= 8.2:
				gp2y2 = 2.7
			elif g2y2 >=  7.7 and g2y2 <= 7.9:
				gp2y2 = 2.3
			elif g2y2 >=  7.3 and g2y2 <= 7.6:
				gp2y2 = 2.0
			elif g2y2 >=  7 and g2y2 <= 7.2:
				gp2y2 = 1.7
			elif g2y2 >=  6.7 and g2y2 <= 6.9:
				gp2y2 = 1.3
			elif g2y2 >=  6.3 and g2y2 <= 6.6:
				gp2y2 = 1.0
			elif g2y2 >=  6 and g2y2 <= 6.2:
				gp2y2 = .7
			elif g2y2 < 6:
				gp2y2 = 0
				
		elif y == 3:
			if g3y2 >= 9.3     and g3y2 <= 10:
				gp3y2 = 4.0
			elif g3y2 >=  9   and g3y2 <= 9.2:
				gp3y2 = 3.7
			elif g3y2 >=  8.7 and g3y2 <= 8.9:
				gp3y2 = 3.3
			elif g3y2 >=  8.3 and g3y2 <= 8.6:
				gp3y2 = 3.0
			elif g3y2 >=  8   and g3y2 <= 8.2:
				gp3y2 = 2.7
			elif g3y2 >=  7.7 and g3y2 <= 7.9:
				gp3y2 = 2.3
			elif g3y2 >=  7.3 and g3y2 <= 7.6:
				gp3y2 = 2.0
			elif g3y2 >=  7   and g3y2 <= 7.2:
				gp3y2 = 1.7
			elif g3y2 >=  6.7 and g3y2 <= 6.9:
				gp3y2 = 1.3
			elif g3y2 >=  6.3 and g2y2 <= 6.6:
				gp3y2 = 1.0
			elif g3y2 >=  6   and g2y2 <= 6.2:
				gp3y2 = .7
			elif g3y2 < 6:
				gp3y2 = 0
				
		elif y == 4:
			if g4y2 >= 9.3     and g4y2 <= 10:
				gp4y2 = 4.0
			elif g4y2 >=  9   and g4y2 <= 9.2:
				gp4y2 = 3.7
			elif g4y2 >=  8.7 and g4y2 <= 8.9:
				gp4y2 = 3.3
			elif g4y2 >=  8.3 and g4y2 <= 8.6:
				gp4y2 = 3.0
			elif g4y2 >=  8   and g4y2 <= 8.2:
				gp4y2 = 2.7
			elif g4y2 >=  7.7 and g4y2 <= 7.9:
				gp4y2 = 2.3
			elif g4y2 >=  7.3 and g4y2 <= 7.6:
				gp4y2 = 2.0
			elif g4y2 >=  7   and g4y2 <= 7.2:
				gp4y2 = 1.7
			elif g4y2 >=  6.7 and g4y2 <= 6.9:
				gp4y2 = 1.3
			elif g4y2 >=  6.3 and g4y2 <= 6.6:
				gp4y2 = 1.0
			elif g4y2 >=  6   and g4y2 <= 6.2:
				gp4y2 = .7
			elif g4y2 < 6:
				gp4y2 = 0
				
		elif y == 5:
			if   g5y2 >= 9.3  and g5y2 <= 10:
				gp5y2 = 4.0
			elif g5y2 >=  9   and g5y2 <= 9.2:
				gp5y2 = 3.7
			elif g5y2 >=  8.7 and g5y2 <= 8.9:
				gp5y2 = 3.3
			elif g5y2 >=  8.3 and g5y2 <= 8.6:
				gp5y2 = 3.0
			elif g5y2 >=  8   and g5y2 <= 8.2:
				gp5y2 = 2.7
			elif g5y2 >=  7.7 and g5y2 <= 7.9:
				gp5y2 = 2.3
			elif g5y2 >=  7.3 and g5y2 <= 7.6:
				gp5y2 = 2.0
			elif g5y2 >=  7   and g5y2 <= 7.2:
				gp5y2 = 1.7
			elif g5y2 >=  6.7 and g5y2 <= 6.9:
				gp5y2 = 1.3
			elif g5y2 >=  6.3 and g5y2 <= 6.6:
				gp5y2 = 1.0
			elif g5y2 >=  6   and g5y2 <= 6.2:
				gp5y2 = .7
			elif g5y2 < 6:
				gp5y2 = 0
	
		elif y == 6:
			if g6y2 >= 9.3  and g6y2 <= 10:
				gp6y2 = 4.0
			elif g6y2 >=  9   and g6y2 <= 9.2:
				gp6y2 = 3.7
			elif g6y2 >=  8.7 and g6y2 <= 8.9:
				gp6y2 = 3.3
			elif g6y2 >=  8.3 and g6y2 <= 8.6:
				gp6y2 = 3.0
			elif g6y2 >=  8   and g6y2 <= 8.2:
				gp6y2 = 2.7
			elif g6y2 >=  7.7 and g6y2 <= 7.9:
				gp6y2 = 2.3
			elif g6y2 >=  7.3 and g6y2 <= 7.6:
				gp6y2 = 2.0
			elif g6y2 >=  7   and g6y2 <= 7.2:
				gp6y2 = 1.7
			elif g6y2 >=  6.7 and g6y2 <= 6.9:
				gp6y2 = 1.3
			elif g6y2 >=  6.3 and g6y2 <= 6.6:
				gp6y2 = 1.0
			elif g6y2 >=  6   and g6y2 <= 6.2:
				gp6y2 = .7
			elif g6y2 < 6:
				gp6y2 = 0
				
		elif y == 7:
			if g7y2 >= 9.3  and g7y2 <= 10:
				gp7y2 = 4.0
			elif g7y2 >=  9   and g7y2 <= 9.2:
				gp7y2 = 3.7
			elif g7y2 >=  8.7 and g7y2 <= 8.9:
				gp7y2 = 3.3
			elif g7y2 >=  8.3 and g7y2 <= 8.6:
				gp7y2 = 3.0
			elif g7y2 >=  8   and g7y2 <= 8.2:
				gp7y2 = 2.7
			elif g7y2 >=  7.7 and g7y2 <= 7.9:
				gp7y2 = 2.3
			elif g7y2 >=  7.3 and g7y2 <= 7.6:
				gp7y2 = 2.0
			elif g7y2 >=  7   and g7y2 <= 7.2:
				gp7y2 = 1.7
			elif g7y2 >=  6.7 and g7y2 <= 6.9:
				gp7y2 = 1.3
			elif g7y2 >=  6.3 and g7y2 <= 6.6:
				gp7y2 = 1.0
			elif g7y2 >=  6   and g7y2 <= 6.2:
				gp7y2 = .7
			elif g7y2 < 6:
				gp7y2 = 0
				
		elif y == 8:		
			if g8y2 >= 9.3  and g8y2 <= 10:
				gp8y2 = 4.0
			elif g8y2 >=  9   and g8y2 <= 9.2:
				gp8y2 = 3.7
			elif g8y2 >=  8.7 and g8y2 <= 8.9:
				gp8y2 = 3.3
			elif g8y2 >=  8.3 and g8y2 <= 8.6:
				gp8y2 = 3.0
			elif g8y2 >=  8   and g8y2 <= 8.2:
				gp8y2 = 2.7
			elif g8y2 >=  7.7 and g8y2 <= 7.9:
				gp8y2 = 2.3
			elif g8y2 >=  7.3 and g8y2 <= 7.6:
				gp8y2 = 2.0
			elif g8y2 >=  7   and g8y2 <= 7.2:
				gp8y2 = 1.7
			elif g8y2 >=  6.7 and g8y2 <= 6.9:
				gp8y2 = 1.3
			elif g8y2 >=  6.3 and g8y2 <= 6.6:
				gp8y2 = 1.0
			elif g8y2 >=  6   and g8y2 <= 6.2:
				gp8y2 = .7
			elif g8y2 < 6:
				gp8y2 = 0
		
		elif y == 9:
			if g9y2 >= 9.3  and g9y2 <= 10:
				gp9y2 = 4.0
			elif g9y2 >=  9   and g9y2 <= 9.2:
				gp9y2 = 3.7
			elif g9y2 >=  8.7 and g9y2 <= 8.9:
				gp9y2 = 3.3
			elif g9y2 >=  8.3 and g9y2 <= 8.6:
				gp9y2 = 3.0
			elif g9y2 >=  8   and g9y2 <= 8.2:
				gp9y2 = 2.7
			elif g9y2 >=  7.7 and g9y2 <= 7.9:
				gp9y2 = 2.3
			elif g9y2 >=  7.3 and g9y2 <= 7.6:
				gp9y2 = 2.0
			elif g9y2 >=  7   and g9y2 <= 7.2:
				gp9y2 = 1.7
			elif g9y2 >=  6.7 and g9y2 <= 6.9:
				gp9y2 = 1.3
			elif g9y2 >=  6.3 and g9y2 <= 6.6:
				gp9y2 = 1.0
			elif g9y2 >=  6   and g9y2 <= 6.2:
				gp9y2 = .7
			elif g9y2 < 6:
				gp9y2 = 0
				
		elif y == 10:
			if g10y2 >= 9.3  and g10y2 <= 10:
				gp10y2 = 4.0
			elif g10y2 >=  9   and g10y2 <= 9.2:
				gp10y2 = 3.7
			elif g10y2 >=  8.7 and g10y2 <= 8.9:
				gp10y2 = 3.3
			elif g10y2 >=  8.3 and g10y2 <= 8.6:
				gp10y2 = 3.0
			elif g10y2 >=  8   and g10y2 <= 8.2:
				gp10y2 = 2.7
			elif g10y2 >=  7.7 and g10y2 <= 7.9:
				gp10y2 = 2.3
			elif g10y2 >=  7.3 and g10y2 <= 7.6:
				gp10y2 = 2.0
			elif g10y2 >=  7   and g10y2 <= 7.2:
				gp10y2 = 1.7
			elif g10y2 >=  6.7 and g10y2 <= 6.9:
				gp10y2 = 1.3
			elif g10y2 >=  6.3 and g10y2 <= 6.6:
				gp10y2 = 1.0
			elif g10y2 >=  6   and g10y2 <= 6.2:
				gp10y2 = .7
			elif g10y2 < 6:
				gp10y2 = 0
				
		elif y == 11:
			if g11y2 >= 9.3  and g11y2 <= 10:
				gp11y2 = 4.0
			elif g11y2 >=  9   and g11y2 <= 9.2:
				gp11y2 = 3.7
			elif g11y2 >=  8.7 and g11y2 <= 8.9:
				gp11y2 = 3.3
			elif g11y2 >=  8.3 and g11y2 <= 8.6:
				gp11y2 = 3.0
			elif g11y2 >=  8   and g11y2 <= 8.2:
				gp11y2 = 2.7
			elif g11y2 >=  7.7 and g11y2 <= 7.9:
				gp11y2 = 2.3
			elif g11y2 >=  7.3 and g11y2 <= 7.6:
				gp11y2 = 2.0
			elif g11y2 >=  7   and g11y2 <= 7.2:
				gp11y2 = 1.7
			elif g11y2 >=  6.7 and g11y2 <= 6.9:
				gp11y2 = 1.3
			elif g11y2 >=  6.3 and g11y2 <= 6.6:
				gp11y2 = 1.0
			elif g11y2 >=  6   and g11y2 <= 6.2:
				gp11y2 = .7
			elif g11y2 < 6:
				gp11y2 = 0
				
		elif y == 12:
			if   g12y2 >= 9.3  and g12y2 <= 10:
				gp12y2 = 4.0
			elif g12y2 >=  9   and g12y2 <= 9.2:
				gp12y2 = 3.7
			elif g12y2 >=  8.7 and g12y2 <= 8.9:
				gp12y2 = 3.3
			elif g12y2 >=  8.3 and g12y2 <= 8.6:
				gp12y2 = 3.0
			elif g12y2 >=  8   and g12y2 <= 8.2:
				gp12y2 = 2.7
			elif g12y2 >=  7.7 and g12y2 <= 7.9:
				gp12y2 = 2.3
			elif g12y2 >=  7.3 and g12y2 <= 7.6:
				gp12y2 = 2.0
			elif g12y2 >=  7   and g12y2 <= 7.2:
				gp12y2 = 1.7
			elif g12y2 >=  6.7 and g12y2 <= 6.9:
				gp12y2 = 1.3
			elif g12y2 >=  6.3 and g12y2 <= 6.6:
				gp12y2 = 1.0
			elif g12y2 >=  6   and g12y2 <= 6.2:
				gp12y2 = .7
			elif g12y2 < 6:
				gp12y2 = 0
				
		elif y == 13:
			if   g5y2 >= 9.3  and g13y2 <= 10:
				gp5y2 = 4.0
			elif g5y2 >=  9   and g13y2 <= 9.2:
				gp5y2 = 3.7
			elif g5y2 >=  8.7 and g13y2 <= 8.9:
				gp5y2 = 3.3
			elif g5y2 >=  8.3 and g13y2 <= 8.6:
				gp5y2 = 3.0
			elif g5y2 >=  8   and g13y2 <= 8.2:
				gp5y2 = 2.7
			elif g5y2 >=  7.7 and g13y2 <= 7.9:
				gp5y2 = 2.3
			elif g5y2 >=  7.3 and g13y2 <= 7.6:
				gp5y2 = 2.0
			elif g5y2 >=  7   and g13y2 <= 7.2:
				gp5y2 = 1.7
			elif g5y2 >=  6.7 and g13y2 <= 6.9:
				gp5y2 = 1.3
			elif g5y2 >=  6.3 and g13y2 <= 6.6:
				gp5y2 = 1.0
			elif g5y2 >=  6   and g13y2 <= 6.2:
				gp5y2 = .7
			elif g5y2 < 6:
				gp5y2 = 0
		
		elif y == 14:
			if   g5y2 >= 9.3  and g13y2 <= 10:
				gp5y2 = 4.0
			elif g5y2 >=  9   and g13y2 <= 9.2:
				gp5y2 = 3.7
			elif g5y2 >=  8.7 and g13y2 <= 8.9:
				gp5y2 = 3.3
			elif g5y2 >=  8.3 and g13y2 <= 8.6:
				gp5y2 = 3.0
			elif g5y2 >=  8   and g13y2 <= 8.2:
				gp5y2 = 2.7
			elif g5y2 >=  7.7 and g13y2 <= 7.9:
				gp5y2 = 2.3
			elif g5y2 >=  7.3 and g13y2 <= 7.6:
				gp5y2 = 2.0
			elif g5y2 >=  7   and g13y2 <= 7.2:
				gp5y2 = 1.7
			elif g5y2 >=  6.7 and g13y2 <= 6.9:
				gp5y2 = 1.3
			elif g5y2 >=  6.3 and g13y2 <= 6.6:
				gp5y2 = 1.0
			elif g5y2 >=  6   and g13y2 <= 6.2:
				gp5y2 = .7
			elif g5y2 < 6:
				gp5y2 = 0
		
		elif y == 15:
			if   g5y2 >= 9.3  and g13y2 <= 10:
				gp5y2 = 4.0
			elif g5y2 >=  9   and g13y2 <= 9.2:
				gp5y2 = 3.7
			elif g5y2 >=  8.7 and g13y2 <= 8.9:
				gp5y2 = 3.3
			elif g5y2 >=  8.3 and g13y2 <= 8.6:
				gp5y2 = 3.0
			elif g5y2 >=  8   and g13y2 <= 8.2:
				gp5y2 = 2.7
			elif g5y2 >=  7.7 and g13y2 <= 7.9:
				gp5y2 = 2.3
			elif g5y2 >=  7.3 and g13y2 <= 7.6:
				gp5y2 = 2.0
			elif g5y2 >=  7   and g13y2 <= 7.2:
				gp5y2 = 1.7
			elif g5y2 >=  6.7 and g13y2 <= 6.9:
				gp5y2 = 1.3
			elif g5y2 >=  6.3 and g13y2 <= 6.6:
				gp5y2 = 1.0
			elif g5y2 >=  6   and g13y2 <= 6.2:
				gp5y2 = .7
			elif g5y2 < 6:
				gp5y2 = 0
		
		elif y == 16:
			if   g5y2 >= 9.3  and g13y2 <= 10:
				gp5y2 = 4.0
			elif g5y2 >=  9   and g13y2 <= 9.2:
				gp5y2 = 3.7
			elif g5y2 >=  8.7 and g13y2 <= 8.9:
				gp5y2 = 3.3
			elif g5y2 >=  8.3 and g13y2 <= 8.6:
				gp5y2 = 3.0
			elif g5y2 >=  8   and g13y2 <= 8.2:
				gp5y2 = 2.7
			elif g5y2 >=  7.7 and g13y2 <= 7.9:
				gp5y2 = 2.3
			elif g5y2 >=  7.3 and g13y2 <= 7.6:
				gp5y2 = 2.0
			elif g5y2 >=  7   and g13y2 <= 7.2:
				gp5y2 = 1.7
			elif g5y2 >=  6.7 and g13y2 <= 6.9:
				gp5y2 = 1.3
			elif g5y2 >=  6.3 and g13y2 <= 6.6:
				gp5y2 = 1.0
			elif g5y2 >=  6   and g13y2 <= 6.2:
				gp5y2 = .7
			elif g5y2 < 6:
				gp5y2 = 0
		
		elif y == 17:
			if   g5y2 >= 9.3  and g13y2 <= 10:
				gp5y2 = 4.0
			elif g5y2 >=  9   and g13y2 <= 9.2:
				gp5y2 = 3.7
			elif g5y2 >=  8.7 and g13y2 <= 8.9:
				gp5y2 = 3.3
			elif g5y2 >=  8.3 and g13y2 <= 8.6:
				gp5y2 = 3.0
			elif g5y2 >=  8   and g13y2 <= 8.2:
				gp5y2 = 2.7
			elif g5y2 >=  7.7 and g13y2 <= 7.9:
				gp5y2 = 2.3
			elif g5y2 >=  7.3 and g13y2 <= 7.6:
				gp5y2 = 2.0
			elif g5y2 >=  7   and g13y2 <= 7.2:
				gp5y2 = 1.7
			elif g5y2 >=  6.7 and g13y2 <= 6.9:
				gp5y2 = 1.3
			elif g5y2 >=  6.3 and g13y2 <= 6.6:
				gp5y2 = 1.0
			elif g5y2 >=  6   and g13y2 <= 6.2:
				gp5y2 = .7
			elif g5y2 < 6:
				gp5y2 = 0
		
		elif y == 18:
			if   g5y2 >= 9.3  and g13y2 <= 10:
				gp5y2 = 4.0
			elif g5y2 >=  9   and g13y2 <= 9.2:
				gp5y2 = 3.7
			elif g5y2 >=  8.7 and g13y2 <= 8.9:
				gp5y2 = 3.3
			elif g5y2 >=  8.3 and g13y2 <= 8.6:
				gp5y2 = 3.0
			elif g5y2 >=  8   and g13y2 <= 8.2:
				gp5y2 = 2.7
			elif g5y2 >=  7.7 and g13y2 <= 7.9:
				gp5y2 = 2.3
			elif g5y2 >=  7.3 and g13y2 <= 7.6:
				gp5y2 = 2.0
			elif g5y2 >=  7   and g13y2 <= 7.2:
				gp5y2 = 1.7
			elif g5y2 >=  6.7 and g13y2 <= 6.9:
				gp5y2 = 1.3
			elif g5y2 >=  6.3 and g13y2 <= 6.6:
				gp5y2 = 1.0
			elif g5y2 >=  6   and g13y2 <= 6.2:
				gp5y2 = .7
			elif g5y2 < 6:
				gp5y2 = 0
				
	y = y + 1
	x = x - 1

x = cla3
y = 1				
while x > 0:
	if cyf3 == 3:
		if y == 1:
			if g1y3 >= 9.3 and g1y3 <= 10:
				gp1y3 = 4.0
			elif g1y3 >=  9 and g1y3 <= 9.2:
				gp1y3 = 3.7
			elif g1y3 >=  8.7 and g1y3 <= 8.9:
				gp1y3 = 3.3
			elif g1y3 >=  8.3 and g1y3 <= 8.6:
				gp1y3 = 3.0
			elif g1y3 >=  8 and g1y3 <= 8.2:
				gp1y3 = 2.7
			elif g1y3 >=  7.7 and g1y3 <= 7.9:
				gp1y3 = 2.3
			elif g1y3 >=  7.3 and g1y3 <= 7.6:
				gp1y3 = 2.0
			elif g1y3 >=  7 and g1y3 <= 7.2:
				gp1y3 = 1.7
			elif g1y3 >=  6.7 and g1y3 <= 6.9:
				gp1y3 = 1.3
			elif g1y3 >=  6.3 and g1y3 <= 6.6:
				gp1y3 = 1.0
			elif g1y3 >=  6 and g1y3 <= 6.2:
				gp1y3 = .7
			elif g1y3 < 6:
				gp1y3 = 0
			print gp1y3
		
		elif y == 2:
			if g2y3 >= 9.3 and g2y3 <= 10:
				gp2y3 = 4.0
			elif g2y3 >=  9 and g2y3 <= 9.2:
				gp2y3 = 3.7
			elif g2y3 >=  8.7 and g2y3 <= 8.9:
				gp2y3 = 3.3
			elif g2y3 >=  8.3 and g2y3 <= 8.6:
				gp2y3 = 3.0
			elif g2y3 >=  8 and g2y3 <= 8.2:
				gp2y3 = 2.7
			elif g2y3 >=  7.7 and g2y3 <= 7.9:
				gp2y3 = 2.3
			elif g2y3 >=  7.3 and g2y3 <= 7.6:
				gp2y3 = 2.0
			elif g2y3 >=  7 and g2y3 <= 7.2:
				gp2y3 = 1.7
			elif g2y3 >=  6.7 and g2y3 <= 6.9:
				gp2y3 = 1.3
			elif g2y3 >=  6.3 and g2y3 <= 6.6:
				gp2y3 = 1.0
			elif g2y3 >=  6 and g2y3 <= 6.2:
				gp2y3 = .7
			elif g2y3 < 6:
				gp2y3 = 0
		
		elif y == 3:
			if g3y3 >= 9.3     and g3y3 <= 10:
				gp3y3 = 4.0
			elif g3y3 >=  9   and g3y3 <= 9.2:
				gp3y3 = 3.7
			elif g3y3 >=  8.7 and g3y3 <= 8.9:
				gp3y3 = 3.3
			elif g3y3 >=  8.3 and g3y3 <= 8.6:
				gp3y3 = 3.0
			elif g3y3 >=  8   and g3y3 <= 8.2:
				gp3y3 = 2.7
			elif g3y3 >=  7.7 and g3y3 <= 7.9:
				gp3y3 = 2.3
			elif g3y3 >=  7.3 and g3y3 <= 7.6:
				gp3y3 = 2.0
			elif g3y3 >=  7   and g3y3 <= 7.2:
				gp3y3 = 1.7
			elif g3y3 >=  6.7 and g3y3 <= 6.9:
				gp3y3 = 1.3
			elif g3y3 >=  6.3 and g3y3 <= 6.6:
				gp3y3 = 1.0
			elif g3y3 >=  6   and g3y3 <= 6.2:
				gp3y3 = .7
			elif g3y3 < 6:
				gp3y3 = 0
				
		elif y == 4:
			if g4y3 >= 9.3     and g4y3 <= 10:
				gp4y3 = 4.0
			elif g4y3 >=  9   and g4y3 <= 9.2:
				gp4y3 = 3.7
			elif g4y3 >=  8.7 and g4y3 <= 8.9:
				gp4y3 = 3.3
			elif g4y3 >=  8.3 and g4y3 <= 8.6:
				gp4y3 = 3.0
			elif g4y3 >=  8   and g4y3 <= 8.2:
				gp4y3 = 2.7
			elif g4y3 >=  7.7 and g4y3 <= 7.9:
				gp4y3 = 2.3
			elif g4y3 >=  7.3 and g4y3 <= 7.6:
				gp4y3 = 2.0
			elif g4y3 >=  7   and g4y3 <= 7.2:
				gp4y3 = 1.7
			elif g4y3 >=  6.7 and g4y3 <= 6.9:
				gp4y3 = 1.3
			elif g4y3 >=  6.3 and g4y3 <= 6.6:
				gp4y3 = 1.0
			elif g4y3 >=  6   and g4y3 <= 6.2:
				gp4y3 = .7
			elif g4y3 < 6:
				gp4y3 = 0
				
		elif y == 5:
			if   g5y3 >= 9.3  and g5y3 <= 10:
				gp5y3 = 4.0
			elif g5y3 >=  9   and g5y3 <= 9.2:
				gp5y3 = 3.7
			elif g5y3 >=  8.7 and g5y3 <= 8.9:
				gp5y3 = 3.3
			elif g5y3 >=  8.3 and g5y3 <= 8.6:
				gp5y3 = 3.0
			elif g5y3 >=  8   and g5y3 <= 8.2:
				gp5y3 = 2.7
			elif g5y3 >=  7.7 and g5y3 <= 7.9:
				gp5y3 = 2.3
			elif g5y3 >=  7.3 and g5y3 <= 7.6:
				gp5y3 = 2.0
			elif g5y3 >=  7   and g5y3 <= 7.2:
				gp5y3 = 1.7
			elif g5y3 >=  6.7 and g5y3 <= 6.9:
				gp5y3 = 1.3
			elif g5y3 >=  6.3 and g5y3 <= 6.6:
				gp5y3 = 1.0
			elif g5y3 >=  6   and g5y3 <= 6.2:
				gp5y3 = .7
			elif g5y3 < 6:
				gp5y3 = 0
				
		elif y == 6:
			if g6y3 >= 9.3  and g6y3 <= 10:
				gp6y3 = 4.0
			elif g6y3 >=  9   and g6y3 <= 9.2:
				gp6y3 = 3.7
			elif g6y3 >=  8.7 and g6y3 <= 8.9:
				gp6y3 = 3.3
			elif g6y3 >=  8.3 and g6y3 <= 8.6:
				gp6y3 = 3.0
			elif g6y3 >=  8   and g6y3 <= 8.2:
				gp6y3 = 2.7
			elif g6y3 >=  7.7 and g6y3 <= 7.9:
				gp6y3 = 2.3
			elif g6y3 >=  7.3 and g6y3 <= 7.6:
				gp6y3 = 2.0
			elif g6y3 >=  7   and g6y3 <= 7.2:
				gp6y3 = 1.7
			elif g6y3 >=  6.7 and g6y3 <= 6.9:
				gp6y3 = 1.3
			elif g6y3 >=  6.3 and g6y3 <= 6.6:
				gp6y3 = 1.0
			elif g6y3 >=  6   and g6y3 <= 6.2:
				gp6y3 = .7
			elif g6y3 < 6:
				gp6y3 = 0
			
		elif y == 7:
			if g7y3 >= 9.3  and g7y3 <= 10:
				gp7y3 = 4.0
			elif g7y3 >=  9   and g7y3 <= 9.2:
				gp7y3 = 3.7
			elif g7y3 >=  8.7 and g7y3 <= 8.9:
				gp7y3 = 3.3
			elif g7y3 >=  8.3 and g7y3 <= 8.6:
				gp7y3 = 3.0
			elif g7y3 >=  8   and g7y3 <= 8.2:
				gp7y3 = 2.7
			elif g7y3 >=  7.7 and g7y3 <= 7.9:
				gp7y3 = 2.3
			elif g7y3 >=  7.3 and g7y3 <= 7.6:
				gp7y3 = 2.0
			elif g7y3 >=  7   and g7y3 <= 7.2:
				gp7y3 = 1.7
			elif g7y3 >=  6.7 and g7y3 <= 6.9:
				gp7y3 = 1.3
			elif g7y3 >=  6.3 and g7y3 <= 6.6:
				gp7y3 = 1.0
			elif g7y3 >=  6   and g7y3 <= 6.2:
				gp7y3 = .7
			elif g7y3 < 6:
				gp7y3 = 0
				
		elif y == 8:
			if g8y3 >= 9.3  and g8y3 <= 10:
				gp8y3 = 4.0
			elif g8y3 >=  9   and g8y3 <= 9.2:
				gp8y3 = 3.7
			elif g8y3 >=  8.7 and g8y3 <= 8.9:
				gp8y3 = 3.3
			elif g8y3 >=  8.3 and g8y3 <= 8.6:
				gp8y3 = 3.0
			elif g8y3 >=  8   and g8y3 <= 8.2:
				gp8y3 = 2.7
			elif g8y3 >=  7.7 and g8y3 <= 7.9:
				gp8y3 = 2.3
			elif g8y3 >=  7.3 and g8y3 <= 7.6:
				gp8y3 = 2.0
			elif g8y3 >=  7   and g8y3 <= 7.2:
				gp8y3 = 1.7
			elif g8y3 >=  6.7 and g8y3 <= 6.9:
				gp8y3 = 1.3
			elif g8y3 >=  6.3 and g8y3 <= 6.6:
				gp8y3 = 1.0
			elif g8y3 >=  6   and g8y3 <= 6.2:
				gp8y3 = .7
			elif g8y3 < 6:
				gp8y3 = 0
				
		elif y == 9:
			if g9y3 >= 9.3  and g9y3 <= 10:
				gp9y3 = 4.0
			elif g9y3 >=  9   and g9y3 <= 9.2:
				gp9y3 = 3.7
			elif g9y3 >=  8.7 and g9y3 <= 8.9:
				gp9y3 = 3.3
			elif g9y3 >=  8.3 and g9y3 <= 8.6:
				gp9y3 = 3.0
			elif g9y3 >=  8   and g9y3 <= 8.2:
				gp9y3 = 2.7
			elif g9y3 >=  7.7 and g9y3 <= 7.9:
				gp9y3 = 2.3
			elif g9y3 >=  7.3 and g9y3 <= 7.6:
				gp9y3 = 2.0
			elif g9y3 >=  7   and g9y3 <= 7.2:
				gp9y3 = 1.7
			elif g9y3 >=  6.7 and g9y3 <= 6.9:
				gp9y3 = 1.3
			elif g9y3 >=  6.3 and g9y3 <= 6.6:
				gp9y3 = 1.0
			elif g9y3 >=  6   and g9y3 <= 6.2:
				gp9y3 = .7
			elif g9y3 < 6:
				gp9y3 = 0
				
		elif y == 10:
			if g10y3 >= 9.3  and g10y3 <= 10:
				gp10y3 = 4.0
			elif g10y3 >=  9   and g10y3 <= 9.2:
				gp10y3 = 3.7
			elif g10y3 >=  8.7 and g10y3 <= 8.9:
				gp10y3 = 3.3
			elif g10y3 >=  8.3 and g10y3 <= 8.6:
				gp10y3 = 3.0
			elif g10y3 >=  8   and g10y3 <= 8.2:
				gp10y3 = 2.7
			elif g10y3 >=  7.7 and g10y3 <= 7.9:
				gp10y3 = 2.3
			elif g10y3 >=  7.3 and g10y3 <= 7.6:
				gp10y3 = 2.0
			elif g10y3 >=  7   and g10y3 <= 7.2:
				gp10y3 = 1.7
			elif g10y3 >=  6.7 and g10y3 <= 6.9:
				gp10y3 = 1.3
			elif g10y3 >=  6.3 and g10y3 <= 6.6:
				gp10y3 = 1.0
			elif g10y3 >=  6   and g10y3 <= 6.2:
				gp10y3 = .7
			elif g10y3 < 6:
				gp10y3 = 0
				
		elif y == 11:
			if g11y3 >= 9.3  and g11y3 <= 10:
				gp11y3 = 4.0
			elif g11y3 >=  9   and g11y3 <= 9.2:
				gp11y3 = 3.7
			elif g11y3 >=  8.7 and g11y3 <= 8.9:
				gp11y3 = 3.3
			elif g11y3 >=  8.3 and g11y3 <= 8.6:
				gp11y3 = 3.0
			elif g11y3 >=  8   and g11y3 <= 8.2:
				gp11y3 = 2.7
			elif g11y3 >=  7.7 and g11y3 <= 7.9:
				gp11y3 = 2.3
			elif g11y3 >=  7.3 and g11y3 <= 7.6:
				gp11y3 = 2.0
			elif g11y3 >=  7   and g11y3 <= 7.2:
				gp11y3 = 1.7
			elif g11y3 >=  6.7 and g11y3 <= 6.9:
				gp11y3 = 1.3
			elif g11y3 >=  6.3 and g11y3 <= 6.6:
				gp11y3 = 1.0
			elif g11y3 >=  6   and g11y3 <= 6.2:
				gp11y3 = .7
			elif g11y3 < 6:
				gp11y3 = 0
				
		elif y == 12:
			if   g12y3 >= 9.3  and g12y3 <= 10:
				gp12y3 = 4.0
			elif g12y3 >=  9   and g12y3 <= 9.2:
				gp12y3 = 3.7
			elif g12y3 >=  8.7 and g12y3 <= 8.9:
				gp12y3 = 3.3
			elif g12y3 >=  8.3 and g12y3 <= 8.6:
				gp12y3 = 3.0
			elif g12y3 >=  8   and g12y3 <= 8.2:
				gp12y3 = 2.7
			elif g12y3 >=  7.7 and g12y3 <= 7.9:
				gp12y3 = 2.3
			elif g12y3 >=  7.3 and g12y3 <= 7.6:
				gp12y3 = 2.0
			elif g12y3 >=  7   and g12y3 <= 7.2:
				gp12y3 = 1.7
			elif g12y3 >=  6.7 and g12y3 <= 6.9:
				gp12y3 = 1.3
			elif g12y3 >=  6.3 and g12y3 <= 6.6:
				gp12y3 = 1.0
			elif g12y3 >=  6   and g12y3 <= 6.2:
				gp12y3 = .7
			elif g12y3 < 6:
				gp12y3 = 0
				
		elif y == 13:
			if   g5y3 >= 9.3  and g13y3 <= 10:
				gp5y3 = 4.0
			elif g5y3 >=  9   and g13y3 <= 9.2:
				gp5y3 = 3.7
			elif g5y3 >=  8.7 and g13y3 <= 8.9:
				gp5y3 = 3.3
			elif g5y3 >=  8.3 and g13y3 <= 8.6:
				gp5y3 = 3.0
			elif g5y3 >=  8   and g13y3 <= 8.2:
				gp5y3 = 2.7
			elif g5y3 >=  7.7 and g13y3 <= 7.9:
				gp5y3 = 2.3
			elif g5y3 >=  7.3 and g13y3 <= 7.6:
				gp5y3 = 2.0
			elif g5y3 >=  7   and g13y3 <= 7.2:
				gp5y3 = 1.7
			elif g5y3 >=  6.7 and g13y3 <= 6.9:
				gp5y3 = 1.3
			elif g5y3 >=  6.3 and g13y3 <= 6.6:
				gp5y3 = 1.0
			elif g5y3 >=  6   and g13y3 <= 6.2:
				gp5y3 = .7
			elif g5y3 < 6:
				gp5y3 = 0
				
		elif y == 14:
			if   g5y3 >= 9.3  and g14y3 <= 10:
				gp5y3 = 4.0
			elif g5y3 >=  9   and g14y3 <= 9.2:
				gp5y3 = 3.7
			elif g5y3 >=  8.7 and g14y3 <= 8.9:
				gp5y3 = 3.3
			elif g5y3 >=  8.3 and g14y3 <= 8.6:
				gp5y3 = 3.0
			elif g5y3 >=  8   and g14y3 <= 8.2:
				gp5y3 = 2.7
			elif g5y3 >=  7.7 and g14y3 <= 7.9:
				gp5y3 = 2.3
			elif g5y3 >=  7.3 and g14y3 <= 7.6:
				gp5y3 = 2.0
			elif g5y3 >=  7   and g14y3 <= 7.2:
				gp5y3 = 1.7
			elif g5y3 >=  6.7 and g14y3 <= 6.9:
				gp5y3 = 1.3
			elif g5y3 >=  6.3 and g14y3 <= 6.6:
				gp5y3 = 1.0
			elif g5y3 >=  6   and g14y3 <= 6.2:
				gp5y3 = .7
			elif g5y3 < 6:
				gp5y3 = 0	
		
		elif y == 15:
			if   g5y3 >= 9.3  and g13y3 <= 10:
				gp5y3 = 4.0
			elif g5y3 >=  9   and g13y3 <= 9.2:
				gp5y3 = 3.7
			elif g5y3 >=  8.7 and g13y3 <= 8.9:
				gp5y3 = 3.3
			elif g5y3 >=  8.3 and g13y3 <= 8.6:
				gp5y3 = 3.0
			elif g5y3 >=  8   and g13y3 <= 8.2:
				gp5y3 = 2.7
			elif g5y3 >=  7.7 and g13y3 <= 7.9:
				gp5y3 = 2.3
			elif g5y3 >=  7.3 and g13y3 <= 7.6:
				gp5y3 = 2.0
			elif g5y3 >=  7   and g13y3 <= 7.2:
				gp5y3 = 1.7
			elif g5y3 >=  6.7 and g13y3 <= 6.9:
				gp5y3 = 1.3
			elif g5y3 >=  6.3 and g13y3 <= 6.6:
				gp5y3 = 1.0
			elif g5y3 >=  6   and g13y3 <= 6.2:
				gp5y3 = .7
			elif g5y3 < 6:
				gp5y3 = 0	
		
		elif y == 16:
			if   g5y3 >= 9.3  and g13y3 <= 10:
				gp5y3 = 4.0
			elif g5y3 >=  9   and g13y3 <= 9.2:
				gp5y3 = 3.7
			elif g5y3 >=  8.7 and g13y3 <= 8.9:
				gp5y3 = 3.3
			elif g5y3 >=  8.3 and g13y3 <= 8.6:
				gp5y3 = 3.0
			elif g5y3 >=  8   and g13y3 <= 8.2:
				gp5y3 = 2.7
			elif g5y3 >=  7.7 and g13y3 <= 7.9:
				gp5y3 = 2.3
			elif g5y3 >=  7.3 and g13y3 <= 7.6:
				gp5y3 = 2.0
			elif g5y3 >=  7   and g13y3 <= 7.2:
				gp5y3 = 1.7
			elif g5y3 >=  6.7 and g13y3 <= 6.9:
				gp5y3 = 1.3
			elif g5y3 >=  6.3 and g13y3 <= 6.6:
				gp5y3 = 1.0
			elif g5y3 >=  6   and g13y3 <= 6.2:
				gp5y3 = .7
			elif g5y3 < 6:
				gp5y3 = 0	
		
		elif y == 17:
			if   g5y3 >= 9.3  and g13y3 <= 10:
				gp5y3 = 4.0
			elif g5y3 >=  9   and g13y3 <= 9.2:
				gp5y3 = 3.7
			elif g5y3 >=  8.7 and g13y3 <= 8.9:
				gp5y3 = 3.3
			elif g5y3 >=  8.3 and g13y3 <= 8.6:
				gp5y3 = 3.0
			elif g5y3 >=  8   and g13y3 <= 8.2:
				gp5y3 = 2.7
			elif g5y3 >=  7.7 and g13y3 <= 7.9:
				gp5y3 = 2.3
			elif g5y3 >=  7.3 and g13y3 <= 7.6:
				gp5y3 = 2.0
			elif g5y3 >=  7   and g13y3 <= 7.2:
				gp5y3 = 1.7
			elif g5y3 >=  6.7 and g13y3 <= 6.9:
				gp5y3 = 1.3
			elif g5y3 >=  6.3 and g13y3 <= 6.6:
				gp5y3 = 1.0
			elif g5y3 >=  6   and g13y3 <= 6.2:
				gp5y3 = .7
			elif g5y3 < 6:
				gp5y3 = 0	
		
		elif y == 18:
			if   g5y3 >= 9.3  and g13y3 <= 10:
				gp5y3 = 4.0
			elif g5y3 >=  9   and g13y3 <= 9.2:
				gp5y3 = 3.7
			elif g5y3 >=  8.7 and g13y3 <= 8.9:
				gp5y3 = 3.3
			elif g5y3 >=  8.3 and g13y3 <= 8.6:
				gp5y3 = 3.0
			elif g5y3 >=  8   and g13y3 <= 8.2:
				gp5y3 = 2.7
			elif g5y3 >=  7.7 and g13y3 <= 7.9:
				gp5y3 = 2.3
			elif g5y3 >=  7.3 and g13y3 <= 7.6:
				gp5y3 = 2.0
			elif g5y3 >=  7   and g13y3 <= 7.2:
				gp5y3 = 1.7
			elif g5y3 >=  6.7 and g13y3 <= 6.9:
				gp5y3 = 1.3
			elif g5y3 >=  6.3 and g13y3 <= 6.6:
				gp5y3 = 1.0
			elif g5y3 >=  6   and g13y3 <= 6.2:
				gp5y3 = .7
			elif g5y3 < 6:
				gp5y3 = 0	
				
	y = y + 1
	x = x - 1

x = cla4
y = 1
while x > 0:
	if cyf4 == 4:
		if y == 1:
			if g1y4 >= 9.3 and g1y4 <= 10:
				gp1y4 = 4.0
			elif g1y4 >=  9 and g1y4 <= 9.2:
				gp1y4 = 3.7
			elif g1y4 >=  8.7 and g1y4 <= 8.9:
				gp1y4 = 3.3
			elif g1y4 >=  8.3 and g1y4 <= 8.6:
				gp1y4 = 3.0
			elif g1y4 >=  8 and g1y4 <= 8.2:
				gp1y4 = 2.7
			elif g1y4 >=  7.7 and g1y4 <= 7.9:
				gp1y4 = 2.3
			elif g1y4 >=  7.3 and g1y4 <= 7.6:
				gp1y4 = 2.0
			elif g1y4 >=  7 and g1y4 <= 7.2:
				gp1y4 = 1.7
			elif g1y4 >=  6.7 and g1y4 <= 6.9:
				gp1y4 = 1.3
			elif g1y4 >=  6.3 and g1y4 <= 6.6:
				gp1y4 = 1.0
			elif g1y4 >=  6 and g1y4 <= 6.2:
				gp1y4 = .7
			elif g1y4 < 6:
				gp1y4 = 0
		
		elif y == 2:
			if g2y4 >= 9.3 and g2y4 <= 10:
				gp2y4 = 4.0
			elif g2y4 >=  9 and g2y4 <= 9.2:
				gp2y4 = 3.7
			elif g2y4 >=  8.7 and g2y4 <= 8.9:
				gp2y4 = 3.3
			elif g2y4 >=  8.3 and g2y4 <= 8.6:
				gp2y4 = 3.0
			elif g2y4 >=  8 and g2y4 <= 8.2:
				gp2y4 = 2.7
			elif g2y4 >=  7.7 and g2y4 <= 7.9:
				gp2y4 = 2.3
			elif g2y4 >=  7.3 and g2y4 <= 7.6:
				gp2y4 = 2.0
			elif g2y4 >=  7 and g2y4 <= 7.2:
				gp2y4 = 1.7
			elif g2y4 >=  6.7 and g2y4 <= 6.9:
				gp2y4 = 1.3
			elif g2y4 >=  6.3 and g2y4 <= 6.6:
				gp2y4 = 1.0
			elif g2y4 >=  6 and g2y4 <= 6.2:
				gp2y4 = .7
			elif g2y4 < 6:
				gp2y4 = 0
		
		elif y == 3:
			if g3y4 >= 9.3     and g3y4 <= 10:
				gp3y4 = 4.0
			elif g3y4 >=  9   and g3y4 <= 9.2:
				gp3y4 = 3.7
			elif g3y4 >=  8.7 and g3y4 <= 8.9:
				gp3y4 = 3.3
			elif g3y4 >=  8.3 and g3y4 <= 8.6:
				gp3y4 = 3.0
			elif g3y4 >=  8   and g3y4 <= 8.2:
				gp3y4 = 2.7
			elif g3y4 >=  7.7 and g3y4 <= 7.9:
				gp3y4 = 2.3
			elif g3y4 >=  7.3 and g3y4 <= 7.6:
				gp3y4 = 2.0
			elif g3y4 >=  7   and g3y4 <= 7.2:
				gp3y4 = 1.7
			elif g3y4 >=  6.7 and g3y4 <= 6.9:
				gp3y4 = 1.3
			elif g3y4 >=  6.3 and g3y4 <= 6.6:
				gp3y4 = 1.0
			elif g3y4 >=  6   and g3y4 <= 6.2:
				gp3y4 = .7
			elif g3y4 < 6:
				gp3y4 = 0
		
		elif y == 4:
			if g4y4 >= 9.3     and g4y4 <= 10:
				gp4y4 = 4.0
			elif g4y4 >=  9   and g4y4 <= 9.2:
				gp4y4 = 3.7
			elif g4y4 >=  8.7 and g4y4 <= 8.9:
				gp4y4 = 3.3
			elif g4y4 >=  8.3 and g4y4 <= 8.6:
				gp4y4 = 3.0
			elif g4y4 >=  8   and g4y4 <= 8.2:
				gp4y4 = 2.7
			elif g4y4 >=  7.7 and g4y4 <= 7.9:
				gp4y4 = 2.3
			elif g4y4 >=  7.3 and g4y4 <= 7.6:
				gp4y4 = 2.0
			elif g4y4 >=  7   and g4y4 <= 7.2:
				gp4y4 = 1.7
			elif g4y4 >=  6.7 and g4y4 <= 6.9:
				gp4y4 = 1.3
			elif g4y4 >=  6.3 and g4y4 <= 6.6:
				gp4y4 = 1.0
			elif g4y4 >=  6   and g4y4 <= 6.2:
				gp4y4 = .7
			elif g4y4 < 6:
				gp4y4 = 0
				
		elif y == 5:
			if   g5y4 >= 9.3  and g5y4 <= 10:
				gp5y4 = 4.0
			elif g5y4 >=  9   and g5y4 <= 9.2:
				gp5y4 = 3.7
			elif g5y4 >=  8.7 and g5y4 <= 8.9:
				gp5y4 = 3.3
			elif g5y4 >=  8.3 and g5y4 <= 8.6:
				gp5y4 = 3.0
			elif g5y4 >=  8   and g5y4 <= 8.2:
				gp5y4 = 2.7
			elif g5y4 >=  7.7 and g5y4 <= 7.9:
				gp5y4 = 2.3
			elif g5y4 >=  7.3 and g5y4 <= 7.6:
				gp5y4 = 2.0
			elif g5y4 >=  7   and g5y4 <= 7.2:
				gp5y4 = 1.7
			elif g5y4 >=  6.7 and g5y4 <= 6.9:
				gp5y4 = 1.3
			elif g5y4 >=  6.3 and g5y4 <= 6.6:
				gp5y4 = 1.0
			elif g5y4 >=  6   and g5y4 <= 6.2:
				gp5y4 = .7
			elif g5y4 < 6:
				gp5y4 = 0
				
		elif y == 6:
			if g6y4 >= 9.3  and g6y4 <= 10:
				gp6y4 = 4.0
			elif g6y4 >=  9   and g6y4 <= 9.2:
				gp6y4 = 3.7
			elif g6y4 >=  8.7 and g6y4 <= 8.9:
				gp6y4 = 3.3
			elif g6y4 >=  8.3 and g6y4 <= 8.6:
				gp6y4 = 3.0
			elif g6y4 >=  8   and g6y4 <= 8.2:
				gp6y4 = 2.7
			elif g6y4 >=  7.7 and g6y4 <= 7.9:
				gp6y4 = 2.3
			elif g6y4 >=  7.3 and g6y4 <= 7.6:
				gp6y4 = 2.0
			elif g6y4 >=  7   and g6y4 <= 7.2:
				gp6y4 = 1.7
			elif g6y4 >=  6.7 and g6y4 <= 6.9:
				gp6y4 = 1.3
			elif g6y4 >=  6.3 and g6y4 <= 6.6:
				gp6y4 = 1.0
			elif g6y4 >=  6   and g6y4 <= 6.2:
				gp6y4 = .7
			elif g6y4 < 6:
				gp6y4 = 0
				
		elif y == 7:
			if g7y4 >= 9.3  and g7y4 <= 10:
				gp7y4 = 4.0
			elif g7y4 >=  9   and g7y4 <= 9.2:
				gp7y4 = 3.7
			elif g7y4 >=  8.7 and g7y4 <= 8.9:
				gp7y4 = 3.3
			elif g7y4 >=  8.3 and g7y4 <= 8.6:
				gp7y4 = 3.0
			elif g7y4 >=  8   and g7y4 <= 8.2:
				gp7y4 = 2.7
			elif g7y4 >=  7.7 and g7y4 <= 7.9:
				gp7y4 = 2.3
			elif g7y4 >=  7.3 and g7y4 <= 7.6:
				gp7y4 = 2.0
			elif g7y4 >=  7   and g7y4 <= 7.2:
				gp7y4 = 1.7
			elif g7y4 >=  6.7 and g7y4 <= 6.9:
				gp7y4 = 1.3
			elif g7y4 >=  6.3 and g7y4 <= 6.6:
				gp7y4 = 1.0
			elif g7y4 >=  6   and g7y4 <= 6.2:
				gp7y4 = .7
			elif g7y4 < 6:
				gp7y4 = 0
				
		elif y == 8:
			if g8y4 >= 9.3  and g8y4 <= 10:
				gp8y4 = 4.0
			elif g8y4 >=  9   and g8y4 <= 9.2:
				gp8y4 = 3.7
			elif g8y4 >=  8.7 and g8y4 <= 8.9:
				gp8y4 = 3.3
			elif g8y4 >=  8.3 and g8y4 <= 8.6:
				gp8y4 = 3.0
			elif g8y4 >=  8   and g8y4 <= 8.2:
				gp8y4 = 2.7
			elif g8y4 >=  7.7 and g8y4 <= 7.9:
				gp8y4 = 2.3
			elif g8y4 >=  7.3 and g8y4 <= 7.6:
				gp8y4 = 2.0
			elif g8y4 >=  7   and g8y4 <= 7.2:
				gp8y4 = 1.7
			elif g8y4 >=  6.7 and g8y4 <= 6.9:
				gp8y4 = 1.3
			elif g8y4 >=  6.3 and g8y4 <= 6.6:
				gp8y4 = 1.0
			elif g8y4 >=  6   and g8y4 <= 6.2:
				gp8y4 = .7
			elif g8y4 < 6:
				gp8y4 = 0
				
		elif y == 9:
			if g9y4 >= 9.3  and g9y4 <= 10:
				gp9y4 = 4.0
			elif g9y4 >=  9   and g9y4 <= 9.2:
				gp9y4 = 3.7
			elif g9y4 >=  8.7 and g9y4 <= 8.9:
				gp9y4 = 3.3
			elif g9y4 >=  8.3 and g9y4 <= 8.6:
				gp9y4 = 3.0
			elif g9y4 >=  8   and g9y4 <= 8.2:
				gp9y4 = 2.7
			elif g9y4 >=  7.7 and g9y4 <= 7.9:
				gp9y4 = 2.3
			elif g9y4 >=  7.3 and g9y4 <= 7.6:
				gp9y4 = 2.0
			elif g9y4 >=  7   and g9y4 <= 7.2:
				gp9y4 = 1.7
			elif g9y4 >=  6.7 and g9y4 <= 6.9:
				gp9y4 = 1.3
			elif g9y4 >=  6.3 and g9y4 <= 6.6:
				gp9y4 = 1.0
			elif g9y4 >=  6   and g9y4 <= 6.2:
				gp9y4 = .7
			elif g9y4 < 6:
				gp9y4 = 0
				
		elif y == 10:
			if g10y4 >= 9.3  and g10y4 <= 10:
				gp10y4 = 4.0
			elif g10y4 >=  9   and g10y4 <= 9.2:
				gp10y4 = 3.7
			elif g10y4 >=  8.7 and g10y4 <= 8.9:
				gp10y4 = 3.3
			elif g10y4 >=  8.3 and g10y4 <= 8.6:
				gp10y4 = 3.0
			elif g10y4 >=  8   and g10y4 <= 8.2:
				gp10y4 = 2.7
			elif g10y4 >=  7.7 and g10y4 <= 7.9:
				gp10y4 = 2.3
			elif g10y4 >=  7.3 and g10y4 <= 7.6:
				gp10y4 = 2.0
			elif g10y4 >=  7   and g10y4 <= 7.2:
				gp10y4 = 1.7
			elif g10y4 >=  6.7 and g10y4 <= 6.9:
				gp10y4 = 1.3
			elif g10y4 >=  6.3 and g10y4 <= 6.6:
				gp10y4 = 1.0
			elif g10y4 >=  6   and g10y4 <= 6.2:
				gp10y4 = .7
			elif g10y4 < 6:
				gp10y4 = 0
				
		elif y == 11:
			if g11y4 >= 9.3  and g11y4 <= 10:
				gp11y4 = 4.0
			elif g11y4 >=  9   and g11y4 <= 9.2:
				gp11y4 = 3.7
			elif g11y4 >=  8.7 and g11y4 <= 8.9:
				gp11y4 = 3.3
			elif g11y4 >=  8.3 and g11y4 <= 8.6:
				gp11y4 = 3.0
			elif g11y4 >=  8   and g11y4 <= 8.2:
				gp11y4 = 2.7
			elif g11y4 >=  7.7 and g11y4 <= 7.9:
				gp11y4 = 2.3
			elif g11y4 >=  7.3 and g11y4 <= 7.6:
				gp11y4 = 2.0
			elif g11y4 >=  7   and g11y4 <= 7.2:
				gp11y4 = 1.7
			elif g11y4 >=  6.7 and g11y4 <= 6.9:
				gp11y4 = 1.3
			elif g11y4 >=  6.3 and g11y4 <= 6.6:
				gp11y4 = 1.0
			elif g11y4 >=  6   and g11y4 <= 6.2:
				gp11y4 = .7
			elif g11y4 < 6:
				gp11y4 = 0
				
		elif y == 12:
			if   g12y4 >= 9.3  and g12y4 <= 10:
				gp12y4 = 4.0
			elif g12y4 >=  9   and g12y4 <= 9.2:
				gp12y4 = 3.7
			elif g12y4 >=  8.7 and g12y4 <= 8.9:
				gp12y4 = 3.3
			elif g12y4 >=  8.3 and g12y4 <= 8.6:
				gp12y4 = 3.0
			elif g12y4 >=  8   and g12y4 <= 8.2:
				gp12y4 = 2.7
			elif g12y4 >=  7.7 and g12y4 <= 7.9:
				gp12y4 = 2.3
			elif g12y4 >=  7.3 and g12y4 <= 7.6:
				gp12y4 = 2.0
			elif g12y4 >=  7   and g12y4 <= 7.2:
				gp12y4 = 1.7
			elif g12y4 >=  6.7 and g12y4 <= 6.9:
				gp12y4 = 1.3
			elif g12y4 >=  6.3 and g12y4 <= 6.6:
				gp12y4 = 1.0
			elif g12y4 >=  6   and g12y4 <= 6.2:
				gp12y4 = .7
			elif g12y4 < 6:
				gp12y4 = 0
				
		elif y == 13:
			if   g5y4 >= 9.3  and g13y4 <= 10:
				gp5y4 = 4.0
			elif g5y4 >=  9   and g13y4 <= 9.2:
				gp5y4 = 3.7
			elif g5y4 >=  8.7 and g13y4 <= 8.9:
				gp5y4 = 3.3
			elif g5y4 >=  8.3 and g13y4 <= 8.6:
				gp5y4 = 3.0
			elif g5y4 >=  8   and g13y4 <= 8.2:
				gp5y4 = 2.7
			elif g5y4 >=  7.7 and g13y4 <= 7.9:
				gp5y4 = 2.3
			elif g5y4 >=  7.3 and g13y4 <= 7.6:
				gp5y4 = 2.0
			elif g5y4 >=  7   and g13y4 <= 7.2:
				gp5y4 = 1.7
			elif g5y4 >=  6.7 and g13y4 <= 6.9:
				gp5y4 = 1.3
			elif g5y4 >=  6.3 and g13y4 <= 6.6:
				gp5y4 = 1.0
			elif g5y4 >=  6   and g13y4 <= 6.2:
				gp5y4 = .7
			elif g5y4 < 6:
				gp5y4 = 0
				
		if y == 14:
			if   g5y4 >= 9.3  and g13y4 <= 10:
				gp5y4 = 4.0
			elif g5y4 >=  9   and g13y4 <= 9.2:
				gp5y4 = 3.7
			elif g5y4 >=  8.7 and g13y4 <= 8.9:
				gp5y4 = 3.3
			elif g5y4 >=  8.3 and g13y4 <= 8.6:
				gp5y4 = 3.0
			elif g5y4 >=  8   and g13y4 <= 8.2:
				gp5y4 = 2.7
			elif g5y4 >=  7.7 and g13y4 <= 7.9:
				gp5y4 = 2.3
			elif g5y4 >=  7.3 and g13y4 <= 7.6:
				gp5y4 = 2.0
			elif g5y4 >=  7   and g13y4 <= 7.2:
				gp5y4 = 1.7
			elif g5y4 >=  6.7 and g13y4 <= 6.9:
				gp5y4 = 1.3
			elif g5y4 >=  6.3 and g13y4 <= 6.6:
				gp5y4 = 1.0
			elif g5y4 >=  6   and g13y4 <= 6.2:
				gp5y4 = .7
			elif g5y4 < 6:
				gp5y4 = 0
				
		elif y == 15:
			if   g5y4 >= 9.3  and g13y4 <= 10:
				gp5y4 = 4.0
			elif g5y4 >=  9   and g13y4 <= 9.2:
				gp5y4 = 3.7
			elif g5y4 >=  8.7 and g13y4 <= 8.9:
				gp5y4 = 3.3
			elif g5y4 >=  8.3 and g13y4 <= 8.6:
				gp5y4 = 3.0
			elif g5y4 >=  8   and g13y4 <= 8.2:
				gp5y4 = 2.7
			elif g5y4 >=  7.7 and g13y4 <= 7.9:
				gp5y4 = 2.3
			elif g5y4 >=  7.3 and g13y4 <= 7.6:
				gp5y4 = 2.0
			elif g5y4 >=  7   and g13y4 <= 7.2:
				gp5y4 = 1.7
			elif g5y4 >=  6.7 and g13y4 <= 6.9:
				gp5y4 = 1.3
			elif g5y4 >=  6.3 and g13y4 <= 6.6:
				gp5y4 = 1.0
			elif g5y4 >=  6   and g13y4 <= 6.2:
				gp5y4 = .7
			elif g5y4 < 6:
				gp5y4 = 0
		
		elif y == 16:
			if   g5y4 >= 9.3  and g13y4 <= 10:
				gp5y4 = 4.0
			elif g5y4 >=  9   and g13y4 <= 9.2:
				gp5y4 = 3.7
			elif g5y4 >=  8.7 and g13y4 <= 8.9:
				gp5y4 = 3.3
			elif g5y4 >=  8.3 and g13y4 <= 8.6:
				gp5y4 = 3.0
			elif g5y4 >=  8   and g13y4 <= 8.2:
				gp5y4 = 2.7
			elif g5y4 >=  7.7 and g13y4 <= 7.9:
				gp5y4 = 2.3
			elif g5y4 >=  7.3 and g13y4 <= 7.6:
				gp5y4 = 2.0
			elif g5y4 >=  7   and g13y4 <= 7.2:
				gp5y4 = 1.7
			elif g5y4 >=  6.7 and g13y4 <= 6.9:
				gp5y4 = 1.3
			elif g5y4 >=  6.3 and g13y4 <= 6.6:
				gp5y4 = 1.0
			elif g5y4 >=  6   and g13y4 <= 6.2:
				gp5y4 = .7
			elif g5y4 < 6:
				gp5y4 = 0
				
		elif y == 17:
			if   g5y4 >= 9.3  and g13y4 <= 10:
				gp5y4 = 4.0
			elif g5y4 >=  9   and g13y4 <= 9.2:
				gp5y4 = 3.7
			elif g5y4 >=  8.7 and g13y4 <= 8.9:
				gp5y4 = 3.3
			elif g5y4 >=  8.3 and g13y4 <= 8.6:
				gp5y4 = 3.0
			elif g5y4 >=  8   and g13y4 <= 8.2:
				gp5y4 = 2.7
			elif g5y4 >=  7.7 and g13y4 <= 7.9:
				gp5y4 = 2.3
			elif g5y4 >=  7.3 and g13y4 <= 7.6:
				gp5y4 = 2.0
			elif g5y4 >=  7   and g13y4 <= 7.2:
				gp5y4 = 1.7
			elif g5y4 >=  6.7 and g13y4 <= 6.9:
				gp5y4 = 1.3
			elif g5y4 >=  6.3 and g13y4 <= 6.6:
				gp5y4 = 1.0
			elif g5y4 >=  6   and g13y4 <= 6.2:
				gp5y4 = .7
			elif g5y4 < 6:
				gp5y4 = 0
				
		elif y == 18:
			if   g5y4 >= 9.3  and g13y4 <= 10:
				gp5y4 = 4.0
			elif g5y4 >=  9   and g13y4 <= 9.2:
				gp5y4 = 3.7
			elif g5y4 >=  8.7 and g13y4 <= 8.9:
				gp5y4 = 3.3
			elif g5y4 >=  8.3 and g13y4 <= 8.6:
				gp5y4 = 3.0
			elif g5y4 >=  8   and g13y4 <= 8.2:
				gp5y4 = 2.7
			elif g5y4 >=  7.7 and g13y4 <= 7.9:
				gp5y4 = 2.3
			elif g5y4 >=  7.3 and g13y4 <= 7.6:
				gp5y4 = 2.0
			elif g5y4 >=  7   and g13y4 <= 7.2:
				gp5y4 = 1.7
			elif g5y4 >=  6.7 and g13y4 <= 6.9:
				gp5y4 = 1.3
			elif g5y4 >=  6.3 and g13y4 <= 6.6:
				gp5y4 = 1.0
			elif g5y4 >=  6   and g13y4 <= 6.2:
				gp5y4 = .7
			elif g5y4 < 6:
				gp5y4 = 0
				
	y = y + 1
	x = x - 1

x = cla5
y = 1
while x > 0:
	if cyf5 == 5:
		if y == 1:
			if g1y5 >= 9.3 and g1y5 <= 10:
				gp1y5 = 4.0
			elif g1y5 >=  9 and g1y5 <= 9.2:
				gp1y5 = 3.7
			elif g1y5 >=  8.7 and g1y5 <= 8.9:
				gp1y5 = 3.3
			elif g1y5 >=  8.3 and g1y5 <= 8.6:
				gp1y5 = 3.0
			elif g1y5 >=  8 and g1y5 <= 8.2:
				gp1y5 = 2.7
			elif g1y5 >=  7.7 and g1y5 <= 7.9:
				gp1y5 = 2.3
			elif g1y5 >=  7.3 and g1y5 <= 7.6:
				gp1y5 = 2.0
			elif g1y5 >=  7 and g1y5 <= 7.2:
				gp1y5 = 1.7
			elif g1y5 >=  6.7 and g1y5 <= 6.9:
				gp1y5 = 1.3
			elif g1y5 >=  6.3 and g1y5 <= 6.6:
				gp1y5 = 1.0
			elif g1y5 >=  6 and g1y5 <= 6.2:
				gp1y5 = .7
			elif g1y5 < 6:
				gp1y5 = 0
				
		elif y == 2:
			if g2y5 >= 9.3 and g2y5 <= 10:
				gp2y5 = 4.0
			elif g2y5 >=  9 and g2y5 <= 9.2:
				gp2y5 = 3.7
			elif g2y5 >=  8.7 and g2y5 <= 8.9:
				gp2y5 = 3.3
			elif g2y5 >=  8.3 and g2y5 <= 8.6:
				gp2y5 = 3.0
			elif g2y5 >=  8 and g2y5 <= 8.2:
				gp2y5 = 2.7
			elif g2y5 >=  7.7 and g2y5 <= 7.9:
				gp2y5 = 2.3
			elif g2y5 >=  7.3 and g2y5 <= 7.6:
				gp2y5 = 2.0
			elif g2y5 >=  7 and g2y5 <= 7.2:
				gp2y5 = 1.7
			elif g2y5 >=  6.7 and g2y5 <= 6.9:
				gp2y5 = 1.3
			elif g2y5 >=  6.3 and g2y5 <= 6.6:
				gp2y5 = 1.0
			elif g2y5 >=  6 and g2y5 <= 6.2:
				gp2y5 = .7
			elif g2y5 < 6:
				gp2y5 = 0
		
		elif y == 3:
			if g3y5 >= 9.3     and g3y5 <= 10:
				gp3y5 = 4.0
			elif g3y5 >=  9   and g3y5 <= 9.2:
				gp3y5 = 3.7
			elif g3y5 >=  8.7 and g3y5 <= 8.9:
				gp3y5 = 3.3
			elif g3y5 >=  8.3 and g3y5 <= 8.6:
				gp3y5 = 3.0
			elif g3y5 >=  8   and g3y5 <= 8.2:
				gp3y5 = 2.7
			elif g3y5 >=  7.7 and g3y5 <= 7.9:
				gp3y5 = 2.3
			elif g3y5 >=  7.3 and g3y5 <= 7.6:
				gp3y5 = 2.0
			elif g3y5 >=  7   and g3y5 <= 7.2:
				gp3y5 = 1.7
			elif g3y5 >=  6.7 and g3y5 <= 6.9:
				gp3y5 = 1.3
			elif g3y5 >=  6.3 and g3y5 <= 6.6:
				gp3y5 = 1.0
			elif g3y5 >=  6   and g3y5 <= 6.2:
				gp3y5 = .7
			elif g3y5 < 6:
				gp3y5 = 0
				
		elif y == 4:
			if g4y5 >= 9.3     and g4y5 <= 10:
				gp4y5 = 4.0
			elif g4y5 >=  9   and g4y5 <= 9.2:
				gp4y5 = 3.7
			elif g4y5 >=  8.7 and g4y5 <= 8.9:
				gp4y5 = 3.3
			elif g4y5 >=  8.3 and g4y5 <= 8.6:
				gp4y5 = 3.0
			elif g4y5 >=  8   and g4y5 <= 8.2:
				gp4y5 = 2.7
			elif g4y5 >=  7.7 and g4y5 <= 7.9:
				gp4y5 = 2.3
			elif g4y5 >=  7.3 and g4y5 <= 7.6:
				gp4y5 = 2.0
			elif g4y5 >=  7   and g4y5 <= 7.2:
				gp4y5 = 1.7
			elif g4y5 >=  6.7 and g4y5 <= 6.9:
				gp4y5 = 1.3
			elif g4y5 >=  6.3 and g4y5 <= 6.6:
				gp4y5 = 1.0
			elif g4y5 >=  6   and g4y5 <= 6.2:
				gp4y5 = .7
			elif g4y5 < 6:
				gp4y5 = 0
				
		elif y == 5:
			if   g5y5 >= 9.3  and g5y5 <= 10:
				gp5y5 = 4.0
			elif g5y5 >=  9   and g5y5 <= 9.2:
				gp5y5 = 3.7
			elif g5y5 >=  8.7 and g5y5 <= 8.9:
				gp5y5 = 3.3
			elif g5y5 >=  8.3 and g5y5 <= 8.6:
				gp5y5 = 3.0
			elif g5y5 >=  8   and g5y5 <= 8.2:
				gp5y5 = 2.7
			elif g5y5 >=  7.7 and g5y5 <= 7.9:
				gp5y5 = 2.3
			elif g5y5 >=  7.3 and g5y5 <= 7.6:
				gp5y5 = 2.0
			elif g5y5 >=  7   and g5y5 <= 7.2:
				gp5y5 = 1.7
			elif g5y5 >=  6.7 and g5y5 <= 6.9:
				gp5y5 = 1.3
			elif g5y5 >=  6.3 and g5y5 <= 6.6:
				gp5y5 = 1.0
			elif g5y5 >=  6   and g5y5 <= 6.2:
				gp5y5 = .7
			elif g5y5 < 6:
				gp5y5 = 0
		
		elif y == 6:
			if g6y5 >= 9.3  and g6y5 <= 10:
				gp6y5 = 4.0
			elif g6y5 >=  9   and g6y5 <= 9.2:
				gp6y5 = 3.7
			elif g6y5 >=  8.7 and g6y5 <= 8.9:
				gp6y5 = 3.3
			elif g6y5 >=  8.3 and g6y5 <= 8.6:
				gp6y5 = 3.0
			elif g6y5 >=  8   and g6y5 <= 8.2:
				gp6y5 = 2.7
			elif g6y5 >=  7.7 and g6y5 <= 7.9:
				gp6y5 = 2.3
			elif g6y5 >=  7.3 and g6y5 <= 7.6:
				gp6y5 = 2.0
			elif g6y5 >=  7   and g6y5 <= 7.2:
				gp6y5 = 1.7
			elif g6y5 >=  6.7 and g6y5 <= 6.9:
				gp6y5 = 1.3
			elif g6y5 >=  6.3 and g6y5 <= 6.6:
				gp6y5 = 1.0
			elif g6y5 >=  6   and g6y5 <= 6.2:
				gp6y5 = .7
			elif g6y5 < 6:
				gp6y5 = 0
		
		elif y == 7:
			if g7y5 >= 9.3  and g7y5 <= 10:
				gp7y5 = 4.0
			elif g7y5 >=  9   and g7y5 <= 9.2:
				gp7y5 = 3.7
			elif g7y5 >=  8.7 and g7y5 <= 8.9:
				gp7y5 = 3.3
			elif g7y5 >=  8.3 and g7y5 <= 8.6:
				gp7y5 = 3.0
			elif g7y5 >=  8   and g7y5 <= 8.2:
				gp7y5 = 2.7
			elif g7y5 >=  7.7 and g7y5 <= 7.9:
				gp7y5 = 2.3
			elif g7y5 >=  7.3 and g7y5 <= 7.6:
				gp7y5 = 2.0
			elif g7y5 >=  7   and g7y5 <= 7.2:
				gp7y5 = 1.7
			elif g7y5 >=  6.7 and g7y5 <= 6.9:
				gp7y5 = 1.3
			elif g7y5 >=  6.3 and g7y5 <= 6.6:
				gp7y5 = 1.0
			elif g7y5 >=  6   and g7y5 <= 6.2:
				gp7y5 = .7
			elif g7y5 < 6:
				gp7y5 = 0
				
		elif y == 8:
			if g8y5 >= 9.3  and g8y5 <= 10:
				gp8y5 = 4.0
			elif g8y5 >=  9   and g8y5 <= 9.2:
				gp8y5 = 3.7
			elif g8y5 >=  8.7 and g8y5 <= 8.9:
				gp8y5 = 3.3
			elif g8y5 >=  8.3 and g8y5 <= 8.6:
				gp8y5 = 3.0
			elif g8y5 >=  8   and g8y5 <= 8.2:
				gp8y5 = 2.7
			elif g8y5 >=  7.7 and g8y5 <= 7.9:
				gp8y5 = 2.3
			elif g8y5 >=  7.3 and g8y5 <= 7.6:
				gp8y5 = 2.0
			elif g8y5 >=  7   and g8y5 <= 7.2:
				gp8y5 = 1.7
			elif g8y5 >=  6.7 and g8y5 <= 6.9:
				gp8y5 = 1.3
			elif g8y5 >=  6.3 and g8y5 <= 6.6:
				gp8y5 = 1.0
			elif g8y5 >=  6   and g8y5 <= 6.2:
				gp8y5 = .7
			elif g8y5 < 6:
				gp8y5 = 0
				
		elif y == 9:
			if   g9y5 >= 9.3  and g9y5 <= 10:
				gp9y5 = 4.0
			elif g9y5 >=  9   and g9y5 <= 9.2:
				gp9y5 = 3.7
			elif g9y5 >=  8.7 and g9y5 <= 8.9:
				gp9y5 = 3.3
			elif g9y5 >=  8.3 and g9y5 <= 8.6:
				gp9y5 = 3.0
			elif g9y5 >=  8   and g9y5 <= 8.2:
				gp9y5 = 2.7
			elif g9y5 >=  7.7 and g9y5 <= 7.9:
				gp9y5 = 2.3
			elif g9y5 >=  7.3 and g9y5 <= 7.6:
				gp9y5 = 2.0
			elif g9y5 >=  7   and g9y5 <= 7.2:
				gp9y5 = 1.7
			elif g9y5 >=  6.7 and g9y5 <= 6.9:
				gp9y5 = 1.3
			elif g9y5 >=  6.3 and g9y5 <= 6.6:
				gp9y5 = 1.0
			elif g9y5 >=  6   and g9y5 <= 6.2:
				gp9y5 = .7
			elif g9y5 < 6:
				gp9y5 = 0
				
		elif y == 10:
			if g10y5 >= 9.3  and g10y5 <= 10:
				gp10y5 = 4.0
			elif g10y5 >=  9   and g10y5 <= 9.2:
				gp10y5 = 3.7
			elif g10y5 >=  8.7 and g10y5 <= 8.9:
				gp10y5 = 3.3
			elif g10y5 >=  8.3 and g10y5 <= 8.6:
				gp10y5 = 3.0
			elif g10y5 >=  8   and g10y5 <= 8.2:
				gp10y5 = 2.7
			elif g10y5 >=  7.7 and g10y5 <= 7.9:
				gp10y5 = 2.3
			elif g10y5 >=  7.3 and g10y5 <= 7.6:
				gp10y5 = 2.0
			elif g10y5 >=  7   and g10y5 <= 7.2:
				gp10y5 = 1.7
			elif g10y5 >=  6.7 and g10y5 <= 6.9:
				gp10y5 = 1.3
			elif g10y5 >=  6.3 and g10y5 <= 6.6:
				gp10y5 = 1.0
			elif g10y5 >=  6   and g10y5 <= 6.2:
				gp10y5 = .7
			elif g10y5 < 6:
				gp10y5 = 0
				
		elif y == 11:
			if g11y5 >= 9.3  and g11y5 <= 10:
				gp11y5 = 4.0
			elif g11y5 >=  9   and g11y5 <= 9.2:
				gp11y5 = 3.7
			elif g11y5 >=  8.7 and g11y5 <= 8.9:
				gp11y5 = 3.3
			elif g11y5 >=  8.3 and g11y5 <= 8.6:
				gp11y5 = 3.0
			elif g11y5 >=  8   and g11y5 <= 8.2:
				gp11y5 = 2.7
			elif g11y5 >=  7.7 and g11y5 <= 7.9:
				gp11y5 = 2.3
			elif g11y5 >=  7.3 and g11y5 <= 7.6:
				gp11y5 = 2.0
			elif g11y5 >=  7   and g11y5 <= 7.2:
				gp11y5 = 1.7
			elif g11y5 >=  6.7 and g11y5 <= 6.9:
				gp11y5 = 1.3
			elif g11y5 >=  6.3 and g11y5 <= 6.6:
				gp11y5 = 1.0
			elif g11y5 >=  6   and g11y5 <= 6.2:
				gp11y5 = .7
			elif g11y5 < 6:
				gp11y5 = 0
				
		elif y == 12:
			if   g12y5 >= 9.3  and g12y5 <= 10:
				gp12y5 = 4.0
			elif g12y5 >=  9   and g12y5 <= 9.2:
				gp12y5 = 3.7
			elif g12y5 >=  8.7 and g12y5 <= 8.9:
				gp12y5 = 3.3
			elif g12y5 >=  8.3 and g12y5 <= 8.6:
				gp12y5 = 3.0
			elif g12y5 >=  8   and g12y5 <= 8.2:
				gp12y5 = 2.7
			elif g12y5 >=  7.7 and g12y5 <= 7.9:
				gp12y5 = 2.3
			elif g12y5 >=  7.3 and g12y5 <= 7.6:
				gp12y5 = 2.0
			elif g12y5 >=  7   and g12y5 <= 7.2:
				gp12y5 = 1.7
			elif g12y5 >=  6.7 and g12y5 <= 6.9:
				gp12y5 = 1.3
			elif g12y5 >=  6.3 and g12y5 <= 6.6:
				gp12y5 = 1.0
			elif g12y5 >=  6   and g12y5 <= 6.2:
				gp12y5 = .7
			elif g12y5 < 6:
				gp12y5 = 0
				
		elif y == 13:
			if   g5y5 >= 9.3  and g13y5 <= 10:
				gp5y5 = 4.0
			elif g5y5 >=  9   and g13y5 <= 9.2:
				gp5y5 = 3.7
			elif g5y5 >=  8.7 and g13y5 <= 8.9:
				gp5y5 = 3.3
			elif g5y5 >=  8.3 and g13y5 <= 8.6:
				gp5y5 = 3.0
			elif g5y5 >=  8   and g13y5 <= 8.2:
				gp5y5 = 2.7
			elif g5y5 >=  7.7 and g13y5 <= 7.9:
				gp5y5 = 2.3
			elif g5y5 >=  7.3 and g13y5 <= 7.6:
				gp5y5 = 2.0
			elif g5y5 >=  7   and g13y5 <= 7.2:
				gp5y5 = 1.7
			elif g5y5 >=  6.7 and g13y5 <= 6.9:
				gp5y5 = 1.3
			elif g5y5 >=  6.3 and g13y5 <= 6.6:
				gp5y5 = 1.0
			elif g5y5 >=  6   and g13y5 <= 6.2:
				gp5y5 = .7
			elif g5y5 < 6:
				gp5y5 = 0
				
		elif y == 14:
			if   g5y5 >= 9.3  and g13y5 <= 10:
				gp5y5 = 4.0
			elif g5y5 >=  9   and g13y5 <= 9.2:
				gp5y5 = 3.7
			elif g5y5 >=  8.7 and g13y5 <= 8.9:
				gp5y5 = 3.3
			elif g5y5 >=  8.3 and g13y5 <= 8.6:
				gp5y5 = 3.0
			elif g5y5 >=  8   and g13y5 <= 8.2:
				gp5y5 = 2.7
			elif g5y5 >=  7.7 and g13y5 <= 7.9:
				gp5y5 = 2.3
			elif g5y5 >=  7.3 and g13y5 <= 7.6:
				gp5y5 = 2.0
			elif g5y5 >=  7   and g13y5 <= 7.2:
				gp5y5 = 1.7
			elif g5y5 >=  6.7 and g13y5 <= 6.9:
				gp5y5 = 1.3
			elif g5y5 >=  6.3 and g13y5 <= 6.6:
				gp5y5 = 1.0
			elif g5y5 >=  6   and g13y5 <= 6.2:
				gp5y5 = .7
			elif g5y5 < 6:
				gp5y5 = 0
				
		elif y == 15:
			if   g5y5 >= 9.3  and g13y5 <= 10:
				gp5y5 = 4.0
			elif g5y5 >=  9   and g13y5 <= 9.2:
				gp5y5 = 3.7
			elif g5y5 >=  8.7 and g13y5 <= 8.9:
				gp5y5 = 3.3
			elif g5y5 >=  8.3 and g13y5 <= 8.6:
				gp5y5 = 3.0
			elif g5y5 >=  8   and g13y5 <= 8.2:
				gp5y5 = 2.7
			elif g5y5 >=  7.7 and g13y5 <= 7.9:
				gp5y5 = 2.3
			elif g5y5 >=  7.3 and g13y5 <= 7.6:
				gp5y5 = 2.0
			elif g5y5 >=  7   and g13y5 <= 7.2:
				gp5y5 = 1.7
			elif g5y5 >=  6.7 and g13y5 <= 6.9:
				gp5y5 = 1.3
			elif g5y5 >=  6.3 and g13y5 <= 6.6:
				gp5y5 = 1.0
			elif g5y5 >=  6   and g13y5 <= 6.2:
				gp5y5 = .7
			elif g5y5 < 6:
				gp5y5 = 0
				
		elif y == 16:
			if   g5y5 >= 9.3  and g13y5 <= 10:
				gp5y5 = 4.0
			elif g5y5 >=  9   and g13y5 <= 9.2:
				gp5y5 = 3.7
			elif g5y5 >=  8.7 and g13y5 <= 8.9:
				gp5y5 = 3.3
			elif g5y5 >=  8.3 and g13y5 <= 8.6:
				gp5y5 = 3.0
			elif g5y5 >=  8   and g13y5 <= 8.2:
				gp5y5 = 2.7
			elif g5y5 >=  7.7 and g13y5 <= 7.9:
				gp5y5 = 2.3
			elif g5y5 >=  7.3 and g13y5 <= 7.6:
				gp5y5 = 2.0
			elif g5y5 >=  7   and g13y5 <= 7.2:
				gp5y5 = 1.7
			elif g5y5 >=  6.7 and g13y5 <= 6.9:
				gp5y5 = 1.3
			elif g5y5 >=  6.3 and g13y5 <= 6.6:
				gp5y5 = 1.0
			elif g5y5 >=  6   and g13y5 <= 6.2:
				gp5y5 = .7
			elif g5y5 < 6:
				gp5y5 = 0
				
		elif y == 17:
			if   g5y5 >= 9.3  and g13y5 <= 10:
				gp5y5 = 4.0
			elif g5y5 >=  9   and g13y5 <= 9.2:
				gp5y5 = 3.7
			elif g5y5 >=  8.7 and g13y5 <= 8.9:
				gp5y5 = 3.3
			elif g5y5 >=  8.3 and g13y5 <= 8.6:
				gp5y5 = 3.0
			elif g5y5 >=  8   and g13y5 <= 8.2:
				gp5y5 = 2.7
			elif g5y5 >=  7.7 and g13y5 <= 7.9:
				gp5y5 = 2.3
			elif g5y5 >=  7.3 and g13y5 <= 7.6:
				gp5y5 = 2.0
			elif g5y5 >=  7   and g13y5 <= 7.2:
				gp5y5 = 1.7
			elif g5y5 >=  6.7 and g13y5 <= 6.9:
				gp5y5 = 1.3
			elif g5y5 >=  6.3 and g13y5 <= 6.6:
				gp5y5 = 1.0
			elif g5y5 >=  6   and g13y5 <= 6.2:
				gp5y5 = .7
			elif g5y5 < 6:
				gp5y5 = 0
				
		elif y == 18:
			if   g5y5 >= 9.3  and g13y5 <= 10:
				gp5y5 = 4.0
			elif g5y5 >=  9   and g13y5 <= 9.2:
				gp5y5 = 3.7
			elif g5y5 >=  8.7 and g13y5 <= 8.9:
				gp5y5 = 3.3
			elif g5y5 >=  8.3 and g13y5 <= 8.6:
				gp5y5 = 3.0
			elif g5y5 >=  8   and g13y5 <= 8.2:
				gp5y5 = 2.7
			elif g5y5 >=  7.7 and g13y5 <= 7.9:
				gp5y5 = 2.3
			elif g5y5 >=  7.3 and g13y5 <= 7.6:
				gp5y5 = 2.0
			elif g5y5 >=  7   and g13y5 <= 7.2:
				gp5y5 = 1.7
			elif g5y5 >=  6.7 and g13y5 <= 6.9:
				gp5y5 = 1.3
			elif g5y5 >=  6.3 and g13y5 <= 6.6:
				gp5y5 = 1.0
			elif g5y5 >=  6   and g13y5 <= 6.2:
				gp5y5 = .7
			elif g5y5 < 6:
				gp5y5 = 0
				
	y = y + 1
	x = x - 1

	
import os
os.system("cls")

space = ' '
equal = ' = '
line = "\n"
if cyf == 1:
	arq = open("GPA Calculator.txt", "w")
	
	if idioma == 1:
		scores = "Your score of the 1st year in the scale is 0 - 10:"
		print "\n", scores
		arq.write(scores)
	elif idioma == 2:
		notas = "As notas do seu primeiro ano na escala de 0 - 10:"
		print "\n", notas
		arq.write(notas)
	elif idioma == 3:
		calificaciones = "Tus calificaciones en tu primer en la escala de 0 - 10 son:"
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
	
	#Writing the scores on the archive
	writeG = (space + c1 + equal + str(g1) + line)
	arq.write(writeG)
	writeG = (space + c2 + equal + str(g2)+ line)
	arq.write(writeG)
	writeG = (space + c3 + equal + str(g3)+ line)
	arq.write(writeG)
	writeG = (space + c4 + equal + str(g4)+ line)
	arq.write(writeG)
	writeG = (space + c5 + equal + str(g5)+ line)
	arq.write(writeG)
	writeG = (space + c6 + equal + str(g6)+ line)
	arq.write(writeG)
	writeG = (space + c7 + equal + str(g7)+ line)
	arq.write(writeG)
	writeG = (space + c8 + equal + str(g8)+ line)
	arq.write(writeG)
	
	y = 8
	x = 8
	while x < cla1:
		y = y + 1
		if y == 9:
			print "\n ", c9, "=", g9
			writeG = (space + c9 + equal + str(g9)+ line)
			arq.write(writeG)
	
		elif y == 10:
			print "\n ", c10, "=", g10
			writeG = (space + c10 + equal + str(g10)+ line)
			arq.write(writeG)
	
		elif y == 11:
			print "\n ", c11, "=", g11
			writeG = (space + c11 + equal + str(g11)+ line)
			arq.write(writeG)

		elif y == 12:
			print "\n ", c12, "=", g12
			writeG = (space + c12 + equal + str(g12)+ line)
			arq.write(writeG)

		elif y == 13:
			print "\n ", c13, "=", g13
			writeG = (space + c13 + equal + str(g13)+ line)
			arq.write(writeG)

		elif y == 14:
			print "\n ", c14, "=", g14
			writeG = (space + c14 + equal + str(g14)+ line)
			arq.write(writeG)

		elif y == 15:
			print "\n ", c15, "=", g15
			writeG = (space + c15 + equal + str(g15)+ line)
			arq.write(writeG)
	
		elif y == 16:
			print "\n ", c16, "=", g16
			writeG = (space + c16 + equal + str(g16)+ line)
			arq.write(writeG)
	
		elif y == 17:
			print "\n ", c17, "=", g17
			writeG = (space + c17 + equal + str(g17)+ line)
			arq.write(writeG)
	
		elif y == 18:
			print "\n ", c18, "=", g18
			writeG = (space + c18 + equal + str(g18)+ line)
			arq.write(writeG)
		x = x + 1
	
	med = (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9 + g10 + g11 + g12 + g13 + g14 + g15 + g16 + g17 + g18) / cla1
	
	gpa = (gp1 + gp2 + gp3 + gp4 + gp5 + gp6 + gp7 + gp8 + gp9 + gp10 + gp11 + gp12 + gp13 + gp14 + gp15 + gp16 + gp17 + gp18) / cla1
	
	
	if idioma == 1:
		print "\n Average of the 1st year: ", med
		print "\n It is your GPA score: ", gpa
		enter = raw_input(" Press enter to continue ")
	elif idioma == 2:
		print "\n Essa e a media do seu 1ro ano: ", med
		print "\n GPA score: ", gpa
		enter = raw_input(" Precione enter para continuar ")
	elif idioma == 3:
		print "\n Este es tu promedio de 1ro ano: ", med
		print "\n GPA score: ", gpa
		enter = raw_input(" Aplaste enter para seguir ")
		
if cyf2 == 2:
	#Asking for the lenguage and writing the phrase
	if idioma == 1:
		scores = "\nYour score of the 2nd year in the scale is 0 - 10:"
		print "\n", scores
		arq.write(scores)
	elif idioma == 2:
		notas = "\nAs notas do seu segundo ano na escala de 0 - 10:"
		print "\n", notas
		arq.write(notas)
	elif idioma == 3:
		calificaciones = "\nTus calificaciones en tu segundo en la escala de 0 - 10 son:"
		print "\n", calificaciones
		arq.write(calificaciones)
		
	arq.write("\n")
		
	print "\n ", c1y2, "=", g2y2
	print "\n ", c2y2, "=", g2y2
	print "\n ", c3y2, "=", g3y2
	print "\n ", c4y2, "=", g4y2
	print "\n ", c5y2, "=", g5y2
	print "\n ", c6y2, "=", g6y2
	print "\n ", c7y2, "=", g7y2
	print "\n ", c8y2, "=", g8y2
	
	#Writing the scores on the archive
	writeG = (space + c1y2 + equal + str(g1y2)+ line)
	arq.write(writeG)
	writeG = (space + c2y2 + equal + str(g2y2)+ line)
	arq.write(writeG)
	writeG = (space + c3y2 + equal + str(g3y2)+ line)
	arq.write(writeG)
	writeG = (space + c4y2 + equal + str(g4y2)+ line)
	arq.write(writeG)
	writeG = (space + c5y2 + equal + str(g5y2)+ line)
	arq.write(writeG)
	writeG = (space + c6y2 + equal + str(g6y2)+ line)
	arq.write(writeG)
	writeG = (space + c7y2 + equal + str(g7y2)+ line)
	arq.write(writeG)
	writeG = (space + c8y2 + equal + str(g8y2)+ line)
	arq.write(writeG)
	
	y = 8
	x = 8
	while x < cla2:
		y = y + 1
		if y == 9:
			print "\n ", c9y2, "=", g9y2
			writeG = (space + c9y2 + equal + str(g9y2)+ line)
			arq.write(writeG)
	
		elif y == 10:
			print "\n ", c10y2, "=", g10y2
			writeG = (space + c10y2 + equal + str(g10y2)+ line)
			arq.write(writeG)
		
		elif y == 11:
			print "\n ", c11y2, "=", g11y2
			writeG = (space + c11y2 + equal + str(g11y2)+ line)
			arq.write(writeG)

		elif y == 12:
			print "\n ", c12y2, "=", g12y2
			writeG = (space + c12y2 + equal + str(g12y2)+ line)
			arq.write(writeG)

		elif cla2 == 13:
			print "\n ", c13y2, "=", g13y2
			writeG = (space + c13y2 + equal + str(g13y2)+ line)
			arq.write(writeG)

		elif cla2 == 14:
			print "\n ", c14y2, "=", g14y2
			writeG = (space + c14y2 + equal + str(g14y2)+ line)
			arq.write(writeG)

		elif cla2 == 15:
			print "\n ", c15y2, "=", g15y2
			writeG = (space + c15y2 + equal + str(g15y2)+ line)
			arq.write(writeG)
	
		elif cla2 == 16:
			print "\n ", c16y2, "=", g16y2
			writeG = (space + c16y2 + equal + str(g16y2)+ line)
			arq.write(writeG)
		
		elif cla2 == 17:
			print "\n ", c17y2, "=", g17y2
			writeG = (space + c17y2 + equal + str(g17y2)+ line)
			arq.write(writeG)
	
		elif cla2 == 18:
			print "\n ", c18y2, "=", g18y2
			writeG = (space + c18y2 + equal + str(g18y2)+ line)
			arq.write(writeG)
		x = x + 1
	
	med = (g1y2 + g2y2 + g3y2 + g4y2 + g5y2 + g6y2 + g7y2 + g8y2 + g9y2 + g10y2 + g11y2 + g12y2 + g13y2 + g14y2 + g15y2 + g16y2 + g17y2 + g18y2) / cla2
	
	gpay2 = (gp1y2 + gp2y2 + gp3y2 + gp4y2 + gp5y2 + gp6y2 + gp7y2 + gp8y2 + gp9y2 + gp10y2 + gp11y2 + gp12y2 + gp13y2 + gp14y2 + gp15y2 + gp16y2 + gp17y2 + gp18y2) / cla2
	
	if idioma == 1:
		print "\n Average of the 2nd year: ", med
		print "\n It is your GPA score: ", gpay2
		enter = raw_input(" Press enter to continue ")
	elif idioma == 2:
		print "\n Essa e a media do seu 2do ano: ", med
		print "\n GPA score: ", gpay2
		enter = raw_input("Aperte enter para continuar ")
	elif idioma == 3:
		print "\n Este es tu promedio de 2do ano: ", med
		print "\n GPA score: ", gpay2
		enter = raw_input("Aplaste enter para seguir ")
		
if cyf3 == 3:
	if idioma == 1:
		scores = "Your score of the 3rd year in the scale is 0 - 10:"
		print "\n", scores
		arq.write(scores)
	elif idioma == 2:
		notas = "As notas do seu tercero ano na escala de 0 - 10:"
		print "\n", notas
		arq.write(notas)
	elif idioma == 3:
		calificaciones = "Tus calificaciones en tu tercer en la escala de 0 - 10 son:"
		print "\n", calificaciones
		arq.write(calificaciones)
		
	arq.write("\n")
	
	print "\n ", c1y3, "=", g1y3
	print "\n ", c2y3, "=", g2y3
	print "\n ", c3y3, "=", g3y3
	print "\n ", c4y3, "=", g4y3
	print "\n ", c5y3, "=", g5y3
	print "\n ", c6y3, "=", g6y3
	print "\n ", c7y3, "=", g7y3
	print "\n ", c8y3, "=", g8y3
	
	#Writing the scores on the archive
	writeG = (space + c1y3 + equal + str(g1y3)+ line)
	arq.write(writeG)
	writeG = (space + c2y3 + equal + str(g2y3)+ line)
	arq.write(writeG)
	writeG = (space + c3y3 + equal + str(g3y3)+ line)
	arq.write(writeG)
	writeG = (space + c4y3 + equal + str(g4y3)+ line)
	arq.write(writeG)
	writeG = (space + c5y3 + equal + str(g5y3)+ line)
	arq.write(writeG)
	writeG = (space + c6y3 + equal + str(g6y3)+ line)
	arq.write(writeG)
	writeG = (space + c7y3 + equal + str(g7y3)+ line)
	arq.write(writeG)
	writeG = (space + c8y3 + equal + str(g8y3)+ line)
	arq.write(writeG)

	y = 8
	x = 8
	while x < cla3:
		y = y + 1
		if y == 9:
			print "\n ", c9y3, "=", g9y3
			writeG = (space + c9y3 + equal + str(g9y3)+ line)
			arq.write(writeG)
	
		elif y == 10:
			print "\n ", c10y3, "=", g10y3
			writeG = (space + c10y3 + equal + str(g10y3)+ line)
			arq.write(writeG)
	
		elif y == 11:
			print "\n ", c11y3, "=", g11y3
			writeG = (space + c11y3 + equal + str(g11y3)+ line)
			arq.write(writeG)

		elif y == 12:
			print "\n ", c12y3, "=", g12y3
			writeG = (space + c12y3 + equal + str(g12y3)+ line)
			arq.write(writeG)

		elif y == 13:
			print "\n ", c13y3, "=", g13y3
			writeG = (space + c13y3 + equal + str(g13y3)+ line)
			arq.write(writeG)
	
		elif y == 14:
			print "\n ", c14y3, "=", g14y3
			writeG = (space + c14y3 + equal + str(g14y3)+ line)
			arq.write(writeG)

		elif y == 15:
			print "\n ", c15y3, "=", g15y3
			writeG = (space + c15y3 + equal + str(g15y3)+ line)
			arq.write(writeG)
	
		elif y == 16:
			print "\n ", c16y3, "=", g16y3
			writeG = (space + c16y3 + equal + str(g16y3)+ line)
			arq.write(writeG)
	
		elif y == 17:
			print "\n ", c17y3, "=", g17y3
			writeG = (space + c17y3 + equal + str(g17y3)+ line)
			arq.write(writeG)
	
		elif y == 18:
			print "\n ", c18y3, "=", g18y3
			writeG = (space + c18y3 + equal + str(g18y3)+ line)
			arq.write(writeG)
	
	med = (g1y3 + g2y3 + g3y3 + g4y3 + g5y3 + g6y3 + g7y3 + g8y3 + g9y3 + g10y3 + g11y3 + g12y3 + g13y3 + g14y3 + g15y3 + g16y3 + g17y3 + g18y3) / cla3
	
	gpay3 = (gp1y3 + gp2y3 + gp3y3 + gp4y3 + gp5y3 + gp6y3 + gp7y3 + gp8y3 + gp9y3 + gp10y3 + gp11y3 + gp12y3 + gp13y3 + gp14y3 + gp15y3 + gp16y3 + gp17y3 + gp18y3) / cla3
	
	if idioma == 1:
		print "\n Average of the 3rd year: ", med
		print "\n It is your GPA score: ", gpay3
		enter = raw_input(" Press enter to continue ")
	elif idioma == 2:
		print "\n Essa e a media do seu 3ro ano: ", med
		print "\n GPA score: ", gpay3
		enter = raw_input("Precione enter para continuar ")
	elif idioma == 3:
		print "\n Este es tu promedio de 3ro ano: ", med
		print "\n GPA score: ", gpay3
		enter = raw_input("Aplaste enter para seguir ")
		
if cyf4 == 4:
	if idioma == 1:
		scores = "Your score of the 4th year in the scale is 0 - 10:"
		print "\n", scores
		arq.write(scores)
	elif idioma == 2:
		notas = "As notas do seu quarto ano na escala de 0 - 10:"
		print "\n", notas
		arq.write(notas)
	elif idioma == 3:
		calificaciones = "Tus calificaciones en tu cuarto en la escala de 0 - 10 son:"
		print "\n", calificaciones
		arq.write(calificaciones)
		
	arq.write("\n")
	
	print "\n ", c1y4, "=", g1y4
	print "\n ", c2y4, "=", g2y4
	print "\n ", c3y4, "=", g3y4
	print "\n ", c4y4, "=", g4y4
	print "\n ", c5y4, "=", g5y4
	print "\n ", c6y4, "=", g6y4
	print "\n ", c7y4, "=", g7y4
	print "\n ", c8y4, "=", g8y4
	
	#Writing the scores on the archive
	writeG = (space + c1y4 + equal + str(g1y4)+ line)
	arq.write(writeG)
	writeG = (space + c2y4 + equal + str(g2y4)+ line)
	arq.write(writeG)
	writeG = (space + c3y4 + equal + str(g3y4)+ line)
	arq.write(writeG)
	writeG = (space + c4y4 + equal + str(g4y4)+ line)
	arq.write(writeG)
	writeG = (space + c5y4 + equal + str(g5y4)+ line)
	arq.write(writeG)
	writeG = (space + c6y4 + equal + str(g6y4)+ line)
	arq.write(writeG)
	writeG = (space + c7y4 + equal + str(g7y4)+ line)
	arq.write(writeG)
	writeG = (space + c8y4 + equal + str(g8y4)+ line)
	arq.write(writeG)

	y = 8
	x = 8
	while x < cla3:
		y = y + 1
		if y == 9:
			print "\n ", c9y4, "=", g9y4
			writeG = (space + c9y4 + equal + str(g9y4)+ line)
			arq.write(writeG)
	
		elif y == 10:
			print "\n ", c10y4, "=", g10y4
			writeG = (space + c10y4 + equal + str(g10y4)+ line)
			arq.write(writeG)
	
		elif y == 11:
			print "\n ", c11y4, "=", g11y4
			writeG = (space + c11y4 + equal + str(g11y4)+ line)
			arq.write(writeG)

		elif y == 12:
			print "\n ", c12y4, "=", g12y4
			writeG = (space + c12y4 + equal + str(g12y4)+ line)
			arq.write(writeG)

		elif y == 13:
			print "\n ", c13y4, "=", g13y4
			writeG = (space + c13y4 + equal + str(g13y4)+ line)
			arq.write(writeG)

		elif y == 14:
			print "\n ", c14y4, "=", g14y4
			writeG = (space + c13y4 + equal + str(g14y4)+ line)
			arq.write(writeG)

		elif y == 15:
			print "\n ", c15y4, "=", g15y4
			writeG = (space + c14y4 + equal + str(g15y4)+ line)
			arq.write(writeG)
	
		elif y == 16:
			print "\n ", c16y4, "=", g16y4
			writeG = (space + c16y4 + equal + str(g16y4)+ line)
			arq.write(writeG)
	
		elif y == 17:
			print "\n ", c17y4, "=", g17y4
			writeG = (space + c17y4 + equal + str(g17y4)+ line)
			arq.write(writeG)
	
		elif cla4 == 18:
			print "\n ", c18y4, "=", g18y4
			writeG = (space + c18y4 + equal + str(g18y4)+ line)
			arq.write(writeG)
			
	med = (g1y4 + g2y4 + g3y4 + g4y4 + g5y4 + g6y4 + g7y4 + g8y4 + g9y4 + g10y4 + g11y4 + g12y4 + g13y4 + g14y4 + g15y4 + g16y4 + g17y4 + g18y4) / cla4
	
	gpay4 = (gp1y4 + gp2y4 + gp3y4 + gp4y4 + gp5y4 + gp6y4 + gp7y4 + gp8y4 + gp9y4 + gp10y4 + gp11y4 + gp12y4 + gp13y4 + gp14y4 + gp15y4 + gp16y4 + gp17y4 + gp18y4) / cla4

	if idioma == 1:
		print "\n Average of the 4th year: ", med
		print "\n It is your GPA score: ", gpay4
		enter = raw_input(" Press enter to continue ")
	elif idioma == 2:
		print "\n Essa e a media do seu 4to ano: ", med
		print "\n GPA score: ", gpay4
		enter = raw_input("Precione enter para continuar ")
	elif idioma == 3:
		print "\n Este es tu promedio de 4to ano: ", med
		print "\n GPA score: ", gpay4
		enter = raw_input("Aplaste enter para seguir ")
	
if cyf5 == 5:
	if idioma == 1:
		scores = "Your score of the 5th year in the scale is 0 - 10:"
		print "\n", scores
		arq.write(scores)
	elif idioma == 2:
		notas = "As notas do seu quinto ano na escala de 0 - 10:"
		print "\n", notas
		arq.write(notas)
	elif idioma == 3:
		calificaciones = "Tus calificaciones en tu quinto en la escala de 0 - 10 son:"
		print "\n", calificaciones
		arq.write(calificaciones)
		
	arq.write("\n")
	
	print "\n ", c1y5, "=", g1y5
	print "\n ", c2y5, "=", g2y5
	print "\n ", c3y5, "=", g3y5
	print "\n ", c4y5, "=", g4y5
	print "\n ", c5y5, "=", g5y5
	print "\n ", c6y5, "=", g6y5
	print "\n ", c7y5, "=", g7y5
	print "\n ", c8y5, "=", g8y5
	
	#Writing the scores on the archive
	writeG = (space + c1y5 + equal + str(g1y5)+ line)
	arq.write(writeG)
	writeG = (space + c2y5 + equal + str(g2y5)+ line)
	arq.write(writeG)
	writeG = (space + c3y5 + equal + str(g3y5)+ line)
	arq.write(writeG)
	writeG = (space + c4y5 + equal + str(g4y5)+ line)
	arq.write(writeG)
	writeG = (space + c5y5 + equal + str(g5y5)+ line)
	arq.write(writeG)
	writeG = (space + c6y5 + equal + str(g6y5)+ line)
	arq.write(writeG)
	writeG = (space + c7y5 + equal + str(g7y5)+ line)
	arq.write(writeG)
	writeG = (space + c8y5 + equal + str(g8y5)+ line)
	arq.write(writeG)
	
	y = 8
	x = 8
	while x < cla3:
		y = y + 1
		
		if y == 9:
			print "\n ", c9y5, "=", g9y5
			writeG = (space + c9y5 + equal + str(g9y5)+ line)
			arq.write(writeG)
		
		elif y == 10:
			print "\n ", c10y5, "=", g10y5
			writeG = (space + c10y5 + equal + str(g10y5)+ line)
			arq.write(writeG)
		
		elif y == 11:
			print "\n ", c11y5, "=", g11y5
			writeG = (space + c11y5 + equal + str(g11y5)+ line)
			arq.write(writeG)

		elif y == 12:
			print "\n ", c12y5, "=", g12y5
			writeG = (space + c12y5 + equal + str(g12y5)+ line)
			arq.write(writeG)

		elif y == 13:
			print "\n ", c13y5, "=", g13y5
			writeG = (space + c13y5 + equal + str(g13y5)+ line)
			arq.write(writeG)

		elif y == 14:
			print "\n ", c14y5, "=", g14y5
			writeG = (space + c14y5 + equal + str(g14y5)+ line)
			arq.write(writeG)

		elif y == 15:
			print "\n ", c15y5, "=", g15y5
			writeG = (space + c15y5 + equal + str(g15y5)+ line)
			arq.write(writeG)
	
		elif y == 16:
			print "\n ", c16y5, "=", g16y5
			writeG = (space + c16y5 + equal + str(g16y5)+ line)
			arq.write(writeG)
	
		elif y == 17:
			print "\n ", c17y5, "=", g17y5
			writeG = (space + c17y5 + equal + str(g17y5)+ line)
			arq.write(writeG)
	
		elif y == 18:
			print "\n ", c18y5, "=", g18y5
			writeG = (space + c18y5 + equal + str(g18y5)+ line)
			arq.write(writeG)
		
	med = (g1y5 + g2y5 + g3y5 + g4y5 + g5y5 + g6y5 + g7y5 + g8y5 + g9y5 + g10y5 + g11y5 + g12y5 + g13y5 + g14y5 + g15y5 + g16y5 + g17y5 + g18y5) / cla5
		
	gpay5 = (gp1y5 + gp2y5 + gp3y5 + gp4y5 + gp5y5 + gp6y5 + gp7y5 + gp8y5 + gp9y5 + gp10y5 + gp11y5 + gp12y5 + gp13y5 + gp14y5 + gp15y5 + gp16y5 + gp17y5 + gp18y5) / cla5
	
	if idioma == 1:
		print "\n Average of the 5th year: ", med
		print "\n It is your GPA score: ", gpay5
		enter = raw_input(" Press enter to continue ")
	elif idioma == 2:
		print "\n Essa e a media do seu 5to ano: ", med
		print "\n GPA score: ", gpay5
		enter = raw_input("Aperte enter para continuar ")
	elif idioma == 3:
		print "\n Este es tu promedio de 5to ano: ", med
		print "\n GPA score: ", gpay5
		enter = raw_input("Aplaste enter para seguir ")

#Calculando o GPA geral
qgpa = (gpa + gpay2) / 2
if cyf3 == 3:
	qgpa = (gpa + gpay2 + gpay3) / 3
	if cyf4 == 4:
		qgpa = (gpa + gpay2 + gpay3 + gpay4) / 4
		if cyf5 == 5:
			qgpa = (gpa + gpay2 + gpay3 + gpay4 + gpay5) / 5

if idioma == 1:
	print "\n Your GPA score of the high-school:",qgpa 
elif idioma == 2:
	print "\n O GPA do seu ensino medio:", qgpa
elif idioma == 2:
	print "\n El GPA de tu bachillerato es:", qgpa

#Creating the archive wich all informations
GPA = str(qgpa)
arq.write("Your GPA: ")
arq.write(GPA)
arq.close()

qui = raw_input("\n If you want to leave press enter: ")
quit()
		