L1 = ['arko', 'ram', 'shayam', 'jadu']
L2 = ['a1', 'b1', 'c1', 'd1']

#-----------------------------------------------------
L1.append('Dibyendu')
print(L1)

#-----------------------------------------------------
L2.insert(2, 'aa')
print(L2)

#-----------------------------------------------------
L1.extend(L2)
print(L1)

#-----------------------------------------------------
L3 = list('abcdefgh')
print(L3)
print(L3.index('b'))
L3.reverse()
print(L3)

#-----------------------------------------------------
l = [1, 2, 3, 4, 5, 6, 7]
L = []
for i in l:
    L.append(i*i)
print(l)
print(L)

#-----------------------------------------------------
LL = [i*i for i in l]
print(LL)

#-----------------------------------------------------
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L = list()
for i in l:
    if i % 2 == 0:
        L.append(i)
print(L)

#-----------------------------------------------------
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L = [ i for i in l if i%2 == 0]
print(L)

#-----------------------------------------------------
List = list()
for i in 'abcd':
    for j in range(1,5):
        List.append((i,j))
print(List)

#-----------------------------------------------------
List = [(i,j) for i in 'abcd' for j in range(1,5)]
print(List)

#-----------------------------------------------------
course = ['python', 'django', 'javascript', 'ML', 'DL']
for index, item in enumerate(course):
    print(f"{index} : {item}")

print('-'.join(course))
