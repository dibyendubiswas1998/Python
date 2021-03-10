
class Persion:

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname
         
    def set_year_of_birth(self, year_birth):
        self.year_birth = year_birth
     
    def __str__(self):
        return f"{self.name} {self.surname} was born in {self.year_birth}"
    
# # Create objectc for persion class
obj = Persion()

# # Set the name
obj.set_name("Dibyendu")
print(obj.name)
# # Set the Surname
obj.set_surname("Biswas")
print(obj.surname)
# # Set the Year of birth
obj.set_year_of_birth(1999)
print(obj.year_birth)
print(obj)
# # But above approach is not good approach.


# --------------------------------------------------------------------------
# Data Abstraction ( Using Access Specifier ):--

class Persion:
    def __init__(self, name, surname, age):
        self._name = name       # protected variable (when use single underscore _name, _sarname, ect.)
        self._surname = surname # protected variable
        self._age = age         # protected variable

    def Age(self):
        return (self._age)

    def __str__(self):
        return f"I am {self._name} {self._surname} and my age is {self._age}"

obj = Persion('Dibyendu', 'Biswas', 25)
print(obj)
print(obj._name)
print(obj.__dict__)


# ---------------------------------------------------------------------------
class Persion:
    def __init__(self, name, surname, age):
        self.__name = name       # Private variable (when use double underscore __name, __sarname, ect.)
        self.__surname = surname # Private variable
        self.__age = age         # Private variable

    def Age(self):
        return (self.__age)

    def __str__(self):
        return f"I am {self.__name} {self.__surname} and my age is {self.__age}"

obj = Persion('Dibyendu', 'Biswas', 25)
print(obj)
# print(obj.__name) # Showing Error ('Persion' object has no attribute '__name') becz variable is private

print(obj.__class__)
print(obj.__dict__) # {'_Persion__name': 'Dibyendu', '_Persion__surname': 'Biswas', '_Persion__age': 25} (Private)

print(obj._Persion__name) # Get the name
print(obj.__dict__.keys())
print(obj.__dict__.values())


# --------------------------------------------------------------------------
# Public Method:---
class Persion:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def DOB(self, year):
        dob = year - self.age
        return f"Your Birth Date is: {dob}"

    def __str__(self):
        return f"I am {self.name} {self.surname} and my age is {self.age}"

obj = Persion('Dibyendu', 'Biswas', 22)
print(obj.DOB(2021))
print(obj)
print(obj.name)

print(obj.__dict__)
print(obj.__dict__.keys())
print(obj.__dict__.values())

class Test:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def Check(self):
        return "This is Public Method/ Function"
ob = Test(10, 20, 30)
print(ob.Check())


# --------------------------------------------------------------------------
# Protected:---
class Persion:
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self._age = age

    def DOB(self, year):
        dob = year - self._age
        return f"Your Birth Date is: {dob}"

    def __str__(self):
        return f"I am {self._name} {self._surname} and my age is {self._age}"

obj = Persion('Dibyendu', 'Biswas', 22)
print(obj.DOB(2021))
print(obj)
print(obj._name)

print(obj.__dict__)
print(obj.__dict__.keys())
print(obj.__dict__.values())

class Test:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def _Check(self):
        return "This is Protected Method/ Function"
ob = Test(10, 20, 30)
# # print(ob.Check()) # showing error becz this is protected 
print(ob._Check())

# --------------------------------------------------------------------------
# Private:----
class Persion:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def DOB(self, year):
        dob = year - self.__age
        return f"Your Birth Date is: {dob}"

    def __str__(self):
        return f"I am {self.__name} {self.__surname} and my age is {self.__age}"

obj = Persion('Dibyendu', 'Biswas', 22)
print(obj.DOB(2021))
print(obj)
print(obj._Persion__name)

print(obj.__dict__)
print(obj.__dict__.keys())
print(obj.__dict__.values())


class Test:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __Check(self):
        return "This is Private Method/ Function"
ob = Test(10, 20, 30)
# print(ob.__Check()) # Error ('Test' object has no attribute '__Check'), becz of this method is private
print(ob._Test__Check()) 

