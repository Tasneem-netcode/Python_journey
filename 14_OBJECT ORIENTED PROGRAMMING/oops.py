class Person:
  pass
print(Person)
# ex 1:
class Employee:
  name = "Suvam"
  language = "Python"
  salary = 12006

object_name = Employee()
print(object_name.name , object_name.language)

#2 nd exaple:
class person:
  name = ""
  age = 0

  def greet(self):
    print(f"Hello my name is {self.name} and i am {self.age} years old")

#object creation :
person1 = person()
person1.name = "Alice"
person1.age = 25
person1.greet()

#ex 3:

class Employee:
  language = "Python" # these are class attribute
  salary = 12006

harry = Employee()
harry.name = "Harry" #here name is object attribute
print(harry.name, harry.language , harry .salary)
rohan = Employee()
rohan.name = "Rohan khan"
print(rohan.name , rohan.language , rohan .salary)