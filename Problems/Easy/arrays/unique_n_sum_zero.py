

def sumZero(n):
    ans = []
    if n == 1:
        return [0]
    if n % 2 != 0:
        ans = [0]
    for i in range(1, n//2 + 1):
        ans.append(i)
        ans.append(-i)
    return ans

n = 5
print(sumZero(n))