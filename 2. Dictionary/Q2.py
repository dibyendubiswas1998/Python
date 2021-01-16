# 26. Questions:----------

# 1. Write a Python program to create a dictionary from a string. Track the count of the letters from the string.
def Count(string):
    dct = {}
    for i in string:
        dct[i]  = dct.get(i, 0) + 1
    print(dct)
Count("w3resources")


# 2. Write a Python program to print a dictionary in table format.
def Format(dct):
    import pandas as pd
    print(pd.DataFrame(dct))
Format({'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]})


# 3. Write a Python program to count the values associated with key in a dictionary.
#     Count of how many dictionaries have success as True
def Get(dct):
    c = 0
    for item in dct:
        if item['success']:
            c += 1
    print("Success have: ",2, 'dictionary')
Get([
    {'id': 1, 'success': True, 'name': 'Lary'}, 
    {'id': 2, 'success': False, 'name': 'Rabi'}, 
    {'id': 3, 'success': True, 'name': 'Alex'}
])


# 4. Write a Python program to convert a list into a nested dictionary of keys.
def NestedDict(List):
    dict = current = {}
    for item in List:
        current[item] = {}
        current = current[item]
    print("Nested Dictionary is: ",dict)
NestedDict([1,2,3,4])


# 5. Write a Python program to sort a list alphabetically in a dictionary.
def Sorted(dct):
    sorted_dict = {x: sorted(y) for x, y in dct.items()}
    print(sorted_dict)
Sorted({'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]})


# 6. Write a Python program to remove spaces from dictionary keys.
def RemoveSpace(dct):
    # student_dict = {x.translate({32: None}): y for x, y in dct.items()}
    # print("New dictionary: ",student_dict)
    new_dct = {}
    for key, value in dct.items():
        new_dct[key.translate({32:None})] = value
    print(new_dct)
RemoveSpace({'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']})


# 7. Write a Python program to get the top three items in a shop.
def TopItem(dct):
    from heapq import nlargest
    from operator import itemgetter
    for key, value in nlargest(3, dct.items(), key=itemgetter(1)):
        print(key, value)
TopItem({'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24})


# 8. Write a Python program to print a dictionary line by line.
def LineByLine(dct):
    for i in dct:
        print(i)
        for j in dct[i]:
            print(j, ':', dct[i][j])
LineByLine({
    'Aex':{'class':'V',  'rolld_id':2},
    'Puja':{'class':'V', 'roll_id':3}
})


# 9. Write a Python program to check multiple keys exists in a dictionary.
def Check(dct):
    for key, value in dct.items():
        print(key, ' ', value)
Check({
  'name': 'Alex',
  'name': 'Yellow',
  'class': 'V',
  'roll_id': '2'
})


# 10. Write a Python program to count number of items in a dictionary value that is a list.
dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
ctr = sum(map(len, dict.values()))
print(ctr)


# 11. Write a Python program to count number of items in a dictionary value that is a list.
def Counter(dct):
    from collections import Counter
    lst = Counter(dct)
    print(lst.most_common())
    
Counter({'Math':81, 'Physics':83, 'Chemistry':87})


# 12. Write a Python program to create a dictionary from two lists without losing duplicate values
def Create(lst1, lst2):
    dct = {}
    for lst1, lst2 in zip(lst1, lst2):
        dct[lst1] = {lst2}
    print(dct)
Create(['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3])


# 13. Write a Python program to replace dictionary values with their average.
def Replace(dct):
    new_dct = {}
    l1 = []
    l2 = []
    for key, value in dct.items():
        l1.append(key)
        l2.append(value)
    for i,j  in zip(l1, l2):
        new_dct[i] = sum(l2)/len(l2)
    print(new_dct)
Replace({'Math':81, 'Physics':81, 'Chemistry':81})


# 14. Write a Python program to match key values in two dictionaries.
def Match(dct1, dct2):
    for (key, value) in set(dct1.items()) & set(dct2.items()):
        print('%s: %s is present in both dictionary' % (key, value))
Match({'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2})
Match({'key1': 1, 'key2': 3, 'key3': 2, 'key4': 12}, {'key1': 1, 'key2': 2, 'key4': 12})


# 15.  Write a Python program to create a dictionary of keys x, y, and z where each key 
#      has as value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth 
#      value of each key from the dictionary.
def CreateDict():
    dct = dict(x=list(range(11, 20)), y=list(range(21, 30)), z=list(range(31, 40)))
    print(dct)
    for key, val in dct.items():
        print(val[4])
CreateDict()


# 16. Write a Python program to drop empty Items from a given Dictionary.
def DropEmpty(dct):
    new_dct = {}
    for key, val in dct.items():
        if val != None:
            new_dct[key] = val
    print(new_dct)
DropEmpty({'c1': 'Red', 'c2': 'Green', 'c3': None})
DropEmpty({'c0': None, 'c1': 'Red', 'c2': 'Green', 'c3': None})


# 17. Write a Python program to filter a dictionary based on values (Marks greater than 170).
def Filter(dct):
    new_dct = {}
    for key, val in dct.items():
        if val > 170:
            new_dct[key] = val
    print(new_dct)
Filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190})


# 18. Write a Python program to convert more than one list to nested dictionary.
def Convert(lst1, lst2, lst3):
    main_dct = {}
    dct = {}
    for lst2, lst3 in zip(lst2, lst3):
        dct[lst2] = lst3
    for i in lst1:
        for key, val in dct.items():
            main_dct[i] = {key, val}
    print(main_dct)

Convert(['S001', 'S002', 'S003', 'S004'],
        ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards'],
        [85, 98, 89, 92])


# 19. Write a Python program to filter the height and width of students, which are 
 #    stored in a dictionary.
def Filter(dct):
    new_dcts = {}
    for key, val in dct.items():
        if val[0] >= 6.0 and val[1] >= 70:
            new_dcts[key] = val
    print(new_dcts)

Filter({'Cierra Vega': (6.2, 70), 
        'Alden Cantrell': (5.9, 65), 
        'Kierra Gentry': (6.0, 68), 
        'Pierre Cox': (5.8, 66)}
)


# 20. Write a Python program to check all values are same in a dictionary. 
def Check(dct):
    lst = []
    for key, item in dct.items():
        lst.append(item)
    for i in lst:
        if i == lst[0]:
            print("True")
Check({'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12})


 # 21. Write a Python program to create a dictionary grouping a sequence of 
 #     key-value pairs into a dictionary of lists.
def Gropping(item):
    new_dct = {}
    for i, j in item:
        new_dct.setdefault(i, []).append(j)
    print(new_dct)
Gropping([('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)])


# 22. Write a Python program to split a given dictionary of lists into list of dictionaries.
def Split(dct):
    keys = dct.keys()
    vals = zip(*[dct[k] for k in keys])
    dcts = [dict(zip(keys, v)) for v in vals]
    print(dcts)
Split({'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]})


# 23. Write a Python program to remove a specified dictionary from a given list.
def Remove(dct, r_id):
    cols = []
    for i in dct:
        if i.get('id') != r_id:
            cols.append(i)
    print(cols)
Remove([
    {'id': '#FF0000', 'color': 'Red'}, 
    {'id': '#800000', 'color': 'Maroon'}, 
    {'id': '#FFFF00', 'color': 'Yellow'}, 
    {'id': '#808000', 'color': 'Olive'}
], '#FF0000')


# 24. Write a Python program to convert string values of a given dictionary, 
#     into integer/float datatypes.
def Convert(dct):
    new_dct = {}
    for j in dct:
        for key, val in j.items():
            new_dct[key] = int(val)
    print([new_dct])
Convert([{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}])


# 25. A Python Dictionary contains List as value. Write a Python program to 
#     clear the list values in the said dictionary.
def Clear(dct):
    new_dct = {}
    for key, value in dct.items():
        new_dct[key] = []
    print(new_dct)
Clear({'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]})


# 26. Write a Python program to extract a list of values from a given list of dictionaries.
def Extract(dct, sub):
    lst = []
    for list1 in dct:
        for key, val in list1.items():
            if key == sub:
                lst.append(val)
    print(f"{sub}'s Marks in list: {lst}")
Extract([
    {'Math': 90, 'Science': 92}, 
    {'Math': 89, 'Science': 94}, 
    {'Math': 92, 'Science': 88}], 'Science')
Extract([
    {'Math': 90, 'Science': 92}, 
    {'Math': 89, 'Science': 94}, 
    {'Math': 92, 'Science': 88}], 'Math')


