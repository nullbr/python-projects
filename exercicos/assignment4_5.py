def computepay():
    if h > 40:
		pay = r * 40 + (r * 1.5 *(h - 40))
    else:
        pay = r * h
    
    return pay

hrs = raw_input("Enter Hours: ")
h = float(hrs)
rate = raw_input("Enter Rate: ")
r = float(rate)

print computepay()