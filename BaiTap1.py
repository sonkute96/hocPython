
def TongTien(von,thang,laisuat):
	if laisuat<=0 or von <=0 or thang<=0:
		return
	else:
		for i in range(thang):
			von = von+ von*(laisuat/100)

		print von

von = float(raw_input("nhap von :"))

thang = int(raw_input("nhap so thang can gui :"))

laisuat = float(raw_input("nhap lai suat :"))

TongTien(von,thang,laisuat)