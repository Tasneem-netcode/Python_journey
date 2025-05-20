 Python Lists: Complete Guide
Python lists are used to store multiple items in a single variable. Lists are ordered, changeable, and allow duplicates.

📌 Table of Contents
✅ What is a List?

📚 Syntax

🆓 Creating an Empty List

➕ Adding Items

🧺 Accessing Items

🛠️ List Methods

🔄 Looping Through a List

🔁 List Comprehension

💡 Uses of Lists

🧪 Practice Examples

✅ What is a List?
A list is a collection of items in a particular order.


my_list = [1, 2, 3, 4, 5]
Lists can store elements of any data type.

They are mutable (you can change them after creation).

📚 Syntax

list_name = [item1, item2, item3, ...]
Example:

fruits = ["apple", "banana", "cherry"]
🆓 Creating an Empty List

empty_list = []
# or
empty_list = list()
➕ Adding Items

my_list = []

# append - adds at end
my_list.append("Python")

# insert - adds at specific index
my_list.insert(0, "C++")

# extend - adds multiple items
my_list.extend(["Java", "JavaScript"])
🧺 Accessing Items

my_list = ["Python", "Java", "C++"]

print(my_list[0])    # Output: Python
print(my_list[-1])   # Output: C++
🛠️ List Methods
Method	Description
append()	Adds an element to the end
insert(index, x)	Inserts item at index
extend(iterable)	Adds multiple items
remove(x)	Removes first occurrence of x
pop([index])	Removes and returns item
clear()	Empties the list
index(x)	Returns index of first occurrence
count(x)	Counts occurrences of x
sort()	Sorts list in-place
reverse()	Reverses the list
copy()	Returns a shallow copy

🔄 Looping Through a List

languages = ["Python", "Java", "C++"]

for lang in languages:
    print(lang)
🔁 List Comprehension
A concise way to create lists.

squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
💡 Uses of Lists
Storing user inputs

Processing collections of items

Queues or stacks

Storing multiple return values

Implementing dynamic arrays

🧪 Practice Examples

# 1. Join two lists
a = [1, 2, 3]
b = [4, 5]
joined = a + b
print(joined)

# 2. Check if item exists
print(3 in a)

# 3. List slicing
print(a[0:2])  # [1, 2]

# 4. Nested lists
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # 3
📌 Summary:
Lists are mutable and flexible.

Can hold different data types.

Lots of built-in methods.

Powerful when used with loops and comprehensions.

