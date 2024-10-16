'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

'''

def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    ans = []
    map1, map2= {}, {}
    for i, value in enumerate(list1):
        if value not in map1:
            map1[value] = i
    for i, value in enumerate(list2):
        if value not in map2:
            map2[value] = i
    mins=float("inf")
    for i in map1:
        if i in map2:
            sum_values = map1[i] + map2[i]
            if sum_values < mins:
                ans =[]
                mins = sum_values
                ans.append(i)
            elif sum_values == mins:
                ans.append(i)
    return ans

list1= ["S","TEXP","BK","KFC"]
list2 = ["KFC","BK","S"]
print(findRestaurant(list1, list2))