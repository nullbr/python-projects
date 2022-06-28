try:
    inp = raw_input("enter the score grade: ")
    scr = float(inp)
    if scr < 0 or scr > 1 :
        print "error, please enter a score between 0 and 1"
    elif scr >= 0.9 and scr < 1.0:
        print "A"
        
    elif scr >= 0.8 and scr < 1.0:
        print "B"
        
    elif scr >= 0.7 and scr < 1.0:
		print "C"
    
    elif scr >= 0.6 and scr < 1.0:
        print "D"
    
    elif scr < 0.6:
        print "F"
	
	#else:
	#	print "error, please enter a score between 0 and 1"
except:
    print "error, please enter numeric input"