# Arrays (They are list in python)
nums = [1, 2, 3, 4]
print(nums)


# Can be used as stack
nums.append(5)
nums.append(6)
print(nums)

nums.pop()
print(nums)

# Insert at certain position
nums.insert(1, 7)
print(nums)

# Access array elements as per their location
nums[0] = 0
nums[1] = 0
print(nums)

# Initialize array with default value 1
n = 5
nums = [1] * n
print(nums)
print(len(nums))  # get length

# -1 is not out of bounds it is the last elements
nums = [1, 2, 3, 4, 5]
print(nums[-1])

# print array with given range
print(nums[0:4])

# No array index out of bounds error
print(nums[0:10])

# Unpacking Array
a, b, c, d, e = [1, 2, 3, 4, 5]
print(a, b, c, d, e)


# Looping Through Arrays
nums = [1, 2, 3, 4, 5]

# index based Looping
for i in range(len(nums)):
    print(nums[i])

# Without index
for n in nums:
    print(n)

# With index and value
for i, n in enumerate(nums):
    print(i, n)

# Looping through multipl Arrays
p = [1, 2, 3]
q = [4, 5, 6]

for a, b in zip(p, q):
    print(a, b)

# Reverse
arr = [1, 2, 3]
arr.reverse()
print(arr)

# Sorting
arr.sort()
print(arr)

# Sorting in reverse order
arr.sort(reverse=True)
print(arr)

# Custom sort
str_arr = ["bob", "alice", "jane", "done"]
str_arr.sort(key=lambda x: len(x))
print(str_arr)

# List comprehension
arr = [i for i in range(5)]
print(arr)

# 2-D list
arr_ = [[0] * 4 for i in range(4)]
print(arr_)
