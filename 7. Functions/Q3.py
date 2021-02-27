
# Map:

# 1. Write a Python program to triple all numbers of a given list of integers. Use Python map.
lst = [1, 2, 3, 4, 5]
res = list(map(lambda x: x+x+x, lst))
print(res)


# 2. Write a Python program to add three given lists using Python map and lambda.
ls1 = [1, 2, 3]
ls2 = [10, 20, 30]
ls3 = [5, 6, 7]
res = list(map(lambda x,y,z: x+y+z, ls1, ls2, ls3))
print(res)


# 3. Write a Python program to listify the list of given strings individually using Python map.
color = ['Red', 'Blue', 'Black', 'White', 'Pink'] 
res = list(map(list, color))
print(res)


# 4. Write a Python program to create a list containing the power of said number in bases 
#     raised to the corresponding number in the index using Python map.
bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(pow, bases_num, index))
print(result)



# 5. Write a Python program to square the elements of a list using map() function.
def Square(lst, n):
    res = list(map(lambda x: x**n, lst))
    print(res)
Square([2, 3, 4], 2)



# 6. Write a Python program to convert all the characters in uppercase and lowercase and 
#     eliminate duplicate letters from a given sequence. 
def Convert(ch):
    upp = list(map(lambda x: x.upper(), ch))
    lww = list(map(lambda x: x.lower(), ch))
    print("".join(upp))
    print("".join(lww))
Convert("Dibyendu")


# 7. Write a Python program to add two given lists and find the difference between lists. 
lst1 = [2, 3, 4, 5]
lst2 = [10, 20, 30, 40]
def ADiff(ls1, ls2):
    add = list(map(lambda x,y: x+y, ls1, ls2))
    print("Adding list: ", add)
    dif = list(map(lambda x, y: x-y, ls1, ls2))
    print("Difference between list1 and list2: ", dif)
ADiff(lst1, lst2)



# 8. Write a Python program to convert a given list of integers and a tuple of integers 
#     in a list of strings.
lst = [1, 2, 3, 4]
tup = (1, 2, 3, 4)
res_lst = list(map(str, lst))
res_tup = tuple(map(str, tup))
print("List: ", res_lst)
print("Tuple: ", res_tup)



# 9. Write a Python program to convert a given list of integers and a tuple of 
#     integers in a list of strings.
data = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), 
        ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]

name = list(map(lambda x: x[0], data))
dob = list(map(lambda x:x[1], data))
print(name)
print(dob)



# 10. Write a Python program to find the ratio of positive numbers, negative numbers 
#      and zeroes in an array of integers.
from array import array
def plusMinus(nums):
    n = len(nums)
    n1 = n2 = n3 = 0
    
    for x in nums:
        if x > 0:
            n1 += 1
        elif x < 0:
            n2 += 1
        else:
            n3 += 1   
    return round(n1/n,2), round(n2/n,2), round(n3/n,2)
nums = array('i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
print("Original array:",nums)
nums_arr = list(map(int, nums))
result = plusMinus(nums_arr)
print("Ratio of positive numbers, negative numbers and zeroes:")
print(result)
nums = array('i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
print("\nOriginal array:",nums)
nums_arr = list(map(int, nums))
result = plusMinus(nums_arr)
print("Ratio of positive numbers, negative numbers and zeroes:")
print(result)
   


# 11. Write a Python program to count the same pair in two given lists. use map() function.
ls1 = [1,2,3,4,5,6,7,8]
ls2 = [2,2,3,1,2,6,7,9]
from operator import eq
res = sum(map(eq, ls1, ls2))
print("Number of Pair: ", res)



# 12. Write a Python program to interleave two given list into another list randomly 
#      using map() function.
import random
lst1 = [1,2,7,8,3,7]
lst2 = [4,3,8,9,4,3,8,9]
res  = list(map(next, random.sample([iter(lst1)]*len(lst1) + [iter(lst2)]*len(lst2), len(lst1)+len(lst2))))
print(res)



# 13. Write a Python program to split a given dictionary of lists into list of 
#      dictionaries using map function.
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
res = list(map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()])))
print(res)



# 14. Write a Python program to convert a given list of tuples to a list of strings 
#      using map function.
color = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
res = list(map(' '.join, color))
print(res)
