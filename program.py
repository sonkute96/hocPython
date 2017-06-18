#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3

database = {
    'home': 'ngoi nha',
    'baby': 'em be'
}
def show_menu():
    print ("--------------------")
    print ("CHUONG TRINH TU DIEN")
    print ("--------------------")
    print ("1. Them tu")
    print ("2. Tim tu")
    print ("3. Xoa tu")
    print ("4. Xem tat ca")
    print ("An 0 de thoat chuong trinh")
    print ("----------------------------")

def add():
    word = input("tu moi :")
    mean = input("nghia la:")
    database[word] = mean
    print ("+ tu moi da duoc them")
def find():
    word = input("tu can tim:")
    if word in database:
        print("tim thay [%s : %s]" %(word, database[word]))
    else:
        print ("khong tim thay tu [%s]" % word)
def delete():
    word = input("tu can xoa :")
    if word in database:
        del database[word]
        print ("xoa thanh cong")
    else:
        print ("Tu can xoa ko tim thay")
def viewAll():
    for word, mean in database.items():
        print ("[%s : %s]"%(word,mean))
#hien thi menu
show_menu()

# chuong trinh chinh

choice = int(input("Your choice :"))

while choice != 0:
    if choice == 0:
        break
    elif choice == 1:
        # them tu
        add()
    elif choice == 2:
        # tim tu
        find()
    elif choice == 3:
        # xoa tu
        delete()
    elif choice == 4:
        # xem tat ca
        viewAll()
    else:
        print ("khong co lua chon nay")

    choice = int(input("Your choice :"))
print ("bye bye")
