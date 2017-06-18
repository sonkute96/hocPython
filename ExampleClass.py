class Animal(object):
    pass
class Dog(Animal):
    def __init__(self,name):
        self.name = name
class Cat(Animal):
    def __init__(self,name):
        self.name = name
class Person(object):
    def __init__(self,name):
        self.name = name

        self.pet = None

class Employee(Person):
    def __init__(self,name,salary):
        super(Employee,self).__init__(name)

        self.salary = salary
class Fish(object):
    pass
class Salmon(Fish):
    pass
class Halibut(Fish):
    pass

bull = Dog("Bull")
pms = Employee("Pham Minh Son",12000)


print pms.name

print pms.salary
pms.pet = bull.name
print pms.pet
