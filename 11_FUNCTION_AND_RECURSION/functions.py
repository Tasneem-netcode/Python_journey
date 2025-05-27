# syntax
# Declaring a function
# def function_name():
#     codes
#     codes
# Calling a function
# function_name()

# example1:
# declare a function
def avg():
    a = int(input("Enter a number :"))
    b = int(input("Enter a number :"))
    c = int(input("Enter a number :"))

    average =(a+b+c) /3
    print(average)

#function call:
avg() # you can call this functio any number of times
avg()
avg()

#function to greet users:
user_name = input("Enter your name:")
def greet():
    print("Hello" , user_name , '!', "Welcome to python programming")

greet()

#types of functions :
#1 . Built-in functions :
print("Hello , you")
user_name = input("Enter name")
type(user_name)
len(user_name)


# 2. user_defined functions
def sayhello():
    print("Hello, you!")
sayhello()
