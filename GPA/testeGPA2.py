t = 1
while t == 1:
	try:
		print "\n How many years do you have of the High-School? "
		years = raw_input(" Enter here: ")
		years = float(years)
		if years == 2:
			print "\n ", years, "years "
			t = 0
		elif years == 3:
			print "\n ", years, "years "
			t = 0
		elif years == 4:
			print "\n ", years, "years "
			t = 0
		elif years == 5:
			print "\n ", years, "years "
			t = 0
		else:
			print " Please enter a number between 2 and 5"
			t = 1
	
	except:
		print " Please enter a number between 2 and 5"
		t = 1