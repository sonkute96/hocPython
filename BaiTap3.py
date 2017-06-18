
def kiemtraSNT(x):
	if x < 2:
		return 0
	elif x == 2:
		return 1
	else:
		t = range(x)
		for i in t[2:]:
			if x % i == 0:
				return 0

		return 1

def inraSNT(m):

	for i in range(m):

		if kiemtraSNT(i) == 1:
			print i

m = int(raw_input("nhap m >> "))

inraSNT(m)