# Assigment during class. Find 4 ways to print a series of numbers from 1 through 10
a = list(range(1,11))

# First, use a for loop
for x in range(len(a)):
    print(a[x])

# Second, use a while loop
b = 1
while b < len(a):
    print(a[b])
    b = b + 1

# Third, use the print list command
print(*a)

# Forth, combo of join() and map()
print('\n'.join(map(str,a)))