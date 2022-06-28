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
g19 = 0
g20 = 0

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
gp19 = 0
gp20 = 0

y = 1
test = 0
year = 0
repeat = 0
yp = 0
suffix = 1
suffixC = 1

print "\n Welcome to the GPA calculator! \n"

while test == 0 or repeat < year:
	u = 1
	yp = yp + 1
	if year >= 2 and year <= 5:
		b = 0
	else:
		b = 1
	while b == 1:
		try:
			print "\n How many years do you have of the High-School? "
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
	
		except:
			print " Please enter a number between 2 and 5"
			b = 1
	
	t = 1
	while t == 1:
		try:
			if suffix == 1:
				suff = "st"
			elif suffix == 2:
				suff = "nd"
			elif suffix == 3:
				suff = "rd"
			elif suffix == 4:
				suff = "th"
			elif suffix == 5:
				suff = "th"
			ys = str(yp)
			print "\n How many classes do you have in your "+ ys + suff +" year? min 8 and max 20"
			qt = raw_input(" Enter here: ")
			cla = int(qt)
			x = cla
			yp = int(ys)
			if cla >= 8 and cla <= 20:
				t = 0
			else:
				print "\n Please, enter a number between 8 and 20 \n"
				t = 1
		
		except:
			print "\n Please, enter a number between 8 and 20 \n"
			t = 1
			
	if cla >= 8 and cla <= 20:
		print "\n How you want to put your score?"
		print "\n Press 1 to use: A, B, C, D, F"
		print " Press 2 to use: 0 - 10"
		print " Press 3 to use: 0 - 100 \n"
		
		while u == 1:
			try:
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
					
			except:
				print "\n Please enter a number between 1 and 3 \n"
				u = 1
		
		
		
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
				print "\n What is the name of your "+ num + suffC +" class?"
				c = raw_input(" Enter here: ")
				y = int(num)
				i = 1
				while i == 1:
					print " What is your grade in this class?"
					g = raw_input(" Enter here: ")
				
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
				print "\n What is the name of your "+ num + suffC +" class?"
				c = raw_input(" Enter here: ")
				y = int(num)
				i = 1
				while i == 1:
					try:
						print " What is your grade in this class?"
						gra = raw_input(" Enter here: ")
						g = float(gra)
						if g >= 0 and g <= 10:
							i = 0
						else:
							print "\n Please enter a number between 0 and 10 \n"
							i = 1
					except:
						print "\n Please enter a number between 0 and 10 \n"
						i = 1
							
			elif opt == 3:	
				num = str(y)
				print "\n What is the name of your "+ num + suffC +" class?"
				c = raw_input(" Enter here: ")
				y = int(num)
				i = 1
				while i == 1:
					try:
						print " What is your grade in this class?"
						gra = raw_input(" Enter here: ")
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
							print "\n Please enter a number between 0 and 100 \n"
							i = 1
					
					except:
						print "\n Please enter a number between 0 and 100 \n"
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
	
	
			elif cla == 19:
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
				
				elif y == 19:
					if yp == 1:
						c19 = c
						g19 = g
					elif yp == 2:
						c19y2 = c
						g19y2 = g
					elif yp == 3:
						c19y3 = c
						g19y3 = g
					elif yp == 4:
						c19y4 = c
						g19y4 = g
					elif yp == 5:
						c19y5 = c
						g19y5 = g
				
	
	
			elif cla == 20:
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
				
				elif y == 19:
					if yp == 1:
						c19 = c
						g19 = g
					elif yp == 2:
						c19y2 = c
						g19y2 = g
					elif yp == 3:
						c19y3 = c
						g19y3 = g
					elif yp == 4:
						c19y4 = c
						g19y4 = g
					elif yp == 5:
						c19y5 = c
						g19y5 = g
				
				elif y == 20:
					if yp == 1:
						c20 = c
						g20 = g
					elif yp == 2:
						c20y2 = c
						g20y2 = g
					elif yp == 3:
						c20y3 = c
						g20y3 = g
					elif yp == 4:
						c20y4 = c
						g20y4 = g
					elif yp == 5:
						c20y5 = c
						g20y5 = g
	
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
			
