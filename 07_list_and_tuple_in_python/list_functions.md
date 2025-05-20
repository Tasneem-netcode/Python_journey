📘 list_functions.md – All Important Python List Functions
Python lists are versatile, and Python provides several built-in methods to manipulate them effectively. Below is a detailed reference of all important list functions with meaningful examples.

📑 Table of Contents
append()

extend()

insert()

remove()

pop()

clear()

index()

count()

sort()

reverse()

copy()

len()

in keyword

Looping Techniques

🔹 append()
Definition: Adds a single item to the end of the list.

skills = ["Python", "SQL"]
skills.append("Git")
print(skills)
📤 Output:

['Python', 'SQL', 'Git']
🔹 extend()
Definition: Adds all elements from another iterable (like another list).

projects = ["Portfolio", "E-Commerce"]
more_projects = ["Chat App", "Blog"]
projects.extend(more_projects)
print(projects)
📤 Output:

['Portfolio', 'E-Commerce', 'Chat App', 'Blog']
🔹 insert()
Definition: Inserts an item at a specific index.


languages = ["C++", "Python", "JavaScript"]
languages.insert(1, "Java")
print(languages)
📤 Output:

['C++', 'Java', 'Python', 'JavaScript']
🔹 remove()
Definition: Removes the first occurrence of a value.

tools = ["Git", "VS Code", "Git", "Jupyter"]
tools.remove("Git")
print(tools)
📤 Output:

['VS Code', 'Git', 'Jupyter']
🔹 pop()
Definition: Removes and returns the item at the given index. Default is the last item.

certificates = ["AWS", "Azure", "GCP"]
certificates.pop()
print(certificates)
📤 Output:


['AWS', 'Azure']
🔹 clear()
Definition: Removes all items from the list.

todo = ["Submit assignment", "Read book"]
todo.clear()
print(todo)
📤 Output:

[]
🔹 index()
Definition: Returns the index of the first matching value.

skills = ["Python", "Java", "C++", "Python"]
position = skills.index("Python")
print(position)
📤 Output:

0
🔹 count()
Definition: Counts the number of times a value appears.

languages = ["Python", "Python", "Java"]
print(languages.count("Python"))
📤 Output:


2
🔹 sort()
Definition: Sorts the list in ascending order (or descending with reverse=True).

marks = [85, 72, 90, 60]
marks.sort()
print(marks)
📤 Output:


[60, 72, 85, 90]
🔁 Descending order:


marks.sort(reverse=True)
🔹 reverse()
Definition: Reverses the list in-place.

tasks = ["Deploy", "Test", "Build"]
tasks.reverse()
print(tasks)
📤 Output:


['Build', 'Test', 'Deploy']
🔹 copy()
Definition: Returns a shallow copy of the list.


original = ["HTML", "CSS"]
duplicate = original.copy()
print(duplicate)
📤 Output:

['HTML', 'CSS']
🔹 len()
Definition: Returns the number of items in the list.


courses = ["Python", "DSA", "AI"]
print(len(courses))
📤 Output:

3
🔹 in Keyword
Definition: Checks if an item exists in the list.

tools = ["VS Code", "PyCharm"]
print("VS Code" in tools)
📤 Output:

True
🔁 Looping Techniques

skills = ["Python", "C++", "Java"]

# Using for loop
for skill in skills:
    print(skill)

# Using enumerate
for i, skill in enumerate(skills):
    print(f"{i}: {skill}")
    
🧠 Summary Table
Method	Description
append()	Add one item to the end
extend()	Add elements from another list
insert()	Insert item at specific position
remove()	Remove first matching item
pop()	Remove and return item by index
clear()	Remove all items
index()	Find index of value
count()	Count occurrences of a value
sort()	Sort the list
reverse()	Reverse the list
copy()	Copy the list
