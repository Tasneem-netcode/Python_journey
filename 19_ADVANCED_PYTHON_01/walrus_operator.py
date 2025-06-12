# syntax 
# variable := expression

while(data := input("Enter something:")) != "exit":
    print("You entered:", data)

if (n := len([1,2,3,4,5,6,7])) >3:
    print(F"List is too long {n} elements are present , expected <=3")