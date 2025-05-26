# 1. while loop:
  # syntax
# while condition:
#     code goes here

#example 1 :
i = 0 
while(i<=5):
    print(i)
    i+=1

#example 2 :
user_input = ""
while user_input != "stop":
    user_input = input("Type 'stop' to exit: ")

#example 3:
num = 1 
while(num<51):
    print(num)
    num +=1

    #example 5:
list_1 = [1 , "Harry" , False , "ik kudi" , "while" , 9.7]
length = len(list_1)
i = 0
while(i < length):
    print(list_1[i])
    i+=1

# while loop using else:
# syntax:

# while condition:
#     code goes here
# else:
    # code goes here

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print("count value is :",count)

# using break in while loop :
#example 1
i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1
print(i) #6

#example 2 :
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

# using continue in while loop :
  # syntax
# while condition:
#     code goes here
#     if another_condition:
#         continue
#example 1 :
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

#example 2 :
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
