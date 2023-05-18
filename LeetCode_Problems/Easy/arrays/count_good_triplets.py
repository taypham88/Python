'''
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c

'''

def countGoodTriplets(arr, a, b, c):
    count = 0
    n = len(arr)
    # for i in range(n):
    #     for j in range(i+1, n):
    #         for k in range(j+1, n):
    #             if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
    #                 count += 1
    #             print(arr[i],arr[j],arr[k])
    # return count
# this one runs a bit faster than brute force.
# also set up the math to make it eliminate faster.
    if a > b + c:
        a = b + c
    elif b > a + c:
        b = a + c
    for i in range(n-2):
        for j in range(i+1, n-1):
            if abs(arr[i] - arr[j]) > a: continue
            for k in range(j+1, n):
                if abs(arr[j] - arr[k]) > b: continue
                if abs(arr[i] - arr[k]) > c: continue
                count += 1
    return count



arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
print(countGoodTriplets(arr, a, b, c))