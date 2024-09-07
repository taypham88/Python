'''
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
For each such pair, there are freq elements with value val concatenated in a sublist.
Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.
'''

def decompressRLElist(nums):
    # ans = []
    # for i in range(0, len(nums), 2):
    #     for _ in range(0, nums[i]):
    #         ans.append(nums[i+1])
    # return ans
    ans = []
    temp = 0
    amount = 0
    for i in range(0,len(nums),2):
        amount = nums[i]
        temp = nums[i+1]
        for j in range(0,amount):
            ans.append(temp)
    return ans

a = [1,2,3,4]
print(decompressRLElist(a))
