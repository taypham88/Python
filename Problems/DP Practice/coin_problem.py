'''Coin Problem. Practice for Dynamic Programing'''

# Problem example: Coins:{1,4,5}, target 13
# return minium number of coins that makes the target

from collections import defaultdict
def min_ignore_none(a,b):
    '''ignores None'''
    if a is None:
        return b
    if b is None:
        return a
    return min(a,b)

# top down
def min_coins(m, coins):
    '''Simple Recusion without DP'''

    if m in memo:
        return memo[m]
    if m == 0:
        answer = 0
    else:
        answer = None
        for coin in coins:
            subproblem = m - coin
            if subproblem < 0:
                # avoid negative subproblems
                continue
            answer = min_ignore_none(answer, min_coins(subproblem, coins)+ 1)
    memo[m] = answer
    return answer

# bottom up
def bu_min_coin(m,coins):
    memo[0] = 0
    for i in range(1, m+1):
      for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                # avoid negative subproblems
                continue
            memo[i] = min_ignore_none(memo.get(i), memo.get(subproblem)+ 1)
    return memo[m]


if __name__ == '__main__':
    memo = defaultdict()
    print(min_coins(150, [1,4,5]))
    memo = defaultdict()
    print(bu_min_coin(150, [1,4,5]))

