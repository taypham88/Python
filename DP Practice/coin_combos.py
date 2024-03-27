'Coin Problem 2'
# given a set of coins, how many ways can we construct the target value.

from collections import defaultdict

def returnNone(input):
    if input is None:
        return 0
    return input

def coin_combo(m,coins):
    if m in memo:
        return memo[m]
    if m == 0:
        return 1
    else:
        answer = 0
        for coin in coins:
            subproblem = m - coin
            if subproblem < 0:
                continue
            answer = answer + coin_combo(subproblem, coins)
    memo[m] = answer
    return answer

def coin_combo_bottom(m,coins):
    memo[0] = 1
    for i in range(1,m+1):
        memo[i] = 0
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue

            memo[i] = returnNone(memo.get(i)) + returnNone(memo.get(subproblem))
    return memo[m]

if __name__ == '__main__':

    memo = defaultdict()
    print(coin_combo(87, [1,4,5,8]))
    memo = defaultdict()
    print(coin_combo_bottom(87, [1,4,5,8]))