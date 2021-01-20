# 20 Questions:-----------

# 1. Write a Python program to check whether a list contains a sublist.
def is_Sublist(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False

	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1
				
				if n == len(s):
					sub_set = True
	return sub_set
a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))


# 2. Write a Python program to generate all sublists of a list.
def SubList(lst):
    from itertools import combinations
    subs = []
    temp = []
    for i in range(0, len(lst)+1):
        for x in combinations(lst, i):
            temp.append(list(x))
    if len(temp) > 0:
        subs.extend(temp)
    print(subs)

SubList(['X', 'Y', 'Z'])
SubList(list('12345'))


# 3. Write a Python program to create a list by concatenating a given list which 
#    range goes from 1 to n.
def Concatenating(lst, rn):
    new_lst = []
    for i in range(1, rn+1):
        for j in lst:
            new_lst.append(f'{j}{i}')
    print(new_lst)
Concatenating(['p', 'q'], 5)


# 4. Write a Python program to get variable unique identification number or string.
x = 100
print(format(id(x), 'x'))
s = 'w3resource'
print(format(id(s), 'x')) 


# 5. Write a Python program to find common items from two lists.
def GetCommon(lst1, lst2):
    s1 = set(lst1)
    s2 = set(lst2)
    print("Common Item is: ", list(s1 & s2))
GetCommon([1,2,3,4,5], [5,7,10])


# 6. Write a Python program to change the position of every n-th value with 
#    the (n+1)th in a list.
def replace2copy(lst):
    from itertools import zip_longest, chain, tee
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
n = [0,1,2,3,4,5]
print(replace2copy(n))


# 7. Write a Python program to convert a list of multiple integers into 
#    a single integer.
def Convert(lst):
    s = int(''.join(map(str, lst)))
    print(s)
Convert([11, 33, 50])


# 8. Write a Python program to create multiple lists.
def Create(n):
    obj = {}
    for i in range(1, n+1):
        obj[str(i)] = []
    print(obj)
Create(5)


# 9. Write a Python program to find missing and additional values in two lists.
def Missing(lst1, lst2):
    s1 = set(lst1)
    s2 = set(lst2)
    print("Missing values in second list: ", s1 - s2)
    print("Additional values in second list: ", s2 - s1)
Missing(['a','b','c','d','e','f'], ['d','e','f','g','h'])


# 10. Write a Python program to split a list into different variables.
def Split(lst):
    var1, var2, var3 = lst
    print(var1)
    print(var2)
    print(var3)
Split([("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
        ("Yellow", "#FFFF00", "rgb(255, 255, 0)")])


# 11. Write a Python program to generate groups of five consecutive numbers in a list.
def Consecutive(n):
    l = [[5*i + j for j in range(1,6)] for i in range(5)]
    print(l)
Consecutive(5)


# 12. Write a Python program to convert a pair of values into a sorted unique array.
def Pair(pv):
    lst = []
    fL = []
    for i in pv:
        for j in i:
            lst.append(j)
    for i in lst:
        if i not in fL:
            fL.append(i)
    print(fL)
    print("Sorted Unique Data:",sorted(set().union(*pv)))

Pair([(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
      (7, 8), (9, 10)])


# 13. Write a Python program to select the odd items of a list.
def Odd(lst):
    flst =  []
    for i in lst:
        if i % 2 != 0:
            flst.append(i)
    print("Odd Item List: ", flst)
Odd([1, 2, 3, 4, 5, 6, 7, 8, 9])


# 14. Write a Python program to insert an element before each element of a list.
def Insert(lst):
    fL = []
    for ele in lst:
        for i in ('kk', ele):
            fL.append(i)
    print(fL)
Insert(['Red', 'Green', 'Black'])


# 15. Write a Python program to print a nested lists (each list on a new line) 
#      using the print() function.
def Nested(lst):
    for i in lst:
        print(i)
Nested([['Red'], ['Green'], ['Black']])


# 16. Write a Python program to convert list to list of dictionaries.
def Convert(ls1, ls2):
    new_lst = []
    
    for l1, l2 in zip(ls1, ls2):
        new_lst.append({'color name':l1, 'color code':l2})
    print(new_lst)
Convert(["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"])


# 17. Write a Python program to sort a list of nested dictionaries.
def Sort(lst):
    lst.sort(key=lambda e: e['key']['subkey'], reverse=True)
    print(lst)
Sort([{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}])


# 18. Write a Python program to split a list every Nth element. 
def Split(lst, n):
    Ls = []
    for i in range(n):
        Ls.append(lst[i::n])
    print(Ls)
Split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3)


# 19. Write a Python program to compute the difference between two lists.
def Different(lst1, lst2):
    s1 = set(lst1)
    s2 = set(lst2)
    print(s1 - s2)
    print(s2 - s1)
Different(["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"])


# 20. Write a Python program to create a list with infinite elements.
def Create(n):
    lst = []
    for i in range(1, n+1):
        lst.append(i)
    print(lst)
Create(20)


