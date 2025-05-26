#for loop :
# For loop with list

# syntax
# for iterator in lst:
#     code goes here

numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5


# For loop with string
# syntax
# for iterator in string:
    # code goes here

language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])

for i in range(5):
    print("Hello", i)


# For loop with tuple
# syntax
# for iterator in tpl:
#     code goes here

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# For loop with dictionary Looping through a dictionary gives you the key of the dictionary.
  # syntax
# for iterator in dct:
#     code goes here

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out



# Loops in set
# syntax
# for iterator in st:
#     code goes here

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)


#break
# syntax
# for iterator in sequence:
#     code goes here
#     if condition:
#         break


numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break


#continue:
  # syntax
# for iterator in sequence:
#     code goes here
#     if condition:
#         continue


numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

#nested loop :
# syntax
# for x in y:
#     for t in x:
#         print(t)

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)

# example 2
for i in range(3):          # Outer loop
    for j in range(2):      # Inner loop
        print(i, j)


for i in range(1, 4):      # rows
    for j in range(1, 6):  # columns
        print("*", end=" ")
    print()  # new line after each row
