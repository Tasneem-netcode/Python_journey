#make a dictionary for hindi and english words meaning:
words= {
    'madad' : 'help',
    'chasma': 'glasses',
    'billi' : 'cat'
}

word = input("Enter the word you are searching meaning for:")
print(words[word])

# #write a program to input eight numbers from user and display all unique numbers(once)
sets= set()
n=int(input("Enter number :"))
sets.add(n)
n=int(input("Enter number :"))
sets.add(n)
n=int(input("Enter number :"))
sets.add(n)
n=int(input("Enter number :"))
sets.add(n)
n=int(input("Enter number :"))
sets.add(n)
n=int(input("Enter number :"))
sets.add(n)
n=int(input("Enter number :"))
sets.add(n)
n=int(input("Enter number :"))
sets.add(n)

print(sets)

#set can have both  int 18 and string'18;
set2 = set()
set2.add(18)
set2.add("18")
print(set2) 

set3 = set()
set3.add(20)
set3.add(20.0) # will not be included as 20 == 20.0
set3.add("20")
print(set3)
print(len(set3)) 

d={}
name = input("Enter friend name:")
fav_lang = input("Enter fav coding language:")
d.update({name: fav_lang})
name = input("Enter friend name:")
fav_lang = input("Enter fav coding language:")
d.update({name: fav_lang})
name = input("Enter friend name:")
fav_lang = input("Enter fav coding language:")
d.update({name: fav_lang})
name = input("Enter friend name:")
fav_lang = input("Enter fav coding language:")
d.update({name: fav_lang})
print(d)