x = 1
while x == 1:
	try:	
		print ""
		inp1 = raw_input("enter this year: ")
		year1 = int(inp1)
		print ""
		inp2 = raw_input("enter year of you birth: ")
		year2 = int(inp2)
		print " "
		age = year1 - year2
		if age < 18:
			ida = str(age)
			print "you can't drink, you have " + ida + " years old"
			print " "
		else:
			ida = str(age)
			print "you can drink, you have " + ida + " years old"
			print " "
	except:
		print " "
		print "error, please enter numeric input"
		print " "
		
		try:
			print ""
			inp1 = raw_input("enter this year: ")
			year1 = int(inp1)
			print ""
			inp2 = raw_input("enter year of you birth: ")
			year2 = int(inp2)
			print " "
			age = year1 - year2
			if age < 18:
				ida = str(age)
				print "you can't drink, you have " + ida + " years old"
				print " "
			else:
				ida = str(age)
				print "you can drink, you have " + ida + " years old"
				print " "
			
			
		except:
			quit()
		
	try:
		y = raw_input("if you want to try again enter 1, or if you wont enter 0: ")
		x = int(y)
		if x < 1:
			print "Finis"
			print " "
	except:
		print " "
		print "error, please enter numeric input"
		print " "	
		quit()