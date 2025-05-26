#check for prime number:
n = int(input("Enter a number:"))
for i in range(2 , n ):
    if(n %i) == 0:
        print("Number is not prime")
        break
else :
    print("number is prime")

#print sum of n natural no.
n = int(input("Enter the number :"))
i = 0 
sum = 0 
while(i<=n):
    sum += i
    i+=1
print(sum)

#factorial :
num = int(input("Enter number :"))
product =1 
for i in range(1 , n+1):
     product= product* i 
print("Factorial is :", product)


#pattern:
'''
     *
    ***
   *****
  *******
 *********
***********
'''
n = int(input("Enter the number :"))
for i in range(1  , n+1):
    print(" "* (n-i), end="") # 3-0 =3 space then 3-1 =2 spaces soo on for n=3
    print("*" * (2*i-1), end="") # odd number of stars 
    print("")

#pattern problem 2 :
'''
*
**
***
****
'''
n = int(input("Enter the number :"))
for i in range(1  , n+1): 
    print("*" * i, end="") # odd number of stars 
    print("")

#pattern 3 :
'''
***
* *
***
'''
n = int(input("Enter the number :"))
for i in range(1  , n+1): 
    if (i == 1 or i == n ):
        print("*" * n , end ="")
    else:
        print("*" , end ="")
        print(" " * (n-2), end ="")
        print("*" , end ="")
    print("")
