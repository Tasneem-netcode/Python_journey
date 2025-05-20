#find length of a string
# len()
s="python"
print(len(s))

# check if a string ends with given string or not
# endswith() 
mystring= "code"
print(mystring.endswith("de")) #true
print(mystring.endswith("deq")) #false

# checks if a string starts with given string or not
#startswith()
mystring= "code"
print(mystring.startswith("c")) #true
print(mystring.startswith("ce")) #true

# to conver all string char into lowercase
str = "GOOD"
print(str.lower())

# to convert into uppercase
str2 = "ok"
print(str2.upper())

# to replace the substring
r = "I like C++"
print(r.replace("C++" , "python"))

#join list into string
words = ['hello' , 'python']
print(" ".join(words))

# breaks or split into list
string = "python , java, cpp , js"
print(string.split(","))

name =input("Enter name : ")
print(f"Good afternoon {name}")

letter = '''Dear name ,
You are selected!
Date '''

print(letter.replace("name" , "Harry").replace("Date" , "11 feb 2026"))

name = "Harry is a good  boy  "
print(name.find("  ")) #15

name = "Harry is a good  boy  "
print(name.replace("  " , " ")) #makes a new string but doesnt change the original one

print(name) #prints the original string and doent chane the original one as strings are immutable 

 


