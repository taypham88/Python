#--- Advent of code 2024---
#--- Day 6: Guard Gallivant ---


import os

current_directory = os.getcwd()
file_name = 'input.txt'
file_path = os.path.join(current_directory, file_name)


Graph = []
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        Graph.append(list(line.strip()))

row, col = len(Graph), len(Graph[0])

def find_start(Graph):

    for i in range(row):
        for j in range(col):
            if Graph[i][j] == '^':
                return (i,j)

def rotate_clockwise(direction):
    x, y = direction
    return (y, -x)

def count_x(Graph):
    count = 0
    for i in range(row):
        for j in range(col):
            if Graph[i][j] == 'X':
                count += 1
    return count

x, y = find_start(Graph)
Direction = (-1,0) # up

while 0 <= x < row and 0 <= y < col:
    nx,ny = x + Direction[0], y + Direction[1]
    if 0 <= nx < row and 0 <= ny < col:
        if Graph[nx][ny] != '#':
            Graph[nx][ny] = 'X'
        else:
            Direction = rotate_clockwise(Direction)
            nx,ny = x, y
    x,y = nx,ny

print(count_x(Graph))

# for line in Graph:
#     print(line)

# Part 2
# if you came back to a visisted spot. the spot right before it (if its an x should be an op)