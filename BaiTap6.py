

def timso():

	t = range(10)

	for a in t[1:]:
		for b in t:
			for c in t:
				if (a*a*a + b*b*b + c*c*c == 100*a + 10 *b +c):
					print 100 * a + 10 *b +c



timso()