med = (g1 + g2 + g3 + g4 + g5 + g6 + g7 + g8 + g9 + g10 + g11 + g12 + g13 + g14 + g15 + g16 + g17 + g18 + g19 + g20) / cla 

print "\n Your score in the scale 0 - 10 is:"
print "\n ", c1, "=", g1
print "\n ", c2, "=", g2
print "\n ", c3, "=", g3
print "\n ", c4, "=", g4
print "\n ", c5, "=", g5
print "\n ", c6, "=", g6
print "\n ", c7, "=", g7
print "\n ", c8, "=", g8

if cla == 9:
	print "\n ", c9, "=", g9
	
elif cla == 10:	
	print "\n ", c9, "=", g9
	print "\n ", c10, "=", g10
	
elif cla == 11:
	print "\n ", c9, "=", g9
	print "\n ", c10, "=", g10
	print "\n ", c11, "=", g11

elif cla == 12:	
	print "\n ", c9, "=", g9
	print "\n ", c10, "=", g10
	print "\n ", c11, "=", g11
	print "\n ", c12, "=", g12

elif cla == 13:
	print "\n ", c9, "=", g9
	print "\n ", c10, "=", g10
	print "\n ", c11, "=", g11
	print "\n ", c12, "=", g12
	print "\n ", c13, "=", g13

elif cla == 14:
	print "\n ", c9, "=", g9
	print "\n ", c10, "=", g10
	print "\n ", c11, "=", g11
	print "\n ", c12, "=", g12
	print "\n ", c13, "=", g13
	print "\n ", c14, "=", g14

elif cla == 15:
	print "\n ", c9, "=", g9
	print "\n ", c10, "=", g10
	print "\n ", c11, "=", g11
	print "\n ", c12, "=", g12
	print "\n ", c13, "=", g13
	print "\n ", c14, "=", g14
	print "\n ", c15, "=", g15
	
elif cla == 16:
	print "\n ", c9, "=", g9
	print "\n ", c10, "=", g10
	print "\n ", c11, "=", g11
	print "\n ", c12, "=", g12
	print "\n ", c13, "=", g13
	print "\n ", c14, "=", g14
	print "\n ", c15, "=", g15
	print "\n ", c16, "=", g16
	
elif cla == 17:
	print "\n ", c9, "=", g9
	print "\n ", c10, "=", g10
	print "\n ", c11, "=", g11
	print "\n ", c12, "=", g12
	print "\n ", c13, "=", g13
	print "\n ", c14, "=", g14
	print "\n ", c15, "=", g15
	print "\n ", c16, "=", g16
	print "\n ", c17, "=", g17
	
elif cla == 18:
	print "\n ", c9, "=", g9
	print "\n ", c10, "=", g10
	print "\n ", c11, "=", g11
	print "\n ", c12, "=", g12
	print "\n ", c13, "=", g13
	print "\n ", c14, "=", g14
	print "\n ", c15, "=", g15
	print "\n ", c16, "=", g16
	print "\n ", c17, "=", g17
	print "\n ", c18, "=", g18
 	
elif cla == 19:
	print "\n ", c9, "=", g9
	print "\n ", c10, "=", g10
	print "\n ", c11, "=", g11
	print "\n ", c12, "=", g12
	print "\n ", c13, "=", g13
	print "\n ", c14, "=", g14
	print "\n ", c15, "=", g15
	print "\n ", c16, "=", g16
	print "\n ", c17, "=", g17
	print "\n ", c18, "=", g18
	print "\n ", c19, "=", g19
	
