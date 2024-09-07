'''Simple excercise to create all subsets of a set of n characters'''
'''See mind map of backtrack subsets, this dosn't eleminate dublicats'''
res = []
nums = [1,2,3]
curr_subset = []
def allsubsets(i):

    if i >= len(nums):
        res.append(curr_subset[:])
        return
    curr_subset.append(nums[i])
    allsubsets(i+1)
    curr_subset.pop()
    allsubsets(i+1)

if __name__ == '__main__':
    allsubsets(0)
    print(res)
