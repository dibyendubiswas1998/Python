
# Inheritance:-----

class Persion:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def Age(self):
        return self.age
    
    def __str__(self):
        return f"My name is {self.name} and age is {self.age}"

class Student(Persion):
    def __init__(self, id, *args):
        super(Student, self).__init__(*args)
        self.id = id
    
    def __str__(self):
        return f"id: {self.id}, Name: {self.name}, Age: {self.age}"

obj_Student = Student(10, "Dibyendu", 22)
print(obj_Student)



# ------------------------------------------------------------------------------------
class XYZ:
    def __init__(self, a, b, c = 10, d=20):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def __str__(self):
        return f"XYZ class:--  a: {self.a}, b: {self.b}, c: {self.c},  d: {self.d}"
    
class ABC(XYZ):
    # # I just want only 2 variable, so I call a and b from parent class (XYZ) (method-01)
    def __init__(self, *args):
        super(ABC, self).__init__(*args)  # *args--> carray all the arguments from parent 
         
    def __str__(self):
        return f"a: {self.a}, b: {self.b}"
    
# # obj_XYZ = XYZ(10, 20, 30, 40)
# # print(obj_XYZ)
obj_ABC = ABC(1, 100)
print(obj_ABC)



# ---------------------------------------------------------------------------------
class XYZ:
    def __init__(self, a, b, c = 10, d=20):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def __str__(self):
        return f"XYZ class:--  a: {self.a}, b: {self.b}, c: {self.c},  d: {self.d}"
    
class ABC(XYZ):
    # # I just want only 2 variable, so I call a and b from parent class (XYZ) (method-02)
    def __init__(self, a, b):
        XYZ.__init__(self, a, b)

    def __str__(self):
        return f"a: {self.a}, b: {self.b}"
    
# # obj_XYZ = XYZ(10, 20, 30, 40)
# # print(obj_XYZ)
obj_ABC = ABC(1, 100)
print(obj_ABC)
print("'obj_ABC' is object/ instance of ABC: ", isinstance(obj_ABC, ABC)) # # true
print("'obj_ABC' is object/ instance of XYZ: ", isinstance(obj_ABC, XYZ)) # # true



# --------------------------------------------------------------------------------------
# Single level Ingeritance (where we inherit the method/functions)

class A:     
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def features1(self):
        return ("Features-1 is working")
    
    def features2(self):
        return ("Features-2 is working")
    
    def __str__(self):
        return f"a: {self.a}, b: {self.b}"

class B(A):    
    def __init__(self, a, b):
        super(B, self).__init__(a, b)

    def features3(self):
        return ("Features-3 is working")
    
    def features4(self):
        return ("Features-4 is working")

    def __str__(self):
        return f"a: {self.a}, b: {self.b}"
    
b = B(10, 20)
print(b.features1())
print(b.features2())
print(b.features3())
print(b.features4())
print(b)



# ----------------------------------------------------------------------------------------
# Multi-Level of Inheritance (where we inherit the method/functions)
class A:     
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def features1(self):
        return ("Features-1 is working")
    
    def features2(self):
        return ("Features-2 is working")
    
    def __str__(self):
        return f"a: {self.a}, b: {self.b}"

class B(A):    
    def __init__(self, a, b):
        super(B, self).__init__(a, b) # inherit from class A

    def features3(self):
        return ("Features-3 is working")
    
    def features4(self):
        return ("Features-4 is working")

    def __str__(self):
        return f"a: {self.a}, b: {self.b}"

class C(B):    
    def __init__(self, a, b):
        super(C, self).__init__(a, b) # inherit from class B

    def features5(self):
        return ("Features-5 is working")
    
    def features6(self):
        return ("Features-6 is working")

    def __str__(self):
        return f"a: {self.a}, b: {self.b}"    

c = C(10, 30)
print(c.features1()) # call the method using 'c'.
print(c.features2())
print(c.features3())
print(c.features4())
print(c.features5())
print(c.features6())
print(c)



# -------------------------------------------------------------------------------------------
# Multiple inheritance (where we inherit the method/functions)
# Ex-01:-
class A:     
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("It's A_class init")

    def features1(self):
        return ("Features-1 is working")
    
    def features2(self):
        return ("Features-2 is working")
    
    def __str__(self):
        return f"a: {self.a}, b: {self.b}"

class B:    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("It's B_class init")

    def features3(self):
        return ("Features-3 is working")
    
    def features4(self):
        return ("Features-4 is working")

    def __str__(self):
        return f"a: {self.a}, b: {self.b}"

class C(A, B):    
    def __init__(self, a, b):
        super(C, self).__init__(a, b)
        print("It's C_class init")

    def features5(self):
        return ("Features-5 is working")
    
    def features6(self):
        return ("Features-6 is working")

    def __str__(self):
        return f"a: {self.a}, b: {self.b}"    

c = C(10, 20)
print(c)
print(c.features1())
print(c.features2())
print(c.features3())
print(c.features4())
print(c.features5())
print(c.features6())

# Ex-02:--
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def test(self):
        return ("Test A")

class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def test(self):
        return ("Test B")
    
class C(A, B):
    obj1 = A(10, 20)
    obj2 = B(30, 50)
    obj1.test()
    obj2.test()
    
c = C(1, 2)
print(c.test()) # Test A
print(c.obj1.test()) # Test A
print(c.obj2.test()) # Test B
