#1.storing info of employees working in microsoft:
class Programmer:
    company = "Microsoft"
    def __init__(self, name , salary , pincode):
        self.name = name 
        self.salary = salary
        self .pincode = pincode

    def getinfo(self):
        print(f"Name:{self.name} , Salary: {self.salary} , Pincode: {self.pincode} , Company:{self.company}" )
  
p1 =Programmer("Harry" , 1200000, 78904)
p1.getinfo()


#2 . class for calculator to find square , cube:
class Calculator:
    def __init__(self, n):
        self.n =n 

    def square(self):
        print(f"Square is : {self.n * self.n}")
    def cube(self):
        print(f"Square is : {self.n * self.n * self.n}")
    def square_root(self):
        print(f"Square is : {self.n ** 1/2}")

a = Calculator(4)
a.square()
a.cube()
a.square_root()

#4.class attribute and instance attribute:
class Demo:
    a=4

o= Demo()
print(o.a)# Prints the class attribute beacuse instance attribute is not present 

o.a =0  # Instance attribute is set
print(o.a) # Print the instance attibute as its present 

print(Demo.a)

# finally we can say that class attribute never changes its just overwritten by instace attribute but main class attribute always stays
        
#5. Add a static method into this :
class Calculator:
    def __init__(self, n):
        self.n =n 

    def square(self):
        print(f"Square is : {self.n * self.n}")
    def cube(self):
        print(f"Square is : {self.n * self.n * self.n}")
    def square_root(self):
        print(f"Square is : {self.n ** 1/2}")

    @staticmethod
    def note():
        print("This is a static method that says thank you !")

a = Calculator(4)
Calculator.note()
a.square()
a.cube()
a.square_root()