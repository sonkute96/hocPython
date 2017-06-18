#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
database = {}
def menu():

    print ("-------------------------")
    print ("----MENU TU DIEN --------")
    print ("1. Them tu  ")
    print ("2. Tim tu ")
    print ("3. Xoa tu ")
    print ("4. Xem tat ca ")
    print ("5. Out chuong trinh")
    print ("-------------------------")

def add():
    word = input("nhap vao mot tu moi:")
    mean = input("nghia cua no la:")
    database[word] = mean
    print ("tu moi da duoc them")
def find():
    word = input("nhap vao mot tu can tim :")
    if word in database:
        print("tim thay")
    else:
        print ("khong tim thay")
def delete():
    word = input ("nhap vao tu can xoa :")
    if word in database:
        del database[word]
        print ("tim da bi xoa")
    else:
        print ("khong tim thay tu can xoa")
def viewAll():
    print ("tat ca danh sach :",database)
# hien thi menu
menu()

choice = int(input("Lua chon cua ban :"))

while choice != 0:
    if choice == 1:
        # them tu
        add()
    elif choice == 2:
        # tim tu
        find()
    elif choice == 3:
        # xoa tu
        delete()
    elif choice == 4:
        viewAll()
    else:
        exit()
    choice = int (input ("lua chon cua ban :"))
