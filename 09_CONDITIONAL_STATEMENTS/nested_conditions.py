num = 10

if num > 0:
    if num % 2 == 0:
        print("Positive even number")


a = int(input("Enter a number:"))
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
