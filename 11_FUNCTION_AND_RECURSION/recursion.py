'''
factorial(0) =1
factorial(1) =1
factorial(2) =2 X 1
factorial(3) =3 X 2 X 1
factorial(4) =4 X 3 X 2 X 1
factorial(5) =5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X n-2 ........X3 X 2 X1 
factorial(n) = n X factorial(n-1)
factorial(n-1) = n-1  X factorial(n-2 ) ......

'''

def factorial(n):
    if( n ==1 or n==0): #base case
        return 1 
    return n * factorial(n-1)
n= int(input("Enter a number:"))
print("The factorial is ", factorial(n))