'''
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.
'''

def countMatches(items, ruleKey, ruleValue):
    count =0
    key ={'type': 0, 'color': 1, 'name': 2}
    rule = key[ruleKey]
    for i in range(len(items)):
        if items[i][rule] == ruleValue:
            count += 1
    return count

items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"

print(countMatches(items, ruleKey, ruleValue))