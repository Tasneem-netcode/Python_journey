#empty set
st = set()
st = {'item1' , 'item2', 'item3' , 'item4'}
print(st)

fruits = {'avocado' ,'grapes' , 'berrys', 'mango'}
print(fruits)


#len()
print(len(st))
print(len(fruits))

#Checking an Item
print('mango' in fruits)
print('star' in fruits)

# Adding Items to a Set
# add()
st.add('item6')
print(st)

fruits.add('orange')
print(fruits)

#update()
st.update(['item5' , 'item7' , 'item8'])
print(st)

more_fruits = ('tomato' , 'lime' , 'leechi' , 'pine')
fruits.update(more_fruits)
print(fruits)

#removing items from set 
# .remove()
st.remove('item3')
print(st)

# .pop()
removed_item =fruits.pop()
print("removed item =" ,removed_item)

# Clearing Items in a Set
st.clear()
print(st) #set()

# Deleting a Set
del fruits
# print(fruits) #error

# Converting List to Set
# we can convert list to set and set to list 
lst = ['l1' , 'l2' , 'l3']
st = set(lst)
print(st) # the printed set order will be random beacuse set are generally unordered

skills= ['HTML' , 'css' , 'c++']
skills_set = set(skills)
print(skills_set)

#Joining Sets
# .union()
st1 = {'item1' , 'item2' , 'item3' , 'item4'}
st2 = {'item6' , 'item7' , 'item8' , 'item9'}

st3 = st1.union(st2) 
print(st3)
#.intersection()
a ={1 , 2, 3, 4}
b = {2 ,3 ,5 ,6}
c = a.intersection(b)
print(c)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}

#difference()
print(python.difference(dragon))
print(dragon.difference(python))

#Symmetric Difference :
print(python.symmetric_difference(dragon))

#isdisjoint()
python.isdisjoint(dragon)