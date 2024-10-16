'''
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].
'''

def shuffle(nums, n):
    ans =[]
    for i in range(n):
        ans.append(nums[i])
        ans.append(nums[i+n])
    return ans

nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums,n))