'''

'''

def countNegatives(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    count = 0
    for array in grid:
        for indx in range(len(array)-1,-1,-1):
            if array[indx] < 0:
                count +=1
            else:
                break
    return count

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(countNegatives(grid))