Python Dictionary – Full Beginner-Friendly Guide
A dictionary in Python is an unordered and mutable collection of key-value pairs. It is used when you want to associate (map) unique keys to values—like a real dictionary where each word (key) has a meaning (value).

📚 What is a Dictionary in Python?

my_dict = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}

Keys: "name", "age", "is_student"

Values: "Alice", 25, True

✅ Keys are unique
✅ Values can be of any data type
✅ Dictionaries are mutable, meaning you can change their contents after creation

🛠️ How to Create a Dictionary
python

# Empty dictionary
empty_dict = {}

# Dictionary with data
person = {
    "name": "Bob",
    "age": 30,
    "city": "New York"
}
🔄 Accessing Values
python

print(person["name"])       # Bob
print(person.get("age"))    # 30
[] gives an error if key not found

.get() returns None if key not found

🧩 Adding or Updating Items
python
Copy
Edit
person["job"] = "Engineer"       # Add new key
person["age"] = 31               # Update existing key
❌ Removing Items

person.pop("city")         # Removes 'city' key
del person["job"]          # Deletes 'job' key
person.clear()             # Removes all items


🔍 Common Dictionary Methods

Method	Description
.get(key)	Returns value of key, or None
.keys()	Returns list of all keys
.values()	Returns list of all values
.items()	Returns list of (key, value) tuples
.pop(key)	Removes and returns value
.update(dict2)	Updates with another dictionary
.clear()	Removes all items

python

print(person.keys())       # dict_keys(['name', 'age'])
print(person.values())     # dict_values(['Bob', 31])
print(person.items())      # dict_items([('name', 'Bob'), ('age', 31)])
🔁 Looping Through a Dictionary

for key in person:
    print(key, ":", person[key])

# OR

for key, value in person.items():
    print(f"{key}: {value}")
📌 Use Cases of Dictionary
Storing structured data – like user profiles

Counting frequency of items (e.g., word counts)

JSON-like data structure for APIs

Mappings – like student roll numbers to names

⚠️ Things to Remember
Keys must be unique and immutable

Accessing a missing key using [] raises a KeyError, so prefer .get()

Dictionaries are mutable — changes happen in-place

📌 When to Use Dictionaries?
When you need to associate keys with values

For structured data (e.g., user info, settings, records)

To make lookups faster than lists

🧠 Example – Word Counter Using Dictionary

text = "apple banana apple orange banana apple"
word_count = {}

for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
# Output: {'apple': 3, 'banana': 2, 'orange': 1}
✅ Summary
Dictionaries use key-value pairs.

Keys must be unique and immutable (e.g., strings, numbers, tuples).

Values can be anything.

Use them for fast lookups, structured data, and mappings.
