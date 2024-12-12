# Division is decimal by default
print(5 / 2)

# Double slash rounds down
print(5 // 2)

# Negative numbers will round down (other languages round towards 0)
print(-5 // 2)

# A workaroud for rounding towards 0
# is to use decimal division and then convert it to int
print(int(-5 / 2))

# Mod is similar to other languages
print(10 % 3)

# Except for negative values
print(-10 % 3)

# To have consistent mod as per other languages we can use
import math
from multiprocessing import heap

print(math.fmod(-10, 3))

# More math function
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(4))
print(math.pow(2, 3))

# Max / Min int
float("inf")
float("-inf")

# python numbers are infinie so they never overflow
