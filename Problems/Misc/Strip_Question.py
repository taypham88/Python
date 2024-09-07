# Practice Question

# Let's say there are at most 500 bank accounts, some of their balances are above 100 and some are below.
# How do you move money between them so that they all have at least 100?

accounts = [
            ["EU", 70],
            ["US", 80],
            ["FF", 80],
            ["FR", 120],
            ["AU", 150],
        ]

# multiple accounts needed to fill one account
# accounts = [
#             ["US", 70],
#             ["FR", 110],
#             ["GB", 110],
#             ["AU", 110],
#         ]

# not enough money in system
# accounts = [
#             ["US", 70],
#             ["FR", 110],
#             ["GB", 110],
#         ]

under, over, ans = [],[],[]
record = []
# split the problem into two array
[over.append(account) if account[1] > 100 else under.append(account) for account in accounts]

# keep track of which accounts we are looking at during this loop iteration
current_under = 0
current_over = 0

# bonus validations that are good to mention in an interview even if you don't actually code these:
# do we need to move any money at all? Then we can just exit now! (you did this already by checking the len(under) list in your original code)
# is there enough money in the system to even do anything? We should fail right away to avoid weird mistakes. (make sure average amount in each account is > 100)
# checking these validations ahead of time just makes sure the core algorithm doesn't run into any unexpected edge cases

# if we run out of accounts to look at, stop looking
while(current_under < len(under) and current_over < len(over)):
    # core idea for the algorithm:
    # look at the first 'over' and 'under' account in each list and compare the amounts to figure out what we need to do.
    # After every run of the loop, one of these three things has to have happened.
    # we have completely fixed the 'under' account to have enough money
    # we have completely drained the 'over' account and can't use it any longer
    # or both of these things happened, (if the 'under' account needed exactly what the 'over' account had), and we can't use either account any longer


    valueNeeded = 100 - under[current_under][1]
    valueAvailable = over[current_over][1] - 100

    if valueAvailable > valueNeeded:
        # we have more available than we need, so take enough money to finish the 'under' account
        under[current_under][1] += valueNeeded
        over[current_over][1] -= valueNeeded
        record.append(f'{over[current_over][0]} - {valueNeeded}, {under[current_under][0]} + {valueNeeded}')
        # move the 'under' index so we start looking at the next account and ignore this one
        current_under += 1
    elif valueAvailable < valueNeeded:
        # we don't have enough money to fix this account, so take what we can and finish the 'over' account
        under[current_under][1] += valueAvailable
        over[current_over][1] -= valueAvailable
        record.append(f'{over[current_over][0]} - {valueAvailable}, {under[current_under][0]} + {valueAvailable}')
        # move the 'over' index so we start looking at the next account and ignore this one
        current_over += 1
    else:
        # we have exactly enough money available that we need, so take it and close both accounts at once
        under[current_under][1] += valueAvailable
        over[current_over][1] -= valueAvailable
        record.append(f'{over[current_over][0]} - {valueAvailable}, {under[current_under][0]} + {valueAvailable}')
        # move the 'under' index so we start looking at the next account and ignore this one
        current_over += 1
        # move the 'over' index so we start looking at the next account and ignore this one
        current_under += 1

# A super bonus validation that would score awesome points during an interview (but not required)
# Validate the moves the algorithm did actually make sense
# (way 1: this is what this algo does) Algorithm updates the state of each account as it makes changes. After algo runs, we can check every account to make sure they each have amount > 100
# Or
# (way 2) Algorithm only tracks each time money moves between accounts and doesn't update the account data. After algo runs, we can duplicate the original state of the accounts in a temporary list, do each transaction to every account in the list, and then validate the account amounts are all > 100


print(record)
print(under + over)