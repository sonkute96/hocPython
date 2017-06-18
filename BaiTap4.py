
def USCLN(a,b):
	if a < 0:
		a = -a

	if b < 0:

		b = -b

	while (a != 0 and b != 0):
		if a >= b:

			a = a % b
		else:

			b = b % a

	return a + b

a = int(raw_input ("nhap tu so  >> "))

b = int (raw_input ("nhap mau so >> "))

USC = USCLN(a,b)

print "phan so ban dau la : %d / %d" % (a,b)

print "phan so sau khi toi gian : %d / %d" % (a/USC,b/USC)