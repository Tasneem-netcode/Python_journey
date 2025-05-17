# types of type casting
#1.) IMPLICIT : CONVERTS AUTOMATICALLY 

a =10
b= 5.5

result = a+b
print(result) #15.5
print(type(result)) #float 

#2.) EXPLICIT : MANUALLY CONVERTED
x ="100" #string
y = int(x)
print(type(y)) #int



# String to int
s = "42"
print(int(s))  # 42

# Float to int
f = 3.9
print(int(f))  # 3 (truncates, doesn't round)

# Int to string
n = 25
print(str(n))  # "25"

# List to tuple
lst = [1, 2, 3]
print(tuple(lst))  # (1, 2, 3)

