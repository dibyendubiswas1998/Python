# 20 Questions:------

# 1. Write a Python program to create a set.
s = set()
print(set())
print(s)


# 2. Write a Python program to iterate over sets.
def Iterate(st):
    for i in st:
        print(i)
Iterate({10, 20, 30, 40, 50})


# 3. Write a Python program to add member(s) in a set.
def Add(sets):
    st = {1,2,3} 
    st.update(sets)
    print('Update Set: ', st)
Add({10,20,30})


# 4. Write a Python program to remove item(s) from set.
def Remove(sets):
    print("Before Remove: ", sets)
    sets.pop()
    print("After Remove: ", sets)
Remove({10,20,30,40,50,60})


# 5. Write a Python program to remove an item from a set if it is present in the set. 
def Remove1(sets, item):
    print("Before Remove: ", sets)
    sets.discard(item)
    print("After Remove: ", sets)
Remove1({10,20,30,40,50,60}, 30)


# 6. Write a Python program to create an intersection of sets.
def Intersection(set1, set2):
    print("Intersection of two sets: ", set1 & set2)
Intersection({10,20,30,40}, {1,20,3,30})


# 7. Write a Python program to create a union of sets.
def Union(set1, set2):
    print("union: ", set1 | set2)
Union({10,20,30,40}, {1,20,3,30})


# 8. Write a Python program to create set difference.
def Difference(set1, set2):
    print("SetDifference between set1 and set2", set1 - set2)
    print("SetDifference between set2 and set1", set2 - set2)
Difference({10,20,30,40}, {1,20,3,30})


# 9. Write a Python program to check if a set is a subset of another set.
def isSubset(set1, set2):
    print('If set1 is subset of set2', set1.issubset(set2))
    print('If set2 is subset of set1', set2.issubset(set1))
isSubset({10,20,30,40}, {20,30})


# 10. Write a Python program to create a shallow copy of sets.
setp = set(["Red", "Green"])
setq = set(["Green", "Red"])
setr = setp.copy()
print(setr)
print(setp)


# 11. Write a Python program to clear a set.
def Clear(sets):
    sets.clear()
    print(sets)
Clear({10,20,30,40})


# 12. Write a Python program to use of frozensets. Go to the editor
#      Note: Frozensets behave just like sets except they are immutable.
x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7]) 
print(x.isdisjoint(y))
print(x.difference(y))
print(x | y)


# 13. Write a Python program to find maximum and the minimum value in a set.
def Find(sets):
    print("Maximum Value: ", max(sets))
    print("Minimum Value: ", min(sets))
Find({10,20,30,40,100})


# 14. Write a Python program to find the length of a set.
def Length(sets):
    print("Length of sets: ", len(sets))
Length({10,20,30,40,100})


# 15. Write a Python program to check if a given value is present in a set or not.
def Present(sets, n):
    if n in sets:
        print(f"{n} is Present")
Present({10,20,30,40,100}, 40)


# 16. Write a Python program to check if two given sets have no elements in common.
def Common(set1, set2):
    print("Common elements is: ", set1 & set2)
Common({10,20,30,40}, {20,3, 2, 11})


# 17. Write a Python program to check if a given set is superset of itself and superset of another given set.
def Check(sets, sets1):
    print("Is sets is Supersets: ", sets.issuperset(sets))
    print("Is sets1 is Supersets of sets: ", sets1.issuperset(sets))
    print("Is sets is Supersets of sets1: ", sets.issuperset(sets1))
Check({10,20,30,40}, {20,3})


# 18. Write a Python program to find the elements in a given set that are not in another set.
def SameOrNot(set1, set2):
    print("Difference between set1 and set2: ", set1 - set2)
    print("Difference between set2 and set1: ", set2 - set1)
SameOrNot({10,20,30,40}, {20,3, 2, 11})


# 19. Write a Python program to check a given set has no elements in common with other given set.
sn1 = {1,2,3}
sn2 = {4,5,6}
sn3 = {3}
print("Original sets:")
print(sn1)
print(sn2)
print(sn3)
print("Check sn1 set has no elements in common with sn2 set:")
print(sn1.isdisjoint(sn2))
print("Check sn1 set has no elements in common with sn3 set:")
print(sn1.isdisjoint(sn3))


# 20. Write a Python program to remove the intersection of a 2nd set from the 1st set.
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("Remove the intersection of a 2nd set from the 1st set using difference_update():")
sn1.difference_update(sn2)
print(sn1)
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Remove the intersection of a 2nd set from the 1st set using -= operator:")
print(sn1-sn2)
