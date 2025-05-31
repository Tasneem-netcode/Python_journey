x = 5
print(eval("x + 10"))   # Output: 15
  

expr = input("Enter a math expression: ")  # like 3 + 4 * 2
result = eval(expr)
print("Result:", result)


x = 10
y = 5
print(eval("x * y + 3"))  # Output: 53


lst = eval("[1, 2, 3, 4]")
print(lst)  # Output: [1, 2, 3, 4]

dct = eval("{'name': 'Ali', 'age': 20}")
print(dct['name'])  # Output: Ali


user_input = input("Enter a math expression: ")  # User: 5 + 3
print("Result:", eval(user_input))
