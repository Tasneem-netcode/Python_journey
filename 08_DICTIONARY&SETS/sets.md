# 🔹 Python Sets – Complete Guide

A **Set** in Python is an **unordered, mutable collection of unique elements**. It is useful when you want to store non-duplicate values and perform mathematical set operations.

---

## 📘 Table of Contents

- [What is a Set?](#what-is-a-set)
- [Creating Sets](#creating-sets)
- [Important Properties](#important-properties)
- [Empty Set](#empty-set)
- [Set Use Cases](#set-use-cases)
- [Common Set Functions/Methods](#common-set-functionsmethods)
- [Adding Elements](#adding-elements)
- [Removing Elements](#removing-elements)
- [Membership Test (Using `in`)](#membership-test-using-in)
- [Set Operations](#set-operations)
  - Union
  - Intersection
  - Difference
  - Symmetric Difference
- [Set Comprehension](#set-comprehension)
- [Set vs List vs Tuple](#set-vs-list-vs-tuple)
- [Quick Tips & Notes](#quick-tips--notes)

---

## 📌 What is a Set?

A **set** is a built-in Python data structure used to store **unique**, **unordered** elements.

```python
my_set = {1, 2, 3, 4}
```
###🛠️ Creating Sets
```
# Using curly braces
fruits = {"apple", "banana", "cherry"}

# Using set() constructor
numbers = set([1, 2, 3, 4])

# ⚠️ Important: {} creates an empty dictionary, not a set
empty_set = set()   # ✅ correct
not_a_set = {}      # ❌ this is a dictionary
```
### Getting Set's Length

We use **len()** method to find the length of a set.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
```

**Example:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
```
📌 Important Properties
Feature                        	Description
✅ Unordered                	No indexing or slicing
✅ Mutable                   	Can add/remove elements
❌ No duplicates	            Automatically removes duplicate data
✅ Iterable                  	Can loop through it
❌ Unindexed	                Cannot access items by position
---
🧠 Set Use Cases
Removing duplicates from a list

Checking for unique values

Fast membership test (x in set)

Performing set operations (union, intersection, etc.)

Useful in recommendations, filtering, and tagging systems
---

  ##➕ Adding Elements
```python

my_set = {1, 2}
my_set.add(3)        # {1, 2, 3}
```
##➖ Removing Elements
```
my_set = {1, 2, 3}

my_set.remove(2)     # {1, 3}, Error if 2 not found
my_set.discard(4)    # No error if 4 not found
my_set.pop()         # Removes a random item
my_set.clear()       # Becomes an empty set

```

##🔍 Membership Test (Using in)
```
colors = {"red", "blue", "green"}

print("red" in colors)     # True
print("yellow" in colors)  # False
```

🔄 Set Operations
- 1. Union (| or .union())
Combines all unique elements from both sets.

```
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)               # {1, 2, 3, 4, 5}
print(a.union(b))          # Same result
```
2. Intersection (& or .intersection())
Elements common to both sets.
```
print(a & b)               # {3}
print(a.intersection(b))   # Same
```
3. Difference (- or .difference())
Elements in a but not in b.

```
print(a - b)               # {1, 2}
print(a.difference(b))     # Same
```
4. Symmetric Difference (^ or .symmetric_difference())
All elements from both sets except the common ones.

```
print(a ^ b)                      # {1, 2, 4, 5}
print(a.symmetric_difference(b)) # Same
```
## ⚙️ Common Set Functions/Methods
Method                	                       Description
.add(x)	                               Adds x to the set
.remove(x)                           	Removes x (Error if not found)
.discard(x)            	              Removes x (No error if not found)
.pop()	                              Removes a random element
.clear()                            	Removes all elements
.union(other)                         All elements from both sets
.intersection(other)	                Elements common to both sets
.difference(other)	                  Elements only in the first set
.symmetric_difference(other)	        Elements in either, not both
.issubset(other)	                   Checks if set is part of another
.issuperset(other)	                 Checks if set contains another
.isdisjoint(other)	                 Checks if sets have no common elements

