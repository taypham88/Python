'''Fibonacci. Classic DP practice problem.'''

def fib_recruse(n):
    '''fibonacci sequence'''
    if n in memo:
        return memo[n]

    if n <= 2:
        result = 1
    else:
        result = fib_recruse(n-1) + fib_recruse(n-2)

    memo[n] = result
    return result

def fib_bottom_up(n):
    '''fibonacci sequence using bottom up'''

    for i in range(1, n+1):
        if i <= 2:
            result = 1
        else:
            result = memo[i-1] + memo[i-2]
        memo[i] = result
    return memo[n]

if __name__ == "__main__":
    memo = {}
    print(fib_recruse(20))
    memo = {}
    print(fib_bottom_up(20))

