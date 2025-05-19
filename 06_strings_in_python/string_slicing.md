What is String Slicing?
String slicing means extracting a part (substring) from a string using index positions.

The basic syntax is:

string[start:stop]

start: index where the slice begins (inclusive)

stop: index where the slice ends (exclusive)

You can also use string[start:stop:step] to skip characters using the step

✅ Example:

s = "Python"

print(s[0:2])   # Output: "Py" → characters at index 0 and 1
print(s[2:5])   # Output: "tho"

🔹 Indexing Recap:
String indexes start at 0.

  P  y  t  h  o  n
  0  1  2  3  4  5
 -6 -5 -4 -3 -2 -1  ← Negative indexes
🔹 More Examples:

s = "Python"

print(s[:3])     # "Pyt"  → from start to index 2
print(s[3:])     # "hon" → from index 3 to end
print(s[:])      # "Python" → whole string
print(s[-3:])    # "hon" → last 3 characters
print(s[::2])    # "Pto" → every 2nd character

🔸 Slicing with Negative Indexes:

s = "Hello"

print(s[-4:-1])  # "ell" → from index -4 to -2
🧠 Quick Tip:
If you go out of range with slicing, Python won’t give an error. It will just return what it can.

Great! 💡 Practicing string slicing will make it super easy to handle text data in Python. Here are some practice questions for you — from beginner to a little tricky.

🔹 Basic Level:
1. Extract first 4 characters
Input: "HelloWorld" → Output: "Hell"

2. Get last 3 characters
Input: "Python" → Output: "hon"

3. Get substring from index 2 to 5
Input: "Developer" → Output: "velo"

4. Print whole string using slicing
Input: "Learn" → Output: "Learn"

🔹 Intermediate Level:
1. Reverse the string using slicing
Input: "Python" → Output: "nohtyP"

2. Skip every second character
Input: "abcdefg" → Output: "aceg"

3. Extract "gram" from "Instagram" using positive indexing

4. Extract "tag" from "Hashtag" using negative indexing

5. Get the middle 3 characters
Input: "Amazing" → Output: "azi"

🔹 Challenge Level:
1. Given a string of even length, print its first half.
Input: "Program" → Output: "Prog"

2. Extract every 3rd character from index 0 to 9 in the string
Input: "abcdefghij" → Output: "adg"

3. Check if the reversed string equals the original (i.e., is a palindrome)
Input: "madam" → Output: "Yes" (since it reads same backward)

