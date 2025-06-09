try :
    a =int(input("Enter a number:"))
    b =int(input("Enter a number:"))

    print(a / b)
except ZeroDivisionError:
    print("You cant divide by 0")

except ValueError:
    print("Please enter only numbers")

#  else and finally

# else
try:
    x =10/2
except ZeroDivisionError:
    print("Error!")

else:
    print("Sucess!")

#finally:

try:
    file = open("data.txt")

except FileNotFoundError:
    print("File is missing!")
finally:
    print("Done trying!")

# Catching All Exceptions
try:
    #risky code
    a =12/0
except Exception as e :
    print("Something went wrong " , e)

#example 2:
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)
except Exception as e:
    print("Something went wrong:", e)
    print(type(e))       # Shows the error type
    print(str(e))        # Shows the error message




# Raising Your Own Errors
age = int(input("Enter age:"))
if age <0:
    raise ValueError("Age cannot be negative!") #Use raise to manually throw exceptions when something's wrong.


