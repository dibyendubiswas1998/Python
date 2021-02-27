
from functools import reduce

# 1. Write a Python program to create a function that takes one argument, 
#     and that argument will be multiplied with an unknown given number. 

res = lambda x: x*x
print(res(10))


# 2. Write a Python program to sort a list of tuples using Lambda.

lst = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
lst.sort(key=lambda x:x[1])
print(lst)


# 3. Write a Python program to sort a list of dictionaries using Lambda.

dct = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
sort_color = sorted(dct, key=lambda x:x['color'])
sort_model = sorted(dct, key=lambda x:int(x['model']))

print(sort_color)
print(sort_model)


# 4. Write a Python program to filter a list of integers using Lambda.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = list(filter(lambda x: x%2==0, lst))
print(res)


# 5. Write a Python program to square and cube every number in a given list of 
#     integers using Lambda.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = list(map(lambda x: x*2, lst))
print(res)


# 6. Write a Python program to find if a given string starts with a given character using Lambda.

st = "Dibyendu Biswas"
res = lambda x: True if x.startswith('D') else False
print(res(st))


# 7. Write a Python program to extract year, month, date and time using Lambda.

import datetime
now = datetime.datetime.now()

year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))


# 8. Write a Python program to create Fibonacci series upto n using Lambda.

res = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print(res(3))
print(res(5))


# 9. Write a Python program to find intersection of two given arrays using Lambda.

l1 = [1, 2, 3, 5, 7, 8, 9, 10]
l2 = [1, 2, 4, 8, 9]
res = lambda x,y: set(x).intersection(set(y))
print(res(l1, l2))


# 10. Write a Python program to rearrange positive and negative numbers in a given 
#      array using Lambda.

l1 = [-1, 2, -3, 5, 7, 8, 9, -10]
res = lambda x: sorted(x, reverse=True)
print(res(l1))


# 11. Write a Python program to count the even, odd numbers in a given array 
#      of integers using Lambda.

l1 = [1, 2, 3, 5, 7, 8, 9, 10]
even = len(list(filter(lambda x: x%2 ==0, l1)))
odd = len(list(filter(lambda x: x%2 !=0, l1)))
print(even)
print(odd)


# 12. Write a Python program to add two given lists using map and lambda.

l1 = [1, 2, 3]
l2 = [4, 5, 6]
add = list(map(lambda x,y: x+y, l1, l2))
print(add)


# 13. Write a Python program to find numbers divisible by nineteen or thirteen from 
#      a list of numbers using Lambda.

lst1 = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
res = list(filter(lambda x: x%13 == 0 or x%19 == 0, lst1))
print(res)


# 14. Write a Python program to find palindromes in a given list of strings using Lambda.

lst = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
res = list(filter(lambda x: (x == "".join(reversed(x))), lst))
print(res)


# 15. Write a Python program to find the numbers of a given string and store them 
#      in a list, display the numbers which are bigger than the length of the list in 
#      sorted form. Use lambda function to solve the problem.

st = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
st_num = list(i for i in st.split(' '))
length = len(st_num)
number = sorted(list(int(x) for x in st_num if x.isdigit()))
for i in ((filter(lambda x:x> length, number))):
    print(i,end=' ')


# 16. Write a Python program that multiply each number of given list with a given 
#      number using lambda function. Print the result. 

lst = [2, 4, 6, 9, 11]
res = list(filter(lambda x: x*2, lst))
print(res)


# 17. Write a Python program to calculate the sum of the positive and negative numbers 
#      of a given list of numbers using lambda function.

lst = [2, 4, -6, -9, 11, -12, 14, -5, 17]
positive = list(filter(lambda x: x>0, lst))
negative = list(filter(lambda x: x<0, lst))

print("Sum positive: ", sum(positive))
print("Sum negative: ", sum(negative))


# 18. Write a Python program to create the next bigger number by rearranging the digits 
#     of a given number.

def rearrange_bigger(n):
    #Break the number into digits and store in a list
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
n = 12
print("Original number:",n)
print("Next bigger number:",rearrange_bigger(n))

n = 10
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
      
n = 201
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
n = 102
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
n = 445
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))


# 19. Write a Python program to sort each sublist of strings in a given list of 
#      lists using lambda.

lst = [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
res = list(sorted(x, key=lambda x:x[0]) for x in lst)
print(res)


# 20. Write a Python program to sort a given matrix in ascending order according to 
#      the sum of its rows using lambda.

matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
res = list(sorted(matrix, key= lambda mat: sum(mat)))
print(res)


