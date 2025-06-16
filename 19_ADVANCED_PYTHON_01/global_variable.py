x = 10  # 🌍 global variable

def show():
    print("Value of x:", x)

show()  # Output: Value of x: 10


a = 34
def func():
    global a 
    a =3 
    print(a)

func()
print(a)