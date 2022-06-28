lsf = raw_input("number1: ")
lsf1 = int(lsf)
lsf = raw_input("number2: ")
lsf2 = int(lsf)
lsf = raw_input("number3: ")
lsf3 = int(lsf)
lsf = raw_input("number4: ")
lsf4 = int(lsf)

for lsf in lsf1, lsf2, lsf3, lsf4:
	if lsf < lsf1:
		lsf = lsf1
	elif lsf < lsf2:
		lsf = lsf2
	elif lsf < lsf3:
		lsf = lsf3
	elif lsf < lsf4:
		lsf = lsf4
	print lsf 
	
print lsf