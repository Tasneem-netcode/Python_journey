# import tkinter as tk
# import random

# # Generate the random number
# secret_number = random.randint(1, 100)
# attempts_left = 7

# # Function to handle guess
# def check_guess():
#     global attempts_left
#     try:
#         guess = int(entry.get())
#         result = ""

#         if guess < 1 or guess > 100:
#             result = "Enter a number between 1 and 100."
#         elif guess == secret_number:
#             result = f"🎉 You guessed it! The number was {secret_number}."
#             button.config(state="disabled")
#         elif guess < secret_number:
#             result = "Too low! Try again."
#         else:
#             result = "Too high! Try again."

#         attempts_left -= 1
#         if attempts_left == 0 and guess != secret_number:
#             result = f"😞 Game Over! The number was {secret_number}."
#             button.config(state="disabled")

#         result_label.config(text=result)
#         attempts_label.config(text=f"Attempts left: {attempts_left}")

#     except ValueError:
#         result_label.config(text="Please enter a valid number.")

# # Set up the main window
# root = tk.Tk()
# root.title("Number Guessing Game")
# root.geometry("300x250")

# # GUI Components
# tk.Label(root, text="Guess a number between 1 and 100").pack(pady=10)
# entry = tk.Entry(root)
# entry.pack(pady=5)

# button = tk.Button(root, text="Check", command=check_guess)
# button.pack(pady=5)

# result_label = tk.Label(root, text="")
# result_label.pack(pady=10)

# attempts_label = tk.Label(root, text=f"Attempts left: {attempts_left}")
# attempts_label.pack()

# # Run the GUI app
# root.mainloop()


import tkinter as tk
import random

# Generate the random number
secret_number = random.randint(1, 100)
attempts_left = 7

# Function to handle guess
def check_guess():
    global attempts_left
    try:
        guess = int(entry.get())
        result = ""

        if guess < 1 or guess > 100:
            result = "Enter a number between 1 and 100."
        elif guess == secret_number:
            result = f"🎉 You guessed it! The number was {secret_number}."
            button.config(state="disabled")
        elif guess < secret_number:
            result = "Too low! Try again."
        else:
            result = "Too high! Try again."

        attempts_left -= 1
        if attempts_left == 0 and guess != secret_number:
            result = f"😞 Game Over! The number was {secret_number}."
            button.config(state="disabled")

        result_label.config(text=result)
        attempts_label.config(text=f"Attempts left: {attempts_left}")

    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Set up the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x250")

# GUI Components
tk.Label(root, text="Guess a number between 1 and 100").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Check", command=check_guess)
button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

attempts_label = tk.Label(root, text=f"Attempts left: {attempts_left}")
attempts_label.pack()

# Run the GUI app
root.mainloop()
