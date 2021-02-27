# 20. Questions:-----

import array as arr

# 1. Write a Python program to create an array of 5 integers and display 
#     the array items. Access individual element through indexes.
ar = arr.array('i', [1, 3, 5, 9, 7])
print(ar)
print(ar[0])
print(ar[3])


# 2. Write a Python program to append a new item to the end of the array.
ar = arr.array('i', [1, 3, 5, 9, 7])
ar.append(20)
print(ar)


# 3. Write a Python program to reverse the order of the items in the array.
ar = arr.array('i', [1, 3, 5, 9, 7])
ar.reverse()
print(ar)


# 4. Write a Python program to get the length in bytes of one array item in 
#     the internal representation.
ar = arr.array('i', [1, 3, 5, 9, 7])
print(ar.itemsize)


# 5. Write a Python program to get the current memory address and the length
#     in elements of the buffer used to hold an array's contents and also 
#     find the size of the memory buffer in bytes.
ar = arr.array('i', [1, 3, 5, 9, 7])
print(ar.buffer_info())


# 6. Write a Python program to get the number of occurrences of a specified 
#     element in an array.
ar = arr. array('i', [1, 3, 5, 3, 7, 9, 3])
print(ar.count(3))


# 7. Write a Python program to append items from inerrable to the end of the array.
ar1 = arr. array('i', [1, 3, 5, 3, 7, 9, 3])
ar2 = arr.array('i', [1, 3, 5, 9, 7])
ar1.extend(ar2)
print(ar1)


# 8. Write a Python program to convert an array to an array of machine values 
#     and return the bytes representation.
ar = arr.array('b', [119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
print(ar.tobytes())


# 9. Write a Python program to append items from a specified list.
lst = [10, 20, 30, 40]
ar = arr.array('i', lst)
print(ar)
print(type(ar))


# 10. Write a Python program to insert a new item before the second element in 
#      an existing array.
arx = arr.array('i', [1, 3, 5, 7, 9])
arx.insert(1, 4)
print(arx)


# 11. Write a Python program to remove a specified item using the index from an array.
arx = arr.array('i', [1, 3, 5, 7, 9])
arx.pop(2)
print(arx)


# 12. Write a Python program to remove the first occurrence of a specified element from an array.
ar = arr.array('i', [1, 3, 5, 3, 7, 1, 9, 3])
ar.remove(3)
print(ar)


# 13. Write a Python program to convert an array to an ordinary list with the same items.
ar = arr.array('i', [1, 3, 5, 3, 7, 1, 9, 3])
lst = []
for i in ar:
    lst.append(i)
print("List: ", lst)


# 14. Write a Python program to find whether a given array of integers contains 
#      any duplicate element. Return true if any value appears at least twice in 
#      the said array and return false if every element is distinct.
def Check(ar):
    result = 'False'
    ar_set = set(ar)
    if len(ar) != len(ar_set):
        result = 'True'
    else:
        result = 'False'
    print(result)

Check(arr.array('i', [1, 3, 5, 3, 7, 1, 9, 3]))
Check(arr.array('i', [1, 3, 5, 2]))


# 15. Write a Python program to find the first duplicate element in a given 
#      array of integers. Return -1 If there are no such elements. 
def Check(ar):
    result = -1
    ar_set = set(ar)
    if len(ar) != len(ar_set):
        result = 1
    else:
        result = -1
    print(result)

Check(arr.array('i', [1, 3, 5, 3, 7, 1, 9, 3]))
Check(arr.array('i', [1, 3, 5, 2]))


# 16. Write a Python program to check whether it follows the sequence given 
#       in the patterns array.
def is_samePatterns(colors, patterns):    
    if len(colors) != len(patterns):
        return False    
    sdict = {}
    pset = set()
    sset = set()    
    for i in range(len(patterns)):
        pset.add(patterns[i])
        sset.add(colors[i])
        if patterns[i] not in sdict.keys():
            sdict[patterns[i]] = []

        keys = sdict[patterns[i]]
        keys.append(colors[i])
        sdict[patterns[i]] = keys

    if len(pset) != len(sset):
        return False   

    for values in sdict.values():

        for i in range(len(values) - 1):
            if values[i] != values[i+1]:
                return False

    return True
print(is_samePatterns(["red", 
 "green", 
 "green"], ["a", 
 "b", 
 "b"])) 
print(is_samePatterns(["red", 
 "green", 
 "greenn"], ["a", 
 "b", 
 "b"])) 


# 17. Write a Python program to find a pair with highest product from 
#      a given array of integers.
def Highest(ar):
    if (len(ar) < 2):
        print("No Pair Exist")
    else:
        x = ar[0]
        y = ar[1]
        for i in range(len(ar)):
            for j in range(i+1, len(ar)):
                if (ar[i] * ar[j] > x * y):
                    x = ar[i]
                    y = ar[j]
        print((x, y))

Highest([1, 2, 3, 4, 7, 0, 8, 4])


# 18. Write a Python program to create an array contains six integers. 
#      Also print all the members of the array.
print(arr.array('i', [10, 20, 30, 40, 50, 60]))


# 19. Write a Python program to get the array size of types unsigned integer and float.
a = arr.array("I", (12, 25))
print(a.itemsize)
b = arr.array("f", (12.236, 36.36))
print(b.itemsize)


# 20. Write a Python program to read a string and interpreting the string as 
#      an array of machine values
import binascii
ar = arr.array('i', [7, 8, 9, 10])
print('Bytes: ', binascii.hexlify(ar.tobytes()))

