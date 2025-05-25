# syntax
# if condition:
#     code
# elif condition:
#     code
# else:
#     code

a = int(input("Enter any number:"))
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')



marks = int(input("Enter marks :"))
if marks >= 90:
    print("Grade : A")
elif marks >= 75:
    print("Grade : B")
elif marks >= 60:
    print("Grade : c")
else:
    print("FAIL")
