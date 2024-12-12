# Strings are similar to array
s = "abc"
print(s[0:2])

# So each time it creates a new string
s += "def"
print(s)

# Valid numeric string can be converted
print(int("123") + int("123"))

# Numbers can be converted to string
print(str(123) + str(123))

# ASCII values can be calculated by using "ord" function
print(ord("a"))
print(ord("b"))

# Combine List of strings
strings = ["ab", "cd", "ef"]
print("".join(strings))
