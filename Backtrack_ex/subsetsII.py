'''Simple excercise to create all subsets of a set of n characters'''
res = []
nums = [1,2,2]
curr_subset = []
def allsubsets(i):

    if i >= len(nums):
        res.append(curr_subset.copy())
        return
    curr_subset.append(nums[i])
    allsubsets(i+1)
    curr_subset.pop()
    if i < len(nums) -1 and nums[i] == nums[i+1]:
        i += 1
    allsubsets(i+1)


if __name__ == '__main__':
    allsubsets(0)
    print(res)
