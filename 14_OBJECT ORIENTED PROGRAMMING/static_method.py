class Employee:
    language = "Python"
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}, salary is {self.salary}")
    
    @staticmethod #means its a function in class that dont require an object
    def greet():
        print("Good work!")

harry =Employee()
# harry.greet() #same
Employee.greet() #same can be called by only using class 
harry.getInfo()