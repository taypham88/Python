#backtrack2


def permute(nums):
    res = []

    # base case
    if len(nums) == 1:
        return [nums[:]]  # nums[:] is a deep copy

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)
        print('nums', nums, 'n', n)

        for perm in perms:
            perm.append(n)
        res.extend(perms)
        print('res',res, 'perms', perms)
        nums.append(n)
    return res

print(permute([1,2,3]))