# 20 Questions:---------

# 1. Write a Python program to concatenate elements of a list.
def Concatenate(lst):
    print(['-'.join(lst)])
    print([''.join(lst)])
Concatenate(['red', 'green', 'orange'])


# 2.  Write a Python program to remove key values pairs from a list of dictionaries.
def Remove(lst):
    ls = []
    for item in lst:
        for key, val in item.items():
            if key != 'key1':
                ls.append([{key: val}])
    print(ls) 
Remove([{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}])


# 3. Write a Python program to convert a string to a list.
def Convert(st):
    lst = list(st)
    print(lst)
    print(type(lst))
Convert('Dibyendu')


# 4. Write a Python program to check whether all items of a list is 
#     equal to a given string.
def Check(lst, st):
    if list(st) == lst:
        print("Yes")
    else:
        print("No")
Check(['A', 'r', 'k', 'o'], 'Arko')
Check(['A', 'r', 'k', 'o'], 'Arkb')
Check(['A', 'r', 'k', 'o'], 'Dibyendu')


# 5. Write a Python program to replace the last element in a list with another list.
def Replace(lst1, lst2, n):
    lst1.remove(n)
    lst1.extend(lst2)
    print(lst1)

Replace([1, 3, 5, 7, 9, 10], [2, 4, 6, 8], 10)


# 6. Write a Python program to check whether the n-th element exists in a given list.
def Present(lst, n):
    c = 0
    for i in lst:
        if i == n:
            c += 1
    if c >= 1:
        print(f"{n} is present in given list")
    else:
        print(f"{n} is not present in given list")
Present([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 100)
Present([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10)


# 7. Write a Python program to find a tuple, the smallest second index 
#     value from a list of tuples.
def Find(lst):
    print(min(lst, key=lambda n: (n[1], -n[0])))

Find([(4, 1), (1, 2), (6, 0)])


# 8. Write a Python program to create a list of empty dictionaries.
def CreateDct(n):
    lt = []
    for i in range(n):
        lt.append({})
    print(lt)
CreateDct(5)


# 9. Write a Python program to print a list of space-separated elements.
def Separated(lst):
    print(*lst)
Separated([1, 2, 3, 4, 5])


# 10. Write a Python program to insert a given string at the beginning of all 
#      items in a list.
def Insert(lst, st):
    lt = []
    for i in lst:
        lt.append(f"{st}{i}")
    print(lt)
Insert([1,2,3,4], 'emp')


# 11. Write a Python program to iterate over two lists simultaneously.
def Iterate(lst, num):
    for i,j in zip(num, lst):
        print(i, j)
Iterate(['red', 'white', 'black'], [1, 2, 3])


# 12. Write a Python program to access dictionary keys element by index.
def Acess(dct):
    print(list(dct)[0])
Acess({'physics': 80, 'math': 90, 'chemistry': 86})


# 13. Write a Python program to find the list in a list of lists whose sum of 
#      elements is the highest.
def Find(List1):
    print(max(List1, key=sum))
Find([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])


# 14. Write a Python program to find all the values in a list are greater 
#      than a specified number.
def Greater(lst, n):
    ls =[]
    for i in lst:
        if i > n:
            ls.append(i)
    print(ls)
Greater([7, 8, 9, 10, 11, 12, 4, 5, 6], 6)


# 15. Write a Python program to extend a list without append.
def Without(lst1, lst2):
    lst1[:0] = lst2
    print(lst1)
Without([10, 20, 30], [40, 50, 60])


# 16. Write a Python program to remove duplicates from a list of lists.
def Remove(lst):
    Ls = []
    for i in lst:
        for j in i:
            if j not in Ls:
                Ls.append(j)
    print(Ls)
Remove([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]])


# 17. Write a Python program to get the depth of a dictionary.
def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0
dic = {'a':1, 'b': {'c': {'d': {}}}}
print(dict_depth(dic))


# 18. Write a Python program to check whether all dictionaries in a list 
#      are empty or not.
def Check(lst):
    print(all(not i for i in lst))

Check([{},{},{}])
Check([{1,2},{},{}])


# 19. Write a Python program to flatten a given nested list structure.
def Flatten(lst):
    Ls1 = []
    Ls2 = []
    Ls3 = []
    for item in lst:
        if type(item) == int:
            Ls1.append(item)
        else:
            Ls2.append(item)
    for i in Ls2:
        for j in i:
            Ls3.append(j)
    Ls1.extend(Ls3)
    print(sorted(Ls1))

Flatten([0, 10, [20, 30], 40, 50, [6, 70, 80], [90, 100, 110, 120]])


# 20. Write a Python program to remove consecutive duplicates of a given list.
def Remove(lst):
    FL = []
    for i in lst:
        if i not in FL:
            FL.append(i)
    print(FL)

Remove([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4])


