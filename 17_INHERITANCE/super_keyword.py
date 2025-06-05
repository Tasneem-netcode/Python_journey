class Parent:
    def __init__(self):
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Calls Parent's constructor
        print("Child constructor")

c = Child()

#example 2:
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Call Parent’s method
        print("Hello from Child")

c = Child()
c.greet()

