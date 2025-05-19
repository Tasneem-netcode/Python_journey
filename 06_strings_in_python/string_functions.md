🔹 1. len() – Length of String
Returns the number of characters (including spaces).

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

s = "Python is fun"
print(s.find("is"))  # Output: 7
Returns -1 if not found.

🔹 7. .count(substring) – Count Occurrences

s = "banana"
print(s.count("a"))  # Output: 3
🔹 8. .startswith("text") / .endswith("text")

s = "hello world"
print(s.startswith("hello"))  # True
print(s.endswith("world"))    # True
🔹 9. .split("separator") – Break into List

s = "java , python , cpp"
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
