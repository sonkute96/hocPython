def TongTien(m1,m2,s):

	if s <=100:
		tong = m1 * s
	else:
		tong  = m1 * 100 + m2 * (s-100)


	print tong


m1 = float(raw_input("nhap gia m1 :"))

m2 = float(raw_input("nhap gia m2 :"))

s = int (raw_input("nhap so dien da dung :"))

TongTien(m1,m2,s)