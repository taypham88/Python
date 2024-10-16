'''
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements
on the secondary diagonal that are not part of the primary diagonal.
'''

def diagonalSum(mat):
    sum = 0
    i, n = 0, len(mat) -1
    for array in mat:
        if i == n:
            sum += array[i]
        else:
            sum += array[i] + array[n]
        n -= 1
        i += 1
    return sum



mat = [[5]]
print(diagonalSum(mat))