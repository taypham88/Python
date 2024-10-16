'''Given a total due and an array representing the amount of change in your pocket, determine whether or not you are able to pay for the item.
Change will always be represented in the following order: quarters, dimes, nickels, pennies.
Example: changeEnough([25, 20, 5, 0], 4.25) return true because:
25 quarters, 20 dimes, 5 nickels and 0 pennies gives you 6.25 + 2 + .25 + 0 = 8.50.
This means you can afford the item, so return true.'''

def changeEnough(change, total):
    total = int(total * 100)
    money = 0
    for i,amount in zip([25, 10, 5, 1],change):
        money += amount * i
    return money >= total

if __name__ == '__main__':
    print(changeEnough([2, 100, 0, 0], 14.11))
    print(changeEnough([0, 0, 20, 5], 0.75))
    print(changeEnough([30, 40, 20, 5], 12.55))
    print(changeEnough([10, 0, 0, 50], 3.85))
    print(changeEnough([1, 0, 5, 219], 19.99))