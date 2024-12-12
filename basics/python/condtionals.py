n = 1

# If statements don't need parenthesis
# or curly braces
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

print("n = ", n)

# Parenthesis is needed for multi-line conditions
# and = &&
# or = ||

n, m = 1, 2
if (n > 2 and n != m) or n == m:
    n += 1
