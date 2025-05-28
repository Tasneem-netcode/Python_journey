# #find greatest :
# def greatest(a, b, c):
#     if(a>b and a>c):
#         return a 
#     elif(b>a and b>c):
#         return b 
#     else:
#         return c 
# a =1 
# b=3 
# c=7
# print("greatest number is ", greatest(a , b, c))

# #convert fahrenheit to celcius to   :
# # c/5 = (f-32)/9
# def ferh_to_celcius(f):
#     return 5*(f-32)/9


# f = int(input("Enter the value of fahrenheit:"))
# print(ferh_to_celcius(f))


#sum numbers till n using recursion
# def sum_till_n(n):
#     if(n == 0):
#         return 0
#     return n +sum_till_n(n-1)
# n = int(input("Enter n "))
# print("Sum of n numbers are:", sum_till_n(n))

# def pattern(n):
#     if(n==0):
#         return # to stop we can use return 
#     print("*" * n)
#     pattern(n-1)

# pattern(4)

def inch_to_cms(inch):
    return inch * 2.54
n = int(input("Enter value in inches:"))
print("Inch to cms is ", inch_to_cms(n))