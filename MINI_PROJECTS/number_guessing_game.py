import random
n = random.randint(1 , 100)
your_given_num = -1 
guesses = 0 
while(your_given_num != n):
    your_given_num = int(input("Guess the number! :"))
    if(your_given_num > n ):
        print("Choose a lower number")
        guesses +=1
    elif(your_given_num < n ):
        print("Choose higher number ...")
        guesses +=1
print("Yes, you guessed it right!")
print(f"Total number of guesses are {guesses} ")
        