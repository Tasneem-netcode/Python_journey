# import os 

# directory =  os.getcwd()
# contents = os.listdir(directory)

# print(f"Contents of directory '{directory}':")
# for item in contents:
#     print(item)

import os

# Replace with any directory you want to explore
directory = "/PYTHON"

try:
    contents = os.listdir(directory)
    print(f"Contents of '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("Directory not found.")
except PermissionError:
    print("You don't have permission to access this directory.")
