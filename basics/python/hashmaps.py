# Hashmap
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
print(len(myMap))

myMap["alice"] = 80
print("alice" in myMap)

myMap.pop("alice")
print("alice" in myMap)

myMap = {"alice": 90, "bob": 70}
print(myMap)

# Dict Comprehension
intMap = {i: 2 * i for i in range(5)}
print(intMap)

# Looping
for key in myMap:
    print(key, myMap[key])

for value in myMap.values():
    print(value)

for key, value in myMap.items():
    print(key, value)
