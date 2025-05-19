# 🐍 Python String Basics

This repository contains beginner-friendly Python programs that cover all the important concepts of strings, including:

- String creation and input
- String slicing
- Common string functions
- Practice problems 
 
 
 What is a String in Python?
In Python, a string is a sequence of characters enclosed in quotes. It’s used to store textual data, like names, messages, or any combination of letters, numbers, and symbols.

✅ Examples of Strings:
python:

name = "Ayaan"
greeting = 'Hello'
sentence = "I love Python!"
You can use:

Double quotes: "Hello"

Single quotes: 'Hello'

Triple quotes for multi-line strings: '''Hello''' or """Hello"""

🔹 String Type:

x = "Python"
print(type(x))
Output: <class 'str'>


🔸 Strings are Immutable
You cannot change characters in a string directly.

word = "hello"
# word[0] = "y"  ❌ This will cause an error
Instead, you create a new string:


word = "hello"
word = "y" + word[1:]  # "yello"

🔹 Common String Operations:

s = "Python"

print(len(s))        # Length of string → 6
print(s.upper())     # "PYTHON"
print(s.lower())     # "python"
print(s[0])          # 'P' (access first character)
print(s[-1])         # 'n' (last character)
print("th" in s)     # True (checks if 'th' is in string)

