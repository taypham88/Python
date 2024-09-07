'''
You are given an m x n integer grid accounts where accounts[i][j] is the amount of
money the customer has in the bank. Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.
'''

def maximumWealth(accounts):
    total = []
    for i in accounts:
        total.append(sum(i))
    return max(total)

accounts = [[1,2,3],[3,2,1]]
print(maximumWealth(accounts))


