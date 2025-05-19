 📚 Python String Functions

This section lists common string functions in Python with examples and outputs.

---

### 🔹 1. `len()` – Length of String
Returns the number of characters (including spaces).

```python
s = "Python"
print(len(s))  # Output: 6

🔹 2. .lower() – Convert to Lowercase

s = "HeLLo"
print(s.lower())  # Output: "hello"
🔹 3. .upper() – Convert to Uppercase

s = "hello"
print(s.upper())  # Output: "HELLO"
🔹 4. .strip() – Removes Spaces from Start & End

s = "  hello  "
print(s.strip())  # Output: "hello"
🔹 5. .replace(old, new) – Replace Substring

s = "I love Java"
print(s.replace("Java", "Python"))  # Output: "I love Python"
🔹 6. .find(substring) – First Index of Substring
Returns -1 if not found.


s = "Python is fun"
print(s.find("is"))  # Output: 7
🔹 7. .count(substring) – Count Occurrences

s = "banana"
print(s.count("a"))  # Output: 3
🔹 8. .startswith("text") / .endswith("text")

s = "hello world"
print(s.startswith("hello"))  # Output: True
print(s.endswith("world"))    # Output: True
🔹 9. .split("separator") – Break into List

s = "java,python,cpp"
print(s.split(","))  # Output: ['java', 'python', 'cpp']
🔹 10. .join(list) – Join List into String

words = ['Hello', 'Python']
print(" ".join(words))  # Output: "Hello Python"
🔹 11. .capitalize() – Capitalize First Letter

s = "python is fun"
print(s.capitalize())  # Output: "Python is fun"
🔹 12. .title() – Capitalize Each Word

s = "python is fun"
print(s.title())  # Output: "Python Is Fun"
✅ Tip:
All these functions return a new string; original strings remain unchanged as strings are immutable in Python.

💡 Practice Suggestion:
Try each function in your Python editor.


