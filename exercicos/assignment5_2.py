largest = -1
smallest = None

while True:
	try:
		nu = raw_input("Enter a number: ")
		num = int(nu)
		don = raw_input("done? ")
		if don == "done":
			break
			
		if num > largest: 
			largest = num
			print num
		
		if smallest is None:
			smallest = num
			print num
		elif num < smallest:
			smallest = num
			print num
	except:
		print "invalid input"

print "Maximum", largest
print "Minimum", smallest