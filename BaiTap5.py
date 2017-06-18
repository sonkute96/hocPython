

def count(m):

	if m <0:
		m = -m
	dem  = 0
	tong = 0
	while (m != 0):
		tong += m % 10
		dem +=1
		m = m /10

	print "tong : %d" %(tong)

	print "so luong chu so : %d " % (dem)

m = int (raw_input("nhap m :"))

count(m)

