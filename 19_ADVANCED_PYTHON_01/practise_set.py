try:
    with open("1.txt" , "r") as f :
        print(f.read())
except Exception as e :
    print(e)
try:
    with open("2.txt" , "r") as f :
        print(f.read())
except Exception as e :
    print(e)
try:   
    with open("3.txt" , "r") as f :
        print(f.read())
except Exception as e :
    print(e)       



l = [1, 2, 3, 4, 5, 6, 7, 8]
for index , ele in enumerate(l):
    if index == 2 or index== 4 or index == 6:
        print(ele)


n = int(input("Enter  a number :"))

table = [n * i for i in range(1,11)]
with open("table.txt", "w") as f:
    f.write(f"Table of {n} is {str(table)}\n ")
