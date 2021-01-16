# 29. Questions:-----

# 1. Write a Python program to create a tuple.
st = tuple()
print(st)
print(type(st))


# 2. Write a Python program to create a tuple with different data types.
def Create(tup):
    tups = tuple(tup)
    print(tups)
    print(type(tups))
Create(("Dibyendu", True, 100))


# 3. Write a Python program to unpack a tuple in several variables.
def UnPack(tup):
    print(tup)
    n1, n2, n3 = tup
    print(n1 + n2 + n3)
UnPack((2,3,4))


# 4. Write a Python program to add an item in a tuple.
def CreateTuple(tup):
    print(tup)
    print(tup + (10,))
    print(tup[:3] + (10,20,30,))
    lst = list(tup)
    lst.append(10000)
    print(tuple(lst))
CreateTuple((1,2,3,4,5,6,7,8))


# 5. Write a Python program to convert a tuple to a string.
def ToString(tup):
    str = ''.join(tup)
    print(str)
ToString(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))
ToString(('10','20','30','40'))


# 6. Write a Python program to get the 4th element and 4th element from last of a tuple.
def GetElement(tup):
    print("4th element from start: ", tup[3])
    print("4th element from end: ", tup[-4])
GetElement(('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's'))


# 7. Write a Python program to create the colon of a tuple.
from copy import deepcopy
tup = ("Hello", 10, [], True)
print("Original Tuple at first: ", tup)
tup_col = deepcopy(tup)
tup_col[2].append(10)
print("Tup_Col: ", tup_col)
print("Original Tuple: ", tup)


# 8. Write a Python program to find the repeated items of a tuple.
def RepeatedItem(tup):
    n = int(input("enter number for check: "))
    print(f"{n} repeated", tup.count(n), "times")
RepeatedItem((2, 4, 5, 6, 2, 3, 4, 4, 7))


# 9. Write a Python program to convert a list to a tuple.
def ToList(list):
    tuples = tuple(list)
    print("Tuples: ", tuples)
    print("Type of: ", type(tuples))
ToList([10, 20, 30, 40, 100])


# 10. Write a Python program to remove an item from a tuple.
def Remove(tup):
    print(tup)
    #tuples are immutable, so you can not remove elements
    #using merge of tuples with the + operator you can remove an item and it will create a new tuple
    tup = tup[:2] + tup[3:]
    print(tup)
    #converting the tuple to list
    listx = list(tup) 
    #use different ways to remove an item of the list
    listx.remove("c") 
    #converting the tuple to list
    tup = tuple(listx)
    print(tup)
Remove(("w", 3, "r", "s", "o", "u", "r", "c", "e"))


# 11. Write a Python program to slice a tuple.
def Slice(tup):
    print(tup[:3])
    print(tup[3:])
    print(tup[3:8])
Slice(('H', 'E', 'L', 'L', 'O', 'W'))


# 12. Write a Python program to find the index of an item of a tuple.
def FindIndex(tup):
    print("Tuples: ", tup)
    n = input("Enter an element: ")
    print(f"Index of {n} is: ", tup.index(n))
FindIndex(('D', 'I', 'B', 'Y', 'E', 'N', 'D', 'U'))


# 13. Write a Python program to find the length of a tuple.
def Length(tup):
    print("Length: ", len(tup))
Length(('D', 'I', 'B', 'Y', 'E', 'N', 'D', 'U'))


# 14. Write a Python program to convert a tuple to a dictionary.
def ToDict(tup):
    print(dict((y, x) for x, y in tup))
ToDict(((2, "w"),(3, "r")))


# 15. Write a Python program to unzip a list of tuples into individual lists.
l = [(1,2), (3,4), (8,9)]
print(list(zip(*l)))


# 16. Write a Python program to reverse a tuple
def Reversed(tup):
    s = reversed(tup)
    print(tuple(s))
Reversed(('D', 'I', 'B', 'Y', 'E', 'N', 'D', 'U'))


# 17. Write a Python program to convert a list of tuples into a dictionary.
def ToDict(ListOfTup):
    print(dict((y, x) for x, y in ListOfTup))
ToDict([(2, "w"),(3, "r"), (4, 'k')])


# 18. Write a Python program to replace last value of tuples in a list. 
def Replace(Ltup):
    lst = []
    for item in Ltup:
        lst.append(item[:-1] + (100,))
    print(lst)
Replace([(10, 20, 40), (40, 50, 60), (70, 80, 90)])


# 19. Write a Python program to remove an empty tuple(s) from a list of tuples.
def removeEmpty(tup):
    lst = []
    for i in tup:
        if i:
            lst.append(i)
    print(lst)
removeEmpty([(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')])


# 20. Write a Python program to sort a tuple by its float element.
def Sort(tup):
    print( sorted(tup, key=lambda x: float(x[1]), reverse=True))
Sort([('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')])


# 21. Write a Python program to count the elements in a list until an element is a tuple.
def Count(tup):
    ctr = 0
    for n in tup:
        if isinstance(n, tuple):
            break
        ctr += 1
    print(ctr)
Count([10,20,30,(10,20),40])


# 22. Write a Python program convert a given string list to a tuple.
def ToTuple(List):
    print(tuple(List))
ToTuple('Python')


# 23. Write a Python program calculate the product, multiplying all the numbers of a given tuple.
def Calculate(tup):
    s = 0
    m = 1
    for i in tup:
        s += i
        m *= i
    print("Sum of all: ", s)
    print("Product of all: ", m)
Calculate((4, 3, 2, 2, -1, 18))
Calculate((2, 4, 8, 8, 3, 2, 9))


# 24. Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
def Averages(tup):
    lst = []
    s = 0
    c = 0
    for i in tup:
        for j in i:
            s += j
        lst.append(s/len(i))
    print("Average value list: ", lst)
Averages(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))


# 25. Write a Python program to convert a tuple of string values to a tuple of integer values.
def Convert(tup):
    lst = []
    for i in tup:
        lst.append((int(i[0]), int(i[1])))
    print(tuple(lst))
Convert((('333', '33'), ('1416', '55')))


# 26. Write a Python program to convert a given tuple of positive integers into an integer.
def Integer(tup):
    for i in tup:
        print(i, end='')
    print()
    print(int(''.join(map(str,tup))))
Integer((1,2,3))

# 27. Write a Python program to check if a specified element presents in a tuple of tuples.
def Presents(tup, item):
    for i in tup:
        if item in i:
            print("yes, Present")
        else:
            print("Not, Present")
Presents((('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime')), 'Red')
Presents((('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'White')), 'White')


# 28. Write a Python program to compute element-wise sum of given tuples.
def Compute(tup):
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    for item in tup:
        s1 += item[0]
        s2 += item[1]
        s3 += item[2]
        s4 += item[3]
    print((s1, s2, s3, s4))
Compute(
    ((1, 2, 3, 4),
     (3, 5, 2, 1),
     (2, 2, 3, 1))
)


# 29. Write a Python program to compute the sum of all the elements of each tuple 
#     stored inside a list of tuples.
def Sum(tup):
    s = 0
    lst = []
    for i in tup:
        lst.append(sum(i))
    print("Sum:  ", lst)
Sum([(1, 2), (2, 3), (3, 4)])
Sum([(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)])
