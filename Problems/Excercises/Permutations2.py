#backtrack2


def permute(nums):
    res = []

    # base case
    if len(nums) == 1:
        return [nums[:]]  # nums[:] is a deep copy

    for i in range(len(nums)):
        n = nums.pop(0)
        print('nums', nums, 'n', n)
        perms = permute(nums)

        print('res',res, 'perms', perms)

        for perm in perms:
            perm.append(n)
        
        print('res',res, 'perms', perms)
        res.extend(perms)
        nums.append(n)
    return res

print(permute([1,2,3]))