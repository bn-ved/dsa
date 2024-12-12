# HashSet
myset = set()

myset.add(1)
myset.add(2)

print(myset)
print(len(myset))

print(1 in myset)
print(2 in myset)
print(3 in myset)


myset.remove(2)
print(2 in myset)

# list to set
print(set([1, 2, 3]))

# Set Comprehension
myset = {i for i in range(5)}
print(myset)
