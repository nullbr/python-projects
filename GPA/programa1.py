hrs = raw_input("Enter your hours: ")
rate = raw_input("Enter your rate per hours: ")
h = float(hrs)
r = float(rate)
pay = h * r

if r > 0 and h > 0:
	print pay
quit()