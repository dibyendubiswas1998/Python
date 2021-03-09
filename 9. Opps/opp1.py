# https://www.javatpoint.com/python-oops-concepts

# Class and Object:------

class Persion:
    pass
obj = Persion()
print(type(obj))

# ----------------------------------------------------------------------

class Persion:
    pass
obj1 = Persion()
obj1.name = "Dibyendu"
obj1.age = 21
obj1.surname = 'Biswas'

print(obj1.name)
print(obj1.surname)
print(obj1.age)

obj2 = Persion()
obj2.name = 'Arko'
obj2.age = 21

print(obj2.name)
print(obj2.surname) # showing error (AttributeError: 'Persion' object has no attribute 'surname')

# ----------------------------------------------------------------------
# __init__ method:-----

class Persion:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
obj = Persion('Dibyendu', 'Biswas', 22)
print(obj.name)
print(obj.surname)
print(obj.age)

obj2 = Persion("arko", 'biswas', 22)
print(obj2.name)


# ----------------------------------------------------------------------
class Persion:
    def __init__(self, name, surname, age):
        self.name1 = name
        self.surname1 = surname
        self.age1 = age
obj = Persion('Dibyendu', 'Biswas', 22)
print(obj.name1)
print(obj.surname1)
print(obj.age1)


# ----------------------------------------------------------------------

class Persion:
    def __init__(you, name, surname, age): # self ---> you
        you.name1 = name
        you.surname1 = surname
        you.age1 = age
obj = Persion('Dibyendu', 'Biswas', 22)
print(obj.name1)
print(obj.surname1)
print(obj.age1)


# ----------------------------------------------------------------------
# Methods:---------

class Persion:
    def __init__(self, name, surname, age):
        self.name1 = name
        self.surname1 = surname
        self.age1 = age

    def Age(self):
        return (self.age1)


obj = Persion('Dibyendu', 'Biswas', 25)
print(obj.Age())


# ----------------------------------------------------------------------

class Persion:
    def __init__(self, name, surname, age):
        self.name1 = name
        self.surname1 = surname
        self.age1 = age

    def Age(self):
        return (self.age1)

    def __str__(self):
        return f"I am {self.name1} {self.surname1} and my age is {self.age1}"

obj = Persion('Dibyendu', 'Biswas', 25)
print(obj)


# --------------------------------------------------------------------------

class Persion:
    def __init__(self, name, surname, year):
        self.name1 = name
        self.surname1 = surname
        self.year1 = year

    def Age(self, current_year):
        age = current_year - self.year1
        return age

    def __str__(self):
        return f"I am {self.name1} {self.surname1} and my birth year is {self.year1}"

obj = Persion('Dibyendu', 'Biswas', 1999)
print(obj.Age(2020))
print(obj)

# ---------------------------------------------------------------------------

class Persion:
    
    def __init__(self):
        self.name = "Dibyendu" # here we can pass any functions or method
        self.surname = "Biswas"
    
    def print(self):
        return f"My Name is {self.name} {self.surname}"
    
obj = Persion()
print(obj.print())

# -------------------------------------------------------------------------

def Num():
    return 10
class Persion:

    def __init__(self):
        self.number = Num() # Here we pass function.
    
    def Print(self):
        return self.number

obj = Persion()
print(obj.Print())