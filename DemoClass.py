class Human():
    def __init__(self, name,gender):
        self.name = name
        self.gender = gender
    def show_info(self):
        print "My name is %s" % self.name
        print "I'm %s" % self.gender
    def performed_math_operations(self, math_operation, *args):
        print "Tong so diem cua ban la : %d" % math_operation(*args)

def add (a,b,c):
    return a + b + c
son = Human("Pham Minh Son", "Male")
son.show_info()
son.performed_math_operations(add, 10, 15, 20)
