## Python Dictionary – Full Beginner-Friendly Guide

```markdown
#  🧠Python Dictionary – Full Beginner-Friendly Guide

## Table of Contents
- [What is a Dictionary?](#what-is-a-dictionary-in-python)
- [Creating a Dictionary](#how-to-create-a-dictionary)
- [Accessing Values](#accessing-values)
- [Adding & Updating Items](#adding-or-updating-items)
- [Removing Items](#removing-items)
- [Common Dictionary Methods](#common-dictionary-methods)
- [Looping Through a Dictionary](#looping-through-a-dictionary)
- [Use Cases](#use-cases-of-dictionary)
- [Common Pitfalls](#common-pitfalls)
- [Example: Word Counter](#example--word-counter-using-dictionary)
- [Summary](#summary)

---

## What is a Dictionary in Python?

A dictionary in Python is an unordered and mutable collection of key-value pairs.

```python
my_dict = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}
```

- **Keys**: "name", "age", "is_student" (must be unique and immutable)
- **Values**: "Alice", 25, True (can be any data type)

---

## How to Create a Dictionary 📚

```python
# Empty dictionary
empty_dict = {}

# Dictionary with data
person = {
    "name": "Bob",
    "age": 30,
    "city": "New York"
}
```

---

## Accessing Values 🛠️

```python
print(person["name"])       # Bob
print(person.get("age"))    # 30
```
- `[]` gives a KeyError if key not found.
- `.get()` returns `None` if key not found.

---

## 🧩 Adding or Updating Items

```python
person["job"] = "Engineer"   # Add new key
person["age"] = 31           # Update existing key
```

---

## ❌ Removing Items

```python
person.pop("city")           # Removes 'city' key
del person["job"]            # Deletes 'job' key
person.clear()               # Removes all items
```

---

## Common Dictionary Methods

| Method             | Description                          | Example                                 |
|--------------------|--------------------------------------|-----------------------------------------|
| `get(key)`         | Returns value of key, or None        | `person.get("name")`                    |
| `keys()`           | Returns all keys                     | `person.keys()`                         |
| `values()`         | Returns all values                   | `person.values()`                       |
| `items()`          | Returns all (key, value) pairs       | `person.items()`                        |
| `pop(key)`         | Removes and returns value            | `person.pop("age")`                     |
| `update(dict2)`    | Updates with another dictionary      | `person.update({"city":"Boston"})`      |
| `clear()`          | Removes all items                    | `person.clear()`                        |

---

## Looping Through a Dictionary

```python
for key in person:
    print(key, ":", person[key])

# OR

for key, value in person.items():
    print(f"{key}: {value}")
```

---

## Use Cases of Dictionary

- Storing structured data (e.g., user profiles)
- Counting frequency of items (e.g., word counts)
- JSON-like data structure for APIs
- Mappings (e.g., student roll numbers to names)

---

## Common Pitfalls

- Keys must be **unique** and **immutable** (e.g., strings, numbers, tuples)
- Accessing a missing key using `[]` raises a `KeyError`
- Dictionaries are mutable—changes happen in-place

---

## Example – Word Counter Using Dictionary

```python
text = "apple banana apple orange banana apple"
word_count = {}

for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# Output: {'apple': 3, 'banana': 2, 'orange': 1}
```

---

## Summary

- Dictionaries use key-value pairs.
- Keys must be unique and immutable.
- Values can be any data type.
- Use them for fast lookups, structured data, and mappings.
```
