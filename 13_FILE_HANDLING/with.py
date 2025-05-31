f = open("myfile.txt")
print(f.read())
f.close()

#insted of closing files all the time we can use with 
with open("myfile.txt") as f:
    print(f.read())