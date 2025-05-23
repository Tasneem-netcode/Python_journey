#tuples in python:
#empty list:
empty_tuples =() 
empty_tuples=tuple()
print(len(empty_tuples))

a=(1,2,3,4,5)
print(type(a))

#single element tuple 
single_tuple=(10,)
print(type(single_tuple))

my_tuple =('item' , 'car' , 'house' , 'money')
print(len(my_tuple))

#accesing elements from tuple
print(my_tuple[1])
print(my_tuple[3])

#negative index
print(my_tuple[-1])
print(my_tuple[-3])

#slicing tuples
all_items = my_tuple[0:]
print(all_items)
all_items = my_tuple[1:3]
print(all_items)


#changing tuple to list
tpl = (1 , 2, 3, 4, 5, 6, 7, 8)
lst = list(tpl)
print(type(lst))
print(type(tpl))

print(lst)
print(tpl)

print('money' in my_tuple)
print('books' in my_tuple)

#joining tuples :
t1 = (12 , 67, 54, 89,22)
t2 = (23, 89, 34, 89, 12 )
t3 = t1+ t2 

print(t2.count(89))
print(t1.index(67))

