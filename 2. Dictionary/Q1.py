# 20 Questions:----------

# 1. Write a Python script to sort (ascending and descending) a dictionary by value.
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
ind = []
val = []
mdct = {}
for index, value in d.items():
    val.append(value)
for i in sorted(val):
    ind.append(d.get(i))
for index, value in zip(ind, sorted(val)):
    mdct[index] = value
print("Ascending Order: ", mdct)


# 2. Write a Python script to add a key to a dictionary.
d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)


# 3. Write a Python script to concatenate following dictionaries to create a new one.
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
dct = dict()
for d in (dic1, dic2, dic3):
    dct.update(d)
print("New Dictionary: ", dct)


# 4. Write a Python script to check whether a given key already exists in a dictionary.
def Check(dct, key):
    if key in dct:
        print("Key is Present")
    else:
        print("Key is not Present")
Check({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 10)
Check({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}, 4)


# 5. Write a Python program to iterate over dictionaries using for loops.
def Iterate(dct):
    for key, value in dct.items():
        print(f"{key}--->{value}")
Iterate({'x': 10, 'y': 20, 'z': 30} )


# 6. Write a Python script to generate and print a dictionary that 
#    contains a number (between 1 and n) in the form (x, x*x).
def Generate(n):
    dct = {}
    for i in range(1, n+1):
        dct[i] = i*i
    print(dct)
Generate(5)
Generate(15)


# 7. Write a Python script to merge two Python dictionaries.
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)


# 8. Write a Python program to sum all the items in a dictionary.
def Sum(dct):
    sum = 0
    for key, value in dct.items():
        sum += value
    print("Sum of all items: ", sum)
Sum({'a': 100, 'b': 200, 'x': 300, 'y': 200})


# 9. Write a Python program to multiply all the items in a dictionary.
def Multiply(dct):
    m = 1
    for key, value in dct.items():
        m *= value
    print("Multiply of all items: ", m)
Multiply({'a': 10, 'b': 2, 'x': 3, 'y': 2})


# 10. Write a Python program to remove a key from a dictionary.
def DeleteKey(dct, key):
    print("Original Dictionary: ", dct)
    if key in dct:
        del dct[key]
    print("After Delete key, dictionary is: ", dct)
DeleteKey({'a':1,'b':2,'c':3,'d':4}, 'c')


# 11. Write a Python program to map two lists into a dictionary.
def MapTwoList(list1, list2):
    dict = {}
    for l1, l2 in zip(list1, list2):
        dict[l1] = l2
    print("Dictionary: ", dict)
MapTwoList(['Arko', 'Dibyendu', 'Ram', 'Shyam'], ['Biswas', 'Paul', 'Roy', 'Sen'])


# 12. Write a Python program to sort a dictionary by key.
def SortByKey(d):
    dct = {}
    for key in sorted(d):
        print(key, d[key])
    for key in sorted(d):
        dct[key] = d[key]
    print("Dict: ", dct)
SortByKey({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})


# 13. Write a Python program to get the maximum and minimum value in a dictionary.
def MaxMin(dct):
    s = []
    for key, value in dct.items():
        s.append(value)
    print("Maximun: ", max(s))
    print("Minimum: ", min(s))
MaxMin({'x':500, 'y':5874, 'z': 560})


# 14. Write a Python program to remove duplicates from Dictionary.
def removeDuplicate(dct):
    finalDct = {}
    for key, value in dct.items():
        if value not in finalDct.values():
            finalDct[key] = value
    print(finalDct)
removeDuplicate({
    'id1': 
        {'name': ['Sara'], 
            'class': ['V'], 
            'subject_integration': ['english, math, science']
        },
    'id2': 
        {'name': ['David'], 
            'class': ['V'], 
            'subject_integration': ['english, math, science']
        },
    'id3': 
        {'name': ['Sara'], 
        'class': ['V'], 
        'subject_integration': ['english, math, science']
    },
    'id4': 
    {'name': ['Surya'], 
        'class': ['V'], 
        'subject_integration': ['english, math, science']
    },
})


# 15. Write a Python program to check a dictionary is empty or not.
def CheckEmpty(dct):
    if not bool(dct):
        print("Dictionary is empty")
    else:
        print(dct)
CheckEmpty({'x':500, 'y':5874, 'z': 560})
CheckEmpty({})
CheckEmpty({1,2})


# 16. Write a Python program to combine two dictionary adding values for common keys
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
from collections import Counter
print(Counter(d1) + Counter(d2))


# 17. Write a Python program to print all unique values in a dictionary.
dta =  [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
lst = []
for i in dta:
    for key, value in i.items():
        if value not in lst:
            lst.append(value)
print(set(lst))


# 18. Write a Python program to create and display all combinations of letters, 
#     selecting each letter from a different key in a dictionary.
def Display(dct):
    L1 = []
    for index, value in dct.items():
        L1.append(value)
    for i in L1[0]:
        for j in L1[1]:
            print(f"{i}{j}")
Display({'1':['a','b'], '2':['c','d']})


# 19. Write a Python program to find the highest 3 values in a dictionary.
def Highest3(dct):
    lst = []
    for key, value in dct.items():
        lst.append(value)
    print(sorted(lst, reverse=True)[:3])
Highest3({'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20})


# 20. Write a Python program to find the highest 3 values in a dictionary.
from collections import Counter
item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for d in item_list:
    result[d['item']] += d['amount']
print(result) 
