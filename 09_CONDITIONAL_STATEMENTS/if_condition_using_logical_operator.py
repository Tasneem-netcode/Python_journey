#1. and:
# syntax
# if condition and condition:
#     code

a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')


age = 20
has_voter_id = True

if age >= 18 and has_voter_id:
    print("You can vote.")
else:
    print("You cannot vote.")


#2.or:
# syntax
# if condition or condition:
#     code

user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')

is_raining = False
has_umbrella = True

if is_raining or has_umbrella:
    print("You can go outside.")
else:
    print("Stay inside.")
