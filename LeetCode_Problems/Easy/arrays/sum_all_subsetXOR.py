'''
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums.

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
'''

def find_all_subsets(arr):

    # def combinations(input):
    #     if len(input) == 0:
    #         return [[]]

    #     combos = []
    #     for item in combinations(input[1:]):
    #         combos += [item, item + [input[0]]]

    #     return combos

    # combos = combinations(arr)
    # ans = 0
    # for combo in combos:
    #     result = 0
    #     for item in combo:
    #         result ^= item
    #     ans += result
    # return ans

    result = [0]
    for num in nums:
        # print(result,num)
        # result += [r ^ num for r in result]

    return sum(result), result




nums = [5,1,6]
print(find_all_subsets(nums))


