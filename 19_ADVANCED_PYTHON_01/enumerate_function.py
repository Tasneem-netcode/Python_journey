fruits = ["apple", "banana", "avo"]
for index , fruit in enumerate(fruits):
    print(index , fruit)



list = [1,5,3,7,4]
for index , ele in enumerate(list):
    print(index , ele)



#  Start from a Custom Index:
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


#quick practise qn :
names = ["Tasneem", "Sara", "Ali"]

for i, name in enumerate(names, start=100):
    print(f"{i}: {name}")
