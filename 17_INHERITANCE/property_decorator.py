class Employee:
    a =1

    @classmethod 
    def name(cls):
        print(f"The class attribute of a is{cls.a}")
    @property
    def name(self):
        return f"{self.fname} {self.lname}" 
    @name.setter
    def name(self , value):
        self.fname =value.split(" ")[0]
        self.lname =value.split(" ")[1]

e= Employee()
e.name = "Harry Khan "
print(e.name)

# print(type(Employee))