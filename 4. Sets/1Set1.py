a1 = {1,2,3,4,5}
a2 = {10,11,12,13}
a3 = {1,4,10,22,11,13}

# delete 4:--
a1.discard(4)
print(a1)

# union:--
print(a1 | a2)
print(a1 | a2 | a3)

# Common Element:--
print(a1 & a3)

# Difference:--
print(a1 - a3)
print(a3 - a1)
print(a3 - a3)

# Symmetric Difference (Uncommon Element):--
print(a1 ^ a2)
print(a3 ^ a2)
print(a1 ^ a3)

print(list(a2))
print(set(list(a2)))

mySet = set()
for i in a3:
    mySet.add(i)
print(mySet)

