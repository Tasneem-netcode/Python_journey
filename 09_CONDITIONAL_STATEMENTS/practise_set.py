# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("Enter your age:"))
if age >= 18:
    print("You are old enough to drive , good luck!")
else:
     remaining_years = 18 - age 
     print("You need " , remaining_years, "more to learn driving , have pateince")
     


# print the greatest number among given 4 numbers:
a1 = int(input("Enter number 1:"))
a2 = int(input("Enter number 2:"))
a3 = int(input("Enter number 3:"))
a4 = int(input("Enter number 4:"))
if(a1 > a2 and a1 >a3 and a1>a4):
     print("a1 is greater : " , a1) 
elif(a2> a1 and a2 >a3 and a2>a4):
     print("a2 is greater : " , a2) 
elif(a3> a1 and a3 >a2 and a3>a4):
     print("a3 is greater : " , a3) 
elif(a4> a1 and a4 >a2 and a4>a3):
     print("a4 is greater : " , a4) 


# to check spam msg;
m1 = "Make a lot of money"
m2 = "buy now"
m3 = "subscribe to this channel"
m4 = "click this link"

msg = input("Enter your msg")
if((m1 in msg) or (m2 in msg) or (m3 in msg) or( m4 in msg)):
     print("This is a scam or spam msg , be aware ")
else:
     print("Not a spam or scam")
