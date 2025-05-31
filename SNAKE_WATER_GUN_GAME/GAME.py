'''
1 for snake 
-1 for water
0 gor gun
'''
import random
computer = random.choice([-1 , 0, 1])
your_input= input("Enter your choice:")
game_dictionary = {'snake' : 1 , 'water' : -1 , 'gun' : 0}
reverseDict = {1 :"Snake", -1 : "Water" , 0 : "Gun"}

yourchoise = game_dictionary[your_input]

print(f"You choose {reverseDict[yourchoise]} \n Computer choose {reverseDict[computer]}")

if(computer == yourchoise):
    print("ITS A DRAW <>")
else:
  if(computer == -1 and yourchoise == 1):
    print("YOU WIN!")
  elif(computer == -1 and yourchoise == 0):
    print("YOU LOSE:(")
  elif(computer == 1 and yourchoise == -1):
    print("YOU LOSE:(")
  elif(computer == 1 and yourchoise == 0):
    print("YOU WIN!")
  elif(computer == 0 and yourchoise == -1):
    print("YOU WIN!")
  elif(computer == 1 and yourchoise == 0):
    print("YOU LOSE:(")
  else:
    print("Not valid, try again...")