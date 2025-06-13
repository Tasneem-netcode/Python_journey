try :
    a = int(input("Hey , enter a number :"))
    print(a)
except Exception as e :
    print(e)

print("Thank you")

#exception doesnt mean error , but its the crash of code if something wrong happens then it will execute the message in except block acc to the exception , and the code run fine after that 



#raise an error in python code:
a =int(input("Enter a number:"))
b =int(input("Enter another number:"))

if(b == 0):
    raise ZeroDivisionError("Hey you cannot divide by zero")
else :
    print(f"The division a/b is {a/b}")
