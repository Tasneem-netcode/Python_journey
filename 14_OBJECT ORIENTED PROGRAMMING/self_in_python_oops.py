class student:
  def set_details(self , name , age ):
    self.name = name 
    self.age = age 

  def show_details(self):
    print(f"My name is {self.name} and i am {self.age} years old")

#objects:
s1 = student()
s2 = student()
s3 = student()

#set details:
s1.set_details("Aman" , 17)
s2.set_details("ortha" , 19)
s3.set_details("neha" , 20)

s1.show_details()
s2.show_details()
s3.show_details()


# Behind the scenes:

# s1.set_details("Aman", 20)
# is actually doing this:


# Student.set_details(s1, "Aman", 20)
# So self = s1 here.


class Employee:
  language = "Python" # these are class attribute
  salary = 12006
  
  def getInfo(self):
    print(f"The language is {self.language}, salary is {self.salary}")


harry = Employee()
harry.language = "Javascript"#instance attribute has more preference 
harry.getInfo()#same
Employee.getInfo(harry) #same

