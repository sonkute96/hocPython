#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

print ("Kiem tra so nguyen to :")

number = int(input("so nguyen n:"))

if number < 2:
    print ("so nhap vao phai lon hon 2")
    exit()
is_prime = True
for i in range(2, int(number /2 + 1)):
    if number % i == 0:
        is_prime = False;
        break
if is_prime:
    print("%d la so nguyen to" % number)
else:
    print ("%d khong fai la so nguyen to " %number)
