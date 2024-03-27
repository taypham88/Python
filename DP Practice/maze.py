'Dynamic Programing Maze Problem'
# Given an NXM grid. if a rabbit can only move forward and down, how many unique ways can it make it to the botoom?


def grid_paths(n,m):
    memo ={}

    for i in range(1, n+1):
        memo[(i,1)] = 1
    for j in range(1,m+1):
        memo[(1,j)] = 1

    for i in range(2, n+1):
        for j in range(2, m+1):
            memo[(i,j)] = memo[(i-1, j)] + memo[(i, j-1)]
    return memo[(n,m)]

if __name__ == '__main__':
    print(grid_paths(18,6))