# #--------------------------------------- lambda method ----------------------------------------

rs = lambda x: x+2
print(rs(10))


r = lambda x: x*x
print(r(10))


rs = lambda x,y: x == y 
print(rs(10, 20))
print(rs(10, 10))


rp = lambda lst1, lst2: list(i +j for i in lst1 for j in lst2)
print(rp([10, 20, 30], [1, 2, 3]))


rp = lambda lst1, lst2: lst1+lst2
print(rp([10, 20, 30], [1, 2, 3]))



# #--------------------------------------filter() method -----------------------------------------

# normal function:
lst = [2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even(n):
    if n%2 == 0:
        return True
evens = list(filter(is_even, lst))
print("Even list: ", evens)


lst = [2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda n: n%2 == 0, lst))
print(evens)




# #--------------------------------------- map() method -----------------------------------------

lst = [10, 20, 30]
result = map(lambda x: x+x, lst)
print(list(result))


ls1 = [1, 2, 3]
ls2 = [10, 20, 30]
result = map(lambda i, j: i+j, ls1, ls2)
print(list(result))


ls1 = [1, 2, 3]
ls2 = [10, 20, 30]
result = list(map(lambda i, j: i+j, ls1, ls2))
print(result)


def to_upper(n):
    return n.upper()
l = ['arko', 'dibyendu']
result = list(map(to_upper, l))
print(result)


l = ['arko', 'dibyendu']
result = list(map(lambda x: x.upper(), l))
print(result)


a = [1, 2, 3]
b = [4, 5, 6]
c = [1, 2, 1]
r1 = list(map(lambda i,j: i+j, a,b))
r2 = list(map(lambda i,j,k: i+j+k, a,b,c))
print("Result1: ", r1)
print("Result2: ", r2)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: x%2==0, lst))
print("Even list: ", result) # # Even list:  [False, True, False, True, False, True, False, True, False, True]




# #----------------------------------- reduce() method --------------------------------------

from functools import reduce

lst = [10, 20, 30, 40]
s= 0
for i in lst:
    s += i
print(s)


def Add(n, m):
    return n+m
lst = [10, 20, 30, 40, 50]
result = reduce(Add, lst)
print("Sum value: ", result)


lst = [10, 20, 30, 40, 50]
result = reduce(lambda x,y: x+y, lst)
print("Sum value: ", result)


lst = [1, 2, 3, 4]
result = reduce(lambda i,j: i*j, lst)
print("Product: ", result)


s = 'cat'
s2 = 'act'
 

if set(s) - set(s2):
    print('yes')
else:
    print('no')