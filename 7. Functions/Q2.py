# # 1. Write a Python program to extract specified size of strings from a give list of 
# #      string values using lambda.

# st = ['Python', 'list', 'exercises', 'practice', 'solution']
# res = lambda x: len(x[0])
# print(res(st))


# # 2. Write a Python program to count float number in a given mixed list using lambda.
# lst = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# res = map(lambda x: isinstance(x, float), lst)
# len = len([x for x in res if x])
# print(len)


# # 3. Write a Python program to check whether a given string contains a capital letter, 
# #     a lower case letter, a number and a minimum length using lambda.
# str = "Dibyendu12"
# cp = lambda st: any(x.isupper() for x in st)
# lw = lambda st: any(x.islower() for x in st)
# nm = lambda st: any(x.isdigit() for x in st)
# ln = lambda st: len(st)>=7
# if cp(str)==True and lw(str)==True and nm(str)==True and ln(str)==True:
#     print("Valid String")
# else:
#     print("not valid")  


# # 4. Write a Python program to filter the height and width of students, which are 
# #     stored in a dictionary using lambda.
# dct = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# res = dict(filter(lambda x: (x[1][0], x[1][1])>(6.0, 70), dct.items()))
# print(res)

# # 5. Write a Python program to check whether a specified list is sorted or not using lambda.
# lst = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# def is_sorted_list(nums, key=lambda x:x):
#     for i, e in enumerate(nums[1:]):
#         if key(e) < key(nums[i]):
#             return False
#     return True
# print(is_sorted_list(lst))


# # 6. Write a Python program to extract the nth element from a given list of tuples using lambda.
# lst = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# n = 0
# res = list(map(lambda x: x[n], lst))
# print(res)


# # 7. Write a Python program to sort a list of lists by a given index of the inner list using lambda.
# lst = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# n = 1
# res = sorted(lst, key=lambda x:x[n])
# print(res)


# # 8. Write a Python program to remove all elements from a given list present in another 
# #     list using lambda.
# ls1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ls2 =  [2, 4, 6, 8]
# res = lambda x, y: set(x)-set(y)
# print(list(res(ls1, ls2)))



# # 9. Write a Python program to find the elements of a given list of strings that contain 
# #     specific substring using lambda.
# lst = ['red', 'black', 'white', 'green', 'orange']
# sub = 'ack'
# def Check(lst, sub):
#     res = list(filter(lambda x: sub in x, lst))
#     print(res)
# Check(lst, sub)
# Check(lst, 'abc')



# # 10. Write a Python program to find the nested lists elements, which are present in 
# #      another list using lambda.
# lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# lst2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# def Nested(ls1, ls2):
#     res = [list(filter(lambda x: x in ls1, sublist)) for sublist in ls2]
#     print(res)
# Nested(lst1, lst2)


# start at 41