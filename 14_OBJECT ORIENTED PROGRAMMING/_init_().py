class Employee:
    language = "Python"
    salary = 120000
#constructor or also called dunder method
    def __init__(self):
        print("Here i am creating an object and this function will be called automatically")


    def getInfo(self):
        print(f"The language is {self.language}, salary is {self.salary}")
    
    @staticmethod #means its a function in class that dont require an object
    def greet():
        print("Good work!")

harry =Employee()
harry.name = "Harry"
harry.getInfo()



#we can also pass parameters 
class Employee:
    language = "Python"
    salary = 120000
#constructor or also called dunder method
    def __init__(self , name , salary , language):
    # self allows to attach parameter to the class
        self.name =name
        self .salary = salary
        self.language = language
        print("Here i am creating an object and this function will be called automatically")


    def getInfo(self):
        print(f"The language is {self.language}, salary is {self.salary}")
    
    @staticmethod #means its a function in class that dont require an object
    def greet():
        print("Good work!")

harry =Employee("Harry" , 340000, "Javascript")
harry.getInfo()

#example 3:
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)