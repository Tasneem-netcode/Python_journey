# lambda arguments: expression

#squares of a number:
Square = lambda x : x *x 
print(Square(5))

#even or odd:
is_even = lambda x : x % 2 == 0
print(is_even(6))
print(is_even(3))

# 3. Find Maximum of Two Numbers
max = lambda a , b : a if a>b else b 
print(max(10 , 20))


#map():
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]


names = ['Anna', 'Hathway', 'ed', 'loren']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    


#filter():
numbers = [1 , 23, 12, 56, 34, 90, 80 , 44]
evens = list(filter(lambda x : x %2 == 0 , numbers))
print(evens)

numbers = [1 , 23, 12, 56, 34, 90, 80 , 44]
odds = list(filter(lambda x : x %2 != 0 , numbers))
print(odds)

#reduce():
from functools import reduce

nums =[1, 2, 3, 4]
product = reduce(lambda x , y : x*y , nums)
print(product)
'''
 What happened here?

Step 1: 1 × 2 = 2

Step 2: 2 × 3 = 6

Step 3: 6 × 4 = 24
'''

