#syntax :
# variable = input("enter value ")

name = input("Enter your name")
print("hello", name)


age= input("enter your age ")
print("you are ",age ,"years old ")

print(type(age)) #str 

# to take user input as int or float 
age2 = int(input("Enter age "))
print("you will be " , age2+1 , "years old next year ")
print(type(age2)) #int

num1 = int(input("enter number "))
num2 = int(input("enter number "))

avg = (num1 + num2) /2 
print(avg)

# sum = num1 + num2 
# avg = sum /2 
# print(avg)

#program to calculate square of a number 
number = int(input("enter number "))
sqr = number**2
print(sqr)

# program to check greater 
a = int(input("Enter a :"))
b = int(input("Enter b :"))
print("a is greater than b ?", a>b )


