import os
print("Working directory:", os.getcwd())

f = open("examplefile.txt", "r")
data = f.read()
print(data)
f.close()

st= "Hey this is one more file to write"
f =open("myfile.txt", "w")
f.write(st)
f.close()

f =open("myfile.txt", "w")
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
f.close()