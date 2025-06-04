# Base class
class Employee:
    company1 = "ITC"
    def show(self):
        print(f"The name of employee is {self.name}, salary if {self.salary}")

#Inplace of doing this we inherit the base class
# class Programmer:
#     company = "ITC INFO TECH "
#     def show(self):
#         print(f"The name of employee is {self.name}, salary if {self.salary}")

#     def show_language(self):
#         print(f"The name is {self.name}, language is {self.language}, salary is :{self.salary} ")

#inherit: Derived class 
class Programmer(Employee):
    company = "ITC INFO TECH "
    def show_language(self):
        print(f"The name is {self.name}, language is {self.language}, salary is :{self.salary} ")

#objects:
a= Employee()#base class obj
b = Programmer()#derived class obj
print(b.company)
print(b.company1) #can print attributes of base class also


#single inheritance:
class A:
    def display(self):
        print("A class")

class B(A):
    def show(self):
        print("B class")

b = B()
b.display()
b.show()


#multiple inheritance:
# Base class
class Employee:
    company1 = "ITC"
    name = "Emp1"
    def show1(self):
        print(f"The name of employee is {self.name}, {self.company1}")

#another base class:
class Coder:
    language = "PYTHON"
    def printLanguage(self):
        print(f"Out of all languages your language is {self. language}")


#inherit: Derived class 
class Programmer(Employee , Coder):
    company = "ITC INFO TECH "
    def show_language(self):
        print(f"The company name is {self.company}, language is {self.language} ")

#objects:
a= Employee()#base class obj
b = Programmer()#derived class obj
print(b.company)
print(b.company1) #can print attributes of base class also

b.show1()
b.show_language()
b.printLanguage()
b.language = "JAVASCRIPT"
b.printLanguage()

c= Coder()
print(c.language)

#Multilevel inheritance:
class A:
    def method1(self):
        print("Class A")

class B(A):
    def method2(self):
        print("Class B")

class C(B):
    def method3(self):
        print("Class C")

obj = C()
obj.method1()
obj.method2()
obj.method3()

# example 2:
class Employee:
    a= 1 

class Programmer(Employee):
    b= 2 

class Manager(Programmer):
    c =3 

o =Employee()
print(o.a) #prints hte a attribute
# print(o.b) #shows error

o = Programmer()
print(o.a , o.b)

o = Manager()
print(o.a , o.b , o.c)