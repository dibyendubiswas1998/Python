# 20 Questions:--------

# 1. Write a Python program to sum all the items in a list
def sum_list(List):
    sum = 0
    for i in List:
        sum += i
    print("Sum of all: ", sum)
sum_list([1, 2, 3, 4])
sum_list([10, 20, -35, 6])


# 2. Write a Python program to multiplies all the items in a list.
def mul_list(List):
    mul = 1
    for i in List:
        mul *= i
    print("Multiplies: ", mul)
mul_list([10,20,2])
mul_list([10,20,-2])


# 4. Write a Python program to get the smallest number from a list.
def Smallest_list( list ):
    small = list[ 0 ]
    for i in list:
        if i < small:
            small = i
    print("Smallest Number: ", small)
Smallest_list([1, 2, -8, 0])


# 5. Write a Python program to count the number of strings where the string 
#    length is 2 or more and the first and last character are 
#    same from a given list of strings
def GetAns(List):
    for i in List:
        if len(i) >= 2 and i[0] == i[-1]:
            print(i)
GetAns(['abc', 'xyz', 'aba', '1221'])


# 6. Write a Python program to get a list, sorted in increasing order by the last element 
#    in each tuple from a given list of non-empty tuples.
def last(n): 
    return n[-1]
def sort_list_last(tuples):
  return sorted(tuples, key=last)
print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# 7. Write a Python program to remove duplicates from a list.
def Duplicate(list):
    L = []
    for i in list:
        if i not in L:
            L.append(i)
    print(L)
Duplicate([50,10,20,30,10,40,20,50])
Duplicate([5,10,200,30,10,40,20,50])


# 8. Write a Python program to check a list is empty or not.
def Check(list):
    if not list:
        print('Empty List')
    else:
        print("Not Empty")
Check([10,2,30])
Check([])


# 9. Write a Python program to clone or copy a list.
def Copy(original):
    duplicate = list(original)
    duplicate[0] = 1000
    print("Original List is: ", original)
    print("Duplicate List is: ", duplicate)
Copy([10,20,30,40])


# 10. Write a Python function that takes two lists and returns True if they 
#     have at least one common member.
def Common(l1, l2):
    result = 'No'
    for i in l1:
        for j in l2:
            if i == j:
                result = 'Yes'
    print("Both List is Common: ", result)
Common([10,20,30,40], [5,10,30,1,2])
Common([1,2,3,4], [5,6,7,8,9])


# 11. Write a Python program to print a specified list after removing the 0th, 
#     4th and 5th elements.
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)


# 12. Write a Python program to shuffle and print a specified list.
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)


# 13. Write a Python program to generate all permutations of a list in Python.
import itertools
print(list(itertools.permutations([1,2,3])))


# 14. Write a Python program to get the difference between the two lists.
L1 = [10,20,30,40,50,60,70]
L2 = [1,5,7,8,10,50,40,10]
LL1 = list(set(L1)-set(L2))
LL2 = list(set(L2)-set(L1))
print(LL1+LL2)


# 15. Write a Python program access the index of a list.
L1 = [10,20,30,40,50,60,70]
for index, ele in enumerate(L1):
    print(f"{index}  {ele}")


# 16. Write a Python program to flatten a shallow list.
List = [[1,2,3], [10,20,30], [-10,-20,100]]
ShallowList = []
for i in List:
    for j in i:
        ShallowList.append(j)
print("Shallow List: ", ShallowList)


# 17. Write a Python program to select an item randomly from a list.
import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))


# 18. Write a python program to check whether two lists are circularly identical.
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))


# 19. Write a Python program to find the second smallest number in a list.
def secSmallest(numbers):
    if len(numbers) <= 2:
        print("Can't Find Second Smallest")
    else:
        sm2 = sorted(numbers)
        print("Second Smallest: ", sm2[1])
secSmallest([10,1,30,67,-10,100])
secSmallest([2,2])
secSmallest([])


# 20. Write a Python program to count the number of elements in a list within a specified range
def WithinRange(List, mn, mx):
    count = 0
    for i in List:
        if mn <= i <= mx:
            count += 1
    
    print('Presents of elements within range is: ', count)
List = [10,20,30,40,40,40,70,80,99]
WithinRange(List, 40,100)
