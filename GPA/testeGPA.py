print "\n How you want to put your score:"
print "\n Press 1 to use: A, B, C, D, F"
print " Press 2 to use: 0 - 10"
print " Press 3 to use: 0 - 100 \n"

i = 1
while i == 1:
	try:
		u = 1
		while u == 1:
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
				print " Please enter a number between 1 and 3"
				u = 1
		i = 0
			


		
	except:
		print " Please enter a number between 1 and 3"
		i = 1

i = 1		
while i == 1:		
	if opt == 1:		
		try:
			g = raw_input("\n what is your grade?")
			if g == "A" or g == "a":
				g = 9.5
				print g
				i = 0
			
			elif g == "B" or g == "b":
				g = 8.5
				print g
				i = 0
			elif g == "C" or g == "c":
				g = 7.5
				print g
				i = 0
			elif g == "D" or g == "d":
				g = 6.5
				print g
				i = 0
			elif g == "F" or g == "f":
				g = 5.5
				print g
				i = 0
			else:
				print " Please enter a valid score \n"
				i = 1
	
		except:
			print " Please enter a valid score \n"
			i = 1