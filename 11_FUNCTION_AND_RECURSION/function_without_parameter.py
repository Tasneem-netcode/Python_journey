#full name:
def generate_full_name():
    first_name = "Anna"
    last_name ="Hathway"
    space = " "
    full_name=first_name + space +last_name
    print(full_name)
generate_full_name()

# add 3 numbers
def add_two_number():
    num_one = 2 
    num_two = 3 
    total = num_one +num_two
    print(total)
add_two_number()

#3. Display a Menu (useful in CLI apps)

def show_menu():
    print("----- MENU -----")
    print("1. Start")
    print("2. Settings")
    print("3. Exit")

show_menu()

#4. Print a Motivational Quote

def motivation():
    print("Keep going! You're doing great. 💪")

motivation()

# 5. Simple Loading Animation (concept)

import time

def loading():
    print("Loading", end="")
    for i in range(3):
        time.sleep(0.5)
        print(".", end="")
    print("\nDone!")

loading()

# 6. Print a Line Separator

def separator():
    print("-" * 40)

separator()