elif cla == 20:
	print "\n ", c9, "=", g9
	print "\n ", c10, "=", g10
	print "\n ", c11, "=", g11
	print "\n ", c12, "=", g12
	print "\n ", c13, "=", g13
	print "\n ", c14, "=", g14
	print "\n ", c15, "=", g15
	print "\n ", c16, "=", g16
	print "\n ", c17, "=", g17
	print "\n ", c18, "=", g18
	print "\n ", c19, "=", g19
	print "\n ", c20, "=", g20
	
	
print "\n Average: ", med

x = cla
y = 1
while x > 0:
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
		if g3 >= 9.3 and g3 <= 10:
			gp3 = 4.0
		elif g3 >=  9 and g3 <= 9.2:
			gp3 = 3.7
		elif g3 >=  8.7 and g3 <= 8.9:
			gp3 = 3.3
		elif g3 >=  8.3 and g3 <= 8.6:
			gp3 = 3.0
		elif g3 >=  8 and g3 <= 8.2:
			gp3 = 2.7
		elif g3 >=  7.7 and g3 <= 7.9:
			gp3 = 2.3
		elif g3 >=  7.3 and g3 <= 7.6:
			gp3 = 2.0
		elif g3 >=  7 and g3 <= 7.2:
			gp3 = 1.7
		elif g3 >=  6.7 and g3 <= 6.9:
			gp3 = 1.3
		elif g3 >=  6.3 and g3 <= 6.6:
			gp3 = 1.0
		elif g3 >=  6 and g3 <= 6.2:
			gp3 = .7
		elif g3 < 6:
			gp3 = 0
			
	elif y == 4:
		if g4 >= 9.3 and g4 <= 10:
			gp4 = 4.0
		elif g4 >=  9 and g4 <= 9.2:
			gp4 = 3.7
		elif g4 >=  8.7 and g4 <= 8.9:
			gp4 = 3.3
		elif g4 >=  8.3 and g4 <= 8.6:
			gp4 = 3.0
		elif g4 >=  8 and g4 <= 8.2:
			gp4 = 2.7
		elif g4 >=  7.7 and g4 <= 7.9:
			gp4 = 2.3
		elif g4 >=  7.3 and g4 <= 7.6:
			gp4 = 2.0
		elif g4 >=  7 and g4 <= 7.2:
			gp4 = 1.7
		elif g4 >=  6.7 and g4 <= 6.9:
			gp4 = 1.3
		elif g4 >=  6.3 and g4 <= 6.6:
			gp4 = 1.0
		elif g4 >=  6 and g4 <= 6.2:
			gp4 = .7
		elif g4 < 6:
			gp4 = 0
			
	elif y == 5:
		if g5 >= 9.3 and g5 <= 10:
			gp5 = 4.0
		elif g5 >=  9 and g5 <= 9.2:
			gp5 = 3.7
		elif g5 >=  8.7 and g5 <= 8.9:
			gp5 = 3.3
		elif g5 >=  8.3 and g5 <= 8.6:
			gp5 = 3.0
		elif g5 >=  8 and g5 <= 8.2:
			gp5 = 2.7
		elif g5 >=  7.7 and g5 <= 7.9:
			gp5 = 2.3
		elif g5 >=  7.3 and g5 <= 7.6:
			gp5 = 2.0
		elif g5 >=  7 and g5 <= 7.2:
			gp5 = 1.7
		elif g5 >=  6.7 and g5 <= 6.9:
			gp5 = 1.3
		elif g5 >=  6.3 and g5 <= 6.6:
			gp5 = 1.0
		elif g5 >=  6 and g5 <= 6.2:
			gp5 = .7
		elif g5 < 6:
			gp5 = 0
			
	elif y == 6:
		if g6 >= 9.3 and g6 <= 10:
			gp6 = 4.0
		elif g6 >=  9 and g6 <= 9.2:
			gp6 = 3.7
		elif g6 >=  8.7 and g6 <= 8.9:
			gp6 = 3.3
		elif g6 >=  8.3 and g6 <= 8.6:
			gp6 = 3.0
		elif g6 >=  8 and g6 <= 8.2:
			gp6 = 2.7
		elif g6 >=  7.7 and g6 <= 7.9:
			gp6 = 2.3
		elif g6 >=  7.3 and g6 <= 7.6:
			gp6 = 2.0
		elif g6 >=  7 and g6 <= 7.2:
			gp6 = 1.7
		elif g6 >=  6.7 and g6 <= 6.9:
			gp6 = 1.3
		elif g6 >=  6.3 and g6 <= 6.6:
			gp6 = 1.0
		elif g6 >=  6 and g6 <= 6.2:
			gp6 = .7
		elif g6 < 6:
			gp6 = 0
			
	elif y == 7:
		if g7 >= 9.3 and g7 <= 10:
			gp7 = 4.0
		elif g7 >=  9 and g7 <= 9.2:
			gp7 = 3.7
		elif g7 >=  8.7 and g7 <= 8.9:
			gp7 = 3.3
		elif g7 >=  8.3 and g7 <= 8.6:
			gp7 = 3.0
		elif g7 >=  8 and g7 <= 8.2:
			gp7 = 2.7
		elif g7 >=  7.7 and g7 <= 7.9:
			gp7 = 2.3
		elif g7 >=  7.3 and g7 <= 7.6:
			gp7 = 2.0
		elif g7 >=  7 and g7 <= 7.2:
			gp7 = 1.7
		elif g7 >=  6.7 and g7 <= 6.9:
			gp7 = 1.3
		elif g7 >=  6.3 and g7 <= 6.6:
			gp7 = 1.0
		elif g7 >=  6 and g7 <= 6.2:
			gp7 = .7
		elif g7 < 6:
			gp7 = 0
			
	elif y == 8:
		if g8 >= 9.3 and g8 <= 10:
			gp8 = 4.0
		elif g8 >=  9 and g8 <= 9.2:
			gp8 = 3.7
		elif g8 >=  8.7 and g8 <= 8.9:
			gp8 = 3.3
		elif g8 >=  8.3 and g8 <= 8.6:
			gp8 = 3.0
		elif g8 >=  8 and g8 <= 8.2:
			gp8 = 2.7
		elif g8 >=  7.7 and g8 <= 7.9:
			gp8 = 2.3
		elif g8 >=  7.3 and g8 <= 7.6:
			gp8 = 2.0
		elif g8 >=  7 and g8 <= 7.2:
			gp8 = 1.7
		elif g8 >=  6.7 and g8 <= 6.9:
			gp8 = 1.3
		elif g8 >=  6.3 and g8 <= 6.6:
			gp8 = 1.0
		elif g8 >=  6 and g8 <= 6.2:
			gp8 = .7
		elif g8 < 6:
			gp8 = 0
			
	elif y == 9:
		if g9 >= 9.3 and g9 <= 10:
			gp9 = 4.0
		elif g9 >=  9 and g9 <= 9.2:
			gp9 = 3.7
		elif g9 >=  8.7 and g9 <= 8.9:
			gp9 = 3.3
		elif g9 >=  8.3 and g9 <= 8.6:
			gp9 = 3.0
		elif g9 >=  8 and g9 <= 8.2:
			gp9 = 2.7
		elif g9 >=  7.7 and g9 <= 7.9:
			gp9 = 2.3
		elif g9 >=  7.3 and g9 <= 7.6:
			gp9 = 2.0
		elif g9 >=  7 and g9 <= 7.2:
			gp9 = 1.7
		elif g9 >=  6.7 and g9 <= 6.9:
			gp9 = 1.3
		elif g9 >=  6.3 and g9 <= 6.6:
			gp9 = 1.0
		elif g9 >=  6 and g9 <= 6.2:
			gp9 = .7
		elif g9 < 6:
			gp9 = 0
			
	elif y == 10:
		if g10 >= 9.3 and g10 <= 10:
			gp10 = 4.0
		elif g10 >=  9 and g10 <= 9.2:
			gp10 = 3.7
		elif g10 >=  8.7 and g10 <= 8.9:
			gp10 = 3.3
		elif g10 >=  8.3 and g10 <= 8.6:
			gp10 = 3.0
		elif g10 >=  8 and g10 <= 8.2:
			gp10 = 2.7
		elif g10 >=  7.7 and g10 <= 7.9:
			gp10 = 2.3
		elif g10 >=  7.3 and g10 <= 7.6:
			gp10 = 2.0
		elif g10 >=  7 and g10 <= 7.2:
			gp10 = 1.7
		elif g10 >=  6.7 and g10 <= 6.9:
			gp10 = 1.3
		elif g10 >=  6.3 and g10 <= 6.6:
			gp10 = 1.0
		elif g10 >=  6 and g10 <= 6.2:
			gp10 = .7
		elif g10 < 6:
			gp10 = 0
			
	elif y == 11:
		if g11 >= 9.3 and g11 <= 10:
			gp11 = 4.0
		elif g11 >=  9 and g11 <= 9.2:
			gp11 = 3.7
		elif g11 >=  8.7 and g11 <= 8.9:
			gp11 = 3.3
		elif g11 >=  8.3 and g11 <= 8.6:
			gp11 = 3.0
		elif g11 >=  8 and g11 <= 8.2:
			gp11 = 2.7
		elif g11 >=  7.7 and g11 <= 7.9:
			gp11 = 2.3
		elif g11 >=  7.3 and g11 <= 7.6:
			gp11 = 2.0
		elif g11 >=  7 and g11 <= 7.2:
			gp11 = 1.7
		elif g11 >=  6.7 and g11 <= 6.9:
			gp11 = 1.3
		elif g11 >=  6.3 and g11 <= 6.6:
			gp11 = 1.0
		elif g11 >=  6 and g11 <= 6.2:
			gp11 = .7
		elif g11 < 6:
			gp11 = 0
			
	elif y == 12:
		if g12 >= 9.3 and g12 <= 10:
			gp12 = 4.0
		elif g12 >=  9 and g12 <= 9.2:
			gp12 = 3.7
		elif g12 >=  8.7 and g12 <= 8.9:
			gp12 = 3.3
		elif g12 >=  8.3 and g12 <= 8.6:
			gp12 = 3.0
		elif g12 >=  8 and g12 <= 8.2:
			gp12 = 2.7
		elif g12 >=  7.7 and g12 <= 7.9:
			gp12 = 2.3
		elif g12 >=  7.3 and g12 <= 7.6:
			gp12 = 2.0
		elif g12 >=  7 and g12 <= 7.2:
			gp12 = 1.7
		elif g12 >=  6.7 and g12 <= 6.9:
			gp12 = 1.3
		elif g12 >=  6.3 and g12 <= 6.6:
			gp12 = 1.0
		elif g12 >=  6 and g12 <= 6.2:
			gp12 = .7
		elif g12 < 6:
			gp12 = 0
			
	elif y == 13:
		if g13 >= 9.3 and g13 <= 10:
			gp13 = 4.0
		elif g13 >=  9 and g13 <= 9.2:
			gp13 = 3.7
		elif g13 >=  8.7 and g13 <= 8.9:
			gp13 = 3.3
		elif g13 >=  8.3 and g13 <= 8.6:
			gp13 = 3.0
		elif g13 >=  8 and g13 <= 8.2:
			gp13 = 2.7
		elif g13 >=  7.7 and g13 <= 7.9:
			gp13 = 2.3
		elif g13 >=  7.3 and g13 <= 7.6:
			gp13 = 2.0
		elif g13 >=  7 and g13 <= 7.2:
			gp13 = 1.7
		elif g13 >=  6.7 and g13 <= 6.9:
			gp13 = 1.3
		elif g13 >=  6.3 and g13 <= 6.6:
			gp13 = 1.0
		elif g13 >=  6 and g13 <= 6.2:
			gp13 = .7
		elif g13 < 6:
			gp13 = 0
			
	elif y == 14:
		if g14 >= 9.3 and g14 <= 10:
			gp14 = 4.0
		elif g14 >=  9 and g14 <= 9.2:
			gp14 = 3.7
		elif g14 >=  8.7 and g14 <= 8.9:
			gp14 = 3.3
		elif g14 >=  8.3 and g14 <= 8.6:
			gp14 = 3.0
		elif g14 >=  8 and g14 <= 8.2:
			gp14 = 2.7
		elif g14 >=  7.7 and g14 <= 7.9:
			gp14 = 2.3
		elif g14 >=  7.3 and g14 <= 7.6:
			gp14 = 2.0
		elif g14 >=  7 and g14 <= 7.2:
			gp14 = 1.7
		elif g14 >=  6.7 and g14 <= 6.9:
			gp14 = 1.3
		elif g14 >=  6.3 and g14 <= 6.6:
			gp14 = 1.0
		elif g14 >=  6 and g14 <= 6.2:
			gp14 = .7
		elif g14 < 6:
			gp14 = 0
			
	elif y == 15:
		if g15 >= 9.3 and g15 <= 10:
			gp15 = 4.0
		elif g15 >=  9 and g15 <= 9.2:
			gp15 = 3.7
		elif g15 >=  8.7 and g15 <= 8.9:
			gp15 = 3.3
		elif g15 >=  8.3 and g15 <= 8.6:
			gp15 = 3.0
		elif g15 >=  8 and g15 <= 8.2:
			gp15 = 2.7
		elif g15 >=  7.7 and g15 <= 7.9:
			gp15 = 2.3
		elif g15 >=  7.3 and g15 <= 7.6:
			gp15 = 2.0
		elif g15 >=  7 and g15 <= 7.2:
			gp15 = 1.7
		elif g15 >=  6.7 and g15 <= 6.9:
			gp15 = 1.3
		elif g15 >=  6.3 and g15 <= 6.6:
			gp15 = 1.0
		elif g15 >=  6 and g15 <= 6.2:
			gp15 = .7
		elif g15 < 6:
			gp15 = 0
			
	elif y == 16:
		if g16 >= 9.3 and g16 <= 10:
			gp16 = 4.0
		elif g16 >=  9 and g16 <= 9.2:
			gp16 = 3.7
		elif g16 >=  8.7 and g16 <= 8.9:
			gp16 = 3.3
		elif g16 >=  8.3 and g16 <= 8.6:
			gp16 = 3.0
		elif g16 >=  8 and g16 <= 8.2:
			gp16 = 2.7
		elif g16 >=  7.7 and g16 <= 7.9:
			gp16 = 2.3
		elif g16 >=  7.3 and g16 <= 7.6:
			gp16 = 2.0
		elif g16 >=  7 and g16 <= 7.2:
			gp16 = 1.7
		elif g16 >=  6.7 and g16 <= 6.9:
			gp16 = 1.3
		elif g16 >=  6.3 and g16 <= 6.6:
			gp16 = 1.0
		elif g16 >=  6 and g16 <= 6.2:
			gp16 = .7
		elif g16 < 6:
			gp16 = 0
			
	elif y == 17:
		if g17 >= 9.3 and g17 <= 10:
			gp17 = 4.0
		elif g17 >=  9 and g17 <= 9.2:
			gp17 = 3.7
		elif g17 >=  8.7 and g17 <= 8.9:
			gp17 = 3.3
		elif g17 >=  8.3 and g17 <= 8.6:
			gp17 = 3.0
		elif g17 >=  8 and g17 <= 8.2:
			gp17 = 2.7
		elif g17 >=  7.7 and g17 <= 7.9:
			gp17 = 2.3
		elif g17 >=  7.3 and g17 <= 7.6:
			gp17 = 2.0
		elif g17 >=  7 and g17 <= 7.2:
			gp17 = 1.7
		elif g17 >=  6.7 and g17 <= 6.9:
			gp17 = 1.3
		elif g17 >=  6.3 and g17 <= 6.6:
			gp17 = 1.0
		elif g17 >=  6 and g17 <= 6.2:
			gp17 = .7
		elif g17 < 6:
			gp17 = 0
			
	elif y == 18:
		if g18 >= 9.3 and g18 <= 10:
			gp18 = 4.0
		elif g18 >=  9 and g18 <= 9.2:
			gp18 = 3.7
		elif g18 >=  8.7 and g18 <= 8.9:
			gp18 = 3.3
		elif g18 >=  8.3 and g18 <= 8.6:
			gp18 = 3.0
		elif g18 >=  8 and g18 <= 8.2:
			gp18 = 2.7
		elif g18 >=  7.7 and g18 <= 7.9:
			gp18 = 2.3
		elif g18 >=  7.3 and g18 <= 7.6:
			gp18 = 2.0
		elif g18 >=  7 and g18 <= 7.2:
			gp18 = 1.7
		elif g18 >=  6.7 and g18 <= 6.9:
			gp18 = 1.3
		elif g18 >=  6.3 and g18 <= 6.6:
			gp18 = 1.0
		elif g18 >=  6 and g18 <= 6.2:
			gp18 = .7
		elif g18 < 6:
			gp18 = 0
			
	elif y == 19:
		if g19 >= 9.3 and g19 <= 10:
			gp19 = 4.0
		elif g19 >=  9 and g19 <= 9.2:
			gp19 = 3.7
		elif g19 >=  8.7 and g19 <= 8.9:
			gp19 = 3.3
		elif g19 >=  8.3 and g19 <= 8.6:
			gp19 = 3.0
		elif g19 >=  8 and g19 <= 8.2:
			gp19 = 2.7
		elif g19 >=  7.7 and g19 <= 7.9:
			gp19 = 2.3
		elif g19 >=  7.3 and g19 <= 7.6:
			gp19 = 2.0
		elif g19 >=  7 and g19 <= 7.2:
			gp19 = 1.7
		elif g19 >=  6.7 and g19 <= 6.9:
			gp19 = 1.3
		elif g19 >=  6.3 and g19 <= 6.6:
			gp19 = 1.0
		elif g19 >=  6 and g19 <= 6.2:
			gp19 = .7
		elif g19 < 6:
			gp19 = 0
			
	elif y == 20:
		if g20 >= 9.3 and g20 <= 10:
			gp20 = 4.0
		elif g20 >=  9 and g20 <= 9.2:
			gp20 = 3.7
		elif g20 >=  8.7 and g20 <= 8.9:
			gp20 = 3.3
		elif g20 >=  8.3 and g20 <= 8.6:
			gp20 = 3.0
		elif g20 >=  8 and g20 <= 8.2:
			gp20 = 2.7
		elif g20 >=  7.7 and g20 <= 7.9:
			gp20 = 2.3
		elif g20 >=  7.3 and g20 <= 7.6:
			gp20 = 2.0
		elif g20 >=  7 and g20 <= 7.2:
			gp20 = 1.7
		elif g20 >=  6.7 and g20 <= 6.9:
			gp20 = 1.3
		elif g20 >=  6.3 and g20 <= 6.6:
			gp20 = 1.0
		elif g20 >=  6 and g20 <= 6.2:
			gp20 = .7
		elif g20 < 6:
			gp20 = 0
			
	y = y + 1
	x = x - 1

gpa = (gp1 + gp2 + gp3 + gp4 + gp5 + gp6 + gp7 + gp8 + gp9 + gp10 + gp11 + gp12 + gp13 + gp14 + gp15 + gp16 + gp17 + gp18 + gp19 + gp20) / cla

print "\n It is your GPA score: ", gpa

qui = raw_input("\n If you want to leave press enter: ")
quit()
		