# f =open("demo.txt")
# content =f.read()
# if("twinkle" in content):
#     print(" Word Twinkle is present   in this content ")
# else:
#     print("Not present")
# f.close()


#2nd ques:
# import random

# def game():
#     print("You are playing the game...")
#     score= random.randint(1 , 80)
#     #fetch the hiscore:
#     with open("hiscore.txt") as f :
#         hiscore = f.read()
#         if(hiscore != ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0 
#     print(f"Your score is :{score}")
#     if(score > hiscore):
#         #write this hiscore to file
#         with open("hiscore.txt", "w") as f:
#             f.write(str(score))

#     return score
# game()

#3rd ques:
# def generateTables(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n}X{i}= {n*i}\n"
    
#     with open(f"tables/table_{n}", "w") as f:
#         f.write(table)

# for i in range(2 , 21):
#     generateTables(i)

#4th ques
# words = ["pillow" , "curtains", "bed"]
# with open("demo2.txt" , "r") as f :
#     content = f.read()
# for word in words:
#     NEWcontent = content.replace(word , "#" *len(word))

# with open("demo2.txt" , "w") as f:
#     f.write(NEWcontent)

#5 th ques
with open('log.html') as f:
    lines = f.readlines() #each line will be stored in form of list into lines

lineno = 1 
for line in lines:
    if("python" in line):
        print(f"Yes python is present in line {lineno}")
        break
    lineno +=1

else:
    print("Python not present")