

def power(a, n):
    if n==0:
        return 1
    x = power(a,n/2)
    if n % 2 == 0:
        return x**2
    else:
        return a * x**2

print(power(2,2))
# print(power(2,10))